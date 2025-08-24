#!/usr/bin/env python3

"""
Create a csv viewr using python and built-in libraries.
@ostadsgo
Aug 11 2025
"""


## TODO
# [DONE]: Create line number
# [DONE]: Get head and tail of the data
# TODO: Trim empty line
# TODO: Do some useful stats at the end (like ave, max, min)
# [DONE]: Get specific row and column
# [DONE]: Head and tail of the data
# TODO: Defualt view should trim middle part for large data.
# TODO: Add custom range rows and columns options
# TODO: Connect this program features to tk table

## FIX
# [DONE] Generate number before string format

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


def max_len(columns):
    mx = []
    for column in columns:
        mx.append(len(max(column, key=len)))
    return mx


def max_cell_length(row):
    return max(row, key=len)


def view(data: list[Row]):
    columns = transponse(data)
    max_size = max_len(columns)

    # TOP Line
    print("-" * (sum(max_size) + 3 * len(max_size) + 2))

    # Header
    header = data.pop(0)
    s = ""
    for h, mx in zip(header, max_size):
        s += f"| {h:<{mx}} "
    s = f"{s} | "
    print(s)
    print("-" * (len(s) - 1))

    # Each row
    for row in data:
        ss = ""
        for cell, mx in zip(row, max_size):
            ss += f"| {cell:<{mx}} "
        ss = f"{ss} | "
        print(ss)

    # Bottom Line
    print("-" * (len(s) - 1))


def view_row(data, index_range):
    # If only one number passed (specific row)
    if len(index_range) == 1:
        index = index_range[0]
        if 0 < index < len(data):
            header = data[0]
            row = data[index]
            rows = [header, row]
            view(rows)
            return
        else:
            print(f"ERROR: No row in index {index}")
            return

    if len(index_range) == 2:
        start, end = index_range
        end += 1
        if start < end - start < end:
            header = data[0]
            row = data[start: end]
            rows = [header, *row]
            view(rows)
            return
        else:
            print(f"ERROR: start is to small or end is to big.")
            return

    # Check if there is more than 2 numbers
    if len(index_range) > 2:
        print("ERROR: Require start and end range.")
        return 


def view_column(data, index_range):

    if len(index_range) == 2:
        start, end = index_range
        end += 1
        header = data[0]
        header = header[start: end]
        data = data[start: end]
        rows = [header]
        for row in data:
            rows.append(row[start: end])

        view(rows)

    if len(index_range) == 1:
        index = index_range[0]
        new_data = [[row[0], row[index]] for row in data]
        view(new_data)


def view_head(data):
    view(data[:6])


def view_tail(data):
    header = data.pop(0)
    tail = data[-5:]
    new_data = [header, *tail]
    view(new_data)


def add_row_number(data):
    new_data = []
    header = data.pop(0)
    header.insert(0, "ROW")
    for index, row in enumerate(data, 1):
        new_data.append([str(index)] + row)
    new_data.insert(0, header)
    return new_data


def main():
    parser = argparse.ArgumentParser(description="CSV viewer")
    parser.add_argument("csvfile", nargs="?", help="CSV file name")
    parser.add_argument("-R", "--row",nargs='+', type=int, help="row number start from 1")
    parser.add_argument("-C", "--column", nargs='+', type=int, help="column number start from 1")
    parser.add_argument("-E", "--head", action="store_true", help="Head of the csv")
    parser.add_argument("-T", "--tail", action="store_true", help="tail of the csv")
    parser.add_argument(
        "-V", "--version", action="store_true", help="print version of the program"
    )

    args = parser.parse_args()

    if args.version:
        print("CSV viewer version 0.1")
        return

    data = read(args.csvfile)
    data = add_row_number(data)
    if args.row is not None:
        view_row(data, args.row)
    elif args.column is not None:
        view_column(data, args.column)
    elif args.head:
        view_head(data)
    elif args.tail:
        view_tail(data)
    else:
        view(data)


if __name__ == "__main__":
    main()
