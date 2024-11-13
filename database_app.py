import tkinter as tk
from tkinter import ttk, Scrollbar
from tkinter import messagebox
import psycopg2
from typing import List, Tuple, Any


def run_query(query: str, parameters: tuple = ()) -> List[Tuple[Any, ...]]:
    # Connect to the database
    conn = psycopg2.connect(
        dbname="studentdb",
        user="postgres",
        password="2179",
        host="localhost",  # or the IP address of your PostgreSQL server
        port="5432",
    )
    cur = conn.cursor()
    query_result = []
    try:
        cur.execute(query, parameters)
        if query.lower().startswith("select"):
            query_result = cur.fetchall()
        conn.commit()
    except psycopg2.Error as e:
        messagebox.showerror("Error", f"Error: {e}")
    finally:
        cur.close()
        conn.close()
    return query_result


def refresh_treeview():
    records = run_query("SELECT * FROM students")
    for i in tree.get_children():
        tree.delete(i)
    for record in records:
        tree.insert("", tk.END, values=record)


def insert_data():
    query = (
        "INSERT INTO students (student_id, name, age, address) VALUES (%s, %s, %s, %s)"
    )
    parameters = (
        id_entry.get(),
        name_entry.get(),
        age_entry.get(),
        address_entry.get(),
    )
    run_query(query, parameters)
    messagebox.showinfo("Success", "Record inserted successfully")
    refresh_treeview()


def delete_record():
    try:
        selected_item = tree.selection()[0]
        student_id = tree.item(selected_item, "values")[0]
        query = "DELETE FROM students WHERE student_id = %s"
        run_query(query, (student_id,))
        messagebox.showinfo("Success", "Record deleted successfully")
        refresh_treeview()
    except IndexError:
        messagebox.showerror("Error", "Please select a record to delete")


def update_data():
    try:
        selected_item = tree.selection()[0]
        student_id = tree.item(selected_item, "values")[0]
        query = "UPDATE students SET name = %s, age = %s, address = %s WHERE student_id = %s"
        parameters = (
            name_entry.get(),
            age_entry.get(),
            address_entry.get(),
            student_id,
        )
        run_query(query, parameters)
        messagebox.showinfo("Success", "Record updated successfully")
        refresh_treeview()
    except IndexError:
        messagebox.showerror("Error", "Please select a record to update")


def create_table():
    query = "CREATE TABLE if not exists students (student_id SERIAL PRIMARY KEY, name VARCHAR(100), age INTEGER, address TEXT)"
    run_query(query)
    messagebox.showinfo("Success", "Table created successfully")
    refresh_treeview()


root = tk.Tk()
root.title("Student Management System")

frame = tk.LabelFrame(root, text="Student Details")
frame.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

tk.Label(frame, text="Student ID:").grid(row=0, column=0, padx=10, pady=10, sticky="w")
id_entry = tk.Entry(frame)
id_entry.grid(row=0, column=1, padx=10, pady=10, sticky="ew")

tk.Label(frame, text="Name:").grid(row=1, column=0, padx=10, pady=10, sticky="w")
name_entry = tk.Entry(frame)
name_entry.grid(row=1, column=1, padx=10, pady=10, sticky="ew")

tk.Label(frame, text="Age:").grid(row=2, column=0, padx=10, pady=10, sticky="w")
age_entry = tk.Entry(frame)
age_entry.grid(row=2, column=1, padx=10, pady=10, sticky="ew")

tk.Label(frame, text="Address:").grid(row=3, column=0, padx=10, pady=10, sticky="w")
address_entry = tk.Entry(frame)
address_entry.grid(row=3, column=1, padx=10, pady=10, sticky="ew")

button_frame = tk.Frame(root)
button_frame.grid(row=1, column=0, padx=10, pady=10, sticky="ew")

tk.Button(button_frame, text="Add Record", command=insert_data).grid(
    row=0, column=0, padx=10, pady=10
)
tk.Button(button_frame, text="Update Data", command=update_data).grid(
    row=0, column=1, padx=10, pady=10
)
tk.Button(button_frame, text="Update Record").grid(row=0, column=2, padx=10, pady=10)
tk.Button(button_frame, text="Update Record", command=update_data).grid(
    row=0, column=2, padx=10, pady=10
)
tk.Button(button_frame, text="Read Record", command=refresh_treeview).grid(
    row=0, column=3, padx=10, pady=10
)
tk.Button(button_frame, text="Create Table", command=create_table).grid(
    row=0, column=5, padx=10, pady=10
)
tk.Button(button_frame, text="Exit").grid(row=0, column=6, padx=10, pady=10)

tree_frame = tk.Frame(root)
tree_frame.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")

tree = ttk.Treeview(tree_frame, columns=(1, 2, 3, 4), show="headings")
tree.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

tree_scroll = Scrollbar(tree_frame, orient="vertical", command=tree.yview)
tree_scroll.grid(row=0, column=1, sticky="ns")

tree.configure(yscrollcommand=tree_scroll.set)

tree["columns"] = ("Student ID", "Name", "Age", "Address")
tree.column("#0", width=0, stretch=tk.NO)
tree.column("Student ID", anchor=tk.W, width=100)
tree.column("Name", anchor=tk.W, width=100)
tree.column("Age", anchor=tk.W, width=100)
tree.column("Address", anchor=tk.W, width=250)

tree.heading("Student ID", text="Student ID", anchor=tk.W)
tree.heading("Name", text="Name", anchor=tk.W)
tree.heading("Age", text="Age", anchor=tk.W)
tree.heading("Address", text="Address", anchor=tk.W)

refresh_treeview()

root.mainloop()
