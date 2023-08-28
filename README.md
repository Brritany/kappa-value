![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)
![Version](https://img.shields.io/badge/version-1.0.0-blue)
![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)
[![Colab](https://img.shields.io/badge/Colab-Example-orange)](https://github.com/Brritany/search_impact_factor/blob/main/Example_Calculate_Kappa_Value.ipynb)
![Python Versions](https://img.shields.io/pypi/pyversions/kappa-value.svg?logo=python&logoColor=white)
![Coverage Status](https://coveralls.io/repos/github/Brritany/kappa-value/badge.svg?branch=main)

English | [繁體中文](README_ch.md)

# Example on Colab
<a href="https://colab.research.google.com/github/Brritany/kappa-value/blob/main/Example_Calculate_Kappa_Value.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

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
```

## Reference
1. [Cohen’s Kappa](https://real-statistics.com/reliability/interrater-reliability/cohens-kappa/)
2. [Fleiss’ Kappa](https://real-statistics.com/reliability/interrater-reliability/fleiss-kappa/)

## Tools
1. [pandas](https://pandas.pydata.org/)
2. [numpy](https://numpy.org/)
3. [sklearn.metrics.cohen_kappa_score](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.cohen_kappa_score.html)
4. [statsmodels.stats.inter_rater.fleiss_kappa](https://www.statsmodels.org/dev/generated/statsmodels.stats.inter_rater.fleiss_kappa.html)
