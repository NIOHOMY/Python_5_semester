
def view_funds_menu(bank):
    if bank:
        print(f"Средства банка: {bank.get_funds()} рублей.")
    else:
        print("Ошибка.")