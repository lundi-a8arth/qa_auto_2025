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
        query = """SELECT address, city, postalCode, country \
            FROM customers WHERE name = ?"""
        self.cursor.execute(query, (name,))
        record = self.cursor.fetchall()
        return record

    def update_product_qnt_by_id(self, qnt, product_id):
        query = """UPDATE products SET quantity = ? WHERE id = ?"""
        params = (qnt, product_id)
        self.cursor.execute(query, params)
        self.connection.commit()

    def select_product_qnt_by_id(self, product_id):
        query = """SELECT quantity FROM products WHERE id = ?"""
        self.cursor.execute(query, (product_id,))
        record = self.cursor.fetchall()
        return record

    def insert_new_product(self, product_id, name, description, qnt):
        query = """INSERT OR REPLACE INTO products (id, name, description, quantity) \
            VALUES (?, ?, ?, ?)"""
        params = (product_id, name, description, qnt)
        self.cursor.execute(query, params)
        self.connection.commit()

    def delete_product(self, product_id):
        query = """DELETE FROM products WHERE id = ?"""
        self.cursor.execute(query, (product_id,))
        self.connection.commit()

    def insert_new_customer(
        self, customer_id, name, address, city, postalCode, country
    ):
        query = """INSERT OR REPLACE INTO customers (id, name, address, city, postalCode, country) \
            VALUES (?, ?, ?, ?, ?, ?)"""
        params = (customer_id, name, address, city, postalCode, country)
        self.cursor.execute(query, params)
        self.connection.commit()

    def delete_customer(self, customer_id):
        query = """DELETE FROM customers WHERE id = ?"""
        self.cursor.execute(query, (customer_id,))
        self.connection.commit()

    def change_customer_address_by_id(
        self, customer_id, address, city, postalCode, country
    ):
        query = """
            UPDATE customers 
            SET address = ?, 
                city = ?, 
                postalCode = ?, 
                country = ?
            WHERE id = ?"""
        params = (address, city, postalCode, country, customer_id)
        self.cursor.execute(query, params)
        self.connection.commit()

    def select_customers_quantity_by_name(self, customer_name):
        query = """SELECT * FROM customers WHERE name = ?"""
        self.cursor.execute(query, (customer_name,))
        record = self.cursor.fetchall()
        return record

    def get_order(self, order_id):
        query = """SELECT * FROM orders WHERE id = ?"""
        self.cursor.execute(query, (order_id,))
        record = self.cursor.fetchone()

        if record is None:
            print(f"No order found with id={order_id}")
            return None

        return record

    def insert_new_order(self, order_id, customer_id, product_id, date):
        query = f"INSERT OR REPLACE INTO orders (id, customer_id, product_id, order_date) \
            VALUES (?, ?, ?, ?)"
        params = (order_id, customer_id, product_id, date)
        self.cursor.execute(query, params)
        self.connection.commit()

    def update_order(self, order_id, customer_id=None, product_id=None):
        fields = []
        params = []

        if customer_id is not None:
            fields.append("customer_id = ?")
            params.append(customer_id)

        if product_id is not None:
            fields.append("product_id = ?")
            params.append(product_id)

        if not fields:
            return False

        params.append(order_id)

        query = f"UPDATE orders SET {', '.join(fields)} WHERE id = ?"
        self.cursor.execute(query, tuple(params))
        self.connection.commit()

    def delete_order(self, order_id):
        query = """DELETE from orders WHERE id = ?"""
        self.cursor.execute(query, (order_id,))
        self.connection.commit()

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
