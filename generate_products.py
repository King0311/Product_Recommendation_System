import os
import django
import random
from faker import Faker

# Set the correct settings path
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "product_recommender.settings")
django.setup()

from recommending_system.models import Product  # adjust if your app name is different

fake = Faker()


def create_products(n=50):
    for _ in range(n):
        product = Product(
            name=fake.unique.word().capitalize() + " " + fake.word().capitalize(),
            description=fake.text(max_nb_chars=200),
            price=round(random.uniform(10.0, 1000.0), 2),
        )
        product.save()

    print(f"{n} products created successfully!")


if __name__ == "__main__":
    create_products()
