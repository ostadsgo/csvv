"""
Create a csv viewr using python and built-in libraries.
@ostadsgo
Aug 11 2025
"""

# TODO: Create line number
# TODO: Get head and tail of the data
# TODO: Trim empty line
# TODO: Do some useful stats at the end (like ave, max, min)
# FIX: 

import csv
import sys

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


def view(data):
    header = data[0]

    max_size = max_len(data)
    print('-' * (sum(max_size) + 3 * len(max_size) + 2))
    s = ""
    for h, mx in zip(header, max_size):
        s += f"| {h:<{mx}} "
    s += " | " # last
    print(s)
    print("-" * (len(s) - 1))

    data = data[1:]
    for row in data:
        ss = ""
        for item, mx in zip(row, max_size):
            ss += f"| {item:<{mx}} "
        ss += " | "
        print(ss)
    print("-" * (len(s)-1))


def main():
    if len(sys.argv) < 2:
        print("Usage: \n\tpython csvv.py <csv_file>")
        return

    filename = sys.argv[1]
    data = read(filename)
    view(data)


if __name__ == "__main__":
    main()
