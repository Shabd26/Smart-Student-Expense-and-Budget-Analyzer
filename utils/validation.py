def check_amount(amount):
    if amount <= 0:
        print("Amount must be greater than 0.")
        return False
    return True


def check_category(category):
    if category == "":
        print("Category cannot be empty.")
        return False
    return True