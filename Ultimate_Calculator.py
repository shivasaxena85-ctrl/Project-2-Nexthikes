import tkinter as tk
from tkinter import ttk
import math
from datetime import date, datetime
from calendar import monthrange
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import os
import customtkinter as ctk
import random
import json
from urllib.request import urlopen
from urllib.error import URLError, HTTPError


root = tk.Tk()
root.title("Advanced Calculator")
root.geometry("650x600")
root.minsize(600, 550)
root.configure(bg="#071b35")

# Main Application Layout
main_container = tk.Frame(root, bg="#071B35")
main_container.pack(fill="both", expand=True)

# Right Side - Full Height Sidebar
right_panel = tk.Frame(
    main_container,
    bg="#071B35",
    width=250
)
right_panel.pack(side="right", fill="y")
right_panel.pack_propagate(False)

# Left Side - Main Calculator Area
left_content = tk.Frame(main_container, bg="#071B35")
left_content.pack(side="left", fill="both", expand=True)

header_frame = tk.Frame(left_content, bg="#071B35")
header_frame.pack(fill="x", padx=5, pady=(10, 0))

header_left = tk.Frame(header_frame, bg="#071B35")
header_left.pack(side="left", anchor="nw", fill="x", expand=True, padx=(15, 0))

title = tk.Label(
    header_left,
    text="Advanced Calculator",
    font=("Arial", 11, "bold"),
    bg="#071B35",
    fg="#38BDF8",
    anchor="w"
)
title.pack(anchor="w", pady=(5, 2))

home_back_button = ctk.CTkButton(
    root,
    text="←",
    width=24,
    height=26,
    corner_radius=12,
    font=("Arial", 17, "bold"),
    fg_color="transparent",
    hover_color="#164783",
    text_color="#38BDF8",
    border_width=0
)

home_back_button.place_forget()

home_back_button = ctk.CTkButton(
    root,
    text="←",
    command=lambda: go_back_home(),
    width=32,
    height=28,
    corner_radius=6,
    font=("Arial", 17, "bold"),
    fg_color="#164783",
    hover_color="#2563EB",
    text_color="#FFFFFF",
    border_width=0
)

header_info_frame = tk.Frame(header_left, bg="#071B35")
header_info_frame.pack(anchor="w", pady=(0, 8))

calculator_icon = tk.Canvas(
    header_info_frame,
    width=30,
    height=34,
    bg="#071B35",
    highlightthickness=0
)
calculator_icon.pack(side="left", padx=(0, 8))

# Calculator body
calculator_icon.create_rectangle(
    4, 2, 26, 32,
    fill="#1677F2",
    outline="#38BDF8",
    width=1
)

# Display screen
calculator_icon.create_rectangle(
    7, 6, 23, 12,
    fill="#071B35",
    outline="#FFFFFF",
    width=1
)

# Small calculator buttons
for row in range(3):
    for col in range(3):
        x = 8 + col * 5
        y = 16 + row * 4
        calculator_icon.create_rectangle(
            x, y, x + 3, y + 2,
            fill="#FFFFFF",
            outline="#FFFFFF"
        )

# Equals button
calculator_icon.create_rectangle(
    20, 27, 23, 29,
    fill="#38BDF8",
    outline="#38BDF8"
)

for row in range(3):
    for col in range(3):
        x = 8 + col * 5
        y = 16 + row * 4
        calculator_icon.create_rectangle(
            x, y, x + 3, y + 2,
            fill="#FFFFFF",
            outline="#FFFFFF"
        )

info_text_frame = tk.Frame(header_info_frame, bg="#071B35")
info_text_frame.pack(side="left", anchor="w")

app_name = tk.Label(
    info_text_frame,
    text="Python Ultimate Calculator",
    font=("Arial", 10, "bold"),
    bg="#071B35",
    fg="#FFFFFF",
    anchor="w"
)
app_name.pack(anchor="w")

subtitle = tk.Label(
    info_text_frame,
    text="Scientific Calculations, Smart, Fast, Powerful",
    font=("Arial", 8),
    bg="#071B35",
    fg="#CBD5E1",
    anchor="w"
)
subtitle.pack(anchor="w")

menu_button = tk.Button(
    header_frame,
    text="☰",
    font=("Arial", 10),
    bg="#071B35",
    fg="#38BDF8",
    activebackground="#12345A",
    activeforeground="#FFFFFF",
    relief="flat",
    bd=0,
    cursor="hand2"
)

menu_button.place(x=0, y=2, width=16, height=16)

style = ttk.Style()
style.theme_use("clam")

style.configure(
    "History.Vertical.TScrollbar",
    background="#38BDF8",
    troughcolor="#CBD5E1",
    bordercolor="#CBD5E1",
    arrowcolor="#071B35",
    lightcolor="#38BDF8",
    darkcolor="#1677F2",
    relief="flat",
    borderwidth=0,
    arrowsize=14,
    width=18
)

style.configure(
    "TNotebook",
    background="#071B35",
    borderwidth=0,
    padding=0,
    relief="flat"
)

style.configure(
    "TNotebook",
    background="#071B35",
    borderwidth=0,
    relief="flat",
    padding=0
)

style.configure(
    "TNotebook.Tab",
    background="#071B35",
    borderwidth=0
)

style.layout("TNotebook", [
    ("Notebook.client", {
        "sticky": "nswe"
    })
])

style.configure(
    "TNotebook",
    background="#071B35",
    borderwidth=0,
    padding=0,
    relief="flat"
)

style.configure(
    "TNotebook",
    background="#071B35",
    borderwidth=0,
    relief="flat"
)

style.configure(
    "TFrame",
    background="#071B35",
    borderwidth=0,
    relief="flat"
)

style.configure(
    "TNotebook.Tab",
    borderwidth=0,
    padding=(1, 2),
    font=("Arial", 6, "bold")
)

style.configure(
    "Action.TButton",
    background="#1677F2",
    foreground="#FFFFFF",
    font=("Arial", 8, "bold"),
    padding=(4, 2),
    borderwidth=0
)

style.map(
    "Action.TButton",
    background=[
        ("active", "#0958D9"),
        ("pressed", "#0646A6")
    ],
    foreground=[
        ("active", "#FFFFFF"),
        ("pressed", "#FFFFFF")
    ]
)

style.configure(
    "TNotebook",
    background="#071B35",
    borderwidth=0,
    padding=0,
    relief="flat"
)

style.configure(
    "TNotebook.tab",
    expand=False
)

style.configure(
    "TFrame",
    background="#071B35"
)

style.configure(
    "TLabel",
    background="#071B35",
    foreground="#FFFFFF",
    font=("Arial", 8)
)

style.configure(
    "TCheckbutton",
    background="#071B35",
    foreground="#FFFFFF",
    font=("Arial", 9)
)

style.map(
    "TCheckbutton",
    background=[("active", "#071B35")],
    foreground=[("active", "#38BDF8")]
)

style.configure(
    "TNotebook.Tab",
    background="#12345A",
    foreground="#FFFFFF",
    padding=[2, 3],
    borderwidth=0,
    font=("Arial", 6, "bold")
)

style.map(
    "TNotebook.Tab",
    background=[
        ("selected", "#0878F9"),
        ("active", "#2563EB")
    ],
    foreground=[
        ("selected", "#FFFFFF"),
        ("active", "#FFFFFF")
    ]
)

# Remove white border around Notebook
style.configure(
    "TNotebook",
    background="#071B35",
    borderwidth=0,
    relief="flat",
    lightcolor="#071B35",
    darkcolor="#071B35",
    bordercolor="#071B35",
    focuscolor="#071B35"
)

style.map(
    "TNotebook",
    bordercolor=[("!disabled", "#071B35")],
    lightcolor=[("!disabled", "#071B35")],
    darkcolor=[("!disabled", "#071B35")]
)

notebook = ttk.Notebook(left_content)
notebook.configure(style="TNotebook")
notebook.pack(fill="both", expand=True, padx=0, pady=(5, ))

def update_back_button(event=None):
    if graph_view_frame.winfo_ismapped():
        home_back_button.place_forget()
        return

    if notebook.index("current") == 0:
        home_back_button.place_forget()
    else:
        home_back_button.place(
            relx=1.0,
            rely=1.0,
            x=-8,
            y=-8,
            anchor="se"
        )
        home_back_button.lift()

notebook.bind("<<NotebookTabChanged>>", update_back_button)
root.after(100, update_back_button)

scientific_tab = ttk.Frame(notebook)
age_tab = ttk.Frame(notebook)
graph_tab = ttk.Frame(notebook)
guided_tab = ttk.Frame(notebook)
unit_tab = ttk.Frame(notebook)
history_tab = ttk.Frame(notebook)
currency_tab = ttk.Frame(notebook)

notebook.add(scientific_tab, text="Scientific")
notebook.add(age_tab, text="Age Calculator")
notebook.add(graph_tab, text="Graph Plotter")
notebook.add(guided_tab, text="Guided Calculator")
notebook.add(unit_tab, text="Unit Converter")
notebook.add(history_tab, text="Calculation History")
notebook.add(currency_tab, text="Currency Converter")

def go_back_home():
    graph_view_frame.place_forget()
    notebook.select(scientific_tab)

tk.Label(
    history_tab,
    text="Calculation History",
    font=("Arial", 10, "bold"),
    bg="#071B35",
    fg="#38BDF8"
).pack(pady=(10, 5))

# History list and vertical scrollbar
history_frame = tk.Frame(
    history_tab,
    bg="#071B35",
    bd=0,
    highlightthickness=0
)

history_frame.pack(
    padx=15,
    pady=5,
    fill="both",
    expand=True
)

history_frame.grid_rowconfigure(0, weight=1)
history_frame.grid_columnconfigure(0, weight=1)

history_scrollbar = tk.Scrollbar(
    history_frame,
    orient="vertical",
    width=18,
    bg="#38BDF8",
    activebackground="#1677F2",
    troughcolor="#CBD5E1",
    relief="flat",
    bd=0
)

history_list = tk.Listbox(
    history_frame,
    font=("Arial", 10),
    bg="#0B2545",
    fg="#FFFFFF",
    selectbackground="#1677F2",
    selectforeground="#FFFFFF",
    borderwidth=0,
    highlightthickness=0,
    activestyle="none",
    yscrollcommand=history_scrollbar.set
)

history_list.configure(yscrollcommand=history_scrollbar.set)
history_scrollbar.configure(command=history_list.yview)

history_scrollbar.configure(
    command=history_list.yview
)

history_list.grid(
    row=0,
    column=0,
    sticky="nsew"
)

history_scrollbar.grid(
    row=0,
    column=1,
    sticky="ns"
)

def save_history(expression, answer):
    history_list.insert(
        tk.END,
        f"{expression} = {answer}"
    )

    right_history_list.insert(tk.END, f"{expression} = {answer}")

    try:
        with open ("calculator_history.txt","a", encoding="utf-8") as file:
            file. write(f"{expression} = {answer}\n ")
    except OSError as err:
        print("History save error:", err)

def load_history():
    try:
        with open("calculator_history.txt", "r", encoding="utf-8") as file:
            for line in file:
                entry = line.strip()
                if entry:
                    history_list.insert(tk.END, entry)
                    right_history_list.insert(tk.END, entry)
    except FileNotFoundError:
        pass
    except OSError as err:
        print("History load error:", err)
        
def clear_history():
    history_list.delete(0, tk.END)
    history_list.update_idletasks()
    right_history_list.delete(0, tk.END)
    clear_display()

    try:
        with open("calculator_history.txt", "w", encoding="utf-8") as file:
            file.write("")
    except OSError as err:
        print("History clear error:", err)

def delete_selected_history():
    selected = right_history_list.curselection()

    if not selected:
        return

    index = selected[0]
    right_history_list.delete(index)

    history_list.delete(0, tk.END)
    for item in right_history_list.get(0, tk.END):
        history_list.insert(tk.END, item)

    try:
        with open("calculator_history.txt", "w", encoding="utf-8") as file:
            for item in right_history_list.get(0, tk.END):
                file.write(item + "\n")
    except OSError as err:
        print("History delete error:", err)
        
ctk.CTkButton(
    history_tab,
    text="Clear History",
    command=clear_history,
    width=140,
    height=30,
    corner_radius=8,
    font=("Arial", 9, "bold"),
    text_color="#FFFFFF",
    fg_color="#DC3545",
    hover_color="#B02A37",
    border_width=1,
    border_color="#38BDF8"
).pack(pady=10)

ctk.CTkButton(
    history_tab,
    text="Delete Selected",
    command=delete_selected_history,
    width=170,
    height=36,
    corner_radius=8,
    font=("Arial", 11, "bold"),
    text_color="#FFFFFF",
    fg_color="#F59E0B",
    hover_color="#D97706",
    border_width=1,
    border_color="#38BDF8"
).pack(pady=5)

tk.Label(
    unit_tab,
    text="Unit Converter",
    font=("Arial", 10, "bold")
).pack(pady=15)

tk.Label(
    unit_tab,
    text="Enter Value:",
    font=("Arial", 10)
).pack()

unit_entry = tk.Entry(
    unit_tab,
    font=("Arial", 10),
    width=20
)
unit_entry.pack(pady=5)

conversion_options = [
    "Centimeter to Meter",
    "Meter to Kilometer",
    "Kilometer to Mile",
    "Celsius to Fahrenheit",
    "Kilogram to Gram"
]

unit_choice = ttk.Combobox(
    unit_tab,
    values=conversion_options,
    state="readonly",
    font=("Arial", 10),
    width=25
)
unit_choice.set("Centimeter to Meter")
unit_choice.pack(pady=10)

unit_result = tk.Label(
    unit_tab,
    text="Result will appear here",
    font=("Arial", 10)
)
unit_result.pack(pady=15)

def convert_units():
    try:
        value = float(unit_entry.get())
        choice = unit_choice.get()

        if choice == "Centimeter to Meter":
            result = value / 100
            output = f"{result:g} meters"

        elif choice == "Meter to Kilometer":
            result = value / 1000
            output = f"{result:g} kilometers"

        elif choice == "Kilometer to Mile":
            result = value * 0.621371
            output = f"{result:.4f} miles"

        elif choice == "Celsius to Fahrenheit":
            result = (value * 9 / 5) + 32
            output = f"{result:g} °F"

        elif choice == "Kilogram to Gram":
            result = value * 1000
            output = f"{result:g} grams"

        else:
            output = "Please select a conversion."

        unit_result.config(text=f"Result: {output}")
        save_history(f"{value} | {choice}", output)

    except ValueError:
        unit_result.config(text="Please enter a valid number.")

ctk.CTkButton(
    unit_tab,
    text="Convert",
    command=convert_units,
    width=130,
    height=30,
    corner_radius=8,
    font=("Arial", 9, "bold"),
    text_color="#FFFFFF",
    fg_color="#1677F2",
    hover_color="#0958D9",
    border_width=1,
    border_color="#38BDF8"
).pack(pady=10)

# ==========================================
# CURRENCY CONVERTER
# ==========================================

tk.Label(
    currency_tab,
    text="💱 Currency Converter",
    font=("Arial", 12, "bold"),
    bg="#071B35",
    fg="#38BDF8"
).pack(pady=(15, 12))

tk.Label(
    currency_tab,
    text="Enter Amount:",
    font=("Arial", 10)
).pack(pady=4)

currency_amount_entry = tk.Entry(
    currency_tab,
    font=("Arial", 11),
    width=22,
    justify="center"
)
currency_amount_entry.pack(pady=5)
currency_amount_entry.insert(0, "1")

currency_codes = [
    "INR", "USD", "EUR", "GBP", "JPY",
    "AUD", "CAD", "CHF", "CNY", "SGD",
    "NZD", "HKD", "SEK", "NOK", "DKK",
    "ZAR", "BRL", "MXN", "KRW", "IDR",
    "ILS", "PLN", "CZK", "HUF", "TRY"
]

tk.Label(
    currency_tab,
    text="From Currency:",
    font=("Arial", 10)
).pack(pady=(8, 3))

currency_from = ttk.Combobox(
    currency_tab,
    values=currency_codes,
    state="readonly",
    font=("Arial", 10),
    width=18
)
currency_from.set("INR")
currency_from.pack(pady=4)

tk.Label(
    currency_tab,
    text="To Currency:",
    font=("Arial", 10)
).pack(pady=(8, 3))

currency_to = ttk.Combobox(
    currency_tab,
    values=currency_codes,
    state="readonly",
    font=("Arial", 10),
    width=18
)
currency_to.set("USD")
currency_to.pack(pady=4)


def swap_currencies():
    old_from = currency_from.get()
    old_to = currency_to.get()

    currency_from.set(old_to)
    currency_to.set(old_from)


def convert_currency():
    try:
        amount = float(currency_amount_entry.get())

        if not math.isfinite(amount) or amount < 0:
            raise ValueError

        from_code = currency_from.get()
        to_code = currency_to.get()

        if not from_code or not to_code:
            raise ValueError

        if from_code == to_code:
            rate = 1.0
            rate_date = "Same Currency"
        else:
            url = (
                f"https://api.frankfurter.dev/v2/"
                f"rate/{from_code}/{to_code}"
            )

            with urlopen(url, timeout=10) as response:
                data = json.loads(response.read().decode("utf-8"))

            rate = float(data["rate"])
            rate_date = data["date"]

        converted_amount = amount * rate

        currency_result.config(
            text=(
                f"{amount:,.2f} {from_code}\n"
                f"= {converted_amount:,.2f} {to_code}"
            ),
            fg="#38BDF8"
        )

        currency_rate_label.config(
            text=f"Exchange Rate: 1 {from_code} = "
                 f"{rate:.6f} {to_code}\n"
                 f"Rate Date: {rate_date}"
        )

        save_history(
            f"Currency: {amount:g} {from_code} to {to_code}",
            f"{converted_amount:.2f} {to_code}"
        )

    except ValueError:
        currency_result.config(
            text="Please enter a valid amount.",
            fg="#F87171"
        )
        currency_rate_label.config(text="")

    except (URLError, HTTPError, TimeoutError, KeyError, OSError):
        currency_result.config(
            text="Unable to fetch exchange rate.\nCheck your internet connection.",
            fg="#F87171"
        )
        currency_rate_label.config(text="")

    except Exception as err:
        currency_result.config(
            text=f"Conversion Error: {err}",
            fg="#F87171"
        )
        currency_rate_label.config(text="")


currency_buttons_frame = tk.Frame(
    currency_tab,
    bg="#071B35"
)
currency_buttons_frame.pack(pady=12)

ctk.CTkButton(
    currency_buttons_frame,
    text="Convert",
    command=convert_currency,
    width=115,
    height=32,
    corner_radius=8,
    font=("Arial", 9, "bold"),
    fg_color="#1677F2",
    hover_color="#0958D9",
    text_color="#FFFFFF"
).pack(side="left", padx=5)

ctk.CTkButton(
    currency_buttons_frame,
    text="⇄ Swap",
    command=swap_currencies,
    width=100,
    height=32,
    corner_radius=8,
    font=("Arial", 9, "bold"),
    fg_color="#0E7490",
    hover_color="#155E75",
    text_color="#FFFFFF"
).pack(side="left", padx=5)

currency_result = tk.Label(
    currency_tab,
    text="Converted amount will appear here",
    font=("Arial", 11, "bold"),
    bg="#071B35",
    fg="#38BDF8",
    justify="center"
)
currency_result.pack(pady=(12, 8))

currency_rate_label = tk.Label(
    currency_tab,
    text="",
    font=("Arial", 9),
    bg="#071B35",
    fg="#CBD5E1",
    justify="center"
)
currency_rate_label.pack(pady=5)

tk.Label(
    guided_tab,
    text="Guided Calculator",
    font=("Arial", 10, "bold")
).pack(pady=15)

tk.Label(
    guided_tab,
    text="Enter a math expression (Example: 25 + 35):",
    font=("Arial", 10)
).pack(pady=5)

guided_entry = tk.Entry(
    guided_tab,
    font=("Arial", 10),
    width=30
)
guided_entry.pack(pady=10)

guided_result = tk.Label(
    guided_tab,
    text="Your answer will appear here",
    font=("Arial", 10),
    justify="left"
)
guided_result.pack(pady=15)

def guided_calculate():
    try:
        expression = guided_entry.get().strip()
        expression = expression.replace("^", "**")

        # Convert percentage expressions, e.g. 200*10% -> 200*10/100
        import re
        expression = re.sub(
            r"(\d+(?:\.\d+)?)%",
            r"(\1/100)",
            expression
        )

        if not expression:
            guided_result.config(text="Please enter an expression.")
            return

        allowed = {
            "abs": abs,
            "round": round,
            "sqrt": math.sqrt,
            "pi": math.pi,
            "e": math.e
        }

        answer = eval(
            expression,
            {"_builtins_": {}},
            allowed
        )

        steps = f"Expression: {expression}\n"

        if expression.startswith("sqrt(") and expression.endswith(")"):
            number = expression[5:-1]
            steps += f"Step 1: Find the square root of {number}.\n"

        elif "+" in expression:
            steps += "Step 1: Add the numbers.\n"

        elif "-" in expression:
            steps += "Step 1: Subtract the numbers.\n"

        elif "*" in expression:
            steps += "Step 1: Multiply the numbers.\n"

        elif "/" in expression:
            steps += "Step 1: Divide the numbers.\n"

        elif "**" in expression:
            steps += "Step 1: Calculate the power.\n"

        else:
            steps += "Step 1: Evaluate the expression.\n"

        steps += f"Calculation: {expression} = {answer}\n"
        steps += f"Final Answer: {answer}"

        guided_result.config(text=steps)
        save_history(expression, answer)

    except Exception:
        guided_result.config(
            text="Invalid expression. Please check your input."
        )

ctk.CTkButton(
    guided_tab,
    text="Calculate",
    command=guided_calculate,
    width=130,
    height=30,
    corner_radius=8,
    font=("Arial", 9, "bold"),
    text_color="#FFFFFF",
    fg_color="#1677F2",
    hover_color="#0958D9",
    border_width=1,
    border_color="#38BDF8"
).pack(pady=10)

calculator_layout = tk.Frame(
    scientific_tab,
    bg="#071B35",
    bd=0,
    borderwidth=0,
    highlightthickness=0,
    relief="flat"
)

calculator_layout.pack(
    fill="both",
    expand=True,
    padx=0,
    pady=0,
    ipadx=0,
    ipady=0
)

left_panel = tk.Frame(
    calculator_layout,
    bg="#0B2545",
    highlightbackground="#164E78",
    highlightthickness=1,
    bd=0
)

left_panel.configure(height=490)

left_panel.pack(
    side="left",
    fill="x",
    expand=False,
    padx=(0, 4),
    pady=(40, 0),
    anchor="nw"
)

# Calculation History Box
history_box = tk.Frame(
    right_panel,
    bg="#0B2545",
    highlightbackground="#164E78",
    highlightthickness=1,
    bd=0
)

history_box.pack(
    fill="x",
    padx=4,
    pady=(5, 4),
    ipadx=2,
    ipady=3
)

history_heading = tk.Frame(
    history_box,
    bg="#0B2545"
)
history_heading.pack(
    fill="x",
    padx=3,
    pady=(2, 4)
)

tk.Label(
    history_heading,
    text="🕘",
    font=("Segoe UI Emoji", 16),
    bg="#0B2545",
    fg="#38BDF8"
).pack(side="left", padx=(0, 5))

tk.Label(
    history_heading,
    text="Calculation History",
    font=("Arial", 9, "bold"),
    bg="#0B2545",
    fg="#38BDF8"
).pack(side="left")

# History list: reduced height
right_history_list = tk.Listbox(
    history_box,
    font=("Arial", 8),
    width=20,
    height=7,
    bg="#0B2545",
    fg="#FFFFFF",
    selectbackground="#2563EB",
    relief="flat",
    borderwidth=0,
    highlightthickness=0
)
right_history_list.pack(
    fill="x",
    expand=False,
    padx=4,
    pady=(0, 2)
)

# History Buttons - Improved Size
history_buttons_frame = tk.Frame(
    history_box,
    bg="#0B2545"
)

history_buttons_frame.pack(
    fill="x",
    padx=5,
    pady=(6, 10)
)

history_buttons_frame.grid_columnconfigure(
    0, weight=1, uniform="history_buttons"
)

history_buttons_frame.grid_columnconfigure(
    1, weight=1, uniform="history_buttons"
)

ctk.CTkButton(
    history_buttons_frame,
    text="Clear All",
    command=clear_history,
    height=32,
    corner_radius=6,
    font=("Arial", 9, "bold"),
    fg_color="#DC3545",
    text_color="#FFFFFF",
    hover_color="#B02A37",
    border_width=0
).grid(
    row=0,
    column=0,
    sticky="ew",
    padx=3,
    pady=2
)

ctk.CTkButton(
    history_buttons_frame,
    text="Delete Selected",
    command=delete_selected_history,
    height=32,
    corner_radius=6,
    font=("Arial", 9, "bold"),
    fg_color="#F59E0B",
    text_color="#FFFFFF",
    hover_color="#D97706",
    border_width=0
).grid(
    row=0,
    column=1,
    sticky="ew",
    padx=3,
    pady=2
)

# Memory Box
memory_box = tk.Frame(
    right_panel,
    bg="#0B2545",
    highlightbackground="#164E78",
    highlightthickness=1,
    bd=0
)
memory_box.pack(
    fill="x",
    padx=5,
    pady=7,
    ipadx=4,
    ipady=5
)

memory_heading = tk.Label(
    memory_box,
    text="🧠  Memory",
    font=("Arial", 9, "bold"),
    bg="#0B2545",
    fg="#38BDF8"
)
memory_heading.pack(
    anchor="w",
    padx=6,
    pady=(5, 4)
)

memory_controls_frame = tk.Frame(
    memory_box,
    bg="#0B2545"
)
memory_controls_frame.pack(
    fill="x",
    padx=4,
    pady=(0, 5)
)

# Memory Value Display Box
memory_value_frame = tk.Frame(
    memory_box,
    bg="#071B35",
    highlightbackground="#164E78",
    highlightthickness=1,
    bd=0
)

memory_value_frame.pack(
    fill="x",
    padx=5,
    pady=(3, 6)
)

memory_value_label = tk.Label(
    memory_value_frame,
    text="Memory Value: 0",
    font=("Arial", 9, "bold"),
    bg="#071B35",
    fg="#38BDF8",
    anchor="w",
    padx=8,
    pady=5
)

memory_value_label.pack(fill="x")

# Calculator Tabs Box
calculator_tabs_frame = tk.Frame(
    right_panel,
    bg="#0B2545",
    highlightbackground="#164E78",
    highlightthickness=1,
    bd=0
)

calculator_tabs_frame.pack(
    fill="both",
    expand=True,
    padx=5,
    pady=3
)

calculator_tabs_heading = tk.Frame(
    calculator_tabs_frame,
    bg="#0B2545"
)
calculator_tabs_heading.pack(fill="x", padx=3, pady=(2, 5))

tk.Label(
    calculator_tabs_heading,
    text="🧮",
    font=("Segoe UI Emoji", 16),
    bg="#0B2545",
    fg="#38BDF8"
).pack(side="left", padx=(0, 5))

tk.Label(
    calculator_tabs_heading,
    text="Calculator Tabs",
    font=("Arial", 10, "bold"),
    bg="#0B2545",
    fg="#38BDF8",
    anchor="w"
).pack(side="left")

calculator_tab_items = [
    ("🧮", "Scientific", scientific_tab),
    ("📊", "Graph Plotter", graph_tab),
    ("📅", "Age Calculator", age_tab),
    ("🎓", "Guided Calculator", guided_tab),
    ("🔄", "Unit Converter", unit_tab),
    ("📜", "Calculation History", history_tab),
    ("💱", "Currency Converter", currency_tab),
]

for icon_text, tab_name, tab_frame in calculator_tab_items:
    ctk.CTkButton(
        calculator_tabs_frame,
        text=f"{icon_text}  {tab_name}",
        command=lambda tab=tab_frame: notebook.select(tab),
        height=25,
        corner_radius=6,
        font=("Arial", 10, "bold"),
        anchor="w",
        fg_color="#0B2545",
        hover_color="#164783",
        text_color="#FFFFFF",
        border_width=0
    ).pack(fill="x", padx=2, pady=1)

tk.Label(
    left_panel,
    text="Scientific Calculator",
    font=("Arial", 10, "bold"),
    bg="#071B35",
    fg="#38BDF8"
).pack(pady=(3, 5))

display = tk.Entry(
    left_panel,
    font=("Arial", 15, "bold"),
    justify="right",
    bg="#0B2545",
    fg="#FFFFFF",
    insertbackground="#38BDF8",
    relief="flat",
    bd=0,
    highlightthickness=2,
    highlightbackground="#0B2545",
    highlightcolor="#0B2545"
)

display.pack(
    fill="x",
    padx=(5, 8),
    pady=(5, 4),
    ipady=9
)

# Keyboard controls: More Symbols and ABC/123
keyboard_controls = tk.Frame(
    left_panel,
    bg="#071B35"
)
keyboard_controls.pack(
    fill="x",
    padx=2,
    pady=(0, 0)
)

mode_button = ctk.CTkButton(
    keyboard_controls,
    text="ABC",
    command=lambda: toggle_keyboard_mode(),
    width=46,
    height=34,
    corner_radius=6,
    font=("Arial", 10, "bold"),
    fg_color="#7138E8",
    hover_color="#5B21B6",
    text_color="#FFFFFF",
    border_width=0
)
mode_button.pack(side="left", padx=1, pady=1)

memory_value = 0

def update_memory_value():
    memory_value_label.config(
        text=f"Memory Value: {memory_value:g}"
    )

def memory_add():
    global memory_value
    try:
        memory_value += float(display.get())
        update_memory_value()
    except ValueError:
        pass

def memory_subtract():
    global memory_value
    try:
        memory_value -= float(display.get())
        update_memory_value()
    except ValueError:
        pass

def memory_recall():
    display.delete(0, tk.END)
    display.insert(0, str(memory_value))

def memory_store():
    global memory_value

    try:
        memory_value = float(display.get())
        update_memory_value()
    except ValueError:
        pass

def memory_clear():
    global memory_value
    memory_value = 0
    update_memory_value()

memory_button_styles = {
    "MC": ("#7138E8", "#5B21B6"),
    "MR": ("#0891B2", "#0E7490"),
    "M+": ("#1677F2", "#0958D9"),
    "M−": ("#0E7490", "#155E75"),
    "MS": ("#0891B2", "#0E7490")
}

memory_buttons = [
    ("MC", "Clear", memory_clear),
    ("MR", "Recall", memory_recall),
    ("M+", "Add", memory_add),
    ("M−", "Subtract", memory_subtract),
    ("MS", "Store", memory_store)
]

for label, button_caption, command in memory_buttons:
    bg_color, hover_color = memory_button_styles[label]

    button_frame = tk.Frame(
        memory_controls_frame,
        bg="#0B2545"
    )
    button_frame.pack(
        side="left",
        fill="x",
        expand=True,
        padx=1
    )

    button_text = label
    if button_caption:
        button_text += f"\n{button_caption}"

    ctk.CTkButton(
        button_frame,
        text=button_text,
        command=command,
        width=40,
        height=34,
        corner_radius=6,
        font=("Arial", 8, "bold"),
        fg_color=bg_color,
        hover_color=hover_color,
        text_color="#FFFFFF",
        border_width=0
    ).pack(
        fill="x",
        padx=0,
        pady=1
    )

    # Main Keyboard Memory Buttons
    ctk.CTkButton(
        keyboard_controls,
        text=label,
        command=command,
        width=46,
        height=34,
        corner_radius=6,
        font=("Arial", 10, "bold"),
        text_color="#FFFFFF",
        fg_color=bg_color,
        hover_color=hover_color,
        border_width=0
    ).pack(side="left", padx=1, pady=1)

# Memory Store Button (MS)
ctk.CTkButton(
    keyboard_controls,
    text="MS",
    command=memory_store,
    width=46,
    height=34,
    corner_radius=6,
    font=("Arial", 10, "bold"),
    text_color="#FFFFFF",
    fg_color="#0891B2",
    hover_color="#0E7490",
    border_width=0
).pack(side="left", padx=1, pady=1)

# Backspace Button Function
def backspace_one():
    current = display.get()
    position = display.index(tk.INSERT)

    if current and position > 0:
        display.delete(position - 1)

# Cross / Backspace Button
ctk.CTkButton(
    keyboard_controls,
    text="×",
    command=backspace_one,
    width=46,
    height=34,
    corner_radius=6,
    font=("Arial", 10, "bold"),
    fg_color="#DC3545",
    hover_color="#B02A37",
    text_color="#FFFFFF",
    border_width=0
).pack(side="left", padx=1, pady=1)

def add_to_display(value):
    display.insert(tk.END, value)

def toggle_sign():
    expression = display.get().strip()

    if not expression:
        return

    try:
        value = float(expression)
        display.delete(0, tk.END)
        display.insert(0, str(-value))
    except ValueError:
        display.insert(tk.END, "-")

def open_symbols_window():
    symbols_window = tk.Toplevel(root)
    symbols_window.title("More Symbols")
    symbols_window.geometry("300x300")
    symbols_window.resizable(False, False)
    symbols_window.configure(bg="#071B35")
    symbols_window.transient(root)

    tk.Label(
        symbols_window,
        text="More Symbols",
        font=("Arial", 12, "bold"),
        bg="#071B35",
        fg="#38BDF8"
    ).pack(pady=10)

    symbols = [
        "(", ")", "[", "]",
        "{", "}", "'", '"',
        ",", "%", "//", "**",
        "pi", "e", "sqrt(", "sin(",
        "cos(", "tan(", "log(", "ln("
    ]

    symbols_frame = tk.Frame(
        symbols_window,
        bg="#071B35"
    )
    symbols_frame.pack(padx=10, pady=5)

    for index, symbol in enumerate(symbols):
        ctk.CTkButton(
            symbols_frame,
            text=symbol,
            width=55,
            height=32,
            corner_radius=6,
            font=("Arial", 10, "bold"),
            fg_color="#1677F2",
            hover_color="#0958D9",
            text_color="#FFFFFF",
            command=lambda s=symbol: add_to_display(s)
        ).grid(
            row=index // 4,
            column=index % 4,
            padx=4,
            pady=4
        )

def keyboard_input(event):
    if event.keysym in ("Return", "KP_Enter"):
        calculate_result()
        return "break"

    elif event.keysym == "BackSpace":
        current = display.get()
        if current:
            pos = display.index(tk.INSERT)
            if pos > 0:
                display.delete(pos - 1)
        return "break"

    elif event.keysym == "Escape":
        clear_display()
        return "break"

    elif event.char and event.char in "0123456789.+-*/()":
        display.insert(tk.INSERT, event.char)
        return "break"

display.bind("<Key>", keyboard_input)

def clear_display():
    display.delete(0, tk.END)

angle_mode = "DEG"

def toggle_angle_mode():
    global angle_mode

    if angle_mode == "DEG":
        angle_mode = "RAD"
    else:
        angle_mode = "DEG"

    angle_button.configure(text=angle_mode)

def calculate_result():
    try:
        import ast
        import operator

        expression = display.get().strip()

        if not expression:
            display.delete(0, tk.END)
            display.insert(0, "Enter an expression")
            return

        expression = expression.replace("^", "**")

        def sin_func(value):
            if angle_mode == "DEG":
                value = math.radians(value)
            return math.sin(value)


        def cos_func(value):
            if angle_mode == "DEG":
                value = math.radians(value)
            return math.cos(value)


        def tan_func(value):
            if angle_mode == "DEG":
                value = math.radians(value)
            return math.tan(value)

        allowed_functions = {
            "sin": sin_func,
            "cos": cos_func,
            "tan": tan_func,
            "sqrt": math.sqrt,
            "log": math.log10,
            "ln": math.log,
        }

        allowed_names = {
            "pi": math.pi,
            "e": math.e,
        }

        binary_ops = {
            ast.Add: operator.add,
            ast.Sub: operator.sub,
            ast.Mult: operator.mul,
            ast.Div: operator.truediv,
            ast.FloorDiv: operator.floordiv,
            ast.Mod: operator.mod,
            ast.Pow: operator.pow,
        }

        unary_ops = {
            ast.UAdd: operator.pos,
            ast.USub: operator.neg,
        }

        def safe_eval(node):
            if isinstance(node, ast.Expression):
                return safe_eval(node.body)

            if isinstance(node, ast.Constant):
                if type(node.value) in (int, float):
                    return node.value
                raise ValueError("Only numbers are allowed")

            if isinstance(node, ast.Name):
                if node.id in allowed_names:
                    return allowed_names[node.id]
                raise ValueError("Unknown name")

            if isinstance(node, ast.BinOp):
                op_type = type(node.op)

                if op_type not in binary_ops:
                    raise ValueError("Operator not allowed")

                left = safe_eval(node.left)
                right = safe_eval(node.right)

                if op_type is ast.Pow and abs(right) > 1000:
                    raise ValueError("Power is too large")

                result = binary_ops[op_type](left, right)

                if isinstance(result, complex):
                    raise ValueError("Complex results are not supported")

                if isinstance(result, float) and not math.isfinite(result):
                    raise ValueError("Result is too large")

                return result

            if isinstance(node, ast.UnaryOp):
                op_type = type(node.op)

                if op_type not in unary_ops:
                    raise ValueError("Operator not allowed")

                return unary_ops[op_type](safe_eval(node.operand))

            if isinstance(node, ast.Call):
                if not isinstance(node.func, ast.Name):
                    raise ValueError("Function not allowed")

                name = node.func.id

                if name not in allowed_functions:
                    raise ValueError("Function not allowed")

                if node.keywords:
                    raise ValueError("Invalid function arguments")

                args = [safe_eval(arg) for arg in node.args]

                return allowed_functions[name](*args)

            raise ValueError("Invalid expression")

        tree = ast.parse(expression, mode="eval")
        result = safe_eval(tree)

        display.delete(0, tk.END)
        if isinstance(result, (int, float)):
            result = round(result, 10)

        display.insert(0, str(result))
        save_history(expression, result)

    except ZeroDivisionError:
        display.delete(0, tk.END)
        display.insert(0, "Cannot divide by zero")

    except Exception:
        display.delete(0, tk.END)
        display.insert(0, "Invalid expression")

style.configure(
    "Number.TButton",
    background="#1677F2",
    foreground="#FFFFFF",
    font=("Arial", 9, "bold"),
    padding=2,
    relief="raised",
    borderwidth=0
)

style.map(
    "Number.TButton",
    background=[
        ("active", "#0958D9"),
        ("pressed", "#38BDF8")
    ],
    relief=[
        ("pressed", "sunken"),
        ("!pressed", "raised")
    ],
    foreground=[
        ("active", "#071B35"),
        ("pressed", "#FFFFFF")
    ]
)

style.configure(
    "Scientific.TButton",
    background="#7138E8",
    foreground="#FFFFFF",
    font=("Arial", 8, "bold"),
    padding=2,
    borderwidth=0
)

style.map(
    "Scientific.TButton",
    background=[
        ("active", "#38BDF8"),
        ("pressed", "#5B21B6")
    ],
    foreground=[
        ("active", "#071B35"),
        ("pressed", "#FFFFFF")
    ]
)

style.configure(
    "Operator.TButton",
    background="#079455",
    foreground="#FFFFFF",
    font=("Arial", 9, "bold"),
    padding=2,
    borderwidth=0
)

style.map(
    "Operator.TButton",
    background=[
        ("active", "#38BDF8"),
        ("pressed", "#067647")
    ],
    foreground=[
        ("active", "#071B35"),
        ("pressed", "#FFFFFF")
    ]
)

style.configure(
    "Clear.TButton",
    background="#DC3545",
    foreground="#FFFFFF",
    font=("Arial", 9, "bold"),
    padding=2,
    borderwidth=0
)

style.map(
    "Clear.TButton",
    background=[
        ("active", "#F87171"),
        ("pressed", "#B02A37")
    ],
    foreground=[
        ("active", "#071B35"),
        ("pressed", "#FFFFFF")
    ]
)

style.configure(
    "Equal.TButton",
    background="#00A878",
    foreground="#FFFFFF",
    font=("Arial", 10, "bold"),
    padding=3,
    borderwidth=0
)

style.map(
    "Equal.TButton",
    background=[
        ("active", "#38BDF8"),
        ("pressed", "#067647")
    ],
    foreground=[
        ("active", "#071B35"),
        ("pressed", "#FFFFFF")
    ]
)

# Calculator keypad area
keypad_frame = tk.Frame(
    left_panel,
    bg="#071B35"
)
keypad_frame.pack(
    fill="both",
    expand=True,
    padx=3,
    pady=(0, 3)
)

# Quick Access Buttons - First Row
quick_access_frame = tk.Frame(
    left_panel,
    bg="#071B35"
)

quick_access_frame.pack(
    fill="x",
    padx=5,
    pady=(3, 3),
    before=keyboard_controls
)

for col in range(3):
    quick_access_frame.grid_columnconfigure(
        col, weight=1, uniform="quick"
    )

history_quick_button = ctk.CTkButton(
    quick_access_frame,
    text="💾 Save History",
    command=lambda: notebook.select(history_tab),
    height=34,
    corner_radius=6,
    font=("Segoe UI Emoji", 9, "bold"),
    fg_color="#164783",
    hover_color="#1677F2",
    text_color="#FFFFFF"
)

history_quick_button.grid(
    row=0, column=0,
    sticky="ew",
    padx=2, pady=2
)

percentage_quick_button = ctk.CTkButton(
    quick_access_frame,
    text="％ Percentage",
    command=lambda: notebook.select(percentage_tab),
    height=34,
    corner_radius=6,
    font=("Segoe UI Symbol", 9, "bold"),
    fg_color="#164783",
    hover_color="#1677F2",
    text_color="#FFFFFF",
    border_width=0
)

percentage_quick_button.grid(
    row=0, column=1,
    sticky="ew",
    padx=2, pady=2
)

symbols_button = ctk.CTkButton(
    quick_access_frame,
    text="More Symbols",
    command=lambda: open_symbols_window(),
    height=34,
    corner_radius=6,
    font=("Arial", 9, "bold"),
    fg_color="#0E7490",
    hover_color="#155E75",
    text_color="#FFFFFF",
    border_width=0
)

symbols_button.grid(
    row=0, column=2,
    sticky="ew",
    padx=2, pady=2
)

keyboard_mode = "numeric"

def toggle_keyboard_mode():
    global keyboard_mode

    if keyboard_mode == "numeric":
        keyboard_mode = "alpha"
    else:
        keyboard_mode = "numeric"

    render_keypad()


def render_keypad():
    global angle_button

    for widget in keypad_frame.winfo_children():
        widget.destroy()

    if keyboard_mode == "numeric":
        keys = [
            ["sin(", "cos(", "tan(", "log(", "sqrt(", "ln("],
            ["x²", "(", ")", "pi", "e", "^"],
            ["7", "8", "9", "*", "/", "%"],
            ["4", "5", "6", "+", "-"],
            ["1", "2", "3", "±", "DEL"],
            ["0", ".", "AC", "123"]
        ]

        mode_button_text = "ABC"
    else:
        keys = [
            list("ABCDEF"),
            list("GHIJKL"),
            list("MNOPQR"),
            list("STUVWX"),
            list("YZ"),
            ["(", ")", "pi", "e", "AC", "DEL", "123"]
        ]
        mode_button_text = "123"

    for c in range(6):
        keypad_frame.grid_columnconfigure(c, weight=1, uniform="keypad")

    for r, row_keys in enumerate(keys):
        for c, key in enumerate(row_keys):
            if key == "AC":
                command = clear_display
            elif key == "DEL":
                command = lambda: display.delete(
                    max(0, len(display.get()) - 1), tk.END
                )
            elif key == "x²":
                command = lambda: add_to_display("^2")
            elif key == "%":
                command = lambda: add_to_display("/100")
            elif key =="±":
                command = toggle_sign
            elif key == "123":
                command = toggle_keyboard_mode
            else:
                command = lambda value=key: add_to_display(value)

            button_width = 46
            button_height = 34
            button_text = "C" if key == "AC" else key

            if key == "0":
                button_width = 92
            elif key == "=":
                button_width = 138
                button_height = 54

            button = ctk.CTkButton(
                keypad_frame,
                text=button_text,
                command=command,
                width=button_width,
                height=button_height,
                corner_radius=6,
                font=("Arial", 10, "bold"),
                fg_color=(
                    "#EF3340" if key == "AC"
                    else "#7138E8" if key in (
                        "sin(", "cos(", "tan(", "log(", "sqrt(", "ln(", "x²"
                    )
                    else "#0878F9" if key.isdigit()
                    else "#006400" if key == "="
                    else "#009F83" if key in (
                        "*", "/", "+", "-", "=", "±"
                    )
                    else "#164783" if key in (
                        "(", ")", "pi", "e", "^", "%"
                    )
                    else "#0E7490"
                ),
                hover_color="#0958D9",
                text_color="#FFFFFF"
            )

            if key == "0" and keyboard_mode == "numeric":
                button.grid(
                    row=r, column=0, columnspan=2,
                    padx=2, pady=2, sticky="nsew"
                )
            elif keyboard_mode == "numeric" and r == len(keys) - 1:
                bottom_positions = {
                    ".": 2,
                    "AC": 4,
                    "123": 3
                }
                if key in bottom_positions:
                    button.grid(
                        row=r, column=bottom_positions[key],
                        padx=1, pady=1, sticky="nsew"
                    )
                else:
                    button.grid(
                        row=r, column=c,
                        padx=1, pady=1, sticky="nsew"
                    )
                    
            else:
                button.grid(
                    row=r, column=c,
                    padx=1, pady=1, sticky="nsew"
                )

    if keyboard_mode == "numeric":
        equal_button = ctk.CTkButton(
            keypad_frame,
            text="=",
            command=calculate_result,
            width=42,
            height=44,
            corner_radius=6,
            font=("Arial", 12, "bold"),
            fg_color="#006400",
            hover_color="#0958D9",
            text_color="#FFFFFF"
        )
        equal_button.grid(
            row=4, column=5, rowspan=2,
            padx=1, pady=1, sticky="nsew"
        )

    angle_button = ctk.CTkButton(
        keypad_frame,
        text=angle_mode,
        command=toggle_angle_mode,
        width=42,
        height=24,
        corner_radius=5,
        font=("Arial", 11, "bold"),
        fg_color="#0E7490",
        hover_color="#0958D9",
        text_color="#FFFFFF"
    )

    if keyboard_mode == "numeric":
        angle_button.grid(
            row=3,
            column=5,
            padx=1,
            pady=1,
            sticky="nsew"
        )
    else:
        angle_button.grid(
            row=len(keys) - 1,
            column=3,
            padx=1,
            pady=1,
            sticky="nsew"
        )

    if "mode_button" in globals():
        mode_button.configure(text=mode_button_text)


render_keypad()

tk.Label(
    age_tab,
    text="Age Calculator",
    font=("Arial", 10)
).pack(pady=5)

tk.Label(age_tab, text="Enter Date of Birth (DD-MM-YYYY)",
         font=("Arial", 10)).pack(pady=10)

dob_entry = tk.Entry(age_tab, font=("Arial", 10), justify="center")
dob_entry.pack(pady=5)

age_result = tk.Label(age_tab, text="Your age will appear here",
                      font=("Arial", 10))
age_result.pack(pady=15)

def calculate_age():
    try:
        dob_text = dob_entry.get().strip()
        dob = datetime.strptime(dob_text, "%d-%m-%Y").date()
        today = date.today()

        if dob > today:
            age_result.config(text="Date of birth cannot be in the future")
            return

        years = today.year - dob.year
        months = today.month - dob.month
        days = today.day - dob.day

        if days < 0:
            months -= 1
            previous_month = today.month - 1 or 12
            previous_year = today.year if today.month > 1 else today.year - 1
            from calendar import monthrange
            days += monthrange(previous_year, previous_month)[1]

        if months < 0:
            years -= 1
            months += 12

        age_result.config(
            text=f"Your Age: {years} years, {months} months, {days} days"
        )

    except ValueError:
        age_result.config(text="Please enter date as DD-MM-YYYY")


ctk.CTkButton(
    age_tab,
    text="Calculate Age",
    command=calculate_age,
    width=150,
    height=27,
    corner_radius=8,
    font=("Arial", 8, "bold"),
    text_color="#FFFFFF",
    fg_color="#1677F2",
    hover_color="#0958D9",
    border_width=1,
    border_color="#38BDF8"
).pack(pady=10)

tk.Label(
    graph_tab,
    text="Graph Plotter",
    font=("Arial", 10, "bold")
).pack(pady=(4, 2))

tk.Label(
    graph_tab,
    text="Equation (example: x**2 or sin(x)):",
    font=("Arial", 8)
).pack(pady=1)

equation_entry = tk.Entry(
    graph_tab,
    font=("Arial", 9),
    width=25
)
equation_entry.pack(pady=2)

tk.Label(
    graph_tab,
    text="X Values (comma-separated):",
    font=("Arial", 8)
).pack(pady=1)

x_values_entry = tk.Entry(
    graph_tab,
    font=("Arial", 9),
    width=35
)
x_values_entry.pack(pady=2)

tk.Label(
    graph_tab,
    text="Y Values (comma-separated):",
    font=("Arial", 8)
).pack(pady=1)

y_values_entry = tk.Entry(
    graph_tab,
    font=("Arial", 9),
    width=35
)
y_values_entry.pack(pady=2)

tk.Label(
    graph_tab,
    text="Select Chart Type:",
    font=("Arial", 8)
).pack(pady=(3, 1))

chart_type = ttk.Combobox(
    graph_tab,
    values=[
        "Line Chart",
        "Area Chart",
        "Bar Chart",
        "Pie Chart",
        "Bubble Chart",
        "Combo Chart",
        "Waterfall Chart",
        "Funnel Chart",
    ],
    state="readonly",
    font=("Arial", 8),
    width=15
)
chart_type.set("Line Chart")
chart_type.pack(pady=2)

def open_full_graph():
    graph_view_frame.place(
        x=0,
        y=0,
        relwidth=1,
        relheight=1
    )
    graph_view_frame.lift()
    plot_graph()

def plot_graph():
    try:
        equation = equation_entry.get().strip()
        x_text = x_values_entry.get().strip()
        y_text = y_values_entry.get().strip()
        selected_chart = chart_type.get()

        # Equation mode is available for Line and Area charts.
        if not x_text and not y_text:
            if selected_chart not in ("Line Chart", "Area Chart"):
                raise ValueError(
                    "Please enter X Values and Y Values for this chart."
                )

            if not equation:
                raise ValueError(
                    "Enter an equation such as x**2 or sin(x)."
                )

            x = np.linspace(-10, 10, 400)

            allowed = {
                "x": x,
                "sin": np.sin,
                "cos": np.cos,
                "tan": np.tan,
                "sqrt": np.sqrt,
                "pi": np.pi,
                "abs": np.abs
            }

            y = eval(
                equation.replace("^", "**"),
                {"_builtins_": {"abs": abs,}},
                allowed
            )

            if np.isscalar(y):
                y = np.full_like(x, y, dtype=float)

            y = np.asarray(y, dtype=float)

            if y.shape != x.shape:
                raise ValueError(
                    "Equation must use x correctly."
                )

            y = np.where(np.isfinite(y), y, np.nan)

        else:
            if not x_text or not y_text:
                raise ValueError(
                    "Please enter both X Values and Y Values."
                )

            x = np.array(
                [float(v.strip()) for v in x_text.split(",")]
            )
            y = np.array(
                [float(v.strip()) for v in y_text.split(",")]
            )

            if len(x) != len(y):
                raise ValueError(
                    "X and Y must have the same number of values."
                )

            if len(x) < 2:
                raise ValueError(
                    "Please enter at least 2 data points."
                )

            if not np.all(np.isfinite(x)) or not np.all(np.isfinite(y)):
                raise ValueError(
                    "Please enter valid finite numbers."
                )

        supported_charts = (
            "Line Chart",
            "Area Chart",
            "Bar Chart",
            "Pie Chart",
            "Statistical Chart",
            "Radar Chart",
            "Bubble Chart",
            "Combo Chart",
            "Waterfall Chart",
            "Funnel Chart",
            "Gantt Chart",
        )

        if selected_chart not in supported_charts:
            raise ValueError("Please select a valid chart type.")

        # Charts needing additional data are handled separately later.
        if selected_chart in (
            "Bubble Chart",
            "Combo Chart",
        ):
            raise ValueError(
                selected_chart
                + " needs additional data fields. "
                "We will add those fields in the next step."
            )

        if selected_chart in ("Pie Chart", "Funnel Chart"):
            if np.any(y < 0) or np.sum(y) <= 0:
                raise ValueError(
                    "Values must be non-negative and their total "
                    "must be greater than zero."
                )

        for widget in chart_view_area.winfo_children():
            widget.destroy()

        fig, ax = plt.subplots(
            figsize=(7, 5),
            dpi=100,
            constrained_layout=True
        )

        # Automatic color palette for every new chart

        chart_colors = [
            "#E63946", "#457B9D", "#2A9D8F",
            "#F4A261", "#9B5DE5", "#F15BB5",
            "#00B4D8", "#70AD47", "#FF7F11",
            "#6A4C93", "#D62828", "#0081A7"
        ]

        random.shuffle(chart_colors)

        fig.patch.set_facecolor("white")
        ax.set_facecolor("#F8FAFC")

        labels = [str(v) for v in x]


        if selected_chart == "Line Chart":
            ax.plot(
                x, y,
                color=chart_colors[0],
                linewidth=2.5,
                marker="o" if len(x) <= 30 else None
            )
            ax.set_title(
                f"y = {equation}" if not x_text else "Line Chart"
            )
            ax.set_xlabel("X Values")
            ax.set_ylabel("Y Values")
            ax.grid(True, linestyle="--", alpha=0.4)

        elif selected_chart == "Area Chart":
            ax.fill_between(
                x, y, 0,
                color=chart_colors[1],
                alpha=0.5
            )
            ax.plot(x, y, color=chart_colors[0], linewidth=2)
            ax.set_title("Area Chart")
            ax.set_xlabel("X Values")
            ax.set_ylabel("Y Values")
            ax.grid(True, linestyle="--", alpha=0.4)

        elif selected_chart == "Bar Chart":
            ax.bar(
    labels, y,
    color=[
        chart_colors[i % len(chart_colors)]
        for i in range(len(y))
    ],
    edgecolor="#0B2545"
)
            ax.set_title("Bar Chart")
            ax.set_xlabel("Categories / X Values")
            ax.set_ylabel("Y Values")
            ax.grid(axis="y", linestyle="--", alpha=0.4)
            ax.set_axisbelow(True)

        elif selected_chart == "Pie Chart":
            ax.pie(
                y,
                labels=labels,
                autopct="%1.1f%%",
                startangle=90,
                colors=chart_colors,
                textprops={"fontsize": 8}
            )
            ax.set_title("Pie Chart")
            ax.axis("equal")

        elif selected_chart == "Statistical Chart":
            ax.boxplot(y, patch_artist=True)
            ax.set_title("Statistical Box Plot")
            ax.set_ylabel("Y Values")
            ax.grid(axis="y", linestyle="--", alpha=0.4)

        elif selected_chart == "Radar Chart":
            angles = np.linspace(0, 2 * np.pi, len(y), endpoint=False)
            angles = np.concatenate((angles, [angles[0]]))
            values = np.concatenate((y, [y[0]]))

            plt.close(fig)
            fig, ax = plt.subplots(
                figsize=(5, 2.2),
                dpi=80,
                subplot_kw={"projection": "polar"},
                constrained_layout=True
            )
            ax.plot(angles, values, color=chart_colors[0], linewidth=2)
            ax.fill(angles, values, color=chart_colors[1], alpha=0.3)
            ax.set_xticks(angles[:-1])
            ax.set_xticklabels(labels, fontsize=8)
            ax.set_title("Radar Chart")

        elif selected_chart == "Waterfall Chart":
            running = np.cumsum(y)
            starts = np.concatenate(([0], running[:-1]))
            colors = [
                "#16A34A" if value >= 0 else "#DC2626"
                for value in y
            ]
            ax.bar(
                labels,
                y,
                bottom=starts,
                color=colors
            )
            ax.set_title("Waterfall Chart")
            ax.set_ylabel("Running Total")
            ax.grid(axis="y", linestyle="--", alpha=0.4)

        elif selected_chart == "Funnel Chart":
            order = np.argsort(y)[::-1]
            funnel_labels = [labels[i] for i in order]
            funnel_values = y[order]
            ax.barh(
                funnel_labels[::-1],
                funnel_values[::-1],
                color=[chart_colors[i % len(chart_colors)]
                       for i in range(len(funnel_values))
                ]
            )
            ax.set_title("Funnel Chart")
            ax.set_xlabel("Values")

        canvas = FigureCanvasTkAgg(fig, master=chart_view_area)
        canvas.draw()
        canvas.get_tk_widget().pack(fill="both", expand=True)
        plt.close(fig)

    except Exception as err:
        from tkinter import messagebox
        messagebox.showerror("Graph Error", str(err))

def open_full_graph():
    graph_view_frame.place(x=0, y=0, relwidth=1, relheight=1)
    plot_graph()

ctk.CTkButton(
    graph_tab,
    text="View Chart",
    command= open_full_graph,
    width=130,
    height=32,
    corner_radius=8,
    font=("Arial", 9, "bold"),
    text_color="#FFFFFF",
    fg_color="#1677F2",
    hover_color="#0958D9",
    border_width=1,
    border_color="#38BDF8"
).pack(pady=3)

graph_area = tk.Frame(
    graph_tab,
    bg="#071B35"
)
graph_area.pack(
    fill="both",
    expand=True,
    padx=5,
    pady=2
)

# Full-page Graph View
graph_view_frame = tk.Frame(
    root,
    bg="#071B35"
)

back_button = ctk.CTkButton(
    graph_view_frame,
    text="← Back",
    command=lambda: (
    graph_view_frame.place_forget(),
    update_back_button()
),
    width=100,
    height=30,
    corner_radius=8,
    font=("Arial", 10, "bold"),
    text_color="#FFFFFF",
    fg_color="#1677F2",
    hover_color="#0958D9"
)
back_button.pack(anchor="w", padx=10, pady=8)

chart_view_area = tk.Frame(
    graph_view_frame,
    bg="#071B35"
)
chart_view_area.pack(
    fill="both",
    expand=True,
    padx=8,
    pady=5
)

display.focus_set()

percentage_tab = ttk.Frame(notebook)
notebook.add(percentage_tab, text="Percentage")

# Remove the old hamburger menu
menu_button.place_forget()

style.layout("TNotebook.Tab", [])
tk.Label(
    percentage_tab,
    text="Percentage Calculator",
    font=("Arial", 10, "bold")
).pack(pady=15)

tk.Label(
    percentage_tab,
    text="First Number:",
    font=("Arial", 10)
).pack()

percent_entry1 = tk.Entry(
    percentage_tab,
    font=("Arial", 10),
    justify="center"
)
percent_entry1.pack(pady=5)

tk.Label(
    percentage_tab,
    text="Second Number:",
    font=("Arial", 10)
).pack()

percent_entry2 = tk.Entry(
    percentage_tab,
    font=("Arial", 10),
    justify="center"
)
percent_entry2.pack(pady=5)

tk.Label(
    percentage_tab,
    text="Select Calculation:",
    font=("Arial", 10)
).pack(pady=(10, 0))

percent_choice = ttk.Combobox(
    percentage_tab,
    values=[
        "Percentage of Number",
        "Percentage Increase",
        "Percentage Decrease"
    ],
    state="readonly",
    font=("Arial", 10),
    width=25
)
percent_choice.pack(pady=5)
percent_choice.set("Percentage of Number")

percent_result = tk.Label(
    percentage_tab,
    text="Result will appear here",
    font=("Arial", 10, "bold"),
    wraplength=450
)
percent_result.pack(pady=15)

def calculate_percentage():
    try:
        first_text = percent_entry1.get().strip()
        second_text = percent_entry2.get().strip()

        if not first_text or not second_text:
            percent_result.config(
                text="Please enter both numbers."
            )
            return

        first = float(first_text)
        second = float(second_text)

        if not math.isfinite(first) or not math.isfinite(second):
            percent_result.config(
                text="Please enter finite numbers only."
            )
            return

        choice = percent_choice.get()


        if choice == "Percentage of Number":
            result = first * second / 100
            message = (
                f"{second:g}% of {first:g} = {result:g}"
            )

        elif choice == "Percentage Increase":
            if first == 0:
                percent_result.config(
                    text="Starting number cannot be zero."
                )
                return

            result = ((second - first) / abs(first)) * 100
            message = f"Percentage change = {result:.2f}%"

        elif choice == "Percentage Decrease":
            if first == 0:
                percent_result.config(
                    text="Starting number cannot be zero."
                )
                return

            result = ((first - second) / abs(first)) * 100
            message = f"Percentage decrease = {result:.2f}%"

        else:
            message = "Please select a calculation."
            result = None

        percent_result.config(text=message)

        save_history(
            f"{choice}: {first:g}, {second:g}",
            message
        )

    except ValueError:
        percent_result.config(
            text="Please enter valid numbers in both boxes."
        )

ctk.CTkButton(
    percentage_tab,
    text="Calculate",
    command=calculate_percentage,
    width=130,
    height=30,
    corner_radius=8,
    font=("Arial", 9, "bold"),
    text_color="#FFFFFF",
    fg_color="#1677F2",
    hover_color="#0958D9",
    border_width=1,
    border_color="#38BDF8"
).pack(pady=10)

def clear_percentage():
    percent_entry1.delete(0, tk.END)
    percent_entry2.delete(0, tk.END)
    percent_choice.set("Percentage of Number")
    percent_result.config(text="Result will appear here")

ctk.CTkButton(
    percentage_tab,
    text="Clear",
    command=clear_percentage,
    width=100,
    height=28,
    corner_radius=8,
    font=("Arial", 9, "bold"),
    text_color="#FFFFFF",
    fg_color="#DC3545",
    hover_color="#B02A37",
    border_width=1,
    border_color="#38BDF8"
).pack(pady=5)

dark_mode = True

def set_theme(is_dark):
    global dark_mode

    dark_mode = is_dark

    if dark_mode:
        bg_color = "#071B35"
        fg_color = "#FFFFFF"
        entry_bg = "#0B2545"
    else:
        bg_color = "#F0F4F8"
        fg_color = "#172B4D"
        entry_bg = "#FFFFFF"

    root.configure(bg=bg_color)
    header_frame.configure(bg=bg_color)
    title.configure(
        bg=bg_color,
        fg="#38BDF8" if dark_mode else "#075985"
    )
    subtitle.configure(
        bg=bg_color,
        fg="#CBD5E1" if dark_mode else "#475569"
    )

    def update_widgets(widget):
        for child in widget.winfo_children():
            try:
                if isinstance(child, ctk.CTkSwitch):
                    pass

                elif isinstance(child, ctk.CTkFrame):
                    pass

                elif isinstance(child, ctk.CTkButton):
                    pass

                elif isinstance(child, tk.Frame):
                    child.configure(bg=bg_color)

                elif isinstance(child, tk.Label):
                    child.configure(bg=bg_color, fg=fg_color)

                elif isinstance(child, tk.Entry):
                    child.configure(
                        bg=entry_bg,
                        fg=fg_color,
                        insertbackground=fg_color
                    )

                elif isinstance(child, tk.Listbox):
                    child.configure(
                        bg=entry_bg,
                        fg=fg_color,
                        selectbackground="#1677F2",
                        selectforeground="#FFFFFF"
                    )

                elif isinstance(child, tk.Button):
                    child.configure(
                        bg="#1677F2",
                        fg="#FFFFFF",
                        activebackground="#0958D9",
                        activeforeground="#FFFFFF"
                    )

            except (tk.TclError, ValueError):
                pass

            update_widgets(child)

    update_widgets(root)

    display.configure(
        bg=entry_bg,
        fg="#FFFFFF" if dark_mode else "#172B4D",
        insertbackground="#FFFFFF" if dark_mode else "#172B4D",
        highlightbackground="#1677F2",
        highlightcolor="#38BDF8"
    )

    graph_area.configure(bg=bg_color)


    style.configure(
        "TFrame",
        background=bg_color
    )
    style.configure(
        "TLabel",
        background=bg_color,
        foreground=fg_color
    )
    style.configure(
        "TNotebook",
        background=bg_color
    )
    style.configure(
        "TNotebook.Tab",
        background="#1E4976" if dark_mode else "#D9E5F2",
        foreground="#FFFFFF" if dark_mode else "#172B4D",
        padding=(2, 4),
        borderwidth=0,
        font=("Arial", 6, "bold")
    )

    style.map(
        "TNotebook.Tab",
        background=[
            ("selected", "#0878F9" if dark_mode else "#93C5FD"),
            ("active", "#1D4ED8" if dark_mode else "#BFDBFE")
        ],
        foreground=[
            ("selected", "#FFFFFF" if dark_mode else "#172B4D"),
            ("active", "#FFFFFF" if dark_mode else "#172B4D")
        ]
    )

# ================= THEME BUTTONS =================

def update_theme_buttons():
    if dark_mode:
        selected_bg = "#1677F2"
        normal_bg = "#0B2545"
        normal_hover = "#164783"
        text_color = "#FFFFFF"
    else:
        selected_bg = "#1677F2"
        normal_bg = "#D9E5F2"
        normal_hover = "#BFDBFE"
        text_color = "#172B4D"

    # Bottom Light / Dark Buttons
    light_button.configure(
        fg_color=selected_bg if not dark_mode else normal_bg,
        hover_color=normal_hover,
        text_color=text_color
    )

    dark_button.configure(
        fg_color=selected_bg if dark_mode else normal_bg,
        hover_color=normal_hover,
        text_color=text_color
    )


def change_theme(is_dark):
    set_theme(is_dark)
    update_theme_buttons()

# -------- BOTTOM THEME SECTION --------

bottom_theme_frame = tk.Frame(
    left_panel,
    bg="#071B35",
    highlightbackground="#164E78",
    highlightthickness=1
)

bottom_theme_frame.pack(
    side="bottom",
    fill="x",
    padx=5,
    pady=3
)

tk.Label(
    bottom_theme_frame,
    text="☼  Theme",
    font=("Arial", 10, "bold"),
    bg="#071B35",
    fg="#38BDF8"
).pack(anchor="w", padx=8, pady=(4, 3))

theme_options_frame = tk.Frame(
    bottom_theme_frame,
    bg="#071B35"
)

theme_options_frame.pack(
    fill="x",
    padx=5,
    pady=(0, 5)
)

light_button = ctk.CTkButton(
    theme_options_frame,
    text="☀️ Light",
    command=lambda: change_theme(False),
    height=23,
    corner_radius=7,
    font=("Arial", 11, "bold"),
    fg_color="#0B2545",
    hover_color="#164783",
    text_color="#FFFFFF",
    border_width=0,
    width=85
)

dark_button = ctk.CTkButton(
    theme_options_frame,
    text="☾ Dark",
    command=lambda: change_theme(True),
    height=23,
    corner_radius=7,
    font=("Arial", 11, "bold"),
    fg_color="#1677F2",
    hover_color="#164783",
    text_color="#FFFFFF",
    border_width=0,
    width=85
)

theme_options_frame.grid_columnconfigure(
    0, weight=1, uniform="theme_buttons"
)
theme_options_frame.grid_columnconfigure(
    1, weight=1, uniform="theme_buttons"
)

light_button.grid(
    row=0,
    column=0,
    sticky="ew",
    padx=2,
    pady=1
)

dark_button.grid(
    row=0,
    column=1,
    sticky="ew",
    padx=2,
    pady=1
)

# Start in Dark Mode
set_theme(True)
update_theme_buttons()

# ================================================

load_history()

def refresh_keypad_buttons():
    def refresh_widgets(parent):
        for widget in parent.winfo_children():
            if isinstance(widget, ctk.CTkButton):
                widget._draw()

            refresh_widgets(widget)

    refresh_widgets(root)

root.after(700, refresh_keypad_buttons)

root.mainloop()