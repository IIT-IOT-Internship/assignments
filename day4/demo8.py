# Given tuple of tuples
data = ((10, 10, 10, 12),
        (30, 45, 56, 45),
        (81, 80, 39, 32),
        (1, 2, 3, 4))


average_values = [sum(values) / len(values) for values in zip(*data)]

print(average_values)
