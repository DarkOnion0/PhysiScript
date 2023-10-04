import matplotlib.pyplot as plt


def line(
    title,
    x,
    y,
):
    """
    Créer une ligne en fonction des paramètres suivants :
    - title : le titre du graphique
    - x : l'axe des abscisse [nom, coordonées]
    - y : l'axe des ordonnées [nom, coordonées]
    """

    ##########
    ## Init ##
    ##########

    fig, ax = plt.subplots(figsize=(20, 10))

    # Naming
    ax.set_title(title)
    ax.set_xlabel(x[0])
    ax.set_ylabel(y[0])

    # Plot point
    ax.plot(x[1], y[1], marker="o", color="purple")
