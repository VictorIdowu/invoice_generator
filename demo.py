from tkinter import *
from fpdf import FPDF


root = Tk()
root.title("Invoice Generator")


medicines = {
  "Medicine A": 10,
  "Medicine B": 20,
  "Medicine C": 15,
  "Medicine D": 25,
  }

invoice_items = []

def update_invoice_text():
  invoice_text.delete(1.0, END)
  for item in invoice_items:
    invoice_text.insert(END, f"Medicine: {item[0]}, Quantity: {item[1]}, Total: {item[2]}\n")

def calculate_total():
  total = 0.0
  for item in invoice_items:
    total = total + int(item[2])
  return total

  
def generate_pdf_invoice():
  customer_name = customer_entry.get()

  pdf = FPDF()
  pdf.add_page()

  pdf.set_font("helvetica", size=12)

  pdf.cell(0, 10, text="Invoice", new_x="LMARGIN", new_y="NEXT", align="C")
  pdf.cell(0, 10, text=f"Customer: {customer_name}", new_x="LMARGIN", new_y="NEXT", align="L")
  pdf.cell(0, 10, text="", new_x="LMARGIN", new_y="NEXT")

  for item in invoice_items:
    medicine_name, quantity, item_total = item
    pdf.cell(0, 10, text=f"Medicine: {medicine_name}, Quantity: {quantity}, Total: {item_total}", new_x="LMARGIN", new_y="NEXT", align="L")
  pdf.cell(0, 10, text=f"Total amount: {calculate_total()}", new_x="LMARGIN", new_y="NEXT", align="L")

  pdf.output("invoice.pdf")



def add_medicine():
  selected_medicine = medicine_listbox.get(ANCHOR)
  quantity = int(quantity_entry.get())
  total_amount = medicines[selected_medicine] * quantity
  invoice_items.append((selected_medicine,quantity,total_amount))
  total_amount_entry.delete(0, END)
  total_amount_entry.insert(END, calculate_total())
  update_invoice_text()
  

medicine_label = Label(root, text="Medicine: ")
medicine_label.pack()

medicine_listbox = Listbox(root, selectmode=SINGLE)
for medicine in medicines:
  medicine_listbox.insert(END, medicine)

medicine_listbox.pack()

quantity_label = Label(root, text="Quantity")
quantity_label.pack()
quantity_entry = Entry(root)
quantity_entry.pack()

add_button = Button(root, text="Add Medicine", command=add_medicine)
add_button.pack()

total_amount_label =  Label(root, text="Total Amount")
total_amount_label.pack()

total_amount_entry = Entry(root)
total_amount_entry.pack()

customer_label = Label(root, text="Customer Name:")
customer_label.pack()
customer_entry = Entry(root)
customer_entry.pack()


generate_button = Button(root, text="Generate Invoice", command=generate_pdf_invoice)
generate_button.pack()

invoice_text = Text(root, height=10, width=50)
invoice_text.pack()

root.mainloop()