def fractional(items, capacity):
    items.sort(key=lambda x: x[1] / x[0], reverse=True)

    total_value = 0.0
    selected = []

    for weight, value in items:
        if capacity == 0:
            break

        amount = min(weight, capacity)
        total += amount * (value / weight)
        selected.append((amount, weight, value))

        capacity -= amount

    return total, selected

# Example usage
items = [(2, 10), (3, 5), (5, 15), (7, 7), (1, 6)]
capacity = 10

total, selected = fractional(items, capacity)
print("Total value:", total_value)
print("Selected items:", selected_items)
