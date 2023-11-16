import matplotlib.pyplot as plt
import scipy as sp


def regression(title, x, y, reg):
    """
    Créer une regression linéaire en fonction des paramètres suivants :
    Create a linear regression according to the following parameter :
    - title : the main title of the plot
    - x : Abscissa [name, coordinates]
    - y : Ordinate [name, coordinates]
    - reg : regression's parameters [message, targeted_axis, targeted_axis_value]
    """

    ##########
    ## Init ##
    ##########

    _, ax = plt.subplots(figsize=(20, 10))

    # Naming
    ax.set_title(title)
    ax.set_xlabel(x[0])
    ax.set_ylabel(y[0])

    # Plot point
    ax.scatter(x[1], y[1], marker="o", color="red", label="Points expérimentaux")

    ################
    ## Regression ##
    ################

    # Obtain m (slope), b (intercept) and r of linear regression line
    m, p, r, _, _ = sp.stats.linregress(x[1], y[1])

    # Add linear regression line to scatterplot
    ax.plot(x[1], m * x[1] + p, label=f"Régression linéaire ($R^2$ = {round(r**2, 4)})")

    ############
    ## Search ##
    ############

    # Create point
    if len(reg) != 0:
        if reg[1] == "x":
            x_point = reg[2]
            y_point = round(m * x_point + p, 2)
        elif reg[1] == "y":
            y_point = reg[2]
            x_point = round((y_point - p) / m, 2)
        else:
            raise Exception(
                "Please a give a correct axis for the regression, either x or y"
            )

    # Display on graph
    ax.annotate(
        f"{reg[0]} $(x = {x_point}; \ y = {y_point})$",
        xy=(x_point, y_point),
        xytext=(x_point * 1.15, y_point * 0.85),
        arrowprops=dict(arrowstyle="->", connectionstyle="arc,angleA=0,armA=50,rad=10"),
    )

    ############
    ## Legend ##
    ############

    ax.legend()
