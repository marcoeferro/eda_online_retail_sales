import sqlite3
#nombre de la base de datos
database = "amazon_sales.db"

#Crear Conexion en la DDBB
connection = sqlite3.connect(database)

# Crear un tablas
def create_table():
    with connection as conn:
        curr = conn.cursor()
        try:
            curr.execute("""
                CREATE TABLE IF NOT EXISTS products(
                    id TEXT PRIMARY KEY,
                    product_name TEXT,
                    category_1 TEXT,
                    category_2 TEXT,
                    category_3 TEXT,
                    category_4 TEXT,
                    category_5 TEXT,
                    discounted_price REAL,
                    actual_price REAl,
                    discount_percentage REAL,
                    rating INTEGER,
                    rating_count INTEGER,
                    about_product TEXT,
                    img_link TEXT,
                    product_link TEXT
                )
            """)
            conn.commit()
        except Exception as e:
            print(f"ERROR EN LA CREACION DE LA TABLA PRODUCOTS - ERROR : {e}")

        try:
            curr.execute("""
                CREATE TABLE IF NOT EXISTS reviews(
                    id TEXT PRIMARY KEY,
                    review_title TEXT,
                    review_content TEXT,
                    id_user INTEGER,
                    id_product INTEGER,
                    FOREIGN KEY (id_user) REFERENCES users(id),
                    FOREIGN KEY (id_product) REFERENCES products(id)
                )
            """)
            conn.commit()
        except Exception as e:
            print(f"ERROR EN LA CREACION DE LA TABLA REVIEWS - ERROR : {e}")

        try:
            curr.execute("""
                CREATE TABLE IF NOT EXISTS users(
                    id TEXT PRIMARY KEY,
                    user_name TEXT               
                )
            """)
            conn.commit()
        except Exception as e:
            print(f"ERROR EN LA CREACION DE LA TABLA USERS - ERROR : {e}")

def insert_user(id,name):
    with connection as conn:
        curr = conn.cursor()
        
        try:
            curr.execute(
                "INSERT INTO users (id,user_name) VALUES (?,?)",(id,name))
            conn.commit()
        except Exception as e:
            print(f"ERROR AL INSERTAR USUARIO -ERROR-: {e}")

def insert_review(id,title,content,id_user,id_product):
    with connection as conn:
        curr = conn.cursor()
        try:
            curr.execute(
                "INSERT INTO reviews (id,review_title,review_content,id_user,id_product) VALUES (?,?,?,?,?)",(id,title,content,id_user,id_product))
            conn.commit()
        except Exception as e:
            print(f"ERROR AL INSERTAR REVIEW -ERROR-: {e}")

def insert_product(id,product_name,category_1,category_2,category_3,category_4,category_5,discounted_price,actual_price,discount_percentage,rating,rating_count,about_product,img_link, product_link):
    with connection as conn:
        curr = conn.cursor()
        try:
            curr.execute(
                "INSERT INTO products (id,product_name,category_1,category_2,category_3,category_4,category_5,discounted_price,actual_price,discount_percentage,rating,rating_count,about_product,img_link,product_link) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",(id,product_name,category_1,category_2,category_3,category_4,category_5,discounted_price,actual_price,discount_percentage,rating,rating_count,about_product,img_link,product_link))
            conn.commit()
        except Exception as e:
            print(f"ERROR AL INSERTAR PRODUCT -ERROR-: {e}")