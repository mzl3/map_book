def show_users(user_list: list[dict]) ->None:
    for user in user_list:
        print(f"Twój znajomy {user ['name']} opublikował: {user['posts']}")

        def update_user(users) -> None:
            kogo_szukasz = input("Kogo szukasz?: ")
            for user in users:
                if user['name'] == kogo_szukasz:
                    user['name'] = input('Podaj nowe imie:')
                    user['surname'] = input("Podaj nowe nazwisko:")
                    user['liczba_postow'] = input("Podaj liczbe postow:")