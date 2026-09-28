def check_amount(amount):
    if amount <= 0:
        raise ValueError("Amount must be greater than 0.")

    return amount


def check_category(category):
    if category == "":
        raise ValueError("Category cannot be empty.")

    return category
