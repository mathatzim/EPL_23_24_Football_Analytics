from __future__ import annotations

from .config import OUTPUTS
from .metrics import load_data
from .plots import scatter_with_regression, grouped_bar_home_away

def main() -> None:
    df = load_data()

    # A) xGD -> GD
    scatter_with_regression(
        df,
        x_col="Total_xGD",
        y_col="Total_GD",
        outpath=OUTPUTS / "01_total_xgd_vs_total_gd.png",
        title="Total Goal Difference vs Total Expected Goal Difference (EPL 2023-24)",
    )

    # B1) GD -> Points
    scatter_with_regression(
        df,
        x_col="Total_GD",
        y_col="Total_Points",
        outpath=OUTPUTS / "02_total_gd_vs_total_points.png",
        title="Total Points vs Total Goal Difference (EPL 2023-24)",
    )

    # B2) xGD -> Points
    scatter_with_regression(
        df,
        x_col="Total_xGD",
        y_col="Total_Points",
        outpath=OUTPUTS / "03_total_xgd_vs_total_points.png",
        title="Total Points vs Total Expected Goal Difference (EPL 2023-24)",
    )

    # C) Home advantage visuals
    grouped_bar_home_away(
        df,
        metric="Pts",
        outpath=OUTPUTS / "04_home_vs_away_points.png",
        title="Home vs Away Points by Team (EPL 2023-24)",
    )
    grouped_bar_home_away(
        df,
        metric="xGD",
        outpath=OUTPUTS / "05_home_vs_away_xgd.png",
        title="Home vs Away Expected Goal Difference (xGD) by Team (EPL 2023-24)",
    )

if __name__ == "__main__":
    main()
