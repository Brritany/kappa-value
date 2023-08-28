# Example usage of Fleiss kappa
import pandas as pd
import numpy as np
from statsmodels.stats.inter_rater import fleiss_kappa

# Prepare the dataset, suppose you have one datasets in DataFrame format
n_confirm = pd.DataFrame({
    'confirm_A': [0, 0, 1, 1, 1, 1, 1, 1, 1],
    'confirm_B': [0, 0, 1, 1, 1, 1, 1, 1, 1],
    'confirm_C': [0, 0, 1, 1, 1, 1, 1, 1, 0]
    })
"""
n_confirm represents a DataFrame containing n raters, 
where confirm_A represents the review content of rater A, 
confirm_B represents the review content of rater B, and 
confirm_C represents the review content of rater C, and 
its example content is a binary classification
"""

# Calculate Fleiss Kappa
def Fleiss_kappa(n_confirm: pd.DataFrame):
    # Count the number of each score (0 or 1) for each row, fill missing values with 0
    value_counts = n_confirm.apply(pd.value_counts, axis=1).fillna(0)
    # Compute Fleiss' Kappa using the counts
    return fleiss_kappa(value_counts.to_numpy())

Fleiss_kappa(n_confirm)
