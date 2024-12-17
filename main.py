purchases = [
    {"item": "apple", "category": "fruit", "price": 1.2, "quantity": 10},
    {"item": "banana", "category": "fruit", "price": 0.5, "quantity": 5},
    {"item": "milk", "category": "dairy", "price": 1.5, "quantity": 2},
    {"item": "bread", "category": "bakery", "price": 2.0, "quantity": 3},
]

min_price = 1.0


def total_revenue(purchases: dict) -> float:
    return sum([x['price'] * x['quantity'] for x in purchases])


def items_by_category(purchases: dict) -> dict:
    items_by_category = {}

    categories = (x['category'] for x in purchases)

    for category in categories:
        items_by_category[category] = list(
            (x['item'] for x in purchases if x["category"] == category)
        )

    return items_by_category


def expensive_purchases(purchases: dict, min_price: float) -> dict:
    return {}


def average_price_by_category(purchases: dict) -> list:
    return []


def most_frequent_category(purchases: dict) -> str:
    return ''


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
