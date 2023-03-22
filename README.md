# agreement

## Inter-rater reliability
In statistics, inter-rater reliability (also called by various similar names, such as inter-rater agreement, inter-rater concordance, inter-observer reliability, inter-coder reliability, and so on) is the degree of agreement among independent observers who rate, code, or assess the same phenomenon.

# Cohen's kappa
Cohen’s Kappa is a metric used to measure the agreement of **two raters**. Implemented using `sklearn.metrics.cohen_kappa_score`

# Fleiss kappa
Fleiss’ Kappa is a metric used to measure the agreement when in the study **there are more than two raters**. Furthermore, the Fleiss’ Kappa is the extension of Cohen’s Kappa. Implemented using `statsmodels.stats.inter_rater.fleiss_kappa`

# Example usage of Cohen's kappa

### 1.Prepare the dataset
Suppose you have two datasets in DataFrame format
```
raters_1 = pd.DataFrame({'confirm_A': [0, 0, 1, 1, 1, 1, 1, 1, 1]})
```
