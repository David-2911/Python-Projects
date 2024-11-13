from tkinter import Tk, Label, Listbox, Entry, Button, Text, END, SINGLE
from fpdf import FPDF

from typing import List, Tuple

invoice_items: List[Tuple[str, int, float]] = []


def update_invoice_text():
    invoice_text.delete(1.0, END)
    for item in invoice_items:
        invoice_text.insert(
            END, f"Medicine: {item[0]}, Quantity: {item[1]}, Total: {item[2]}\n"
        )


def add_med():
    medicine = medicine_listbox.get(medicine_listbox.curselection())
    quantity = int(quantity_entry.get())
    price = medicines[medicine]
    invoice_items.append((medicine, quantity, price))
    total_amount = calculate_total()
    total_amount_entry.insert(0, str(total_amount))
    quantity_entry.delete(0, END)
    update_invoice_text()
    total_amount_entry.delete(0, END)


def calculate_total():
    total = 0.0
    for item in invoice_items:
        total += item[1] * item[2]
    return total


def generate_invoice():
    class PDF(FPDF):
        def header(self):
            self.set_fill_color(200, 220, 255)
            self.cell(0, 10, "Custom Invoice Header", 0, 1, "C")

        def footer(self):
            self.set_y(-15)
            self.set_font("Arial", "I", 8)
            self.set_fill_color(200, 220, 255)
            self.cell(0, 10, f"Page {self.page_no()}", 0, 0, "C")

    customer_name = customer_entry.get()
    pdf = PDF(format="letter")
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    # Header
    pdf.cell(200, 10, txt="Invoice", ln=True, align="C")
    pdf.cell(200, 10, txt=f"Customer Name: {customer_name}", ln=True, align="L")
    pdf.cell(200, 10, txt="", ln=True, align="L")

    # Table Header
    pdf.set_fill_color(200, 220, 255)
    pdf.cell(80, 10, txt="Medicine", border=1, align="C", fill=True)
    pdf.cell(40, 10, txt="Quantity", border=1, align="C", fill=True)
    pdf.cell(40, 10, txt="Price", border=1, align="C", fill=True)
    pdf.cell(40, 10, txt="Total", border=1, align="C", fill=True)
    pdf.ln()

    # Table Rows
    for item in invoice_items:
        pdf.cell(80, 10, txt=item[0], border=1, align="C")
        pdf.cell(40, 10, txt=str(item[1]), border=1, align="C")
        pdf.cell(40, 10, txt=f"${item[2]:.2f}", border=1, align="C")
        pdf.cell(40, 10, txt=f"${item[1] * item[2]:.2f}", border=1, align="C")
        pdf.ln()

    # Total Amount
    total_amount = calculate_total()
    pdf.cell(160, 10, txt="Total Amount", border=1, align="C", fill=True)
    pdf.cell(40, 10, txt=f"${total_amount:.2f}", border=1, align="C", fill=True)

    pdf.output("invoice.pdf")


window = Tk()
window.title("Invoice Generator")

medicines = {
    "Paracetamol": 10,
    "Aspirin": 20,
    "Ibuprofen": 30,
    "Cetrizine": 40,
    "Diazepam": 50,
    "Cetirizine": 40,
}

medicine_label = Label(window, text="Medicine:")
medicine_label.pack(pady=5)

medicine_listbox = Listbox(window, selectmode=SINGLE)
for medicine in medicines:
    medicine_listbox.insert(END, medicine)
medicine_listbox.pack(pady=5)

quantity_label = Label(window, text="Quantity:")
quantity_label.pack(pady=5)

quantity_entry = Entry(window)
quantity_entry.pack(pady=5)

add_button = Button(window, text="Add Medicine", command=add_med)
add_button.pack(pady=5)

total_amount_label = Label(window, text="Total Amount:")
total_amount_label.pack(pady=5)

total_amount_entry = Entry(window)
total_amount_entry.pack(pady=5)

customer_label = Label(window, text="Customer Name:")
customer_label.pack(pady=5)

customer_entry = Entry(window)
customer_entry.pack(pady=5)

generate_button = Button(window, text="Generate Invoice", command=generate_invoice)
generate_button.pack(pady=5)

invoice_text = Text(window, height=10, width=50)
invoice_text.pack(pady=5)

window.mainloop()
