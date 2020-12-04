from operation.SplitInfo import SplitInfo


class Split:
    def __init__(self, df):
        self.df = df
        self.size = len(df.columns) - 1

    def split_data(self):
        new_df = self.df
        size = self.size
        columns = []
        columns = self.df.columns[0: size]
        while new_df.shape[0] > 0:
            splits = []
            for column in range(size):  # petla po columnach -atrybutach
                column_values = new_df[columns[column]].unique().tolist()
                column_values.sort()
                column_min = min(column_values)
                column_max = max(column_values)
                tmp_df = new_df.filter([columns[column], new_df.columns[-1]],
                                       axis=1)  # zbiór danych z badaną kolumną i kolumną decyzyjną
                for i in range(len(column_values)):  # petla po wartosciach atrybutu od dołu

                    split_point = column_values[i] + (
                            column_values[i + 1] - column_values[i]) / 2  # punkt podziału w środku między punktami
                    splited_df = tmp_df[tmp_df[columns[column]] < split_point]  # zbiór podzielony względem punktu podziału
                    unique_classes = splited_df[splited_df.columns[-1]].nunique()

                    if unique_classes == 1:
                        split_info: SplitInfo = SplitInfo(split_point=split_point, column=columns[column],
                                                          count=len(splited_df.index), lower=True)
                        splits.append(split_info)
                    else:
                        break
                        # print(unique_classes)

                for i in range(len(column_values) -1, 0, -1):  # petla po wartosciach atrybutu od góry

                    split_point = column_values[i] + (
                            column_values[i - 1] - column_values[i]) / 2  # punkt podziału w środku między punktami
                    splited_df = tmp_df[tmp_df[columns[column]] > split_point]  # zbiór podzielony względem punktu podziału
                    unique_classes = splited_df[splited_df.columns[-1]].nunique()

                    if unique_classes == 1:
                        split_info: SplitInfo = SplitInfo(split_point=split_point, column=columns[column],
                                                          count=len(splited_df.index), lower=False)
                        splits.append(split_info)
                    else:
                        break

            splits.sort(reverse=True, key= lambda x: x.count)
            print(splits)
            #delete splited rows
            best_split = splits[0]
            if best_split.lower:
                new_df = new_df[new_df[best_split.column] > best_split.split_point]
            else:
                new_df = new_df[new_df[best_split.column] < best_split.split_point]

            print(len(new_df))
