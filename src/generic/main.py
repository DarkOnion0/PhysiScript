import matplotlib.pyplot as plt


def line(
    title,
    x,
    y,
):
    """
    Create a line according to the following parameters :
    - title : the main title of the plot
    - x : Abscissa [name, coordinates]
    - y : Ordinate [name, coordinates]
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
