from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

def load_series(csv_path: str, index_col: str, value_col: str) -> pd.Series:
    df = pd.read_csv(csv_path)
    s = pd.Series(df[value_col].values, index=df[index_col].astype(str), name=value_col)
    return s

def ensure_out_dir():
    Path("out").mkdir(exist_ok=True, parents=True)

def style_x_ticks(ax):
    for label in ax.get_xticklabels():
        label.set_rotation(45)
        label.set_ha('right')
    ax.margins(x=0.05)

def save_fig(fig, out: str | None, default_name: str) -> str:
    ensure_out_dir()
    out_path = out or f"out/{default_name}"
    fig.tight_layout()
    fig.savefig(out_path, bbox_inches="tight")
    return out_path
