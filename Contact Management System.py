import tkinter as tk
from tkinter import ttk
import json

class ContactManager:
    def __init__(self, master):
        self.master = master
        self.master.title("Contact Management System")

        self.contacts = []

        # Load contacts from file if available
        self.load_contacts()

        self.name_label = ttk.Label(master, text="Name:")
        self.name_label.grid(row=0, column=0, padx=5, pady=5)

        self.name_entry = ttk.Entry(master)
        self.name_entry.grid(row=0, column=1, padx=5, pady=5)

        self.phone_label = ttk.Label(master, text="Phone:")
        self.phone_label.grid(row=1, column=0, padx=5, pady=5)

        self.phone_entry = ttk.Entry(master)
        self.phone_entry.grid(row=1, column=1, padx=5, pady=5)

        self.email_label = ttk.Label(master, text="Email:")
        self.email_label.grid(row=2, column=0, padx=5, pady=5)

        self.email_entry = ttk.Entry(master)
        self.email_entry.grid(row=2, column=1, padx=5, pady=5)

        self.add_button = ttk.Button(master, text="Add Contact", command=self.add_contact)
        self.add_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

        self.edit_button = ttk.Button(master, text="Edit Contact", command=self.edit_contact)
        self.edit_button.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

        self.delete_button = ttk.Button(master, text="Delete Contact", command=self.delete_contact)
        self.delete_button.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

        self.contact_listbox = tk.Listbox(master, width=50)
        self.contact_listbox.grid(row=6, column=0, columnspan=2, padx=5, pady=5)
        self.contact_listbox.bind("<<ListboxSelect>>", self.select_contact)

        self.update_contact_listbox()

    def add_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()

        if name and phone:
            contact = {"Name": name, "Phone": phone, "Email": email}
            self.contacts.append(contact)
            self.update_contact_listbox()
            self.clear_fields()
            self.save_contacts()
        else:
            tk.messagebox.showwarning("Missing Information", "Please fill in the name and phone number.")

    def edit_contact(self):
        selected_index = self.contact_listbox.curselection()
        if selected_index:
            selected_contact = self.contacts[selected_index[0]]
            name = self.name_entry.get()
            phone = self.phone_entry.get()
            email = self.email_entry.get()

            if name and phone:
                selected_contact["Name"] = name
                selected_contact["Phone"] = phone
                selected_contact["Email"] = email

                self.update_contact_listbox()
                self.clear_fields()
                self.save_contacts()
            else:
                tk.messagebox.showwarning("Missing Information", "Please fill in the name and phone number.")

    def delete_contact(self):
        selected_index = self.contact_listbox.curselection()
        if selected_index:
            del self.contacts[selected_index[0]]
            self.update_contact_listbox()
            self.clear_fields()
            self.save_contacts()

    def select_contact(self, event):
        selected_index = self.contact_listbox.curselection()
        if selected_index:
            selected_contact = self.contacts[selected_index[0]]
            self.name_entry.delete(0, tk.END)
            self.name_entry.insert(0, selected_contact["Name"])
            self.phone_entry.delete(0, tk.END)
            self.phone_entry.insert(0, selected_contact["Phone"])
            self.email_entry.delete(0, tk.END)
            self.email_entry.insert(0, selected_contact["Email"])

    def update_contact_listbox(self):
        self.contact_listbox.delete(0, tk.END)
        for contact in self.contacts:
            self.contact_listbox.insert(tk.END, contact["Name"])

    def load_contacts(self):
        try:
            with open("contacts.json", "r") as file:
                self.contacts = json.load(file)
        except FileNotFoundError:
            pass

    def save_contacts(self):
        with open("contacts.json", "w") as file:
            json.dump(self.contacts, file)

    def clear_fields(self):
        self.name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)

def main():
    root = tk.Tk()
    contact_manager = ContactManager(root)
    root.mainloop()

if __name__ == "__main__":
    main()
