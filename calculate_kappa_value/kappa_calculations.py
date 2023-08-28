from tqdm.notebook import tqdm
tqdm.pandas()

import pandas as pd
import numpy as np

from sklearn.metrics import cohen_kappa_score
from statsmodels.stats.inter_rater import fleiss_kappa

# Fix the random seed for reproducibility
np.random.seed(42)

# Data generation
ids = [f'ID_{i}' for i in range(1, 51)]
random_ids = np.random.choice(ids, 300)
data = {'ID': random_ids}
data.update({f'confirm_{i+1}': np.random.randint(0, 2, 300) for i in range(6)})
df = pd.DataFrame(data)

# Uncomment to use your own dataset
# df = pd.read_excel("your_dataset.xlsx")

# Check if specified columns exist in DataFrame
def check_columns_exist(df, columns):
    return all(col in df.columns for col in columns)

# Calculate Cohen's Kappa; Ensure necessary columns exist
def calculate_cohen_kappa(df, rater_columns):
    if not check_columns_exist(df, rater_columns):
        return "Missing columns in DataFrame."

    return {f'{r1}_vs_{r2}': cohen_kappa_score(df[r1], df[r2])
            for i, r1 in enumerate(rater_columns)
            for j, r2 in enumerate(rater_columns) if i < j}

# Calculate Fleiss Kappa
def Fleiss_kappa(df):
    # Count the number of each score (0 or 1) for each row, fill missing values with 0
    value_counts = df.progress_apply(pd.value_counts, axis=1).fillna(0)
    # Compute Fleiss' Kappa using the counts
    return fleiss_kappa(value_counts.to_numpy())

# Calculate Kappa for each unique ID
def calculate_kappa_per_id(df, rater_columns):
    if not check_columns_exist(df, ['ID'] + rater_columns):
        return "Missing columns in DataFrame."

    grouped = df.groupby("ID")
    kappa_scores = []

    for name, group in tqdm(grouped):
        if len(group) < 2: # Skip groups with fewer than 2 rows
            continue

        kappa_values = {'ID': name, 'Fleiss Kappa': Fleiss_kappa(group[rater_columns])}

        for i, r1 in enumerate(rater_columns):
            for j, r2 in enumerate(rater_columns):
                if i >= j:
                    continue
                kappa = cohen_kappa_score(group[r1], group[r2]) if len(set(group[r1])) > 1 and len(set(group[r2])) > 1 else 'N/A'
                kappa_values[f'{r1}_vs_{r2}'] = kappa

        kappa_scores.append(kappa_values)

    return pd.DataFrame(kappa_scores)
