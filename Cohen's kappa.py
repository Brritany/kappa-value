# Example usage of Cohen's kappa
import pandas as pd
import numpy as np
from sklearn.metrics import cohen_kappa_score

# Prepare the dataset, suppose you have two datasets in DataFrame format
raters_1 = pd.DataFrame({'confirm_A': [0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0]})
raters_2 = pd.DataFrame({'confirm_B': [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0]})

# Calculate cohen's kappa
kappa = cohen_kappa_score(raters_1, raters_2)
print(kappa)
