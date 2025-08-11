"""
Create a csv viewr using python and built-in libraries.
@ostadsgo
Aug 11 2025
"""

import csv


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


def view():
    data = read("sample.csv")
    header = data[0]

    max_size = max_len(data)
    print('-' * (sum(max_size) + 3 * len(max_size) - 1))
    s = ""
    for h, mx in zip(header, max_size):
        s += f"{h:<{mx}} | "
    print(s)
    print("-" * (len(s) - 1))

    data = data[1:]
    for row in data:
        ss = ""
        for item, mx in zip(row, max_size):
            ss += f"{item:<{mx}} | "
        print(ss)
    print("-" * (len(s) - 1))


def main():
    view()


if __name__ == "__main__":
    main()
