import sqlite3
import tkinter as tk
from tkinter import messagebox, ttk
import pandas as pd

# Database Initialization
def init_db():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS timetable (
            id INTEGER PRIMARY KEY,
            day TEXT,
            subject TEXT,
            start_time TEXT,
            end_time TEXT,
            teacher TEXT,
            room TEXT
        )
    ''')
    conn.commit()
    conn.close()

# Function to Add Entry
def add_entry(day, subject, start_time, end_time, teacher, room):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    try:
        cursor.execute('''
            INSERT INTO timetable (day, subject, start_time, end_time, teacher, room)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (day, subject, start_time, end_time, teacher, room))
        conn.commit()
        messagebox.showinfo("Success", "Entry added successfully!")
    except Exception as e:
        messagebox.showerror("Error", str(e))
    finally:
        conn.close()

# Function to View All Entries
def view_entries():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM timetable")
    records = cursor.fetchall()
    conn.close()
    return records

# Function to Delete Entry
def delete_entry(entry_id):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    try:
        cursor.execute("DELETE FROM timetable WHERE id = ?", (entry_id,))
        conn.commit()
        messagebox.showinfo("Success", "Entry deleted successfully!")
    except Exception as e:
        messagebox.showerror("Error", str(e))
    finally:
        conn.close()

# Function to Export to CSV
def export_to_csv():
    records = view_entries()
    if records:
        df = pd.DataFrame(records, columns=["ID", "Day", "Subject", "Start Time", "End Time", "Teacher", "Room"])
        df.to_csv("timetable.csv", index=False)
        messagebox.showinfo("Export Successful", "Time table exported to timetable.csv")
    else:
        messagebox.showwarning("No Data", "No entries to export")

# GUI Setup
def setup_gui():
    root = tk.Tk()
    root.title("Time Table Management System")
    root.geometry("600x400")

    # Labels and Entry Widgets
    day_var = tk.StringVar()
    subject_var = tk.StringVar()
    start_time_var = tk.StringVar()
    end_time_var = tk.StringVar()
    teacher_var = tk.StringVar()
    room_var = tk.StringVar()

    tk.Label(root, text="Day").grid(row=0, column=0)
    tk.Entry(root, textvariable=day_var).grid(row=0, column=1)

    tk.Label(root, text="Subject").grid(row=1, column=0)
    tk.Entry(root, textvariable=subject_var).grid(row=1, column=1)

    tk.Label(root, text="Start Time").grid(row=2, column=0)
    tk.Entry(root, textvariable=start_time_var).grid(row=2, column=1)

    tk.Label(root, text="End Time").grid(row=3, column=0)
    tk.Entry(root, textvariable=end_time_var).grid(row=3, column=1)

    tk.Label(root, text="Teacher").grid(row=4, column=0)
    tk.Entry(root, textvariable=teacher_var).grid(row=4, column=1)

    tk.Label(root, text="Room").grid(row=5, column=0)
    tk.Entry(root, textvariable=room_var).grid(row=5, column=1)

    # Button Widgets
    tk.Button(root, text="Add Entry", command=lambda: add_entry(
        day_var.get(), subject_var.get(), start_time_var.get(),
        end_time_var.get(), teacher_var.get(), room_var.get())
    ).grid(row=6, column=0, pady=10)

    tk.Button(root, text="View Entries", command=lambda: display_entries(root)).grid(row=6, column=1)

    tk.Button(root, text="Export to CSV", command=export_to_csv).grid(row=7, column=0, pady=10)

    tk.Button(root, text="Exit", command=root.quit).grid(row=7, column=1)

    root.mainloop()

# Function to Display Entries
def display_entries(parent):
    top = tk.Toplevel(parent)
    top.title("View Time Table")

    records = view_entries()
    if records:
        tree = ttk.Treeview(top, columns=("ID", "Day", "Subject", "Start Time", "End Time", "Teacher", "Room"), show="headings")
        for col in ("ID", "Day", "Subject", "Start Time", "End Time", "Teacher", "Room"):
            tree.heading(col, text=col)
        for record in records:
            tree.insert("", tk.END, values=record)
        tree.pack()
    else:
        messagebox.showinfo("No Data", "No entries found")

# Main Function
if __name__ == "__main__":
    init_db()
    setup_gui()
