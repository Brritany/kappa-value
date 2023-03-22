# agreement

## Inter-rater reliability
In statistics, inter-rater reliability (also called by various similar names, such as inter-rater agreement, inter-rater concordance, inter-observer reliability, inter-coder reliability, and so on) is the degree of agreement among independent observers who rate, code, or assess the same phenomenon.

## Cohen's kappa
Cohen’s Kappa is a metric used to measure the agreement of **two raters**. Implemented using `sklearn.metrics.cohen_kappa_score`

## Fleiss kappa
Fleiss’ Kappa is a metric used to measure the agreement when in the study **there are more than two raters**. Furthermore, the Fleiss’ Kappa is the extension of Cohen’s Kappa. Implemented using `statsmodels.stats.inter_rater.fleiss_kappa`

## Example usage of Cohen's kappa
```
# Install necessary packages
import pandas as pd
import numpy as np
from sklearn.metrics import cohen_kappa_score

# Prepare the dataset, suppose you have two datasets in DataFrame format
raters_1 = pd.DataFrame({'confirm_A': [0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0]})
raters_2 = pd.DataFrame({'confirm_B': [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0]})

# Calculate cohen's kappa
kappa = cohen_kappa_score(raters_1, raters_2)
print(kappa)
```
## Example usage of Fleiss kappa
```
# Install necessary packages
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
n_confirm represents a DataFrame containing n raters, where confirm_A represents the review content of rater A, confirm_B represents the review content of rater B, and confirm_C represents the review content of rater C, and its example content is a binary classification
"""

# Calculate cohen's kappa
def Fleiss_kappa(n_confirm: pd.DataFrame):    
    df = pd.DataFrame()
    value_counts = n_confirm.apply(pd.value_counts, axis=1)
    for value in value_counts:
        df[value] = value_counts[value]
        df.fillna(value=0, inplace=True)   

    result = fleiss_kappa(np.array(df))
    return result

Fleiss_kappa(n_confirm)
```
