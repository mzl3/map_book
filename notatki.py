import psycopg2
import requests
from bs4 import BeautifulSoup

db_params=psycopg2.connect(
    database="postgres",
    user="postgres",
    password='postgres',
    host="localhost",
    port="5432"
)

def add_new_to_table(db_params) -> None:
    imie = input('Imie: ')
    nazwisko = input('Nazwisko: ')
    post = input('Post: ')
    miejscowosc = input('Miejscowosc: ')

    url: str = f"https://pl.wikipedia.org/wiki/{miejscowosc}"
    response = requests.get(url)
    response_html = BeautifulSoup(response.text, "html.parser")
    latitude = float(response_html.select(".latitude")[1].text.replace(",", "."))
    longitude = float(response_html.select(".longitude")[1].text.replace(",", "."))
    # return [latitude, longitude]

    sql_add_query=f"INSERT INTO public.users(name, surname, post, location, cords)VALUES ('{imie}', '{nazwisko}', '{post}', '{miejscowosc}', 'SRID=4326;POINT({longitude} {latitude})');"
    cursor=db_params.cursor()
    cursor.execute(sql_add_query)
    db_params.commit()

add_new_to_table(db_params)



def show_users(db_params) -> None:
    sql_add_query=f"SELECT * FROM public.users"
    cursor=db_params.cursor()
    cursor.execute(sql_add_query)
    users=cursor.fetchall()
    # print(users)
    # db_params.commit()
    for user in users:
        print(user)

show_users(db_params)


# DELETE FROM public.users
# 	WHERE id=2


def remove_users(db_params) -> None:
    cursor = db_params.cursor()
    sql_remove_query=f"DELETE FROM public.users where name='{input('Imie: ')}'; "
    cursor.execute(sql_remove_query)
    db_params.commit()

# remove_users(db_params)
# show_users(db_params)

# UPDATE public.users
# 	SET name='Paweł', surname='Lębryk', post=2
# 	WHERE id=4

def update_users(db_params) -> None:
    cursor = db_params.cursor()
    sql_update_query=f"UPDATE public.users SET name='{input('Imie: ')}', surname='{input('Nazwisko: ')}', post='{int(input('Liczba postów: '))}' WHERE id=4"
    cursor.execute(sql_update_query)
    db_params.commit()

# update_users(db_params)