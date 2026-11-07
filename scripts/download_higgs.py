import os
import urllib.request
import gzip

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def  download_and_extract():

    data_dir = os.path.join(base_dir,"data")
    os.makedirs(data_dir,exist_ok=True)

    raw_url = "https://archive.ics.uci.edu/ml/machine-learning-databases/00280/HIGGS.csv.gz"
    raw_path = os.path.join(data_dir,"HIGGS.csv.gz")
    subset_path = os.path.join(data_dir,"HIGGS_1M.csv")

    if not os.path.exists(raw_path):
        print("Downloading data(approx. 2.7GB),please wait...")
        urllib.request.urlretrieve(raw_url,raw_path)
        print("Download complete!")
    else:
        print("Data already exists.Skipping download.")

    if not os.path.exists(subset_path):
        print("Extracting the first 1,000,000 rows...")
        
        actual_rows = 0
        target_rows = 1_000_000

        with gzip.open(raw_path,'rt') as f_in,open(subset_path,'w')as f_out:
            for i in range(target_rows):
                line = f_in.readline()
                if not line:
                    break
                f_out.write(line)
                actual_rows += 1

        if actual_rows <target_rows:
            print(f"Data only got{actual_rows}")
            os.remove(subset_path)
            raise RuntimeError("Dataset is incomplete. Please check the raw download file.")
        else:
            print(f"Extraction complete.Save to {subset_path}")
    else:
        print("Subset data already exists.Skipping extraction.")

if __name__ == "__main__":
    download_and_extract()              


