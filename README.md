# Bar_Chart_Comparator

A small CLI toolkit to create side-by-side bar charts and difference charts from one or two CSV files—clean, generic, and portfolio-ready. No course text or proprietary files.

## Features
- **single**: plot a single series as a bar chart.
- **double**: plot two series on separate bars and a combined comparison (grouped bars).
- **difference**: compute and plot the difference (A - B) as bars.
- Smart label rotation for long category names.

## Quick start
```bash
pip install -r requirements.txt
python -m bar_chart_comparator --help
```

### Examples (using included sample CSVs)
```bash
# Single series
python -m bar_chart_comparator single   --csv examples/grain_load_a.csv --index-col Grain --value-col Weight   --title "Load A Weights" --out out/single.png

# Two series grouped + individual subplots
python -m bar_chart_comparator double   --csv1 examples/grain_load_a.csv --csv2 examples/grain_load_b.csv   --index-col Grain --value-col Weight   --title "Loads A vs B" --out out/double.png

# Difference (A - B)
python -m bar_chart_comparator difference   --csv1 examples/grain_load_a.csv --csv2 examples/grain_load_b.csv   --index-col Grain --value-col Weight   --title "Difference in Weights" --out out/diff.png
```

## CSV format
At minimum, an index column (e.g., `Grain`) and a numeric value column (e.g., `Weight`). See `examples/`.

## Notes
- Pure Matplotlib (no seaborn), no fixed colors, 45° x-label rotation.
- Outputs are saved to `out/`.
- MIT licensed.
