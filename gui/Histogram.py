import matplotlib.pyplot as plt
from PyQt5.QtWidgets import QDialog, QVBoxLayout
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar


class Histogram(QDialog):
    def __init__(self, data, column_name, number_of_bins, parent=None):
        QDialog.__init__(self, parent)
        self.data_ = data
        self.column = column_name
        self.bins = number_of_bins

        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        self.toolbar = NavigationToolbar(self.canvas, self)

        self.plot(self.figure)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.toolbar)
        self.layout.addWidget(self.canvas)
        self.setLayout(self.layout)

    def plot(self, figure):
        figure.clear()
        ax = figure.add_subplot(111)
        ax.hist(self.data_[self.column], bins=self.bins, color='green', ec='black')
        ax.set_xlabel(self.column)
        ax.set_ylabel("Ilość")
        self.canvas.draw()
