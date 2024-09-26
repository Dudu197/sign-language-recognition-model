import pandas as pd
from datetime import datetime
from model_training import ModelTraining

model_training = ModelTraining()
print("Loading dataset")
print(datetime.now())

dataset_name = model_training.args.dataset_name


if dataset_name == "minds":
    df = pd.read_csv("datasets/libras_minds_openpose.csv")
    if "person" not in df.columns:
        import re
        df["person"] = df["video_name"].apply(lambda i: int(re.findall(r".*Sinalizador(\d+)-.+.mp4", i)[0]))
else:
    raise ValueError("Invalid dataset name")

epochs = 20

model_training.train(df, epochs)
