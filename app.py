def calculate_total(prices):
    total = sum(prices)

    if total < 0:
        raise ValueError("Total cannot be negative")

    return total


if __name__ == "__main__":
    print("Total price:", calculate_total([100, 200, 300]))
