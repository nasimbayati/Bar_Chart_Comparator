import numpy as np
import matplotlib.pyplot as plt
from .utils import load_series, style_x_ticks, save_fig

def double_cli(subparsers):
    sp = subparsers.add_parser("double", help="Plot two series: two single bar charts plus a grouped comparison.")
    sp.add_argument("--csv1", required=True, help="Path to CSV #1.")
    sp.add_argument("--csv2", required=True, help="Path to CSV #2.")
    sp.add_argument("--index-col", required=True, help="Shared index (categories).")
    sp.add_argument("--value-col", required=True, help="Value column in both CSVs.")
    sp.add_argument("--title", default="Comparison", help="Overall figure title.")
    sp.add_argument("--out", default=None, help="Output image path.")
    return sp

def double_entry(args):
    s1 = load_series(args.csv1, args.index_col, args.value_col)
    s2 = load_series(args.csv2, args.index_col, args.value_col)

    # Align indexes
    cats = list(dict.fromkeys(list(s1.index) + list(s2.index)))
    s1 = s1.reindex(cats).fillna(0)
    s2 = s2.reindex(cats).fillna(0)

    x = np.arange(len(cats))
    width = 0.35

    fig = plt.figure(figsize=(8, 8))
    ax1 = fig.add_subplot(3, 1, 1)
    ax2 = fig.add_subplot(3, 1, 2)
    ax3 = fig.add_subplot(3, 1, 3)

    # Chart 1
    ax1.bar(cats, s1.values, width=0.6)
    style_x_ticks(ax1)
    ax1.grid(True, axis="y")
    ax1.set_title(f"{args.title} — Series 1")
    ax1.set_ylabel(s1.name)

    # Chart 2
    ax2.bar(cats, s2.values, width=0.6)
    style_x_ticks(ax2)
    ax2.grid(True, axis="y")
    ax2.set_title(f"{args.title} — Series 2")
    ax2.set_ylabel(s2.name)

    # Grouped comparison
    ax3.bar(x - width/2, s1.values, width, label="Series 1")
    ax3.bar(x + width/2, s2.values, width, label="Series 2")
    ax3.set_xticks(x)
    ax3.set_xticklabels(cats)
    style_x_ticks(ax3)
    ax3.grid(True, axis="y")
    ax3.set_title(f"{args.title} — Grouped Comparison")
    ax3.set_ylabel(s1.name)
    ax3.set_xlabel(args.index_col)
    ax3.legend(loc="best")

    fig.suptitle(args.title)
    path = save_fig(fig, args.out, "double.png")
    print(f"Wrote: {path}")
