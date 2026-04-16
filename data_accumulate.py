import pandas as pd
import numpy as np
from pathlib import Path
import charset_normalizer

# 生成文件路径
BASE_DIR = Path(__file__).parent
CASE_DIR = BASE_DIR/'data'/'case1' 
data_path = [CASE_DIR/f'{num}({2.5*num}-{2.5*num})_strain.csv' for num in range(1, 13)]

result_df = pd.DataFrame()
cumulative = None

for i in range(len(data_path)):
    df = pd.read_csv(data_path[i], encoding='cp932', usecols=['Distance (m)','Time 1'])
    if cumulative is None:
        cumulative = df['Time 1']
    else:
        cumulative = cumulative + df['Time 1']
    result_df[f'{2.5*(i+1)}-{2.5*(i+1)}'] = cumulative
result_df.index = df['Distance (m)']
print(result_df.head())

out_path = CASE_DIR/'accumulate_result.csv'
result_df.to_csv(out_path)