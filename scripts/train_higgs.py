import os
import pandas as pd
import xgboost as xgb
import time
from sklearn.model_selection import train_test_split

def main():
    data_path = "data/HIGGS_1M"
    if not os.path.exists(data_path):
        raise FileExistsError("Can't find the data file.Please run download_higgs.py")
    
    os.makedirs("results",exist_ok=True)
    os.makedirs("logs",exist_ok=True)
    print("Loading data...")
    df = pd.read_csv(data_path,header=None)
    y = df.iloc[:,0].values
    X = df.iloc[:,2:].values

    X_train,X_test,y_train,y_test = train_test_split( X,y,test_size = 0.2,random_state = 42 )

    # TODO







if __name__ == "__main__":
    main()