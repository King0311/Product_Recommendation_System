import os
import django
import random

# Set Django settings
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "product_recommender.settings")
django.setup()

from recommending_system.models import (
    Order,
    Product,
)  # Update if your app is named differently


def create_random_orders(n=10):
    all_product_ids = list(Product.objects.values_list("id", flat=True))

    if not all_product_ids:
        print("No products found. Please run the product generation script first.")
        return

    for _ in range(n):
        order = Order()
        order.save()

        # Pick 1 to 5 random products for each order
        num_products = random.randint(1, 5)
        selected_product_ids = random.sample(
            all_product_ids, min(num_products, len(all_product_ids))
        )
        selected_products = Product.objects.filter(id__in=selected_product_ids)

        order.products.set(selected_products)

        # Calculate total_price
        total = sum(p.price for p in selected_products)
        order.total_price = total
        order.save()

        print(
            f"Created Order #{order.id} with {len(selected_products)} products. Total: ₹{total}"
        )


if __name__ == "__main__":
    create_random_orders(n=10)
