import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt


df = pd.read_csv('./psn_level.csv', sep=',')
df.columns = ['level']
print(df.head())
sns.set_theme()

# Load an example dataset
# data = sns.load_dataset('./psn_level.csv')

# Create a visualization
sns.histplot(df.level)
plt.show()
