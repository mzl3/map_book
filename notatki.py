class User:
    def __init__(self,name,surname,posts,location):
        self.name=name
        self.surname=surname
        self.posts=posts
        self.location=location

user_1=User(name='Marek', surname='Dybowski', posts:'3', location:"Warszawa")
user_2=User(name='Tomek', surname='Dybowski', posts:'34', location:"Warszawa")
print(user_2.name)