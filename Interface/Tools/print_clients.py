import traceback

def print_clients(controller):
    try:
        clients = controller.clients
        if clients:
            for index, client in enumerate(clients):
                print(f"ID: {index}, Имя: {client.name}")
            return True
        else:
            print("Список клиентов пуст.")
        return False
        
    except Exception as e:
            traceback.print_exc()
            return False