from models.data import users
from utils.crud import show_users


if __name__ == "__main__":
    print("Witaj użytkowniku")
    while True:
        print("Menu:")
        print("1.Wyświetl co u znajomych")
        print("2.")
        print("3.")
        print("4.")
        print("5.")
        print("0.Zamknij program")
        menu_option: str = input("Dokonaj wyboru:")
        if menu_option == "0":
            print("Program kończy pracę")
            break
        if menu_option == "1":
            show_users(users)
        if menu_option == "1":
            show_users(users)
        if menu_option == "1":
            show_users(users)
        if menu_option == "1":
            show_users(users)

