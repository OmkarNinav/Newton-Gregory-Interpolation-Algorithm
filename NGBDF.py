difference_table = []

input_file = "ex1.csv"
with open(input_file) as csv_file:
    # Reads The Data From CSV file and returns x and y values
    temp_x_vals = []
    temp_y_vals = []
    csv_file.readline()
    for row in csv_file:
        data = row.strip('\n').split(',')
        val, y = data

        temp_y_vals.append(float(y))
        temp_x_vals.append(float(val))
    h = temp_x_vals[1] - temp_x_vals[0]

difference_table.append(temp_y_vals)


def factorial(num: int) -> int:
    """
        Return n! (0! is 1).
        Valid for `n` in the range 0 to 998 (inclusive).
        Larger values of `n` will cause a RecursionError.
    """
    if num == 0:
        return 1
    else:
        return num * factorial(num - 1)


def diff_table_row(prev_row: list) -> list:
    """
        Creates a row of Difference Table from the given row
    :param
        prev_row: Row for which next row to be calculated
    """
    res = []

    for ele in range(len(prev_row) - 1):
        res.append(prev_row[ele + 1] - prev_row[ele])
    return res


for i in range(0, len(temp_x_vals) - 1):
    difference_table.append(diff_table_row(difference_table[i]))  # Calculates a ▽ⁱy and adds it to difference_table


def ngbdf(diff_table: list, x: float) -> float:
    """
        Calculates unknown value using Newton Gregory Forward Difference Formula
        f(x) = f(xₙ) + u▽f(xₙ) + u(u+1)/2!▽²f(xₙ) + u(u+1)(u+2)/2!▽³f(xₙ) + ... + u(u+1)(u+2)...(u+n-1)/n!▽ⁿf(xₙ)
    :param diff_table: Difference Table
    :param x: Unknown Value to fond
    :return: Value of 'f(x)'
    """
    u_values = [1]
    algo = []
    u = (x - temp_x_vals[-1]) / h
    for k in range(0, len(diff_table)):

        if k == 0:
            algo.append(diff_table[k][-1])
        else:

            final_u_value = 1
            for j in range(0, k):
                final_u_value = final_u_value * (u + j)

            u_values.append(final_u_value / factorial(k))

            algo.append(diff_table[k][-1] * u_values[k])

    return sum(algo)


print(ngbdf(difference_table, 25))
