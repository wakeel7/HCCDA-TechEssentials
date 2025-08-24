# bankcore.py

users_info = {}  # {cust_id: {"name": str, "user_id": str, "password": str}}

branch_id = "BR01"
user_number = 1000  # increment for each account created


def create_account(name, user_id, psd):
    """Creates a new bank account and returns customer ID"""
    global user_number
    cust_id = f"{branch_id}_{user_number}"
    users_info[cust_id] = {
        "name": name,
        "user_id": user_id,
        "password": psd
    }
    user_number += 1
    print(f"\nAccount created successfully! Your Customer ID is: {cust_id}")
    return cust_id


def login(cust_id, psd):
    """Validates login credentials"""
    if cust_id in users_info and users_info[cust_id]["password"] == psd:
        print(f"\nWelcome back, {users_info[cust_id]['name']}!")
        return True
    else:
        print("\nInvalid Customer ID or Password!")
        return False
