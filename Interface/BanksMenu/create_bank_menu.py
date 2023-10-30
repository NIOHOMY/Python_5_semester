import traceback
def create_bank_menu(controller):
    try:
        name = input("Введите название банка: ")
        bank = controller.create_bank(name)
    
        if bank:
            print(f"Банк '{bank.name}' успешно создан.")
            return controller.get_bank_id(bank)
        else:
            print("Ошибка при создании банка.")
            return None
        
    except Exception as e:
            traceback.print_exc()
            return None