from tkinter import *
import tkinter as tk
import tkinter.font as font
import tkinter.messagebox
import sqlite3


# Function used for coding a window with a specific geometry
# The function is taken  from lecture slides

def root_geometry():
    width, height = 700, 700
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x_cord = int((screen_width / 2) - (width / 2))
    y_cord = int((screen_height / 2) - (height / 2))
    root.geometry("{}x{}+{}+{}".format(width, height, x_cord, y_cord))


# Function to display a specific message, when PayNow button is pressed after all the payments was verified.
def visa_check():
    tk.messagebox.showinfo("VisaCheck", "The payment was a success.All payments are verified")


# Class for coding the shopping cart with the following features:
# 1. Add item to the cart
# 2. Update the cart with new products and quantity
# 3. Delete items added previously in the cart
# 4. Show the cart: used to display the products added to the cart and the applied discount
# 5. Update, display and save  the receipt

class Cart:
    def __init__(self):
        self.total = 0
        self.item = ()

    def add_item(self):
        self.item = entry_entry_item.get()           # the code is reading the data typed by the user
        self.price = float(entry_entry_price.get())
        self.quantity = int(entry_entry_quantity.get())
        self.total = (self.quantity * self.price)        # calculating the price for the products added to the cart
        print("The total price is:", self.total)
        print("Items in the cart:", self.item, " ,Price:", self.price, ", Quantity:", self.quantity)

    def remove_item(self):                              # remove from the cart the unwanted quantity
        self.item = entry_entry_item.get()              # taking  the data from the user interface
        self.quantity = int(entry_entry_quantity.get())
        self.price = float(entry_entry_price.get())
        self.total = float(self.total) - (self.quantity * self.price)    # updating the total price
        print("Items in the cart:", self.item, " ,Price:", self.price, ", Quantity:", self.quantity)
        print("After removing the item the price is:", self.total)

    def update_item(self):                            # update the cart with a different quantity and different item
        self.item = entry_entry_item.get()            # taking  the data from the user interface
        self.price = float(entry_entry_price.get())
        self.quantity = int(entry_entry_quantity.get())
        self.total = float(self.total) + (self.quantity * self.price)    # updating the price
        print("Items in the cart:", self.item, " ,Price:", self.price, ", Quantity:", self.quantity)
        print("The updated price is:", self.total)

    def receipt(self):                        # displaying the receipt
        self.item = entry_entry_item.get()    # taking  the data from the user interface
        self.price = float(entry_entry_price.get())
        self.quantity = int(entry_entry_quantity.get())
        root1 = tk.Tk()                        # creating a window to display the receipt
        root1.title("Receipt")
        file = open("Receipt.txt", "r")         # open the text file to read the details of the transaction
        data = file.read()                     # read the data from the file
        file.close()                           # closing the file
        results = Label(root1, text=data, width="40", height="10")  # displaying the data in a window
        results.grid(row=1, column=1)
        root1.mainloop()

    def receipt_save(self):                         # update the receipt and save it in a file
        self.total1 = self.total - self.total * 0.20
        self.item = entry_entry_item.get()
        self.price = str(entry_entry_price.get())
        self.quantity = str(entry_entry_quantity.get())
        self.total = str(self.total)
        total = str(self.total1)
        file = open("Receipt.txt", "a")          # open a text file to write the details of the transaction line by line
        file.write("Items:")
        file.writelines(self.item)
        file.write("\n")
        file.write("Quantity:")
        file.writelines(self.quantity)
        file.write("\n")
        file.write("Price/item:")
        file.writelines(self.price)
        file.write("\n")
        file.write("Total amount to pay before discount:")
        file.writelines(self.total)
        file.write("\n")
        file.write("Total amount to pay after discount:")
        file.write(total)
        file.close()   # closing the file

    def show_cart(self):                # displaying the cart
        self.total55 = (self.total - self.total * 0.20)
        self.item = entry_entry_item.get()
        self.price = str(entry_entry_price.get())
        self.quantity = str(entry_entry_quantity.get())
        self.total = str(self.total)
        total = str(self.total55)
        file = open("Show Cart.txt", "a")   # open a text file to write the transaction details line by line
        file.write("Items:")
        file.writelines(self.item)
        file.write("\n")
        file.write("Quantity:")
        file.writelines(self.quantity)
        file.write("\n")
        file.write("Price/item:")
        file.writelines(self.price)
        file.write("\n")
        file.write("Total amount to pay before discount:")  # displaying the transaction details before 20 % discount
        file.writelines(self.total)
        file.write("\n")
        file.write("Total amount to pay after discount:")  # display the transaction details after discount is applied
        file.write(total)
        file.close()
        root1 = tk.Tk()        # creating a window to display the cart
        root1.title("Show Cart")
        file = open("Show Cart.txt", "r")  # open the text file to read the data
        data = file.read()                 # reading the data from the file
        file.close()
        results = Label(root1, text=data, width="40", height="10")  # displaying the data in a window
        results.grid(row=1, column=1)
        root1.mainloop()

# The Class 'Radio' is used to code 'Choose the transport' feature
# Is allowing the user to choose between two different transport methods or to pick up from store
# Is updating the price according with the user preferences and displays it
# Saves the user transaction details in the data base


class Radio(Cart):

    def __init__(self):

        super().__init__()

    def selection(self):
        self.master = tk.Toplevel()  # create a window to display the total price after choosing the transport
        self.master.geometry("500x100")  # and applying the  discount
        self.item = entry_entry_item.get()  # getting the data from the GUI
        self.price = float(entry_entry_price.get())
        self.quantity = int(entry_entry_quantity.get())
        self.total = self.quantity * self.price
        self.total5 = self.total * 0.2
        self.dis = self.total - self.total5
        selection1 = str(var.get())    # creating a radio button to offer the possibility of choosing the transport
        if selection1 == '1':
            self.total = self.dis + 5  # Royal Mail + 20% discount/ 5 is the Royal Mail fare
            print(self.total)
        elif selection1 == '2':
            self.total = self.dis + 10  # AmazonPrime + 20% discount/ 10 is the AmazonPrime fare
            print(self.total)
        elif selection1 == '3':
            self.total = self.dis  # Pick up from store + 20% discount
            print(self.total)
            # creating  a label to display the total price in the appropriate window
        self.display_total_price = tk.Label(self.master, text='Total amount to pay with the transport fare and 20% '
                                                              'off is:',
                                            bg="azure3", fg="black",
                                            font=("arial", 11)).pack()
        self.display_total_price = tk.Label(self.master, text=self.total, bg="azure3", fg="black",
                                            font=("arial", 11)).pack()

        connection = sqlite3.connect('AllAboutToys.db')  # saving the details of the transaction in a data base
        cursor1 = connection.cursor()
        create_table = "CREATE TABLE IF NOT EXISTS tran(Item varchar(32),Quantity int,Price int,Total real)"

        cursor1.execute(create_table)
        connection.commit()
        cursor1.execute("INSERT INTO tran VALUES (?, ?, ?, ? )",
                    (self.item, self.quantity, self.price,
                     self.total))  # inserting the data in the table

        connection.commit()


# Function used to create the second window with the checkout functionality
# Its allowing the user to type his personal details (name,card number,address) and save them in the data base
# displaying and saving the receipt

def window():

    class DataBase:                                       # create  a data base to save the costumers details
        def __init__(self):
            self.first_name = str(entry_entry_name.get())  # taking the costumers details from GUI
            self.last_name = str(entry_entry_last_name.get())
            self.card_number = str(entry_entry_card.get())
            self.address = str(entry_entry_address.get())
            connection = sqlite3.connect("AllAboutToys.db")  # creating the data base
            cursor = connection.cursor()     # making the connection and creating the the table in the data base
            cursor.execute("""CREATE TABLE IF NOT EXISTS Customer (      
                               FirstName TEXT,
                               LastName TEXT, 
                               CardNumber INTEGER, 
                               Address TEXT);""")
            connection.commit()

            cursor.execute("INSERT INTO customer VALUES (:FirstName, :LastName, :CardNumber, :Address)",
                           {'FirstName': self.first_name, 'LastName': self.last_name, 'CardNumber': self.card_number,
                            'Address': self.address})   # inserting the data in the table

            connection.commit()

    top = tk.Tk()   # creating the second window with the checkout functionality
    lbl_font = font.Font(family='Georgia', size='14', weight='bold')
    top.title("Checkout")  # the window geometry used to build the second window/ code is borrowed from lecture slides
    width, height = 700, 700
    screen_width = top.winfo_screenwidth()
    screen_height = top.winfo_screenheight()
    x_cord = int((screen_width / 2) - (width / 2))
    y_cord = int((screen_height / 2) - (height / 2))
    top.geometry("{}x{}+{}+{}".format(width, height, x_cord, y_cord))

    en_frame = tk.Frame(top)  # creating a frame in the window with the name 'top'
    en_label = tk.Label(en_frame, text="Costumer details ", font=lbl_font)  # creating a label which is instructing
    en_label.pack(pady=5, side=LEFT)                               # the user what type of data he will need to enter
    en_frame.pack(pady=10, anchor=W)                            # packing the widget and place it in a specific place

    name_frame = tk.Frame(top)  # creating a frame in the window with the name 'top'
    name_label = tk.Label(name_frame, text="First Name ", font=lbl_font)  # creating a label to indicate what data the
    name_label.pack(pady=5, side=LEFT)                                   # user should type and packing the label
    entry_entry_name = tk.Entry(name_frame, font=lbl_font)  # creating an entry box for the user to type his first name
    entry_entry_name.pack(pady=5, side=RIGHT)               # packing the widget and place it in a specific place
    entry_entry_name.get()                                # getting the data from GUI
    name_frame.pack(pady=10, anchor=W)

    last_name_frame = tk.Frame(top)    # creating a frame in the window with the name 'top'
    last_name_label = tk.Label(last_name_frame, text="Last Name ", font=lbl_font)
    last_name_label.pack(pady=5, side=LEFT)  # creating a label to indicate what data the user should type in
    entry_entry_last_name = tk.Entry(last_name_frame, font=lbl_font)  # entry box for the user to type his first name
    entry_entry_last_name.pack(pady=5, side=RIGHT)
    entry_entry_last_name.get()
    last_name_frame.pack(pady=10, anchor=W)

    card_frame = tk.Frame(top)  # creating a widget to indicate the user to enter his Debit card details
    card_label = tk.Label(card_frame, text="Debit Card ", font=lbl_font)
    card_label.pack(pady=5, side=LEFT)
    entry_entry_card = tk.Entry(card_frame, font=lbl_font)  # entry box
    entry_entry_card.pack(pady=5, side=RIGHT)
    entry_entry_card.get()        # getting the details from GUI
    card_frame.pack(pady=10, anchor=W)

    address_frame = tk.Frame(top)   # creating a widget to indicate the user to enter the Address details
    address_label = tk.Label(address_frame, text="Address     ", font=lbl_font)
    address_label.pack(pady=5, side=LEFT)
    entry_entry_address = tk.Entry(address_frame, font=lbl_font)  # entry box
    entry_entry_address.pack(pady=5, side=RIGHT)
    entry_entry_address.get()        # getting the details from GUI
    entry_entry_address.delete(0, tk.END)  # delete the entry box from previous typing data
    address_frame.pack(pady=10, anchor=W)  # packing the widget and place it in the window

    pay_button_frame = tk.Frame(top) # creating a frame for one button
    pay_button = tk.Button(pay_button_frame, text="PayNow", font=lbl_font, command=visa_check)
    pay_button.pack(pady=5)  # creating 'PayNow' button to make the payments and to display a specific message
    pay_button_frame.pack(pady=10, anchor=CENTER)

    save_button_frame = tk.Frame(top)  # creating a button to save the client details in the data base
    save_button = tk.Button(save_button_frame, text="Save", font=lbl_font, command=DataBase)
    save_button.pack(pady=5)
    save_button_frame.place(x=390, y=280)

    en_frame = tk.Frame(top)  # creating a widget
    en_label = tk.Label(en_frame, text="Receipt ", font=lbl_font)
    en_label.pack(pady=5, side=LEFT)  # packing and placing the label in the 'top' window
    en_frame.pack(pady=10, anchor=W)

    print_button_frame = tk.Frame(top)  # display the receipt in a GUI
    print_button = tk.Button(print_button_frame, text="Show", font=lbl_font, command=cart.receipt)
    print_button.pack(pady=5)
    print_button_frame.pack(pady=10, anchor=CENTER)

    save_re_button_frame = tk.Frame(top)  # creating a button to save the receipt
    save_re_button = tk.Button(save_re_button_frame, text="Save", font=lbl_font, command=cart.receipt_save)
    save_re_button.pack(pady=5)
    save_re_button_frame.place(x=377, y=396)

    button_exit_frame = tk.Frame(top)  # create a button to exit from window
    button_exit = tk.Button(button_exit_frame, text="Close", font=lbl_font, command=exit)
    button_exit.pack(pady=5)
    button_exit_frame.pack(pady=5, anchor=E)


# the main program
cart = Cart()
radio_ = Radio()

file_data_base = open("AllAboutToys", "a+")  # open the data base to read and write data
root = tk.Tk()       # create the main window
root_geometry()      # calling the function to create the main window with a specific geometry
root.title("Shopping Cart")  # given a title to the main window
lbl_font = font.Font(family='Georgia', size='14', weight='bold')  # setting the text font
lbl = tk.Label(root, text="All About Toys Ltd.", font=lbl_font)  # creating a label to display the name of the shop
lbl.pack()                                                       # packing the label
lbl_discount = tk.Label(root, text="20% off for all toys.\n The discount will be applied at checkout", font=lbl_font,
                        fg="red")  # creating a label with  a specific message to inform costumer about the sales
lbl_discount.pack()
# Creating a label and an entry box in GUI for costumer to enter the toys he whats to buy
entry_frame_item = tk.Frame(root)
entry_label_item = tk.Label(entry_frame_item, text="Item ", font=lbl_font)  # coding the label
entry_label_item.pack(pady=5, side=LEFT)
entry_entry_item = tk.Entry(entry_frame_item, font=lbl_font)  # coding the entry box
entry_entry_item.pack(pady=5, side=RIGHT)
entry_entry_item.delete(0, tkinter.END)  # clear the entry box from previous data
entry_entry_item.get()
entry_frame_item.pack(pady=10, anchor=W)
entry_entry_item.delete(0, tkinter.END)   # delete the entry box from previous entries
# Creating a label and an entry box in GUI for costumer to enter the price
entry_frame_price = tk.Frame(root)
entry_label_price = tk.Label(entry_frame_price, text="Price", font=lbl_font)
entry_label_price.pack(pady=5, side=LEFT)
entry_entry_price = tk.Entry(entry_frame_price, font=lbl_font)
entry_entry_price.pack(pady=5, side=RIGHT)
entry_entry_price.delete(0, tkinter.END)   # delete the entry box from previous entries
entry_entry_price.get()
entry_frame_price.pack(pady=5, anchor=W)
entry_entry_price.delete(0, tkinter.END)
# coding the Label, Entry box for typing the quantity in the GUI cart option
entry_frame_quantity = tk.Frame(root)
entry_label_quantity = tk.Label(entry_frame_quantity, text="Qty.  ", font=lbl_font)
entry_label_quantity.pack(pady=5, side=LEFT)
entry_entry_quantity = tk.Entry(entry_frame_quantity, font=lbl_font)
entry_entry_quantity.pack(pady=5, side=RIGHT)
entry_entry_quantity.delete(0, tkinter.END)  # delete the entry box from previous entries
entry_entry_quantity.get()
entry_frame_quantity.pack(pady=10, anchor=W)
entry_entry_quantity.delete(0, tkinter.END)
# coding the button for 'Add' the cart option
entry_button_frame = tk.Frame(root)
entry_entry_item.delete(first=0, last=22)
entry_button_item = tk.Button(entry_button_frame, text="Add", font=lbl_font, command=cart.add_item)
entry_button_item.pack(pady=5)
entry_button_frame.pack(pady=10, anchor=CENTER)
# coding the button for 'Update' the cart option
update_button_frame = tk.Frame(root)
update_button = tk.Button(update_button_frame, text="Update", font=lbl_font, command=cart.update_item)
update_button.pack(pady=5)
update_button_frame.pack()
update_button_frame.place(x=384, y=257)
# coding the button for 'Delete' the cart option
delete_button_frame = tk.Frame(root)
delete_button = tk.Button(delete_button_frame, text="Delete", font=lbl_font, command=cart.remove_item)
delete_button.pack(pady=5)
delete_button_frame.pack()
delete_button_frame.place(x=480, y=257)
# coding the button for 'Show' the cart option
cart_button_frame = tk.Frame(root)
cart_button = tk.Button(cart_button_frame, text="Show", font=lbl_font, command=cart.show_cart)
cart_button.pack(pady=5)
cart_button_frame.pack()
cart_button_frame.place(x=570, y=257)

# coding  radiobutton in the main window to give the user the option to choose the transport
lbl1 = tk.Label(root, text="Choose Transport", font=lbl_font)
lbl1.pack(anchor=W)
var = IntVar()  # reading the client options regarding the transport

R1 = Radiobutton(root, text="Royal Mail, 5£", font=lbl_font, variable=var, value=1, command=radio_.selection)
R1.pack(anchor=W)

R2 = Radiobutton(root, text="AmazonPrime, 10£", font=lbl_font, variable=var, value=2, command=radio_.selection)
R2.pack(anchor=W)

R3 = Radiobutton(root, text="Pick up from Store", font=lbl_font, variable=var, value=3, command=radio_.selection)
R3.pack(anchor=W)
# coding a label with a specific message
total_price_frame = tk.Frame(root)
entry_label_total_price = tk.Label(total_price_frame, text="Total Price", font=lbl_font)
entry_label_total_price.pack(pady=5, side=LEFT)
display_total_price = Text(total_price_frame, height=1.5, width=10)
display_total_price.pack(pady=5, side=RIGHT)
# coding a button to open the second window.
next_frame = tk.Frame(root)
btn_next = tk.Button(next_frame, text="Next", font=lbl_font, command=window)
btn_next.pack(pady=20, side=RIGHT)
next_frame.pack(fill='both', expand=1, anchor=W)
file_data_base.close()  # closing the data base
root.mainloop()
