import pandas as pd
import numpy as np
import random
import glob
import os
import gc

import warnings
warnings.simplefilter('ignore')

class CFG:
    path:str = "../input/tabular-playground-series-nov-2022"
    gpu:bool = True
    n_splits:int = 5
    seed:int = 42
    pred = 'pred'
    target = 'label'

def seed_everything(seed=42):
    random.seed(seed)
    os.environ['PYTHONHASHSEED'] = str(seed)
    cupy.random.seed(seed)

seed_everything(CFG.seed)

#labels = pd.read_csv(os.path.join(CFG.path, "train_labels.csv"))
#submission = pd.read_csv(os.path.join(CFG.path, "sample_submission.csv"))
