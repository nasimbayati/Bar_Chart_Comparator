import matplotlib.pyplot as plt
from .utils import load_series, style_x_ticks, save_fig

def single_cli(subparsers):
    sp = subparsers.add_parser("single", help="Plot a single series as a bar chart.")
    sp.add_argument("--csv", required=True, help="Path to CSV.")
    sp.add_argument("--index-col", required=True, help="Index column (categories).")
    sp.add_argument("--value-col", required=True, help="Value column (numeric).")
    sp.add_argument("--title", default="Bar Chart", help="Figure title.")
    sp.add_argument("--out", default=None, help="Output image path.")
    return sp

def single_entry(args):
    s = load_series(args.csv, args.index_col, args.value_col)
    fig, ax = plt.subplots(1, 1, figsize=(7, 5))
    ax.bar(s.index, s.values, width=0.6)
    style_x_ticks(ax)
    ax.grid(True, axis="y")
    ax.set_title(args.title)
    ax.set_ylabel(s.name)
    ax.set_xlabel(args.index_col)
    path = save_fig(fig, args.out, "single.png")
    print(f"Wrote: {path}")
