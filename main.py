from models import User, Account, SavingsAccount
from storage import load_data, save_data
from html_generator import generate_html


data = load_data()
users = data["users"]
accounts = data['accounts']

def register():
    username = input("Login:")
    password = input("Password:")

    for user in users:
        if user.username == username:
            print("⚠️ Користувач вже існує")
            return
    
    new_user = User(username, password)
    users.append(new_user)

    accounts.append(Account(username, 1000))
    accounts.append(SavingsAccount(username, 2000))

    save_data(users, accounts)
    print("✅ Реєстрація успішна!")

def login():
    username = input("Login:")
    password = input("Password:")

    for user in users:
        if user.username == username and user.check_password(password):
            print("✅ Успішний вхід!")
            user_accounts = [acc for acc in accounts if acc.owner == username]

            generate_html(user, user_accounts)
            return
        
    print("❌ Невірний логін або пароль")

def menu():
    while True:
        print("\n1 - Реєстрація")
        print("2 - Вхід")
        print("3 - Вихід")

        choice = input("Оберіть дію: ")

        if choice == "1":
            register()
        elif choice == "2":
            login()
        elif choice == "3":
            break
        else:
            print("Невірний вибір")


if __name__ == "__main__":
    menu()





    

        
