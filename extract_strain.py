import pandas as pd
import numpy as np
from pathlib import Path

Bace_Dir = Path(__file__).parent
Process_Dir = Bace_Dir/'data'/'case1'
print(Process_Dir)
data_path = Process_Dir/'accumulate_result.csv'
result_test = pd.read_csv(data_path, index_col='Distance (m)')
result_df = result_test.copy()

# set the range of strain data
index_ch1 = (result_df.index > 13.961) & (result_df.index < 26.125)
index_ch2 = (result_df.index > 28.555) & (result_df.index < 40.752)
index_ch3 = (result_df.index > 43.020) & (result_df.index < 55.180)
index_ch4 = (result_df.index > 57.599) & (result_df.index < 69.800)

# check the length of range
index_chn = [index_ch1, index_ch2, index_ch3, index_ch4]
range_ch = [index_ch.sum() for index_ch in index_chn]
print(range_ch)

diff = max(range_ch) - range_ch
print(diff)
for i, ch in enumerate(range_ch):
    start = np.where(index_chn[i])[0][0]
    end = np.where(index_chn[i])[0][-1]
    if diff[i] == 0:
        pass
    else:
        right = diff[i] // 2
        left = diff[i] - right
        start = start -left
        end = end + right
    index_chn[i][start : end + 1] = True
range_ch_new = [index_ch.sum() for index_ch in index_chn]
print(range_ch_new)
# def reverse_strain()
