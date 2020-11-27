import random

import matplotlib.pyplot as plt
from PyQt5.QtWidgets import QDialog, QVBoxLayout
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from mpl_toolkits.mplot3d import Axes3D


class Plot3D(QDialog):
    def __init__(self, data, column_x, column_y, column_z, column_class, parent=None):
        QDialog.__init__(self, parent)
        self.data = data
        self.x_val = column_x
        self.y_val = column_y
        self.z_val = column_z
        self.class_column = column_class
        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        self.canvas.resize(500, 400)
        self.toolbar = NavigationToolbar(self.canvas, self)
        self.plot(self.figure)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.toolbar)
        self.layout.addWidget(self.canvas)
        self.setLayout(self.layout)

    def plot(self, figure):
        figure.clear()
        ax = Axes3D(figure)
        if self.class_column:
            colours = ['green', 'red', 'blue', 'orange', 'purple', 'black', 'cyan', 'magenta', 'gray', 'olive', 'lime',
                       'salmon', 'deepskyblue']
            data_classes = self.data[self.class_column].unique()

            for idx, data_class in enumerate(data_classes):
                x_ = self.data[self.data[self.class_column] == data_class][self.x_val]
                y_ = self.data[self.data[self.class_column] == data_class][self.y_val]
                z_ = self.data[self.data[self.class_column] == data_class][self.z_val]
                if len(data_classes) <= len(colours):
                    ax.scatter(x_, y_, z_, cmap=colours[idx], label=data_class)
                else:
                    ax.scatter(x_, y_, z_, cmap=(random.uniform(0, 1), random.uniform(0, 1), random.uniform(0, 1)),
                               label=data_class)

            ax.set_xlabel(self.x_val)
            ax.set_ylabel(self.y_val)
            ax.set_zlabel(self.z_val)
            ax.legend()

        else:
            ax.scatter(self.data[self.x_val], self.data[self.y_val], self.data[self.z_val])
            ax.set_xlabel(self.x_val)
            ax.set_ylabel(self.y_val)
            ax.set_zlabel(self.z_val)
        self.canvas.draw()
