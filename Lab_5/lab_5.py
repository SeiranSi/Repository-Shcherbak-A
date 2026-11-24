import sqlite3
import hashlib


def hash_password(password: str) -> str:
    """Перетворення пароля на SHA-256 хеш."""
    return hashlib.sha256(password.encode('utf-8')).hexdigest()

# Функція 1:  Підключення до БД
def create_table():
   with sqlite3.connect('my_database.db') as connection:
        db = connection.cursor()
        db.execute('''
            CREATE TABLE IF NOT EXISTS Users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                login TEXT NOT NULL UNIQUE,
                password TEXT NOT NULL,
                full_name TEXT NOT NULL )
        ''')

# Функція 2: Додавання користувача

def add_user(login: str, password: str, full_name: str):

    hashed_psw = hash_password(password)

    try:
        with sqlite3.connect('my_database.db') as connection:
            db = connection.cursor()
            db.execute(
                'INSERT INTO Users (login, password, full_name) VALUES (?, ?, ?)',
                (login, hashed_psw, full_name)
            )
        print(f"User '{login}' has been successfully added!")

    except sqlite3.IntegrityError:
        print(f"Error: User with login '{login}' already exists.")

# Функція 3:  Оновлення пароля

def update_password(login: str, new_password: str):

    hashed_psw = hash_password(new_password)

    with sqlite3.connect('my_database.db') as connection:
        db = connection.cursor()
        db.execute(
            'UPDATE Users SET password = ? WHERE login = ?',
            (hashed_psw, login)
        )

        if db.rowcount > 0:
            print(f"Password for '{login}' has been successfully updated.")
        else:
            print(f"Error: User '{login}' not found.")

# Функція 4: Автентифікація

def authenticate_user():

    print("\n--- User Login ---")
    login = input("Enter login: ")
    password = input("Enter password: ")

    # Хешування
    hashed_input_psw = hash_password(password)

    with sqlite3.connect('my_database.db') as connection:
        db = connection.cursor()
        db.execute('SELECT password, full_name FROM Users WHERE login = ?', (login,))
        user_record = db.fetchone()

        if user_record is None:
            print("Error: User with this login does not exist.")
        elif user_record[0] == hashed_input_psw:
            print(f"Login successful! Welcome, {user_record[1]}!")
        else:
            print("Error: Incorrect password.")


if __name__ == '__main__':

    create_table()

    add_user('john', '123456John', 'John Mack-Flow')
    add_user('mary', '789456Mary', 'Maria Honchar')
    add_user('Kolya', 'k0lYa689', 'Nicolas Toretto')
    add_user('Janna', 'jannaDark44', 'Janna Sever')
    add_user('Anna', 'rubinAnn124', 'Anna Dubich')
    add_user('Helen', 'mAr3ch1098', 'Helen Markov')

    # 3. Приклад оновлення пароля
    update_password('john', 'NewSecretPass2026')

    # 4. Запускаємо перевірку входу (спробуй ввести john та NewSecretPass2026)
    authenticate_user()


