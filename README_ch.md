繁體中文 | [English](README.md)

# 協議

## 評分者間信度
在統計學中，評分者間信度（也稱為多種相似名稱，如評分者協議、評分者一致性、觀察者間信度、編碼者間信度等等）是指獨立評分、編碼或評估同一現象的觀察者之間的一致程度。

## Cohen's kappa
Cohen's Kappa是用來測量兩個評分者協議程度的指標。使用`sklearn.metrics.cohen_kappa_score`實現。

## Fleiss kappa
Fleiss Kappa是用來測量研究中有多於兩個評分者時的協議程度的指標。此外，Fleiss Kappa是Cohen's Kappa的擴展。使用`statsmodels.stats.inter_rater.fleiss_kappa`實現。

