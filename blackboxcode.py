import tkinter as tk
from tkinter import messagebox

def operator_interface(conn):
    def view_pending_jobs():
        jobs = get_pending_jobs(conn)
        output.delete(1.0, tk.END)
        for job in jobs:
            output.insert(tk.END, str(job) + '\n')

    root = tk.Tk()
    root.title("Operator Interface")

    output = tk.Text(root, height=10, width=50)
    output.pack()

    view_button = tk.Button(root, text="View Pending Jobs", command=view_pending_jobs)
    view_button.pack()

    root.mainloop()

def administrator_interface(conn):
    def view_jobs(status):
        jobs = eval(f'get_{status}_jobs(conn)')
        output.delete(1.0, tk.END)
        for job in jobs:
            output.insert(tk.END, str(job) + '\n')

    def update_job_status_callback():
        job_id = int(job_id_entry.get())
        new_status = status_var.get()
        try:
            update_job_status(conn, job_id, new_status)
            messagebox.showinfo("Success", "Job status updated successfully.")
        except sqlite3.Error as e:
            messagebox.showerror("Error", str(e))

    def add_plan_to_job_callback():
        job_id = int(job_id_entry.get())
        plan_data = plan_data_entry.get()
        plan_type = plan_type_var.get()
        try:
            add_plan_to_job(conn, job_id, plan_data, plan_type)
            messagebox.showinfo("Success", "Plan added to job successfully.")
        except sqlite3.Error as e:
            messagebox.showerror("Error", str(e))

    root = tk.Tk()
    root.title("Administrator Interface")

    output = tk.Text(root, height=10, width=50)
    output.pack()

    view_pending_button = tk.Button(root, text="View Pending Jobs", command=lambda: view_jobs('pending'))
    view_pending_button.pack()

    view_started_button = tk.Button(root, text="View Started Jobs", command=lambda: view_jobs('started'))
    view_started_button.pack()

    view_completed_button = tk.Button(root, text="View Completed Jobs", command=lambda: view_jobs('completed'))
    view_completed_button.pack()

    job_id_label = tk.Label(root, text="Job ID:")
    job_id_label.pack()
    job_id_entry = tk.Entry(root)
    job_id_entry.pack()

    status_var = tk.StringVar(root)
    status_var.set("pending")
    status_options = ["pending", "started", "completed"]
    status_dropdown = tk.OptionMenu(root, status_var, *status_options)
    status_dropdown.pack()

    update_button = tk.Button(root, text="Update Job Status", command=update_job_status_callback)
    update_button.pack()

    plan_data_label = tk.Label(root, text="Plan Data:")
    plan_data_label.pack()
    plan_data_entry = tk.Entry(root)
    plan_data_entry.pack()

    plan_type_var = tk.StringVar(root)
    plan_type_var.set("PDF")
    plan_type_options = ["PDF"]
    plan_type_dropdown = tk.OptionMenu(root, plan_type_var, *plan_type_options)
    plan_type_dropdown.pack()

    add_plan_button = tk.Button(root, text="Add Plan to Job", command=add_plan_to_job_callback)
    add_plan_button.pack()

    root.mainloop()



import sqlite3

def create_connection():
    conn = sqlite3.connect('blackboxdb.db')
    return conn

def insert_customer(conn, name, contact_name, contact_email):
    cur = conn.cursor()
    cur.execute("INSERT INTO Customers (name, contact_name, contact_email) VALUES (?, ?, ?)", (name, contact_name, contact_email))
    conn.commit()

def insert_payment(conn, customer_id, amount, payment_date):
    cur = conn.cursor()
    cur.execute("INSERT INTO Payments (customer_id, amount, payment_date) VALUES (?, ?, ?)", (customer_id, amount, payment_date))
    conn.commit()

def insert_order(conn, customer_id, order_date, total_cost):
    cur = conn.cursor()
    cur.execute("INSERT INTO Orders (customer_id, order_date, total_cost) VALUES (?, ?, ?)", (customer_id, order_date, total_cost))
    conn.commit()

def insert_job(conn, order_id, job_status, start_date, end_date):
    cur = conn.cursor()
    cur.execute("INSERT INTO Jobs (order_id, job_status, start_date, end_date) VALUES (?, ?, ?, ?)", (order_id, job_status, start_date, end_date))
    conn.commit()

def insert_plan(conn, job_id, plan_data, plan_type):
    cur = conn.cursor()
    cur.execute("INSERT INTO Plans (job_id, plan_data, plan_type) VALUES (?, ?, ?)", (job_id, plan_data, plan_type))
    conn.commit()

def get_pending_jobs(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM Jobs WHERE job_status = 'pending'")
    return cur.fetchall()

def get_started_jobs(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM Jobs WHERE job_status = 'started'")
    return cur.fetchall()

def get_completed_jobs(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM Jobs WHERE job_status = 'completed'")
    return cur.fetchall()

def update_job_status(conn, job_id, new_status):
    cur = conn.cursor()
    cur.execute("UPDATE Jobs SET job_status = ? WHERE id = ?", (new_status, job_id))
    conn.commit()

def add_plan_to_job(conn, job_id, plan_data, plan_type):
    cur = conn.cursor()
    cur.execute("INSERT INTO Plans (job_id, plan_data, plan_type) VALUES (?, ?, ?)", (job_id, plan_data, plan_type))
    conn.commit()



def operator_interface(conn):
    while True:
        print("1. View pending jobs")
        print("2. Exit")
        option = int(input("Enter your option: "))
        if option == 1:
            print("Pending jobs:")
            for job in get_pending_jobs(conn):
                print(job)
        elif option == 2:
            break

def administrator_interface(conn):
    while True:
        print("1. View pending jobs")
        print("2. View started jobs")
        print("3. View completed jobs")
        print("4. Update job status")
        print("5. Add plan to job")
        print("6. Exit")
        option = int(input("Enter your option: "))
        if option == 1:
            print("Pending jobs:")
            for job in get_pending_jobs(conn):
                print(job)
        elif option == 2:
            for job in get_started_jobs(conn):
                print(job)
        elif option == 3:
            for job in get_completed_jobs(conn):
                print(job)
        elif option == 4:
            job_id = int(input("Enter job id: "))
            new_status = input("Enter new status: ")
            update_job_status(conn, job_id, new_status)
        elif option == 5:
            job_id = int(input("Enter job id: "))
            plan_data = input("Enter plan data: ")
            plan_type = input("Enter plan type: ")
            add_plan_to_job(conn, job_id, plan_data, plan_type)
        elif option == 6:
            break

def main():
    conn = create_connection()

    while True:
        print("1. Operator")
        print("2. Administrator")
        print("3. Exit")
        option = int(input("Enter your option: "))
        if option == 1:
            operator_interface(conn)
        elif option == 2:
            administrator_interface(conn)
        elif option == 3:
            break

if __name__ == '__main__':
    main()
    
    import base64

def add_plan_to_job(conn, job_id, plan_data, plan_type):
    with open(plan_data, 'rb') as file:
        plan_data_encoded = base64.b64encode(file.read())
    cur = conn.cursor()
    cur.execute("INSERT INTO Plans (job_id, plan_data, plan_type) VALUES (?, ?, ?)", (job_id, plan_data_encoded, plan_type))
    conn.commit()