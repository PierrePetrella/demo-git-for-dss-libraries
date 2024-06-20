import dataiku 
import pandas as pd
import numpy as np

def feat1_func(var1, var2):
    return var1 * var2

def transform_df(df):
    return df.describe()