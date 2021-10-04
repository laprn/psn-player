import seaborn as sns

sns.set_theme()

# Load an example dataset
tips = sns.load_dataset('psn_level.csv')

# Create a visualization
sns.relplot(
    data=tips,
    x="total_bill", y="tip", col="time",
    hue="smoker", style="smoker", size="size",
)
