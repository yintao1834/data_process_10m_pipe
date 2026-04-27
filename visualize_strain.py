import matplotlib.pyplot as plt
import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).parent
FILE_DIR = BASE_DIR/'data'/'case1'/'output'
fig = plt.figure(figsize=(20,10))
for i in range(1,13):
    df = pd.read_csv(FILE_DIR/f'output{2.5*i}-{2.5*i}.csv', index_col=0)
    signal = df.copy()
    plt.subplot(3,4,i)
    plt.plot(signal.index, signal['ch1'], label='ch1')
    plt.plot(signal.index, signal['ch2'], label='ch2')
    plt.plot(signal.index, signal['ch3'], label='ch3')
    plt.plot(signal.index, signal['ch4'], label='ch4')
    plt.title(f'{2.5*i}-{2.5*i}')
    plt.xlabel('Distance (m)')
    plt.ylabel('Strain')
    plt.tight_layout()
plt.show()