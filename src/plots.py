from __future__ import annotations

from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from .metrics import simple_regression

def _save(fig, outpath: Path) -> None:
    outpath.parent.mkdir(parents=True, exist_ok=True)
    fig.tight_layout()
    fig.savefig(outpath, dpi=200)
    plt.close(fig)

def scatter_with_regression(df: pd.DataFrame, x_col: str, y_col: str, outpath: Path, title: str) -> None:
    res = simple_regression(df, x_col, y_col)
    x = df[x_col].to_numpy(dtype=float)
    y = df[y_col].to_numpy(dtype=float)

    fig, ax = plt.subplots(figsize=(7.5, 5))
    ax.scatter(x, y)
    # regression line
    x_line = np.linspace(x.min(), x.max(), 200)
    y_line = res.intercept + res.slope * x_line
    ax.plot(x_line, y_line)

    ax.set_title(title)
    ax.set_xlabel(x_col)
    ax.set_ylabel(y_col)

    ax.text(
        0.02,
        0.98,
        f"Pearson r = {res.pearson_r:.4f}\nR² = {res.r2:.4f}\nSlope = {res.slope:.2f}",
        transform=ax.transAxes,
        va="top",
        ha="left",
        fontsize=10,
        bbox=dict(boxstyle="round,pad=0.3", alpha=0.1),
    )
    _save(fig, outpath)

def grouped_bar_home_away(df: pd.DataFrame, metric: str, outpath: Path, title: str) -> None:
    # metric should be one of: Pts, xGD, GF, GA, etc.
    home_col = f"home_{metric}"
    away_col = f"away_{metric}"
    if home_col not in df.columns or away_col not in df.columns:
        raise KeyError(f"Missing columns {home_col} / {away_col}")

    teams = df["Squad"].tolist()
    home = df[home_col].to_numpy(dtype=float)
    away = df[away_col].to_numpy(dtype=float)

    x = np.arange(len(teams))
    width = 0.4

    fig, ax = plt.subplots(figsize=(12, 6))
    ax.bar(x - width/2, home, width, label="Home")
    ax.bar(x + width/2, away, width, label="Away")

    ax.set_xticks(x)
    ax.set_xticklabels(teams, rotation=60, ha="right")
    ax.set_ylabel(metric)
    ax.set_title(title)
    ax.legend()
    _save(fig, outpath)
