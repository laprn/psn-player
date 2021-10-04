import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
import numpy as np


data = pd.read_csv('./psn_level.csv')
data.columns = ['level']
sns.set_theme()

# Load an example dataset
# data = sns.load_dataset('./psn_level.csv')

# Create a visualization
def main():
    plot()

def plot():
    fig = plt.figure(figsize=(15, 8))
    # print(data.max())
    plt.hist(data, bins=int(1600/10))
    # 対数をとる
    # log_data = [np.log10(i) for i in data['level'].tolist()]
    # plt.hist(log_data, bins=int(1600/10))
    plt.xlabel('level')
    plt.ylabel('count')
    plt.show()

if __name__ == '__main__':
    main()