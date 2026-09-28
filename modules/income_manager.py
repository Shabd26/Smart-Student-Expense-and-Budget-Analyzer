from utils.file_handler import load_data
from utils.file_handler import save_data

INCOME_FILE = "data/income.json"


def set_income(amount):
    data = {
        "amount": amount
    }

    save_data(INCOME_FILE, data)

    return amount


def get_income_amount():
    data = load_data(INCOME_FILE, {"amount": 0})

    return data["amount"]
