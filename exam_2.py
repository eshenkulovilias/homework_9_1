def func(deposit_amount, amount, annual_percentage):
    result = deposit_amount
    counter = 0
    while result < amount:
        result = annual_percentage / 100 / 12 * result + result
        counter += 1
    return counter


print(func(1000000, 1061520.150601, 12))
