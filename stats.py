def mean(values: any) -> float:
    return sum(values) / len(values)


def median(values: any) -> float:
    values = sorted(values)
    if (len(values) % 2):
        return values[len(values) // 2]
    return mean((values[(len(values) // 2) - 1], values[(len(values) // 2)]))


def first_quartile(values: any) -> float:
    values = sorted(values)
    q1 = median(values[:(len(values) // 2) + len(values) % 2])
    return float(q1)


def third_quartile(values: any) -> float:
    values = sorted(values)
    q2 = median(values[-(len(values) // 2) - len(values) % 2:])
    return float(q2)


def std(values: any) -> float:
    return (var(values) ** 0.5)


def var(values: any) -> float:
    squared_diffs = [(mean(values) - x) ** 2 for x in values]
    return mean(squared_diffs)

def min(values: any) -> float:
    min = values[0]
    for value in values:
        if value < min:
            min = value
    return min

def max(values: any) -> float:
    max = values[0]
    for value in values:
        if value > max:
            max = value
    return max

def count(values: any) -> float:
    i = 0
    for value in values:
        if value:
            i += 1
    return i