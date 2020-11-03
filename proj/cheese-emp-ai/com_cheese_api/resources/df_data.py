import numpy as np
import os
from sklearn.model_selection import train_test_split
import pandas as pd



def df_split():
    feats = pd.read_csv("data/cheese_data.csv", index_col = 0)
    test_size = 0.2
    random_state = 42

    X_train, X_test = train_test_split(
        feats,
        test_size = test_size,
        random_state = random_state
    )

    print(f'Shape of X_train: {X_train.shape}')

    X_train.to_csv(os.path.join('data', 'cheese_train.csv'), index=False)
    X_test.to_csv(os.path.join('data', 'cheese_test.csv'), index=False)    

df_split()