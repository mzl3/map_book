import psycopg2


db_params=psycopg2.connect(
    database="postgres",
    user="postgres",
    password="Postgres",
    host='localhost',
    port='5432'
)

def add_user_to_table(db_params)->None:
    imie=input("Imie: ")
    nazwisko=input("Nazwisko: ")
    posts=input("Posts: ")
    miejscowosc=input("Miejscowosc: ")

    sql_add_query=f"INSERT INTO public.users(name, surname, posts, location, coords)VALUES ('{imie}', '{nazwisko}', {posts}, '{miejscowosc}', 'SRID=4326;POINT(21.0 52.23)');"
    cursor=db_params.cursor()
    cursor.execute(sql_add_query)
    db_params.commit()

#add_user_to_table(db_params)



def show_users(db_params)->None:


    sql_add_query = f"SELECT * FROM public.users"
    cursor = db_params.cursor()
    cursor.execute(sql_add_query)
    users=cursor.fetchall()
    #print(users)
    #db_params.commit()
    for user in users:
        print(user)
        show_users(db_params)

# DELETE FROM public.users
#	WHERE id=2

def remove_users_from_db(db_params)->None:
    cursor=db_params.cursor()
    sql_remove_query=f"DELETE FROM public.users WHERE name='{input('Imie')}'";
    cursor.execute(sql_remove_query)
    db_params.commit()

# remove_users_from_db(db_params)
# show_users(db_params)

#UPDATE public.users
#	SET name='aa', surname='aa', posts=1
#	WHERE id=4

def update_users(db_params)->None:
    cursor = db_params.cursor()
    sl_update_query=f"UPDATE public.users SET name='{input('Imie')}', surname='{input('Nazwisko')}', posts='{int(input('ilosc postów'))}' WHERE id=4"
    cursor.execute(sl_update_query)
    db_params.commit()



update_users(db_params)