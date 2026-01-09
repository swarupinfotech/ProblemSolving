def hill_climbing(start):
    current = start
    while True:
        neighbours = [current - 1, current + 1]
        next_state = max(neighbours)

        if next_state <= current:
            break
        current = next_state

    return current

start = 0
solution = hill_climbing(start)
print("Hill Climbing Solution:", solution)
