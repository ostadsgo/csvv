#!/usr/bin/env python3

"""
Create a csv viewr using python and built-in libraries.
@ostadsgo
Aug 11 2025
"""


# TODO: Create line number
# TODO: Get head and tail of the data
# TODO: Trim empty line
# TODO: Do some useful stats at the end (like ave, max, min)
# [DONE]: Get specific row and column
# TODO: Head and tail of the data 
# TODO: Defualt view should trim middle part for large data.

# FIX:

import csv
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


def max_cell_length(row):
    return max(row, key=len)


def view(data: list[Row]):

    max_size = max_len(data)
    # TOP Line
    print("-" * (sum(max_size) + 3 * len(max_size) + 8))

    # Header
    header = data.pop(0)
    s = ""
    for h, mx in zip(header, max_size):
        s += f"| {h:<{mx}} "
    s = f"| ROW {s} | "
    print(s)
    print("-" * (len(s) - 1))

    # Each row
    for i, row in enumerate(data, 1):
        ss = ""
        for cell, mx in zip(row, max_size):
            ss += f"| {cell:<{mx}} "
        ss = f"| {i:<3} {ss} | "
        print(ss)
    
    # Bottom Line
    print("-" * (len(s) - 1))




def view_row(data, index):
    if index < len(data):
        header = data[0]
        row = data[index]
        rows = [header, row]
        view(rows)
        return

    print("Row index out of range.")


def view_column(data, index):
    columns = transponse(data)
    if index <= 0 or index > len(columns):
        print("ERROR: Column index out of range.")
        return 
    column = columns[index - 1]
    max_cell_len = len(max(column, key=len))
    header = column[0]
    cells = column[1:]

    print(max_cell_len)
    print("-" * (max_cell_len + 4))
    print(f"| {header:<{max_cell_len}} |")
    print("-" * (max_cell_len + 4))

    # ROW
    for cell in cells:
        print(f"| {cell:<{max_cell_len}} |")

    print("-" * (max_cell_len + 4))



def main():
    parser = argparse.ArgumentParser(description="CSV viewer")
    parser.add_argument("csvfile",  nargs='?', help="CSV file name")
    parser.add_argument("-R", "--row", type=int, help="row number start from 1")
    parser.add_argument("-C", "--column", type=int, help="column number start from 1")
    parser.add_argument("-V", "--version", action="store_true", help="print version of the program")

    args = parser.parse_args()

    if args.version:
        print("CSV viewer version 0.1")
        return

    data = read(args.csvfile)
    if args.row is not None:
        view_row(data, args.row)
    elif args.column is not None:
        view_column(data, args.column)
    else:
        view(data)


if __name__ == "__main__":
    main()
