from GUI import *
import sys
# from PySide.QWidget import
# from PySide.QtGui import *
# from PySide.QtCore import *
from PySide import *
import matlab_port as sim
import matplotlib.pyplot as plt


class GUIWindow(QtGui.QMainWindow, Ui_Simulation):

    def __init__(self, parent=None):
        super(GUIWindow,self).__init__(parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.calculate)

    def calculate(self):
        list_keyindices = []  # A list of the indices where each individual experiment crosses the defined threshold.(unused)
        list_keyindices_magnitude = []  # A list of the values where each sim crosses the defined injury threshold
        list_mean_hit = []  # A list of the mean hit of each sim
        list_all_hits = []

        # Values given by Prof. Talavage as equivalent parameters to ensure the sim runs correctly
        cumulative_threshold = int(self.LE_CumThresh.text())
        linear_mean = int(self.LE_LinearMean.text())
        linear_threshold = int(self.LE_LinearThresh.text())
        hidden_threshold = int(self.LE_HiddenThresh.text())
        sim_num = int(self.LE_SimNum.text())

        # The following section invokes the matlab_port function for the number of specified times
        for x in range(sim_num):
            list_hits_single_sim = []
            single_sim_results = sim.single_sim(cumulative_threshold, linear_mean, linear_threshold,hidden_threshold)  # Invokes the sim
            keyindx, keyindx_magnitude, mean_hit, list_hits_single_sim = single_sim_results  # Unpacks values to be appended to respective lists
            for hit in list_hits_single_sim:
                list_all_hits.append(hit)
            # Appending values to their respective lists
            list_keyindices.append(keyindx)
            list_keyindices_magnitude.append(keyindx_magnitude)
            list_mean_hit.append(mean_hit)

        # Prepare data to plot
        n = 50
        list_keyindices_magnitude.sort()  # Sort the mags of where we crossed the threshold
        list_mean_hit.sort()  # Sort each mean hit
        list_max = []
        list_max2 = []
        index = 0
        while index < sim_num:
            list_max.append(100)
            list_max2.append(80)
            index += 1
        histogram = plt.hist(list_all_hits, bins = 50)
        fig, ax = plt.subplots(1)
        ax.scatter(range(0, len(list_keyindices_magnitude)), list_keyindices_magnitude, color='b', marker='.',alpha=.5)
        ax.scatter(range(0, len(list_keyindices_magnitude)), list_mean_hit, color='g', marker='.',alpha=.5)
        ax.fill(range(0, len(list_keyindices_magnitude)), list_max2, color='r')
        plt.ylabel('G-force of hit that crosses threshold')
        plt.title('Head injuries')
        plt.show()

currentApp = QtGui.QApplication(sys.argv)
currentForm = GUIWindow()
currentForm.show()
currentApp.exec_()