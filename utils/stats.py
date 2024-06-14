def mean(values: any) -> float:
    values = [value for value in values if value == value]
    return sum(values) / (len(values))

def mean_for_var(values: any) -> float:
    values = [value for value in values if value == value]
    return sum(values) / ((len(values) - 1))

def get_decimal(floating :float):
    integer = 0
    negative = 1
    if floating < 0:
        negative = -1
        floating *= -1
    while floating >= 1:
        floating -= 1.0 
        integer += 1
    return (integer * negative, round(floating, 5))

def percentile(values, percentile):
    values = [value for value in values if value == value]
    values = sorted(values)
    i, decimal = get_decimal((len(values) - 1) * percentile)
    return (values[i] + (decimal * (values[i + 1] - values[i])))


def first_quartile(values: any) -> float:
    return percentile(values, 0.25)

def median(values: any) -> float:
    return percentile(values, 0.5)



def third_quartile(values: any) -> float:
    return percentile(values, 0.75)


def std(values: any) -> float:
    values = [value for value in values if value == value]
    return (var(values) ** 0.5)


def var(values: any) -> float:
    values = [value for value in values if value == value]
    squared_diffs = [(mean(values) - x) ** 2 for x in values]
    return mean_for_var(squared_diffs)

def min(values: any) -> float:
    values = [value for value in values if value == value]
    values = sorted(values)
    return values[0]

def max(values: any) -> float:
    values = [value for value in values if value == value]
    values = sorted(values)
    return values[-1]

def count(values: any) -> float:
    i = 0
    values = [value for value in values if value == value]
    for value in values:
            i += 1
    return i
