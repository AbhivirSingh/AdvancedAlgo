def fractional_knapsack(items, capacity):
    items.sort(key=lambda x: x[1]/x[0], reverse=True)
    
    total_value = 0.0
    for weight, value in items:
        if capacity >= weight:
            capacity -= weight
            total_value += value
        else:
            total_value += value * (capacity / weight)
            break
    
    return total_value

items = [(60, 10), (100, 20), (120, 30)]
capacity = 50
print(f"Maximum value = {fractional_knapsack(items, capacity)}")
