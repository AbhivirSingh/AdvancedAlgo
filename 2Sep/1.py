def min_coins(denominations, target):
    denominations.sort(reverse=True)
    
    num_coins = 0
    for coin in denominations:
        if target >= coin:
            num_coins += target // coin
            target %= coin
            
    return num_coins

# Example usage
denominations = [1, 2, 5, 10]
target = 27
print(f"Minimum coins required = {min_coins(denominations, target)}")