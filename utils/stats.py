def mean(values: any) -> float:
    values = [value for value in values if value == value]
    return sum(values) / len(values)


def median(values: any) -> float:
    values = [value for value in values if value == value]
    values = sorted(values)
    if (len(values) % 2):
        return values[len(values) // 2]
    return mean((values[(len(values) // 2) - 1], values[(len(values) // 2)]))


def first_quartile(values: any) -> float:
    values = [value for value in values if value == value]
    values = sorted(values)
    q1 = median(values[:(len(values) // 2) + len(values) % 2])
    return float(q1)


def third_quartile(values: any) -> float:
    values = [value for value in values if value == value]
    values = sorted(values)
    q3 = median(values[-(len(values) // 2) - len(values) % 2:])
    return float(q3)


def std(values: any) -> float:
    # values = [value for value in values if value == value]
    return (var(values) ** 0.5)


def var(values: any) -> float:
    # values = [value for value in values if value == value]
    squared_diffs = [(mean(values) - x) ** 2 for x in values]
    return mean(squared_diffs)

def min(values: any) -> float:
    values = [value for value in values if value == value]
    values = sorted(values)
    min = values[0]
    # for value in values:
    #     if value < min:
    #         min = value
    return min

def max(values: any) -> float:
    values = [value for value in values if value == value]
    values = sorted(values)
    max = values[-1]
    # for value in values:
    #     if value > max:
    #         max = value
    return max

def count(values: any) -> float:
    i = 0
    values = [value for value in values if value == value]
    for value in values:
            i += 1
    return i