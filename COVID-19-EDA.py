import math
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import ttest_ind

file_path = '/content/drive/MyDrive/dataset.xlsx'

data = pd.read_excel(file_path)

df = data.copy()

#affiche les 5 premières lignes 
df.head()
# Affiche la taille du dataset (lignes, colonnes)
df.shape
# Compte le nombre de colonnes par type de données
df.dtypes.value_counts()

(df.isna().mean() * 100).sort_values(ascending=False)

df = df.loc[:, df.isna().mean() < 0.9]
df = df.drop(columns=["Patient ID"])

df.shape

df["SARS-Cov-2 exam result"].value_counts(normalize=True) * 100

float_cols = df.select_dtypes(include="float").columns
object_cols = df.select_dtypes(include="object").columns

num_float_cols = len(float_cols)
plots_per_row = 4

for i in range(0, num_float_cols, plots_per_row):
    current_cols = float_cols[i : i + plots_per_row]
    num_current_plots = len(current_cols)

    fig, axes = plt.subplots(1, num_current_plots, figsize=(4 * num_current_plots, 4))

    # Ensure axes is an array even for a single plot
    if num_current_plots == 1:
        axes = [axes]

    for j, col in enumerate(current_cols):
        sns.histplot(df[col].dropna(), kde=True, ax=axes[j])
        axes[j].set_title(col)

    plt.tight_layout()
    plt.show()




cols = float_cols
n_cols = 7
n_rows = math.ceil(len(cols) / n_cols)

fig, axes = plt.subplots(n_rows, n_cols, figsize=(5*n_cols, 4*n_rows))
axes = axes.flatten()

for i, col in enumerate(cols):
    sns.histplot(df[df["SARS-Cov-2 exam result"]=="positive"][col].dropna(),
                 color="green", label="Positive", kde=True, ax=axes[i], stat="density", alpha=0.5)
    sns.histplot(df[df["SARS-Cov-2 exam result"]=="negative"][col].dropna(),
                 color="red", label="Negative", kde=True, ax=axes[i], stat="density", alpha=0.5)
    axes[i].set_title(col)
    axes[i].legend()

# Remove empty subplots
for j in range(i + 1, len(axes)):
    fig.delaxes(axes[j])

plt.tight_layout()
plt.show()


pd.crosstab(df["Influenza A"], df["SARS-Cov-2 exam result"])

df["est_malade"] = df[object_cols].notna().any(axis=1)
pd.crosstab(df["est_malade"], df["SARS-Cov-2 exam result"])

sns.heatmap(df[float_cols].corr(), cmap="coolwarm")
plt.show()


significant_vars = []

for col in float_cols:
    pos = df[df["SARS-Cov-2 exam result"]=="positive"][col].dropna()
    neg = df[df["SARS-Cov-2 exam result"]=="negative"][col].dropna()
    stat, p = ttest_ind(pos, neg, equal_var=False)
    if p < 0.05:
        significant_vars.append(col)

significant_vars

(x_train, y_train) ,(x_test, y_test) 