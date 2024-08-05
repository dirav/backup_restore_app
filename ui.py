from tkinter import *
from tkinter import messagebox, filedialog, simpledialog
from backup import backup
from restore import restore

class BackupRestoreApp:
    def __init__(self, master):
        self.master = master
        master.title("Backup and Restore")

        self.label = Label(master, text="Select Site Directory:")
        self.label.pack()

        self.site_directory_entry = Entry(master, width=50)
        self.site_directory_entry.pack()

        self.browse_button = Button(master, text="Browse", command=self.browse_directory)
        self.browse_button.pack()

        self.backup_button = Button(master, text="Backup", command=self.backup)
        self.backup_button.pack()

        self.restore_button = Button(master, text="Restore", command=self.restore)
        self.restore_button.pack()

        self.status = Label(master, text="", bd=1, relief=SUNKEN, anchor=W)
        self.status.pack(side=BOTTOM, fill=X)

    def browse_directory(self):
        directory = filedialog.askdirectory()
        if directory:
            self.site_directory_entry.delete(0, END)
            self.site_directory_entry.insert(0, directory)

    def backup(self):
        site_directory = self.site_directory_entry.get()
        if not site_directory:
            messagebox.showerror("Error", "Please select a site directory.")
            return

        db_user = "turkcezormu-lms"
        db_password = "NxmeEPl72ScEbMOCE9SP"

        self.status.config(text="Backing up...")
        result = backup(site_directory, db_user, db_password)
        self.status.config(text=result)

    def restore(self):
        site_directory = self.site_directory_entry.get()
        if not site_directory:
            messagebox.showerror("Error", "Please select a site directory.")
            return

        backup_date = self.get_backup_date()
        if not backup_date:
            return

        db_user = "turkcezormu-lms"
        db_password = "NxmeEPl72ScEbMOCE9SP"

        self.status.config(text="Restoring...")
        result = restore(site_directory, backup_date, db_user, db_password)
        self.status.config(text=result)

    def get_backup_date(self):
        backup_date = simpledialog.askstring("Input", "Enter backup date (YYYY-MM-DD):")
        return backup_date
