from collections import Counter

from operation.SplitInfo import SplitInfo
import pandas as pd
import numpy as np
import time

class Split:
    def __init__(self, df):
        self.df = df
        self.size = len(df.columns) - 1
        self.binary_vector = []
        self.values_vector = []
        self.applied_splits = []
        self.vectorized_df = None

    def split_data(self):
        start = time.time()
        self.clean_vectors()
        vector_size = 0
        new_df = self.df
        class_column = new_df.columns[-1]
        size = self.size
        columns = []
        columns = self.df.columns[0: size]
        while new_df.shape[0] > 0 and new_df[class_column].nunique() != 1:
            splits = []
            for column in range(size):  # petla po columnach -atrybutach
                column_values = new_df[columns[column]].unique().tolist()
                column_values.sort()
                column_min = min(column_values)
                column_max = max(column_values)
                tmp_df = new_df.filter([columns[column], new_df.columns[-1]],
                                       axis=1)  # zbiór danych z badaną kolumną i kolumną decyzyjną
                for i in range(len(column_values) - 1):  # petla po wartosciach atrybutu od dołu

                    split_point = column_values[i] + (
                            column_values[i + 1] - column_values[i]) / 2  # punkt podziału w środku między punktami
                    splited_df = tmp_df[
                        tmp_df[columns[column]] < split_point]  # zbiór podzielony względem punktu podziału
                    unique_classes = splited_df[class_column].nunique()

                    if unique_classes == 1:
                        split_info: SplitInfo = SplitInfo(split_point=split_point, column=columns[column],
                                                          count=len(splited_df.index), lower=True, o_class=splited_df.iloc[0][class_column])
                        splits.append(split_info)
                    else:
                        break

                for i in range(len(column_values) - 1, 0, -1):  # petla po wartosciach atrybutu od góry

                    split_point = column_values[i] + (
                            column_values[i - 1] - column_values[i]) / 2  # punkt podziału w środku między punktami
                    splited_df = tmp_df[
                        tmp_df[columns[column]] > split_point]  # zbiór podzielony względem punktu podziału
                    unique_classes = splited_df[class_column].nunique()

                    if unique_classes == 1:
                        split_info: SplitInfo = SplitInfo(split_point=split_point, column=columns[column],
                                                          count=len(splited_df.index), lower=False, o_class=splited_df.iloc[0][class_column])
                        splits.append(split_info)
                    else:
                        break

            splits.sort(reverse=True, key=lambda x: x.count)
            # delete splited rows
            if len(splits) > 0:
                best_split = splits[0]
                self.values_vector.append(best_split.split_point)
                self.applied_splits.append(best_split)
                vector_size += 1
                print('Vector size: ' + str(vector_size) + ' deleted points count: ' + str(best_split.count))
                if best_split.lower:
                    new_df = new_df[new_df[best_split.column] > best_split.split_point]
                else:
                    new_df = new_df[new_df[best_split.column] < best_split.split_point]
            # była blokazda XOR
            else:
                splits = []
                for column in range(size):  # petla po columnach -atrybutach
                    column_values = new_df[columns[column]].unique().tolist()
                    column_values.sort()
                    tmp_df = new_df.filter([columns[column], new_df.columns[-1]],
                                           axis=1)  # zbiór danych z badaną kolumną i kolumną decyzyjną
                    split_info = None
                    for i in range(len(column_values) - 1):  # petla po wartosciach atrybutu od dołu

                        split_point = column_values[i] + (
                                column_values[i + 1] - column_values[i]) / 2  # punkt podziału w środku między punktami
                        splited_df = tmp_df[
                            tmp_df[columns[column]] < split_point]  # zbiór podzielony względem punktu podziału
                        counter = Counter(splited_df[class_column])

                        if len(counter.keys()) == 2 and counter.most_common(2)[1][1] == 1:
                            split_info: SplitInfo = SplitInfo(split_point=split_point, column=columns[column],
                                                              count=len(splited_df.index), lower=True,
                                                              o_class=counter.most_common(1)[0][0])
                        elif split_info is not None:
                            splits.append(split_info)
                            break
                        else:
                            break
                    split_info = None
                    for i in range(len(column_values) - 1, 0, -1):  # petla po wartosciach atrybutu od góry

                        split_point = column_values[i] + (
                                column_values[i - 1] - column_values[i]) / 2  # punkt podziału w środku między punktami
                        splited_df = tmp_df[
                            tmp_df[columns[column]] > split_point]  # zbiór podzielony względem punktu podziału
                        counter = Counter(splited_df[class_column])

                        if len(counter.keys()) == 2 and counter.most_common(2)[1][1] == 1:
                            split_info: SplitInfo = SplitInfo(split_point=split_point, column=columns[column],
                                                              count=len(splited_df.index), lower=False,
                                                              o_class=counter.most_common(1)[0][0])
                        elif split_info is not None:
                            splits.append(split_info)
                            break
                        else:
                            break

                if len(splits) > 0:
                    splits.sort(reverse=True, key=lambda x: x.count)
                    best_split = splits[0]
                    self.values_vector.append(best_split.split_point)
                    self.applied_splits.append(best_split)
                    vector_size += 1
                    print('Vector size: ' + str(vector_size) + ' deleted points count: ' + str(best_split.count))
                    if best_split.lower:
                        new_df = new_df[new_df[best_split.column] > best_split.split_point]
                    else:
                        new_df = new_df[new_df[best_split.column] < best_split.split_point]
                else: # przypadek gdy zostały takie same punkty ale należące do różnych klas - zakończyć algorytm
                    new_df.drop(new_df.index, inplace=True)  # drop df  - nie trzeba dalej dzielić
            print('Left ' + str(len(new_df)) + ' points')

        end = time.time()
        #print(end-start)

    def create_vectorized_df(self):
        start = time.time()
        columns_name = []
        for i in range(len(self.values_vector)):
            columns_name.append('z'+str(i+1))

        columns_name.append('class')
        vectorized_df = pd.DataFrame(columns=columns_name)

        for i in range(len(columns_name) -1):
            column = columns_name[i]
            split = self.applied_splits[i]
            if split.lower:
                vectorized_df[column] = np.where(self.df[split.column] < split.split_point, 1, 0)
            else:
                vectorized_df[column] = np.where(self.df[split.column] > split.split_point, 1, 0)

        vectorized_df['class'] = self.df[self.df.columns[-1]].to_numpy()
        self.vectorized_df = vectorized_df
        end = time.time()
        #print(end-start)
        return vectorized_df

    def classify_new(self, values):
        values_array = np.array(values.split(" ")).astype(np.float)
        new_object_class = None
        columns = []
        columns = self.df.columns[0: self.size]
        columns_dict = dict()
        index = 0
        for col in columns:
            columns_dict.update({col: index})
            index+=1

        for i in range(len(self.applied_splits)):
            split: Split = self.applied_splits[i]
            new_object_value = values_array[columns_dict.get(split.column)]
            if split.lower and new_object_value < split.split_point:
                new_object_class = split.objects_class
                break
            elif not split.lower and new_object_value > split.split_point:
                new_object_class = split.objects_class
                break

        return new_object_class




    def clean_vectors(self):
        self.binary_vector = []
        self.values_vector = []
