import os
import pandas as pd
import time
import matplotlib.pyplot as plt
import logging
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score,roc_curve
from sklearn.ensemble import HistGradientBoostingClassifier

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    base_dir = os.path.dirname(script_dir)
    data_path = os.path.join(base_dir,"data","HIGGS_1M.csv")
    if not os.path.exists(data_path):
        raise FileNotFoundError("Can't find the data file.Please run download_higgs.py")
    
    results_dir = os.path.join(base_dir, "results")
    logs_dir = os.path.join(base_dir, "logs")
    os.makedirs(results_dir,exist_ok=True)
    os.makedirs(logs_dir,exist_ok=True)
   
    print("Loading data...")
    df = pd.read_csv(data_path,header=None)
    y = df.iloc[:,0].values
    X = df.iloc[:,1:].values
    seeds = [42,123,2026]

    all_results = []
    for seed in seeds:
        print(f"\n===== Running sklearn baseline with seed={seed} =====")

        log_path = os.path.join(logs_dir,f"higgs_sklearn_seed{seed}.log")
        logger = logging.getLogger(f"sklearn_seed_{seed}")
        logger.setLevel(logging.INFO)
        logger.propagate = False
        handler = logging.FileHandler(log_path, mode="w",encoding="utf-8")
        handler.setFormatter(logging.Formatter("%(message)s"))
        logger.addHandler(handler)

        X_train, X_temp, y_train, y_temp = train_test_split(X, y, test_size=0.3, random_state=seed)
        X_valid, X_test, y_valid, y_test = train_test_split(X_temp, y_temp, test_size=0.5, random_state=seed)

        n_estimators = 500
        model = HistGradientBoostingClassifier(
            max_iter=n_estimators,
            learning_rate=0.1,
            max_depth=8,
            max_leaf_nodes=255,
            l2_regularization=1.0,
            early_stopping=False,
            random_state=seed,
        )

        start_time = time.time()
        model.fit(X_train,y_train)
        elapsed_time = time.time() - start_time

        time_per_tree = elapsed_time / n_estimators

        preds = model.predict_proba(X_test)[:, 1]
        auc = roc_auc_score(y_test,preds)
       
        logger.info(f"Average time per tree:{time_per_tree:.4f}s")
        logger.info(f"Test AUC:{auc:.4f}")

        print(f"Average time per tree:{time_per_tree:.4f}s")
        print(f"Test AUC:{auc:.4f}")

        fpr,tpr,thresholds = roc_curve(y_test,preds)
        plt.figure(figsize=(8,6))
        plt.plot(fpr,tpr,color='darkorange',lw=2,label=f'sklearn HistGB(AUC={auc:.4f})')
        plt.plot([0,1],[0,1],color='navy',lw=2,linestyle='--')
        plt.xlim([0.0,1.0])
        plt.ylim([0.0,1.05])
        plt.xlabel('False Positive Rate')
        plt.ylabel('True Positive Rate')
        plt.title('Receiver Operating Characteristic(Roc)')
        plt.legend(loc="lower right")
        
        
        plt.savefig(os.path.join(results_dir, f"roc_curve_sklearn_seed{seed}.png"), bbox_inches='tight')
        plt.close()
    
        print(f"ROC curve saved to results/roc_curve_sklearn_seed{seed}.png")
        
        
        results_row = {
            "method": "ssklearn_HistGB",
            "time_per_tree_sec":time_per_tree,
            "test_auc":auc,
            "seed":seed,
            "num_rounds": n_estimators,
        }

        out_path = os.path.join(results_dir,f"higgs_sklearn_seed{seed}.csv")
        pd.DataFrame([results_row]).to_csv(out_path,index=False)
        print(f"Results saved to {out_path}")

        all_results.append(results_row)
        logger.removeHandler(handler)
        handler.close()

    summary_df = pd.DataFrame(all_results)
    summary_path = os.path.join(results_dir,"higgs_sklearn_seeds_summary.csv")
    summary_df.to_csv(summary_path,index=False)
    print(f"Summary results saved to {summary_path}")


if __name__ == "__main__":
    main()