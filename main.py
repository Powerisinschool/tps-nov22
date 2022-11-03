import pandas as pd
import numpy as np
import random
import glob
import os
import gc

from tqdm import tqdm, trange

import warnings
warnings.simplefilter('ignore')

class CFG:
    path:str = "./input/"
    gpu:bool = True
    n_splits:int = 5
    seed:int = 42
    pred = 'pred'
    target = 'label'

def seed_everything(seed=42):
    random.seed(seed)
    os.environ['PYTHONHASHSEED'] = str(seed)
    np.random.seed(seed)

seed_everything(CFG.seed)

labels = pd.read_csv(os.path.join(CFG.path, "train_labels.csv"))
#submission = pd.read_csv(os.path.join(CFG.path, "sample_submission.csv"))

labels = labels.astype({"label": "int8"}).dtypes

all_df = pd.DataFrame(np.zeros(40000), columns=['id'])
all_df['id'] = all_df.index

file_list = sorted(glob.glob(os.path.join(CFG.path, "submission_files/*.csv")))
for idx, file in enumerate(tqdm(file_list)):
    all_df[f'pred_{idx}'] = pd.read_csv(file)[CFG.pred]

train = all_df[:labels.shape[0]]
train[CFG.target] = labels[CFG.target]
test = all_df[labels.shape[0]:].reset_index(drop=True)

del labels
del all_df
gc.collect()

train.to_csv('train.csv')

del train
gc.collect()

test.to_csv('test.csv')

del test
gc.collect()
