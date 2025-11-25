import sqlite3


class Database:

    def __init__(self):
        self.connection = sqlite3.connect(
            r"C:\\Users\\lundi\\qa_auto_2025" + r"\\become_qa_auto.db"
        )
        self.cursor = self.connection.cursor()

    def test_connection(self):
        sqlite_select_Query = "SELECT sqlite_version();"
        self.cursor.execute(sqlite_select_Query)
        record = self.cursor.fetchall()
        return record

    def get_all_users(self):
        query = "SELECT name, address, city FROM customers"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record

    def get_user_adress_by_name(self, name):
        query = f"SELECT address, city, postalCode, country \
            FROM customers WHERE name = '{name}'"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record

    def update_product_qnt_by_id(self, product_id, qnt):
        query = f"UPDATE products SET quantity = {qnt} WHERE id = {product_id}"
        self.cursor.execute(query)
        self.connection.commit()

    def select_product_qnt_by_id(self, product_id):
        query = f"SELECT quantity FROM products WHERE id = {product_id}"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record

    def insert_new_product(self, product_id, name, description, qnt):
        query = f"INSERT OR REPLACE INTO products (id, name, description, quantity) \
            VALUES ({product_id}, '{name}', '{description}', {qnt})"
        self.cursor.execute(query)
        self.connection.commit()

    def delete_product(self, product_id):
        query = f"DELETE FROM products WHERE id = {product_id}"
        self.cursor.execute(query)
        self.connection.commit()

    def insert_new_customer(
        self, customer_id, name, address, city, postalCode, country
    ):
        query = f"INSERT OR REPLACE INTO customers (id, name, address, city, postalCode, country) \
            VALUES ({customer_id}, '{name}', '{address}', '{city}', '{postalCode}', '{country}')"
        self.cursor.execute(query)
        self.connection.commit()

    def delete_customer(self, customer_id):
        query = f"DELETE FROM customers WHERE id = {customer_id}"
        self.cursor.execute(query)
        self.connection.commit()

    def change_customer_address_by_id(
        self, customer_id, address, city, postalCode, country
    ):
        query = f"""
            UPDATE customers 
            SET address = '{address}', 
                city = '{city}', 
                postalCode = '{postalCode}', 
                country = '{country}'
            WHERE id = {customer_id}"""
        self.cursor.execute(query)
        self.connection.commit()

    def select_customers_quantity_by_name(self, customer_name):
        query = f"SELECT * FROM customers WHERE name = '{customer_name}'"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record

    def get_detailed_orders(self):
        query = """
            SELECT 
                orders.id, 
                customers.name, 
                products.name, 
                products.description, 
                orders.order_date 
            FROM orders
            JOIN customers ON orders.customer_id = customers.id
            JOIN products  ON orders.product_id = products.id
        """
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record
