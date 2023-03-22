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
raters_1 = pd.DataFrame({'confirm_A': [0, 0, 1, 1, 1, 1, 1, 1, 1]})
raters_2 = pd.DataFrame({'confirm_B': [0, 0, 1, 1, 1, 1, 1, 1, 1]})

# Calculate cohen's kappa
kappa = cohen_kappa_score(rater1, rater2)
print(kappa)
```
## Example usage of Fleiss kappa
