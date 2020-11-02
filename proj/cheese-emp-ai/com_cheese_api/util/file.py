import os
import pandas as pandas
import xlrd
# import googlemaps
import json

from dataclasses import dataclasses

@dataclasses
class FileReader:
    context: str = ''
    fname: str = ''
    train: object = None
    test: object = None
    id: str = ''
    lable: str = ''

    def new_file(self) -> str:
        return os.path.join(self.context, self.fname)

    def csv_to_dframe(self) -> object:
        return pd.read_csv(self.new_file(), encoding='UTF-8', thousands=',')
    
    def xls_to_dframe(self, header, usecols) -> object:
        print(f'PANDAS VERSION: {pd.__version__}')
        return pd.read_excel(self.new_file(), header = header, usecols = usecols)

    def create_gmaps(self):
        return googlemaps.Client(key='')

    def json_load(self):
        return json.load(open(self.new_file(), encoding='UTF-8'))