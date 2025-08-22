"""
Create a csv viewr using python and built-in libraries.
@ostadsgo
Aug 11 2025
"""

# TODO: Create line number
# TODO: Get head and tail of the data
# TODO: Trim empty line
# TODO: Do some useful stats at the end (like ave, max, min)
# * TODO: Get specific row and column
# TODO: Head and tail of the data 
# TODO: Defualt view should trim middle part for large data.

# FIX:

import csv
import sys
import argparse

Row = list[str]

def read(filename: str):
    with open(filename, "r") as csv_file:
        reader = csv.reader(csv_file)
        data = list(reader)
    return data


def transponse(data):
    return list(zip(*data))


def max_len(data):
    mx = []
    columns = transponse(data)
    for column in columns:
        mx.append(len(max(column, key=len)))
    return mx


def view(data: list[Row]):
    header = data[0]

    max_size = max_len(data)
    print("-" * (sum(max_size) + 3 * len(max_size) + 2))
    s = ""
    for h, mx in zip(header, max_size):
        s += f"| {h:<{mx}} "
    s += " | "  # last
    print(s)
    print("-" * (len(s) - 1))

    data = data[1:]
    for row in data:
        ss = ""
        for item, mx in zip(row, max_size):
            ss += f"| {item:<{mx}} "
        ss += " | "
        print(ss)
    print("-" * (len(s) - 1))




def get_row(data, index):
    if index < len(data):
        header = data[0]
        row = data[index]
        rows = [header, row]
        view(rows)
        return
    print("Row index out of range.")


def main():
    parser = argparse.ArgumentParser(description="CSV viewer")
    parser.add_argument("csvfile", help="CSV file name")
    parser.add_argument("-R", "--row", type=int, help="row number start from 1")
    parser.add_argument("-C", "--column", type=int, help="column number start from 1")
    parser.add_argument("-V", "--version", help="print version of the program")

    args = parser.parse_args()
    data = read(args.csvfile)

    if args.version:
        print("CSV viewer version 0.1")
        return

    if args.row is not None:
        get_row(data, args.row)
    elif args.column is not None:
        print("column")
    else:
        view(data)


if __name__ == "__main__":
    main()
