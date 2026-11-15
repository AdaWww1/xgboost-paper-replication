import os
import pandas as pd
import xgboost as xgb
import time
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score,roc_curve

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    base_dir = os.path.dirname(script_dir)
    data_path = os.path.join(base_dir,"data","HIGGS_1M.csv")
    if not os.path.exists(data_path):
        raise FileNotFoundError("Can't find the data file.Please run download_higgs.py")
    
    results_dir = os.path.join(base_dir, "results")
    os.makedirs(results_dir,exist_ok=True)
   
    print("Loading data...")
    df = pd.read_csv(data_path,header=None)
    y = df.iloc[:,0].values
    X = df.iloc[:,2:].values
    seed = 2026

    X_train,X_test,y_train,y_test = train_test_split( X,y,test_size = 0.2,random_state = seed )

    dtrain = xgb.DMatrix(X_train,label = y_train)
    dtest = xgb.DMatrix(X_test,label = y_test)
    params = {
        "max_depth":8,
        "eta":0.1,
        "objective":"binary:logistic",
        "eval_metric":"auc",
        "nthread":8,
        "seed":seed
    }
    num_rounds = 500

    start_time = time.time()
    model = xgb.train(params,dtrain,num_boost_round=num_rounds)
    elapsed_time = time.time() - start_time
    time_per_tree = elapsed_time / num_rounds

    preds = model.predict(dtest)
    auc = roc_auc_score(y_test,preds)

    print(f"Average time per tree:{time_per_tree:.4f}s")
    print(f"Test AUC:{auc:.4f}")

    fpr,tpr,thresholds = roc_curve(y_test,preds)
    plt.figure(figsize=(8,6))
    plt.plot(fpr,tpr,color='darkorange',lw=2,label=f'XGBoost(AUC={auc:.4f})')
    plt.plot([0,1],[0,1],color='navy',lw=2,linestyle='--')
    plt.xlim([0.0,1.0])
    plt.ylim([0.0,1.05])
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('Receiver Operating Characteristic(Roc)')
    plt.legend(loc="lower right")

    original_cwd = os.getcwd()  
    os.chdir(results_dir)       
    
    plt.savefig(f"roc_curve_seed{seed}.png", bbox_inches='tight')
    plt.close()
    
    os.chdir(original_cwd)    
    print(f"ROC curve saved to results/roc_curve_seed{seed}.png")
    
    
    results_df = pd.DataFrame([{
        "method": "XGBoost",
        "time_per_tree_sec":time_per_tree,
        "test_auc":auc,
        "seed":seed,
        "num_rounds": num_rounds
    }])

    out_path = os.path.join(results_dir,f"higgs_xgb_seed{seed}.csv")
    results_df.to_csv(out_path,index=False)
    print(f"Results saved to {out_path}")



if __name__ == "__main__":
    main()