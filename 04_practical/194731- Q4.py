def sum_up_to_tail(n, accumulator=0):
    if n == 0:
        return accumulator
    return sum_up_to_tail(n - 1, accumulator + n)


print(sum_up_to_tail(5))  