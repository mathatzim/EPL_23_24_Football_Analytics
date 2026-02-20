from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

from .config import DATA_RAW

DATA_FILE = DATA_RAW / "epl_23_24_home_away_xg_xga.csv"

@dataclass(frozen=True)
class RegressionResult:
    x_col: str
    y_col: str
    pearson_r: float
    r2: float
    slope: float
    intercept: float

def load_data(path: Path = DATA_FILE) -> pd.DataFrame:
    return pd.read_csv(path)

def pearson_r(x: np.ndarray, y: np.ndarray) -> float:
    return float(np.corrcoef(x, y)[0, 1])

def simple_regression(df: pd.DataFrame, x_col: str, y_col: str) -> RegressionResult:
    x = df[x_col].to_numpy(dtype=float).reshape(-1, 1)
    y = df[y_col].to_numpy(dtype=float)
    model = LinearRegression().fit(x, y)
    return RegressionResult(
        x_col=x_col,
        y_col=y_col,
        pearson_r=pearson_r(df[x_col].to_numpy(dtype=float), y),
        r2=float(model.score(x, y)),
        slope=float(model.coef_[0]),
        intercept=float(model.intercept_),
    )

def home_away_summary(df: pd.DataFrame) -> dict:
    return {
        "home_points_mean": float(df["home_Pts"].mean()),
        "away_points_mean": float(df["away_Pts"].mean()),
        "home_xgd_mean": float(df["home_xGD"].mean()),
        "away_xgd_mean": float(df["away_xGD"].mean()),
        "home_wins_mean": float(df["home_W"].mean()),
        "away_wins_mean": float(df["away_W"].mean()),
        "home_losses_mean": float(df["home_L"].mean()),
        "away_losses_mean": float(df["away_L"].mean()),
    }
