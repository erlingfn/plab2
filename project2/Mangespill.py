import matplotlib.pyplot as plt
import numpy as np

from Enkeltspill import Enkeltspill


class Mangespill:
    """ A tournament of two players that can run a given amount of games """

    def __init__(self, spiller1, spiller2, antall_spill):
        self.spiller1 = spiller1
        self.spiller2 = spiller2
        self.antall_spill = antall_spill
        # plotting data
        self.percentage_data = []
        self.games_played = []

    def arranger_turnering(self):
        """ Run a tournament for given amount of games """
        for i in range(0, self.antall_spill):
            spill = Enkeltspill(self.spiller1, self.spiller2)
            spill.gjennomfoer_spill()
            # append plotting data
            self.percentage_data.append(self.spiller2.points / (i + 1))
            self.games_played.append(i)
        gevinst_prosent = self.spiller1.points / self.antall_spill * 100
        gevinst_prosent2 = self.spiller2.points / self.antall_spill * 100
        print(self.spiller1.oppgi_navn() + ": " + str(gevinst_prosent) + "% " +
              self.spiller2.oppgi_navn() + ": " + str(gevinst_prosent2) + "%")

        # plot
        fig, ax = plt.subplots(1, 1)
        my_plotter(ax, self.games_played, self.percentage_data)


def my_plotter(ax, data1, data2):
    """
    A helper function to make a graph

    Parameters
    ----------
    ax : Axes
        The axes to draw to

    data1 : array
       The x data

    data2 : array
       The y data

    param_dict : dict
       Dictionary of kwargs to pass to ax.plot

    Returns
    -------
    out : list
        list of artists added
    """
    ax.plot(data1, data2)
    plt.show(block=True)
