items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}


def greedy_algorithm(items, budget):
    for item in items.values():
        item["calories_per_cost"] = item["calories"] / item["cost"]

    sorted_items = sorted(
        items.items(), key=lambda x: x[1]["calories_per_cost"], reverse=True)

    selected_items = []
    total_cost = 0

    for item_name, item_info in sorted_items:
        if total_cost + item_info["cost"] <= budget:
            selected_items.append(item_name)
            total_cost += item_info["cost"]

    return selected_items


def dynamic_programming(items, budget):
    item_list = list(items.items())
    dp = [[0 for _ in range(len(items) + 1)] for _ in range(budget + 1)]

    for i in range(1, budget + 1):
        for j in range(1, len(items) + 1):
            item_cost = item_list[j-1][1]["cost"]
            item_calories = item_list[j-1][1]["calories"]

            if item_cost <= i:
                dp[i][j] = max(dp[i][j-1], dp[i-item_cost]
                               [j-1] + item_calories)
            else:
                dp[i][j] = dp[i][j-1]

    selected_items = []
    budget_remaining = budget
    for j in range(len(items), 0, -1):
        if dp[budget_remaining][j] != dp[budget_remaining][j-1]:
            selected_items.append(item_list[j-1][0])
            budget_remaining -= item_list[j-1][1]["cost"]

    selected_items.reverse()
    return selected_items


# Test Time
budget = 100
greedy_selected = greedy_algorithm(items, budget)
dynamic_selected = dynamic_programming(items, budget)

print("Greedy Algorithm Selected Items:", greedy_selected)
print("Dynamic Programming Selected Items:", dynamic_selected)
