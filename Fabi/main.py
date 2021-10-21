
import pandas as pd
import numpy as np

df1 = pd.read_csv('Longitude.csv').to_numpy()
df2 = pd.read_csv('Latitude.csv').to_numpy()

if __name__ == '__main__':
    df = pd.read_csv("master_dataset.csv", sep=',')
    print('stop')
