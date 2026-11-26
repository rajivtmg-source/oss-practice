import argparse
from tabulate import tabulate

parser = argparse.ArgumentParser()
parser.add_argument("--name", default="World")
args = parser.parse_args()

rows = [
    ["User", args.name],
    ["Library", "tabulate"],
    ["Language", "Python"]
]
print(tabulate(rows, headers=["Field", "Value"], tablefmt="grid"))
