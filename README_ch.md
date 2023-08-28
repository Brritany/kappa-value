![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)
![Version](https://img.shields.io/badge/version-1.0.0-blue)
![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)
[![Colab](https://img.shields.io/badge/Colab-Example-orange)](https://github.com/Brritany/search_impact_factor/blob/main/Example_Calculate_Kappa_Value.ipynb)

繁體中文 | [English](README.md)

# 示範代碼
<a href="https://colab.research.google.com/github/Brritany/kappa-value/blob/main/Example_Calculate_Kappa_Value.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

# 協議

## 評分者間信度
在統計學中，評分者間信度（也稱為多種相似名稱，如評分者協議、評分者一致性、觀察者間信度、編碼者間信度等等）是指獨立評分、編碼或評估同一現象的觀察者之間的一致程度。

## Cohen's kappa
Cohen's Kappa是用來測量兩個評分者協議程度的指標。使用`sklearn.metrics.cohen_kappa_score`實現。

## Fleiss kappa
Fleiss Kappa是用來測量研究中有多於兩個評分者時的協議程度的指標。此外，Fleiss Kappa是Cohen's Kappa的擴展。使用`statsmodels.stats.inter_rater.fleiss_kappa`實現。

## 範例 Cohen's kappa
```
import pandas as pd
import numpy as np
from sklearn.metrics import cohen_kappa_score

# 準備數據集，假設您有兩個DataFrame格式的數據集
raters_1 = pd.DataFrame({'confirm_A': [0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0]})
raters_2 = pd.DataFrame({'confirm_B': [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0]})

# 計算 Cohen's kappa值
kappa = cohen_kappa_score(raters_1, raters_2)
print(kappa)
```
## 範例 Fleiss kappa
```
import pandas as pd
import numpy as np
from statsmodels.stats.inter_rater import fleiss_kappa

# 準備數據集，假設您有3個DataFrame格式的數據集
n_confirm = pd.DataFrame({
    'confirm_A': [0, 0, 1, 1, 1, 1, 1, 1, 1],
    'confirm_B': [0, 0, 1, 1, 1, 1, 1, 1, 1],
    'confirm_C': [0, 0, 1, 1, 1, 1, 1, 1, 0]
    })
"""
n_confirm是一個包含n位評分者的DataFrame，
其中confirm_A代表評分者A的評論內容，confirm_B代表評分者B的評論內容，confirm_C代表評分者C的評論內容，其示例內容為二元分類。
"""

# 計算 Fleiss_kappa
def Fleiss_kappa(n_confirm: pd.DataFrame):
    # Count the number of each score (0 or 1) for each row, fill missing values with 0
    value_counts = n_confirm.apply(pd.value_counts, axis=1).fillna(0)
    # Compute Fleiss' Kappa using the counts
    return fleiss_kappa(value_counts.to_numpy())

Fleiss_kappa(n_confirm)
```

## 參考文獻
[Cohen’s Kappa](https://real-statistics.com/reliability/interrater-reliability/cohens-kappa/)
[Fleiss’ Kappa](https://real-statistics.com/reliability/interrater-reliability/fleiss-kappa/)

## 使用工具
[pandas](https://pandas.pydata.org/)
[numpy](https://numpy.org/)
[sklearn.metrics.cohen_kappa_score](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.cohen_kappa_score.html)
[statsmodels.stats.inter_rater.fleiss_kappa](https://www.statsmodels.org/dev/generated/statsmodels.stats.inter_rater.fleiss_kappa.html)
