import hospital.config as config
import datetime
from tkinter import (
    messagebox,
    Frame,
    Label,
    LEFT,
    Tk,
    Entry,
    Button,
)

# import TransportLayer as tp
from hospital.app.data import Database, DoubleEntryError
import sys

path_to_db = "/".join(sys.path[0].split("/")[:-1]) + "/data/database.db"


# tkinter window
class Application:
    def __init__(self, master):
        self.db = Database(
            path_to_db, config.TABLE_NAME, config.DATABASE_COLUMNS_STR
        )
        self.master = master

        # creating the frames in the master
        self.left = Frame(master, width=720, height=500, bg="cyan")
        # self.bg = PhotoImage(file="bg.png")
        # self.label = Label(self.left, image=self.bg)
        # self.label.place(x=0, y=225, relwidth=1, relheight=1)
        self.left.pack(side=LEFT)

        # labels for the window
        self.heading = Label(
            self.left,
            text="Hospital Admins",
            font="arial 40 bold",
            fg="black",
            bg="cyan",
        )
        self.heading.place(x=0, y=0)
        # patients ID
        self.ID = Label(
            self.left,
            text="Hospital ID",
            font="arial 18 bold",
            fg="black",
            bg="cyan",
        )
        self.ID.place(x=0, y=100)

        # in_care
        self.in_care = Label(
            self.left,
            text="Bed in intensive care",
            font="arial 18 bold",
            fg="black",
            bg="cyan",
        )
        self.in_care.place(x=0, y=140)

        # ven
        self.ven = Label(
            self.left,
            text="Used Ventilators",
            font="arial 18 bold",
            fg="black",
            bg="cyan",
        )
        self.ven.place(x=0, y=180)

        # max_bed
        self.max_bed = Label(
            self.left,
            text="Max bed",
            font="arial 18 bold",
            fg="black",
            bg="cyan",
        )
        self.max_bed.place(x=0, y=220)

        # appointment max_ven
        self.max_ven = Label(
            self.left,
            text="Max ven",
            font="arial 18 bold",
            fg="black",
            bg="cyan",
        )
        self.max_ven.place(x=0, y=260)

        # date
        self.date = Label(
            self.left,
            text="Date (yyyy-mm-dd)",
            font="arial 18 bold",
            fg="black",
            bg="cyan",
        )
        self.date.place(x=0, y=300)

        # Entries for all labels==============================================
        self.ID_ent = Entry(self.left, width=30)
        self.ID_ent.place(x=280, y=100)

        self.in_care_ent = Entry(self.left, width=30)
        self.in_care_ent.place(x=280, y=140)

        self.ven_ent = Entry(self.left, width=30)
        self.ven_ent.place(x=280, y=180)

        self.max_bed_ent = Entry(self.left, width=30)
        self.max_bed_ent.place(x=280, y=220)

        self.max_ven_ent = Entry(self.left, width=30)
        self.max_ven_ent.place(x=280, y=260)

        self.date = Entry(self.left, width=30)
        self.date.place(x=280, y=300)

        # button to perform a command
        self.submit = Button(
            self.left,
            text="Add",
            width=20,
            height=4,
            bg="steelblue",
            command=self.add_appointment,
        )
        self.submit.place(x=300, y=340)

    # funtion to call when the submit button is clicked
    def add_appointment(self):
        # getting the user inputs
        self.val1 = self.ID_ent.get()
        self.val2 = self.in_care_ent.get()
        self.val3 = self.ven_ent.get()
        self.val4 = self.max_bed_ent.get()
        self.val5 = self.max_ven_ent.get()
        self.val6 = self.date.get()

        # checking if the user input is empty
        if (
            self.val1 == ""
            or self.val2 == ""
            or self.val3 == ""
            or self.val4 == ""
            or self.val5 == ""
            or self.val6 == ""
        ):
            messagebox.showinfo("Warning", "Please Fill Up All Boxes")
        # check if ID and Date is repeated for the smae entry
        else:
            # now we add to the database
            try:
                self.db.add_entry(
                    self.val1,
                    self.val2,
                    self.val3,
                    self.val4,
                    self.val5,
                    datetime.datetime.strptime(self.val6, config.DATE_FORMAT),
                )
                messagebox.showinfo(
                    "Success",
                    "Information at " + str(self.val6) + " has been created",
                )
            except DoubleEntryError:
                messagebox.showinfo(
                    "Warning",
                    "Already registered for the same date and hospital ID",
                )


# creating the object
root = Tk()
b = Application(root)

# resolution of the window
root.geometry("720x500+0+0")

# preventing the resize feature
root.resizable(False, False)

# end the loop
root.mainloop()
