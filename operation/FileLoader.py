import pandas as pd

class FileLoader:

    def loadFile(self, file_path: str, separator: str):
        df = pd.read_csv(file_path, separator, index_col=None, comment='#')
        return df

    def loadFile_and_add_headers(self, file_path: str, separator: str):
        df = pd.read_csv(file_path, separator, index_col=None, header=None, comment='#')
        number = len(df.columns)
        headers = []
        for i in range(number):
            headers.append('column' + str(i+1))
        df.columns = headers
        return df
