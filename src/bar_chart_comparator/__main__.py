import argparse
from .single_bar import single_cli, single_entry
from .double_bar import double_cli, double_entry
from .difference_bar import difference_cli, difference_entry

def main():
    parser = argparse.ArgumentParser(prog="bar_chart_comparator", description="Create bar chart comparisons from CSV data.")
    sub = parser.add_subparsers(dest="cmd", required=True)

    single_cli(sub)
    double_cli(sub)
    difference_cli(sub)

    args = parser.parse_args()
    if args.cmd == "single":
        single_entry(args)
    elif args.cmd == "double":
        double_entry(args)
    elif args.cmd == "difference":
        difference_entry(args)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
