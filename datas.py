import sqlite3

db = sqlite3.connect('cars.db')
cursor = db.cursor()

async def start_db():
    cursor.execute('''
CREATE TABLE IF NOT EXISTS cars(
                   seller TEXT,
                   model TEXT,
                   horse_power  INTEGER,
                   cars_num TEXT,
                   date INTEGER,
                   is_new TEXT,
                   photo TEXT
)
'''
    )

# start_db()

async def add_car(seller,model,horse,cars_num,date,is_new,photo):
    cursor.execute('''
INSERT INTO cars(
                   seller,model,horse_power,cars_num,date,is_new,photo
)
                   VALUES(?,?,?,?,?,?,?)
''',(seller,model,horse,cars_num,date,is_new,photo))
    db.commit()


# add_car(seller='Behruz',
#         model='Onix',
#         horse=1234,
#         cars_num='MM007A',
#         date=2023,
#         is_new='TAZA',
#         photo='AgACAgIAAxkBAAICUWaQvKnu6ggYR7alCKxTN8HkXpaAAAKI1zEb71iJSFdUqCGVMJ6ZAQADAgADcwADNQQ')

async def show_cars():
    cursor.execute('SELECT * FROM cars')
    cars = cursor.fetchall()
    return cars