purchases = [
    {"item": "apple", "category": "fruit", "price": 1.2, "quantity": 10},
    {"item": "banana", "category": "fruit", "price": 0.5, "quantity": 5},
    {"item": "milk", "category": "dairy", "price": 1.5, "quantity": 2},
    {"item": "bread", "category": "bakery", "price": 2.0, "quantity": 3},
    {"item": "apple", "category": "fruit", "price": 1.3, "quantity": 11},
]

min_price = 1.0


def get_categories(purchases: dict) -> list:
    return (x['category'] for x in purchases)


def total_revenue(purchases: dict) -> float:
    return sum([x['price'] * x['quantity'] for x in purchases])


def items_by_category(purchases: dict) -> dict:
    categories = get_categories(purchases)

    return {category: list(set(x['item'] for x in purchases if x['category'] == category))
            for category in categories}


def expensive_purchases(purchases: dict, min_price: float) -> dict:
    return [x for x in purchases if x['price'] >= min_price]


def average_price_by_category(purchases: dict) -> list:
    average_price_by_category = {}

    categories = get_categories(purchases)

    for category in categories:
        prices = [x['price'] for x in purchases if x['category'] == category]

        avg_price = sum(prices) / len(prices)

        average_price_by_category[category] = avg_price

    return average_price_by_category


def most_frequent_category(purchases: dict) -> str:
    categories = get_categories(purchases)

    quantity_by_category = {category: sum(x['quantity'] for x in purchases if x['category'] == category)
                            for category in categories}

    return max(quantity_by_category, key=quantity_by_category.get)


def get_report(
      total_revenue: float,
      items_by_category: dict,
      min_price: float,
      expensive_purchases: dict,
      average_price_by_category: list,
      most_frequent_category: str,
) -> str:
    return f"""
Общая выручка: {total_revenue}
Товары по категориям: {items_by_category}
Покупки дороже {min_price}: {expensive_purchases}
Средняя цена по категориям: {average_price_by_category}
Категория с наибольшим количеством проданных товаров: {most_frequent_category}
"""


total_revenue = total_revenue(purchases)
items_by_category = items_by_category(purchases)
expensive_purchases = expensive_purchases(purchases, min_price)
average_price_by_category = average_price_by_category(purchases)
most_frequent_category = most_frequent_category(purchases)

print(get_report(
    total_revenue,
    items_by_category,
    min_price,
    expensive_purchases,
    average_price_by_category,
    most_frequent_category,
  )
)
