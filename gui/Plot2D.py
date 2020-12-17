import random

import matplotlib.pyplot as plt
from PyQt5.QtWidgets import QDialog, QVBoxLayout
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from PyQt5 import QtCore, QtGui, QtWidgets


class Plot2D(QDialog):
    def __init__(self, data, column_x, column_y, column_class, vectors: [], parent=None):
        QDialog.__init__(self, parent)
        QDialog.setMinimumSize(self, 1200, 600)
        self.data = data
        self.x_val = column_x
        self.y_val = column_y
        self.class_column = column_class
        self.vectors = vectors
        self.counter = 0
        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        self.toolbar = NavigationToolbar(self.canvas, self)

        self.drawButton = QtWidgets.QPushButton()
        self.drawButton.setBaseSize(50,35)
        self.drawButton.setText('Draw next line')
        self.drawButton.setObjectName("drawButton")
        self.drawAllButton = QtWidgets.QPushButton()
        self.drawAllButton.setBaseSize(50, 35)
        self.drawAllButton.setText('Draw all lines')
        self.drawAllButton.setObjectName("drawAllButton")

        self.plot(self.figure)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.toolbar)
        self.layout.addWidget(self.canvas)
        self.layout.addWidget(self.drawButton)
        self.layout.addWidget(self.drawAllButton)
        self.setLayout(self.layout)

        self.drawButton.clicked.connect(lambda: self.add_line())
        self.drawAllButton.clicked.connect(lambda: self.draw_all_lines())

    def plot(self, figure):
        figure.clear()
        ax = figure.add_subplot(111)
        if self.class_column:
            colours = ['green', 'red', 'blue', 'orange', 'purple', 'cyan', 'magenta', 'gray', 'olive', 'lime',
                       'salmon', 'deepskyblue', 'black']
            data_classes = self.data[self.class_column].unique()

            for idx, data_class in enumerate(data_classes):
                x_ = self.data[self.data[self.class_column] == data_class][self.x_val]
                y_ = self.data[self.data[self.class_column] == data_class][self.y_val]
                if len(data_classes) <= len(colours):
                    ax.scatter(x_, y_, cmap=colours[idx], label=data_class)
                else:
                    ax.scatter(x_, y_, cmap=(random.uniform(0, 1), random.uniform(0, 1), random.uniform(0, 1)),
                               label=data_class)

            ax.set_xlabel(self.x_val)
            ax.set_ylabel(self.y_val)
            ax.legend()

        else:
            ax.scatter(self.data[self.x_val], self.data[self.y_val])
            ax.set_xlabel(self.x_val)
            ax.set_ylabel(self.y_val)
        self.canvas.draw()

    def add_line(self):
        if self.counter < len(self.vectors):
            vector = self.vectors[self.counter]
            value = vector.split_point
            if vector.column == self.y_val:
                self.figure.axes[0].axhline(y=value, color='black')
            else:
                self.figure.axes[0].axvline(x=value, color='black')
            #self.figure.axes[0].axvline(x=3.0, color='black')
            self.counter+=1
            self.canvas.draw()

    def draw_all_lines(self):
        for vector in self.vectors:
            value = vector.split_point
            if vector.column == self.y_val:
                self.figure.axes[0].axhline(y=value, color='black')
            else:
                self.figure.axes[0].axvline(x=value, color='black')
        self.canvas.draw()
