# Dataset

This repository uses a single season-level dataset for the **English Premier League (EPL) 2023-2024** season with **20 teams** and home/away split performance metrics.

Source (as cited in the report): Kaggle notebook input:
- https://www.kaggle.com/code/plavak10/epl-23-24-home-away-xg-xga/input

Files:
- `epl_23_24_home_away_xg_xga.xls` – working dataset used for the analysis (includes derived total columns).
- `epl_23_24_home_away_xg_xga.csv` – CSV export of the above for easy reuse.
- `epl_23_24_original_dataset.xls` – original dataset version prior to adding derived totals.

Derived totals (computed in the report):
- Total MP = home MP + away MP
- Total Points = home Points + away Points
- Total xGD = home xGD + away xGD
- Total GD = home GD + away GD
