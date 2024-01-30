import sqlite3
from sqlite3 import Error
from tkinter import messagebox
from tkinter import filedialog

def update_into_table(conn, update_sql, values):
    try:
        c = conn.cursor()
        c.execute(update_sql, values)
        conn.commit()
    except Error as e:
        print(e)
        
def delete_into_table(conn, table_name, where_clause):
    """
    Deletes a record from a table in a SQLite database.

    Parameters:
    conn (sqlite3.Connection): The database connection object.
    table_name (str): The name of the table to delete from.
    where_clause (str): The WHERE clause of the DELETE statement.

    Returns:
    None
    """
    try:
        cursor = conn.cursor()
        cursor.execute(f"DELETE FROM {table_name} WHERE {where_clause}")
        conn.commit()
    except sqlite3.Error as e:
        print(e)

def create_connection():
    conn = None
    try:
        conn = sqlite3.connect(':memory:')
        print(sqlite3.version)
    except Error as e:
        print(e)

    return conn

def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

def insert_into_table(conn, insert_sql, values):
    try:
        c = conn.cursor()
        c.execute(insert_sql, values)
        conn.commit()
        return c.lastrowid
    except Error as e:
        print(e)

def select_from_table(conn, select_sql):
    rows = None
    try:
        c = conn.cursor()
        c.execute(select_sql)
        rows = c.fetchall()
    except Error as e:
        print(e)

    return rows

def create_tables(conn):
    sql_create_customers_table = """ CREATE TABLE IF NOT EXISTS customers (
                                            id integer PRIMARY KEY,
                                            name text NOT NULL,
                                            phone text NOT NULL,
                                            email text NOT NULL
                                        ); """

    sql_create_payments_table = """ CREATE TABLE IF NOT EXISTS payments (
                                            id integer PRIMARY KEY,
                                            customer_id integer,
                                            amount real NOT NULL,
                                            FOREIGN KEY (customer_id) REFERENCES customers (id)
                                        ); """

    sql_create_orders_table = """ CREATE TABLE IF NOT EXISTS orders (
                                            id integer PRIMARY KEY,
                                            customer_id integer,
                                            order_date text NOT NULL,
                                            FOREIGN KEY (customer_id) REFERENCES customers (id)
                                        ); """

    sql_create_jobs_table = """ CREATE TABLE IF NOT EXISTS jobs (
                                            id integer PRIMARY KEY,
                                            order_id integer,
                                            job_status text NOT NULL,
                                            FOREIGN KEY (order_id) REFERENCES orders (id)
                                        ); """

    sql_create_drawings_table = """ CREATE TABLE IF NOT EXISTS drawings (
                                            id integer PRIMARY KEY,
                                            job_id integer,
                                            file_path text NOT NULL,
                                            FOREIGN KEY (job_id) REFERENCES jobs (id)
                                        ); """

    if conn is not None:
        create_table(conn, sql_create_customers_table)
        create_table(conn, sql_create_payments_table)
        create_table(conn, sql_create_orders_table)
        create_table(conn, sql_create_jobs_table)
        create_table(conn, sql_create_drawings_table)
    else:
        print("Error! cannot create the database connection.")

def insert_customer(conn, name, phone, email):
    sql = ''' INSERT INTO customers(name,phone,email) 
    VALUES(?,?,?) '''
    customer_id = insert_into_table(conn, sql, (name, phone, email))
    return customer_id

def insert_payment(conn, customer_id, amount):
    sql = ''' INSERT INTO payments(customer_id,amount)
            VALUES(?,?) '''
    payment_id = insert_into_table(conn, sql, (customer_id, amount))
    return payment_id

def insert_order(conn, customer_id, order_date):
    sql = ''' INSERT INTO orders(customer_id,order_date)
            VALUES(?,?) '''
    order_id = insert_into_table(conn, sql, (customer_id, order_date))
    return order_id

def insert_job(conn, order_id, job_status):
    sql = ''' INSERT INTO jobs(order_id,job_status)
    VALUES(?,?) '''
    job_id = insert_into_table(conn, sql, (order_id, job_status))
    return job_id

def insert_drawing(conn, job_id, file_path):
    sql = ''' INSERT INTO drawings(job_id,file_path)
    VALUES(?,?) '''
    drawing_id = insert_into_table(conn, sql, (job_id, file_path))
    return drawing_id

def select_all_customers(conn):
    select_sql = "SELECT * FROM customers"
    rows = select_from_table(conn, select_sql)
    return rows

def select_all_payments(conn):
    select_sql = "SELECT * FROM payments"
    rows = select_from_table(conn, select_sql)
    return rows

def select_all_orders(conn):
    select_sql = "SELECT * FROM orders"
    rows = select_from_table(conn, select_sql)
    return rows

def select_all_jobs(conn):
    select_sql = "SELECT * FROM jobs"
    rows = select_from_table(conn, select_sql)
    return rows

def select_all_drawings(conn):
    select_sql = "SELECT * FROM drawings"
    rows = select_from_table(conn, select_sql)
    return rows

def select_orders_by_customer_id(conn, customer_id):
    select_sql = f"SELECT * FROM orders WHERE customer_id={customer_id}"
    rows = select_from_table(conn, select_sql)
    return rows

def select_payments_by_customer_id(conn, customer_id):
    select_sql = f"SELECT * FROM payments WHERE customer_id={customer_id}"
    rows = select_from_table(conn, select_sql)
    return rows

def select_jobs_by_order_id(conn, order_id):
    select_sql = f"SELECT * FROM jobs WHERE order_id={order_id}"
    rows = select_from_table(conn, select_sql)
    return rows

def select_drawings_by_job_id(conn, job_id):
    select_sql = f"SELECT * FROM drawings WHERE job_id={job_id}"
    rows = select_from_table(conn, select_sql)
    return rows

def update_customer(conn, customer_id, name, phone, email):
    update_sql = f"UPDATE customers SET name=?, phone=?, email=? WHERE id={customer_id}"
    update_into_table(conn, update_sql, (name, phone, email))

def update_payment(conn, payment_id, amount):
    update_sql = f"UPDATE payments SET amount=? WHERE id={payment_id}"
    update_into_table(conn, update_sql, (amount,))
    
def update_order(conn, order_id, order_date):
    update_sql = f"UPDATE orders SET order_date=? WHERE id={order_id}"
    update_into_table(conn, update_sql, (order_date,))
    
def update_job(conn, job_id, job_status):
    update_sql = f"UPDATE jobs SET job_status=? WHERE id={job_id}"
    update_into_table(conn, update_sql, (job_status,))
    
def update_drawing(conn, drawing_id, file_path):
    update_sql = f"UPDATE drawings SET file_path=? WHERE id={drawing_id}"
    update_into_table(conn, update_sql, (file_path,))
    
def delete_customer(conn, customer_id):
    delete_sql = f"DELETE FROM customers WHERE id={customer_id}"
    delete_into_table(conn, delete_sql)
    
