# You are a cashier at a grocery store, and you need to generate all possible combinations of items that a customer can buy. You will use the itertools module in Python to help you accomplish this task. Your goal is to create a program that generates the combinations and prints them out.
#
# To simplify the exercise, consider the following scenario:
#
# You have three types of fruits available: apples, bananas, and oranges. Each type of fruit has a different price: apples cost $1, bananas cost $2, and oranges cost $3. The customer wants to buy a total of 5 fruits.
#
# Your task is to use the itertools module to generate all possible combinations of fruits that the customer can buy within their budget of $10. You should consider all combinations, including the same fruit multiple times.

import itertools

fruits = {
    'apples': 1,
    'bananas': 2,
    'oranges': 3
}

customer_budget = 10
total_fruits = 5

possible_combinations = []

for r in range(total_fruits + 1):
    for combination in itertools.combinations_with_replacement(fruits.keys(), r):
        total_price = sum(fruits[fruit] for fruit in combination)
        if total_price <= customer_budget:
            possible_combinations.append(combination)

for combination in possible_combinations:
    print(combination)