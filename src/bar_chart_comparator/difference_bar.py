import matplotlib.pyplot as plt
from .utils import load_series, style_x_ticks, save_fig

def difference_cli(subparsers):
    sp = subparsers.add_parser("difference", help="Compute and plot (A - B) as bars.")
    sp.add_argument("--csv1", required=True, help="Path to CSV #1 (A).")
    sp.add_argument("--csv2", required=True, help="Path to CSV #2 (B).")
    sp.add_argument("--index-col", required=True, help="Shared index (categories).")
    sp.add_argument("--value-col", required=True, help="Value column in both CSVs.")
    sp.add_argument("--title", default="Difference", help="Figure title.")
    sp.add_argument("--out", default=None, help="Output image path.")
    return sp

def difference_entry(args):
    s1 = load_series(args.csv1, args.index_col, args.value_col)
    s2 = load_series(args.csv2, args.index_col, args.value_col)

    cats = list(dict.fromkeys(list(s1.index) + list(s2.index)))
    s1 = s1.reindex(cats).fillna(0)
    s2 = s2.reindex(cats).fillna(0)
    diff = s1 - s2

    fig, ax = plt.subplots(1, 1, figsize=(7, 5))
    ax.bar(diff.index, diff.values, width=0.6)
    style_x_ticks(ax)
    ax.grid(True, axis="y")
    ax.set_title(args.title)
    ax.set_ylabel(f"{s1.name} (A - B)")
    ax.set_xlabel(args.index_col)

    path = save_fig(fig, args.out, "difference.png")
    print(f"Wrote: {path}")
