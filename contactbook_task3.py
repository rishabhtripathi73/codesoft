import tkinter as tk
from tkinter import messagebox

# Main Application
class ContactManager:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Manager")
        self.root.geometry("600x400")
        self.contacts = {}  # Dictionary to store contacts

        # User Interface
        self.setup_ui()

    def setup_ui(self):
        # Title
        self.title = tk.Label(self.root, text="Contact Manager", font=("Helvetica", 20))
        self.title.pack(pady=10)

        # Frame for contact form
        self.form_frame = tk.Frame(self.root)
        self.form_frame.pack(pady=10)

        tk.Label(self.form_frame, text="Store Name:").grid(row=0, column=0, padx=5, pady=5)
        self.store_name_entry = tk.Entry(self.form_frame)
        self.store_name_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(self.form_frame, text="Phone Number:").grid(row=1, column=0, padx=5, pady=5)
        self.phone_entry = tk.Entry(self.form_frame)
        self.phone_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(self.form_frame, text="Email:").grid(row=2, column=0, padx=5, pady=5)
        self.email_entry = tk.Entry(self.form_frame)
        self.email_entry.grid(row=2, column=1, padx=5, pady=5)

        tk.Label(self.form_frame, text="Address:").grid(row=3, column=0, padx=5, pady=5)
        self.address_entry = tk.Entry(self.form_frame)
        self.address_entry.grid(row=3, column=1, padx=5, pady=5)

        # Buttons for actions
        self.button_frame = tk.Frame(self.root)
        self.button_frame.pack(pady=10)

        self.add_button = tk.Button(self.button_frame, text="Add Contact", command=self.add_contact)
        self.add_button.grid(row=0, column=0, padx=5, pady=5)

        self.view_button = tk.Button(self.button_frame, text="View Contacts", command=self.view_contacts)
        self.view_button.grid(row=0, column=1, padx=5, pady=5)

        self.search_button = tk.Button(self.button_frame, text="Search Contact", command=self.search_contact)
        self.search_button.grid(row=0, column=2, padx=5, pady=5)

        self.update_button = tk.Button(self.button_frame, text="Update Contact", command=self.update_contact)
        self.update_button.grid(row=0, column=3, padx=5, pady=5)

        self.delete_button = tk.Button(self.button_frame, text="Delete Contact", command=self.delete_contact)
        self.delete_button.grid(row=0, column=4, padx=5, pady=5)

        self.clear_button = tk.Button(self.button_frame, text="Clear", command=self.clear_entries)
        self.clear_button.grid(row=0, column=5, padx=5, pady=5)

    def add_contact(self):
        store_name = self.store_name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        address = self.address_entry.get()

        if store_name and phone:
            self.contacts[store_name] = {
                "Phone": phone,
                "Email": email,
                "Address": address
            }
            messagebox.showinfo("Success", "Contact added successfully")
            self.clear_entries()
        else:
            messagebox.showwarning("Input Error", "Store Name and Phone Number are required")

    def view_contacts(self):
        contacts_str = ""
        for name, details in self.contacts.items():
            contacts_str += f"Store Name: {name}\n"
            contacts_str += f"Phone Number: {details['Phone']}\n"
            contacts_str += f"Email: {details['Email']}\n"
            contacts_str += f"Address: {details['Address']}\n\n"

        messagebox.showinfo("Contacts List", contacts_str if contacts_str else "No contacts found")

    def search_contact(self):
        search_term = self.store_name_entry.get() or self.phone_entry.get()
        found = False

        for name, details in self.contacts.items():
            if search_term in (name, details['Phone']):
                found = True
                contacts_str = f"Store Name: {name}\n"
                contacts_str += f"Phone Number: {details['Phone']}\n"
                contacts_str += f"Email: {details['Email']}\n"
                contacts_str += f"Address: {details['Address']}\n"
                messagebox.showinfo("Search Result", contacts_str)
                break
        
        if not found:
            messagebox.showwarning("Search Result", "Contact not found")

    def update_contact(self):
        store_name = self.store_name_entry.get()
        if store_name in self.contacts:
            phone = self.phone_entry.get()
            email = self.email_entry.get()
            address = self.address_entry.get()

            self.contacts[store_name] = {
                "Phone": phone,
                "Email": email,
                "Address": address
            }
            messagebox.showinfo("Success", "Contact updated successfully")
            self.clear_entries()
        else:
            messagebox.showwarning("Update Error", "Contact not found")

    def delete_contact(self):
        store_name = self.store_name_entry.get()
        if store_name in self.contacts:
            del self.contacts[store_name]
            messagebox.showinfo("Success", "Contact deleted successfully")
            self.clear_entries()
        else:
            messagebox.showwarning("Delete Error", "Contact not found")

    def clear_entries(self):
        self.store_name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.address_entry.delete(0, tk.END)

# Start the application
if __name__ == "__main__":
    root = tk.Tk()
    app = ContactManager(root)
    root.mainloop()
