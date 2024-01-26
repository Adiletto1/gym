import sqlite3
from pathlib import Path
from pprint import pprint


def init_db():
    """
    Создается соединение с БД и курсор
    """
    global db, cursor
    db = sqlite3.connect(
        Path(__file__).parent.parent / "db.sqlite"
    )
    cursor = db.cursor()

def create_tables():
    # cursor.execute("""
    #     --sql
    #     DROP TABLE IF EXISTS product;
    # """)
    # cursor.execute("""
    #     --sql
    #     DROP TABLE IF EXISTS cats;
    # """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS cats (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT
        );
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS product (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            price INTEGER,
            cat INTEGER,
            FOREIGN KEY (cat) REFERENCES cats (id)
        );
    """)
    db.commit()

def populate_db():
    """
    Заполнение таблиц
    """
    cursor.execute("""
        --sql
        INSERT INTO cats (name) VALUES
            ('Sportpit'),
            ('Gantels'),
            ('Gym_price')
        """)
    cursor.execute("""
        INSERT INTO product (name, price, cat) VALUES
            ('Протеин', 5000, 1),
            ('Гейнер', 4500, 1),
            ('Гантели', 2000, 2),
            ('Штанги', 1200, 2),
            ('Месячный абонемент', 3000, 3),
            ('Годовой абонемент', 18000, 3)
        """
    )
    db.commit()

def get_products():

    cursor.execute("""
        SELECT * FROM product
    """)
    return cursor.fetchall()

def get_product(id):
    cursor.execute("""
        SELECT * FROM product WHERE id= :cid
    """, {"cid": id})
    return cursor.fetchone()

def get_products_by_cat(id):
    cursor.execute("""
        SELECT * FROM product WHERE cat = :cid
    """, {"cid": id})
    return cursor.fetchall()

if __name__ == '__main__':
    init_db()
    populate_db()
    create_tables()
    print(get_products_by_cat(3))
