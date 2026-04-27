import pandas as pd
import numpy as np
from pathlib import Path
import matplotlib.pyplot as plt

BASE_DIR = Path(__file__).parent
CASE_DIR = BASE_DIR/'data'/'case1' 
data_path = [CASE_DIR/f'{num}({2.5*num}-{2.5*num})_strain.csv' for num in range(1, 13)]

result_df = pd.DataFrame()
fig = plt.figure(figsize=(20,10))
cumulative = None

for i in range(len(data_path)):
    df = pd.read_csv(data_path[i], encoding='cp932', usecols=['Distance (m)','Time 1'])
    df_copy = df.copy()
    mask1 = df_copy['Distance (m)'].between(13.961, 26.125) | df_copy['Distance (m)'].between(28.555, 40.752) | \
    df_copy['Distance (m)'].between(43.020, 55.180) | df_copy['Distance (m)'].between(57.599, 69.800)
    mask2 = (df_copy['Time 1'] > 30) | (df_copy['Time 1'] < -30)
    df_copy.loc[~mask1, 'Time 1'] = 0
    df_copy.loc[mask2, 'Time 1'] = 0
    plt.subplot(3,4,i+1)
    plt.plot(df_copy['Distance (m)'], df_copy['Time 1'])
    plt.title(f'{2.5*(i+1)}-{2.5*(i+1)}', pad=5, fontsize=10)
    plt.xlabel('Distance (m)', fontsize=8)
    plt.ylabel('Strain', fontsize=8)
    plt.tight_layout() 
plt.show()
#     if cumulative is None:
#          cumulative = df_copy['Time 1']
#     else:
#         cumulative = cumulative + df_copy['Time 1']
#     result_df[f'{2.5*(i+1)}-{2.5*(i+1)}'] = cumulative
# result_df.index = df_copy['Distance (m)']
# print(result_df.head())
# out_path = CASE_DIR/'accumulate_result_new.csv'
# result_df.to_csv(out_path)
    

    

