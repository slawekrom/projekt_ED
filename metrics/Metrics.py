import math
import numpy as np
from collections import Counter
from metrics.Distance import Distance
from scipy import linalg


class Metrics:

    def __init__(self, size, dataframe):
        self.euclidean_distance = [[0 for i in range(size)] for j in range(size)]
        self.manhattan_distance = [[0 for i in range(size)] for j in range(size)]
        self.chebyshev_distance = [[0 for i in range(size)] for j in range(size)]
        self.mahalanobis_distance = [[0 for i in range(size)] for j in range(size)]
        self.df = dataframe
        self.size = size

    def calculate_euclidean(self):
        column_count = len(self.df.columns)
        columns = []
        columns = self.df.columns
        for i in range(self.size):
            for j in range(i):
                sum = 0
                for k in range(column_count - 1):
                    sum += math.pow((self.df.at[i, columns[k]] - self.df.at[j, columns[k]]), 2)
                distance: Distance = Distance(math.sqrt(sum), i, j)
                self.euclidean_distance[i][j] = distance

        # print(self.euclidean_distance)

    def calculate_euclidean_normalize(self):
        column_count = math.floor(len(self.df.columns) / 2)
        columns = []
        columns = self.df.columns
        columns = columns[column_count + 1: len(self.df.columns)]
        for i in range(self.size):
            for j in range(i):
                sum = 0
                for k in range(column_count):
                    sum += math.pow(
                        (self.df.at[i, columns[k]] - self.df.at[j, columns[k]]), 2)
                distance: Distance = Distance(math.sqrt(sum), i, j)
                self.euclidean_distance[i][j] = distance

    def classify_euclidean_normalize(self):
        self.calculate_euclidean_normalize()
        column_count = math.floor(len(self.df.columns) / 2)
        counter: Counter
        columns = []
        columns = self.df.columns
        columns = columns[column_count + 1: len(self.df.columns)]
        print('\n')
        k_classify = [0] * (self.size - 1)
        for i in range(self.size):  # i to wiersz danych
            distance_list = [row[i] for row in self.euclidean_distance]
            distance_list = distance_list[i + 1: self.size] + self.euclidean_distance[i][0:i]
            distance_list.sort(key=lambda x: x.distance, reverse=False)
            list_of_knn = list()
            test_object_class = self.df.at[i, self.df.columns[column_count]]
            for k in range(self.size - 1):  # k najblizszych
                if distance_list[k].index1 == i:
                    w = distance_list[k].index2
                else:
                    w = distance_list[k].index1
                list_of_knn.append(self.df.at[w, self.df.columns[column_count]])
                if len(list_of_knn) == k + 1:
                    counter = Counter(([element for element in list_of_knn]))
                    if len(counter) > 1 and counter.most_common(2)[0][1] == counter.most_common(2)[1][1]:
                        if list_of_knn[0] == test_object_class:  # w przypadku remisu decyduje najbliższy obiekt
                            k_classify[k] += 1
                    elif counter.most_common(1)[0][0] == test_object_class:
                        k_classify[k] += 1

        for n in range(len(k_classify)):
            k_classify[n] = round(k_classify[n] / self.size, 2)
        print(k_classify)

    def classify_euclidean(self):
        self.calculate_euclidean()
        counter: Counter
        columns = []
        columns = self.df.columns
        print('\n')
        k_classify = [0] * (self.size - 1)
        for i in range(self.size):  # i to wiersz danych
            distance_list = [row[i] for row in self.euclidean_distance]
            distance_list = distance_list[i + 1: self.size] + self.euclidean_distance[i][0:i]
            distance_list.sort(key=lambda x: x.distance, reverse=False)
            list_of_knn = list()
            test_object_class = self.df.at[i, columns[len(self.df.columns) - 1]]
            for k in range(self.size - 1):  # k najblizszych
                if distance_list[k].index1 == i:
                    w = distance_list[k].index2
                else:
                    w = distance_list[k].index1
                list_of_knn.append(self.df.at[w, columns[len(self.df.columns) - 1]])
                if len(list_of_knn) == k + 1:
                    counter = Counter(([element for element in list_of_knn]))
                    if len(counter) > 1 and counter.most_common(2)[0][1] == counter.most_common(2)[1][1]:
                        if list_of_knn[0] == test_object_class: # w przypadku remisu decyduje najbliższy obiekt
                            k_classify[k] += 1
                    elif counter.most_common(1)[0][0] == test_object_class:
                        k_classify[k] += 1

        for n in range(len(k_classify)):
            k_classify[n] = round(k_classify[n] / self.size, 2)
        print(k_classify)

    def classify_manhattan(self):
        self.calculate_manhattan()
        counter: Counter
        columns = []
        columns = self.df.columns
        print('\n')
        k_classify = [0] * (self.size - 1)
        for i in range(self.size):  # i to wiersz danych
            distance_list = [row[i] for row in self.manhattan_distance]
            distance_list = distance_list[i + 1: self.size] + self.manhattan_distance[i][0:i]
            distance_list.sort(key=lambda x: x.distance, reverse=False)
            list_of_knn = list()
            test_object_class = self.df.at[i, columns[len(self.df.columns) - 1]]
            for k in range(self.size - 1):  # k najblizszych
                if distance_list[k].index1 == i:
                    w = distance_list[k].index2
                else:
                    w = distance_list[k].index1
                list_of_knn.append(self.df.at[w, columns[len(self.df.columns) - 1]])
                if len(list_of_knn) == k + 1:
                    counter = Counter(([element for element in list_of_knn]))
                    if len(counter) > 1 and counter.most_common(2)[0][1] == counter.most_common(2)[1][1]:
                        if list_of_knn[0] == test_object_class:  # w przypadku remisu decyduje najbliższy obiekt
                            k_classify[k] += 1
                    elif counter.most_common(1)[0][0] == test_object_class:
                        k_classify[k] += 1

        for n in range(len(k_classify)):
            k_classify[n] = round(k_classify[n] / self.size, 2)
        print(k_classify)

    def classify_manhattan_normalize(self):
        self.calculate_manhattan_normalize()
        column_count = math.floor(len(self.df.columns) / 2)
        counter: Counter
        columns = []
        columns = self.df.columns
        columns = columns[column_count + 1: len(self.df.columns)]
        print('\n')
        k_classify = [0] * (self.size - 1)
        for i in range(self.size):  # i to wiersz danych
            distance_list = [row[i] for row in self.manhattan_distance]
            distance_list = distance_list[i + 1: self.size] + self.manhattan_distance[i][0:i]
            distance_list.sort(key=lambda x: x.distance, reverse=False)
            list_of_knn = list()
            test_object_class = self.df.at[i, self.df.columns[column_count]]
            for k in range(self.size - 1):  # k najblizszych
                if distance_list[k].index1 == i:
                    w = distance_list[k].index2
                else:
                    w = distance_list[k].index1
                list_of_knn.append(self.df.at[w, self.df.columns[column_count]])
                if len(list_of_knn) == k + 1:
                    counter = Counter(([element for element in list_of_knn]))
                    if len(counter) > 1 and counter.most_common(2)[0][1] == counter.most_common(2)[1][1]:
                        if list_of_knn[0] == test_object_class:  # w przypadku remisu decyduje najbliższy obiekt
                            k_classify[k] += 1
                    elif counter.most_common(1)[0][0] == test_object_class:
                        k_classify[k] += 1

        for n in range(len(k_classify)):
            k_classify[n] = round(k_classify[n] / self.size, 2)
        print(k_classify)

    def classify_chebyshev_normalize(self):
        self.calculate_chebyshev_normalize()
        column_count = math.floor(len(self.df.columns) / 2)
        counter: Counter
        columns = []
        columns = self.df.columns
        columns = columns[column_count + 1: len(self.df.columns)]
        print('\n')
        k_classify = [0] * (self.size - 1)
        for i in range(self.size):  # i to wiersz danych
            distance_list = [row[i] for row in self.chebyshev_distance]
            distance_list = distance_list[i + 1: self.size] + self.chebyshev_distance[i][0:i]
            distance_list.sort(key=lambda x: x.distance, reverse=False)
            list_of_knn = list()
            test_object_class = self.df.at[i, self.df.columns[column_count]]
            for k in range(self.size - 1):  # k najblizszych
                if distance_list[k].index1 == i:
                    w = distance_list[k].index2
                else:
                    w = distance_list[k].index1
                list_of_knn.append(self.df.at[w, self.df.columns[column_count]])
                if len(list_of_knn) == k + 1:
                    counter = Counter(([element for element in list_of_knn]))
                    if len(counter) > 1 and counter.most_common(2)[0][1] == counter.most_common(2)[1][1]:
                        if list_of_knn[0] == test_object_class:  # w przypadku remisu decyduje najbliższy obiekt
                            k_classify[k] += 1
                    elif counter.most_common(1)[0][0] == test_object_class:
                        k_classify[k] += 1

        for n in range(len(k_classify)):
            k_classify[n] = round(k_classify[n] / self.size, 2)
        print(k_classify)

    def classify_chebyshev(self):
        self.calculate_chebyshev()
        counter: Counter
        columns = []
        columns = self.df.columns
        print('\n')
        k_classify = [0] * (self.size - 1)
        for i in range(self.size):  # i to wiersz danych
            distance_list = [row[i] for row in self.chebyshev_distance]
            distance_list = distance_list[i + 1: self.size] + self.chebyshev_distance[i][0:i]
            distance_list.sort(key=lambda x: x.distance, reverse=False)
            list_of_knn = list()
            test_object_class = self.df.at[i, columns[len(self.df.columns) - 1]]
            for k in range(self.size - 1):  # k najblizszych
                if distance_list[k].index1 == i:
                    w = distance_list[k].index2
                else:
                    w = distance_list[k].index1
                list_of_knn.append(self.df.at[w, columns[len(self.df.columns) - 1]])
                if len(list_of_knn) == k + 1:
                    counter = Counter(([element for element in list_of_knn]))
                    if len(counter) > 1 and counter.most_common(2)[0][1] == counter.most_common(2)[1][1]:
                        if list_of_knn[0] == test_object_class:  # w przypadku remisu decyduje najbliższy obiekt
                            k_classify[k] += 1
                    elif counter.most_common(1)[0][0] == test_object_class:
                        k_classify[k] += 1

        for n in range(len(k_classify)):
            k_classify[n] = round(k_classify[n] / self.size, 2)
        print(k_classify)

    def calculate_manhattan(self):
        column_count = len(self.df.columns)
        columns = []
        columns = self.df.columns
        for i in range(self.size):
            for j in range(i):
                sum = 0
                for k in range(column_count - 1):
                    sum += math.fabs(self.df.at[i, columns[k]] - self.df.at[j, columns[k]])
                distance: Distance = Distance(sum, i, j)
                self.manhattan_distance[i][j] = distance

        # for row in self.manhattan_distance:
        #     print(row)

    def calculate_manhattan_normalize(self):
        column_count = math.floor(len(self.df.columns) / 2)
        columns = []
        columns = self.df.columns
        columns = columns[column_count + 1: len(self.df.columns)]
        for i in range(self.size):
            for j in range(i):
                sum = 0
                for k in range(column_count):
                    sum += math.fabs(self.df.at[i, columns[k]] - self.df.at[j, columns[k]])
                distance: Distance = Distance(sum, i, j)
                self.manhattan_distance[i][j] = distance

    def calculate_chebyshev(self):
        column_count = len(self.df.columns)
        columns = []
        columns = self.df.columns
        for i in range(self.size):
            for j in range(i):
                sum = 0
                for k in range(column_count - 1):
                    if math.fabs(self.df.at[i, columns[k]] - self.df.at[j, columns[k]]) > sum:
                        sum = math.fabs(self.df.at[i, columns[k]] - self.df.at[j, columns[k]])
                distance: Distance = Distance(sum, i, j)
                self.chebyshev_distance[i][j] = distance

        # for row in self.chebyshev_distance:
        #     print(row)

    def calculate_chebyshev_normalize(self):
        column_count = math.floor(len(self.df.columns) / 2)
        columns = []
        columns = self.df.columns
        columns = columns[column_count + 1: len(self.df.columns)]
        for i in range(self.size):
            for j in range(i):
                sum = 0
                for k in range(column_count):
                    if math.fabs(self.df.at[i, columns[k]] - self.df.at[j, columns[k]]) > sum:
                        sum = math.fabs(self.df.at[i, columns[k]] - self.df.at[j, columns[k]])
                distance: Distance = Distance(sum, i, j)
                self.chebyshev_distance[i][j] = distance

    def calculate_mahalanobis(self):
        column_count = len(self.df.columns)
        columns = []
        columns = self.df.columns
        cov = self.df.cov().to_numpy()
        inv_cov = linalg.inv(cov)
        for i in range(self.size):
            for j in range(i):
                first = []
                second = []
                for k in range(column_count - 1):
                    first.append(self.df.at[i, columns[k]])
                    second.append(self.df.at[j, columns[k]])
                subtract = np.subtract(first, second)
                subtract_t = subtract.T
                multiply = subtract_t.dot(inv_cov).dot(subtract)
                distance: Distance = Distance(multiply, i, j)
                self.mahalanobis_distance[i][j] = distance
        # print(self.mahalanobis_distance)

    def calculate_mahalanobis_normalize(self):
        column_count = math.floor(len(self.df.columns) / 2)
        columns = []
        columns = self.df.columns
        columns = columns[column_count + 1: len(self.df.columns)]
        cov = self.df[self.df.select_dtypes(['float', 'int']).columns.tolist()[column_count:]].cov().to_numpy()
        inv_cov = linalg.inv(cov)
        copy_df = self.df[self.df.select_dtypes(['float', 'int']).columns.tolist()]
        for i in range(self.size):
            for j in range(i):
                first = []
                second = []
                for k in range(column_count):
                    first.append(copy_df.at[i, columns[k]])
                    second.append(copy_df.at[j, columns[k]])
                subtract = np.subtract(first, second)
                subtract_t = subtract.T
                multiply = subtract_t.dot(inv_cov).dot(subtract)
                distance: Distance = Distance(multiply, i, j)
                self.mahalanobis_distance[i][j] = distance

    def classify_mahalanobis(self):
        self.calculate_mahalanobis()
        counter: Counter
        columns = []
        columns = self.df.columns
        print('\n')
        k_classify = [0] * (self.size - 1)
        for i in range(self.size):  # i to wiersz danych
            distance_list = [row[i] for row in self.mahalanobis_distance]
            distance_list = distance_list[i + 1: self.size] + self.mahalanobis_distance[i][0:i]
            distance_list.sort(key=lambda x: x.distance, reverse=False)
            list_of_knn = list()
            test_object_class = self.df.at[i, columns[len(self.df.columns) - 1]]
            for k in range(self.size - 1):  # k najblizszych
                if distance_list[k].index1 == i:
                    w = distance_list[k].index2
                else:
                    w = distance_list[k].index1
                list_of_knn.append(self.df.at[w, columns[len(self.df.columns) - 1]])
                if len(list_of_knn) == k + 1:
                    counter = Counter(([element for element in list_of_knn]))
                    if len(counter) > 1 and counter.most_common(2)[0][1] == counter.most_common(2)[1][1]:
                        if list_of_knn[0] == test_object_class:  # w przypadku remisu decyduje najbliższy obiekt
                            k_classify[k] += 1
                    elif counter.most_common(1)[0][0] == test_object_class:
                        k_classify[k] += 1

        for n in range(len(k_classify)):
            k_classify[n] = round(k_classify[n] / self.size, 2)
        print(k_classify)

    def classify_mahalanobis_normalize(self):
        self.calculate_mahalanobis_normalize()
        column_count = math.floor(len(self.df.columns) / 2)
        counter: Counter
        columns = []
        columns = self.df.columns
        columns = columns[column_count + 1: len(self.df.columns)]
        print('\n')
        k_classify = [0] * (self.size - 1)
        for i in range(self.size):  # i to wiersz danych
            distance_list = [row[i] for row in self.mahalanobis_distance]
            distance_list = distance_list[i + 1: self.size] + self.mahalanobis_distance[i][0:i]
            distance_list.sort(key=lambda x: x.distance, reverse=False)
            list_of_knn = list()
            test_object_class = self.df.at[i, self.df.columns[column_count]]
            for k in range(self.size - 1):  # k najblizszych
                if distance_list[k].index1 == i:
                    w = distance_list[k].index2
                else:
                    w = distance_list[k].index1
                list_of_knn.append(self.df.at[w, self.df.columns[column_count]])
                if len(list_of_knn) == k + 1:
                    counter = Counter(([element for element in list_of_knn]))
                    if len(counter) > 1 and counter.most_common(2)[0][1] == counter.most_common(2)[1][1]:
                        if list_of_knn[0] == test_object_class:  # w przypadku remisu decyduje najbliższy obiekt
                            k_classify[k] += 1
                    elif counter.most_common(1)[0][0] == test_object_class:
                        k_classify[k] += 1

        for n in range(len(k_classify)):
            k_classify[n] = round(k_classify[n] / self.size, 2)
        print(k_classify)

    @staticmethod
    def manhattan_distance(values: str, df, k: int):
        values_array = np.array(values.split(" ")).astype(np.float)
        column_count = len(df.columns)
        columns = []
        columns = df.columns
        distance = dict()
        for j in range(len(df.index)):
            sum = 0
            for n in range(column_count - 1):
                sum += math.fabs(values_array[n] - df.at[j, columns[n]])
            distance[j] = sum

        print(distance)
        list_of_knn = list()
        for w in sorted(distance, key=distance.get, reverse=False):
            list_of_knn.append(df.at[w, columns[len(df.columns) - 1]])
            if len(list_of_knn) == k:
                break
        print(list_of_knn)
        counter: Counter = Counter(([element for element in list_of_knn]))
        print(counter.most_common(1)[0][0])
        return counter.most_common(1)[0][0]

    @staticmethod
    def euclidean_distance(values: str, df, k: int):
        values_array = np.array(values.split(" ")).astype(np.float)
        column_count = len(df.columns)
        columns = []
        columns = df.columns
        distance = dict()
        for j in range(len(df.index)):
            sum = 0
            for n in range(column_count - 1):
                sum += math.pow((values_array[n] - df.at[j, columns[n]]), 2)
            distance[j] = math.sqrt(sum)

        print(distance)
        list_of_knn = list()
        for w in sorted(distance, key=distance.get, reverse=False):
            list_of_knn.append(df.at[w, columns[len(df.columns) - 1]])
            print(w)
            if len(list_of_knn) == k:
                break

        print('knn ' + str(list_of_knn))
        counter: Counter = Counter(([element for element in list_of_knn]))
        print(counter.most_common(1)[0][0])
        return counter.most_common(1)[0][0]

    @staticmethod
    def chebyshev_distance(values: str, df, k: int):
        values_array = np.array(values.split(" ")).astype(np.float)
        column_count = len(df.columns)
        columns = []
        columns = df.columns
        distance = dict()
        for j in range(len(df.index)):
            sum = 0
            for n in range(column_count - 1):
                if math.fabs(values_array[n] - df.at[j, columns[n]]) > sum:
                    sum = math.fabs(values_array[n] - df.at[j, columns[n]])
            distance[j] = sum

        print(distance)
        list_of_knn = list()
        for w in sorted(distance, key=distance.get, reverse=False):
            list_of_knn.append(df.at[w, columns[len(df.columns) - 1]])
            if len(list_of_knn) == k:
                break
        print(list_of_knn)
        counter: Counter = Counter(([element for element in list_of_knn]))
        print(counter.most_common(1)[0][0])
        return counter.most_common(1)[0][0]

    @staticmethod
    def mahalanobis_distance(values: str, df, k: int):
        values_array_first = np.array(values.split(" ")).astype(np.float)
        column_count = len(df.columns)
        columns = df.columns
        distance = dict()
        cov = df.cov().to_numpy()
        inv_cov = linalg.inv(cov)
        for j in range(len(df.index)):
            values_array_second = []
            for n in range(column_count - 1):
                values_array_second.append(df.at[j, columns[n]])
            subtract = np.subtract(values_array_first, values_array_second)
            subtract_t = subtract.T
            multiply = subtract_t.dot(inv_cov).dot(subtract)
            distance[j] = multiply

        print(distance)
        list_of_knn = list()
        for w in sorted(distance, key=distance.get, reverse=False):
            list_of_knn.append(df.at[w, columns[len(df.columns) - 1]])
            if len(list_of_knn) == k:
                break
        print(list_of_knn)
        counter: Counter = Counter(([element for element in list_of_knn]))
        print(counter.most_common(1)[0][0])
        return counter.most_common(1)[0][0]
