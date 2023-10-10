import matplotlib.pyplot as plt
import numpy as np
import scipy as sp
from math import floor


def titragePH(title, x, y, showVeLine: bool = False):
    """
    Créer un graphique d'analyse de titrage pH-métrique en fonctions des paramètres suivants :
    - title : le titre du graphique
    - x : l'axe des abscisse [nom, coordonées]
    - y : l'axe des ordonnées [nom, coordonées]
    - showVeLine: Affiche la droite verticale corréspondant aux volume à l'équivalence
    """

    ##########
    ## Init ##
    ##########

    fig, ax = plt.subplots(figsize=(20, 10))

    # Naming
    ax.set_title(title)
    ax.set_xlabel(x[0])
    ax.set_ylabel(y[0])

    ####################
    ## Line Smoothing ##
    ####################

    # https://stackoverflow.com/questions/29934831/matplotlib-draw-spline-from-3-points#29948678
    # if len(x[1]) > 3:
    #    tck = sp.interpolate.splrep(x[1], y[1],s=1)
    # else:
    #    tck = sp.interpolate.splrep(x[1], y[1], k=2, s=0)

    # https://docs.scipy.org/doc/scipy/tutorial/interpolate/1D.html#monotone-interpolants
    xnew = np.linspace(min(x[1]), max(x[1]), len(x[1]) * 50)

    spline = sp.interpolate.PchipInterpolator(x[1], y[1])

    ####################
    ## Find the value ##
    ####################

    # Calculate the derivative
    spline_derivative = spline.derivative()(xnew)

    # Find the extremum
    if y[1][0] < y[1][-1]:  # if an acide is the titrating solution
        x_point = xnew[np.where(spline_derivative == max(spline_derivative))]
    else:  # if a base is the titrating solution
        x_point = xnew[np.where(spline_derivative == min(spline_derivative))]

    # Display on graph
    y_point = spline(x_point)
    ax.annotate(
        f"Equivalence $(x = {round(x_point[0], 2)}; \ y = {round(y_point[0], 2)})$",
        xy=(x_point, y_point),
        # xytext=(x_point * 1.1, y_point * 0.75),
        xytext=(x_point * 0.7, y_point * 1.15),
        arrowprops=dict(arrowstyle="->", connectionstyle="arc,angleA=0,armA=50,rad=10"),
    )

    ##############
    ## Plotting ##
    ##############

    # Original point
    plt.scatter(x[1], y[1], marker="o", color="green", label="Experimental points")

    # Smoothed line
    # plt.plot(xnew, sp.interpolate.BSpline(*tck)(xnew), color="orange", label="Smoothed line")
    plt.plot(xnew, spline(xnew), "-", color="orange", label="$V \longmapsto pH$")

    # Derivative
    plt.plot(
        xnew,
        spline_derivative,
        "-",
        color="pink",
        label=r"$\frac {\mathrm{d} pH} {\mathrm{d} V}$",
    )

    # Horizontal line of the V_e
    if showVeLine:
        plt.axvline(x_point, linestyle="--", color="palegreen", label="$V_e$")

    ax.legend()


def titrageConductimetrique(title, x, y, split, showVeLine: bool = False):
    """
    Créer un graphique d'analyse de titrage conductimétrique en fonctions des paramètres suivants :
    - title : le titre du graphique
    - x : l'axe des abscisse [nom, coordonées]
    - y : l'axe des ordonnées [nom, coordonées]
    - split : l'indexe python de ou rompre la série de donnée
    - showVeLine: Affiche la droite verticale corréspondant aux volume à l'équivalence
    """

    ##########
    ## Init ##
    ##########

    fig, ax = plt.subplots(figsize=(20, 10))

    # Naming
    ax.set_title(title)
    ax.set_xlabel(x[0])
    ax.set_ylabel(y[0])

    ######################
    ## Lines Regression ##
    ######################

    # Find the bottom of the V shape dataset
    # split, = np.where(y[1] == min(y[1]))
    split = [split]

    # Split x
    x1 = x[1][: split[0] + 1]
    x2 = x[1][split[0] + 1 :]

    x1_new = np.linspace(min(x1), floor(max(x1) * 1.25), len(x1) * 50)
    x2_new = np.linspace(floor(min(x2) * 0.75), max(x2), len(x2) * 50)

    # Split y
    y1 = y[1][: split[0] + 1]
    # y1 = np.linspace(min(y1), max(y1), len(y1)*50)

    y2 = y[1][split[0] + 1 :]
    # y2 = np.linspace(min(y2), max(y2), len(y2)*50)

    # Obtain m (slope), b (intercept) and r of linear regression line
    m1, p1, r1, _, _ = sp.stats.linregress(x1, y1)
    m2, p2, r2, _, _ = sp.stats.linregress(x2, y2)

    ############################
    ## Find line intersection ##
    ############################

    x_point = (p1 - p2) / (m2 - m1)
    y_point = m1 * x_point + p1

    ax.annotate(
        f"Equivalence $(x = {round(x_point, 2)}; \ y = {round(y_point, 2)})$",
        xy=(x_point, y_point),
        xytext=(x_point * 1.05, y_point * 0.50),
        # xytext=(x_point * 0.7, y_point * 1.15),
        arrowprops=dict(arrowstyle="->", connectionstyle="arc,angleA=0,armA=50,rad=10"),
    )

    ##############
    ## Plotting ##
    ##############

    # Original point
    plt.scatter(x[1], y[1], marker="o", color="chocolate", label="Points expérimentaux")

    # Regressions
    ax.plot(
        x1_new,
        m1 * x1_new + p1,
        color="mediumspringgreen",
        label=f"Régression linéaire 1 ($R^2$ = {round(r1**2, 4)})",
    )
    ax.plot(
        x2_new,
        m2 * x2_new + p2,
        color="mediumslateblue",
        label=f"Régression linéaire 2 ($R^2$ = {round(r2**2, 4)})",
    )

    # Horizontal line of the V_e
    if showVeLine:
        plt.axvline(x_point, linestyle="--", color="olive", label="$V_e$")

    ax.legend()
