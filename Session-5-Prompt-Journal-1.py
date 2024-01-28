import numpy as np
from tabulate import tabulate

def generate_sin_table(start, end, num_entries):
    x_values = np.linspace(start, end, num_entries)
    sin_values = np.sin(x_values)

    table_data = [(a, b) for a, b in zip(x_values, sin_values)]
    table_headers = ["x", "sin(x)"]
    print(tabulate(table_data, headers=table_headers, floatfmt=".3f"))


def main():
    start_x = 0
    end_x = 2 * np.pi
    num_entries = 1000

    generate_sin_table(start_x, end_x, num_entries)

if __name__ == "__main__":
    main()