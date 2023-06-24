import sqlite3
import pathlib
from pathlib import Path
from tkinter import *
from tkinter import ttk
import re
import tkinter as tk


class DBConnect:
    """
    connecting DB
    """
    def __init__(self):
        self.db_path = Path(pathlib.Path.cwd(), 'airports.db')

    def db_connect(self):
        sqlite_connection = sqlite3.connect(self.db_path)
        return sqlite_connection


class DBFetch:
    """
    fetching the airports data and converting to list
    """
    def __init__(self):
        self.db = DBConnect()

    def to_list(self) -> list:
        sqlite_connect = sqlite3.connect('airports.db')
        cursor = sqlite_connect.cursor()
        cursor.execute(f"SELECT DISTINCT city FROM airports ORDER BY city ASC")
        return [city for cities in cursor.fetchall() for city in cities]


class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def get_airports(self, lat_min: str, lat_max: str, lon_min: str, lon_max: str):
        """
        Transferring data from model to view
        """
        self.model.lat_min = lat_min
        self.model.lat_max = lat_max
        self.model.lon_min = lon_min
        self.model.lon_max = lon_max
        airports = self.model.search_airports()
        self.view.show_airports(airports)


class Model:

    def __init__(self):
        self.lat_min = "0"
        self.lat_max = "0"
        self.lon_min = "0"
        self.lon_max = "0"
        self.src_city = "0"
        self.dst_city = "0"
        self.db = None

    def set_db(self, db):
        self.db = db

    def search_airports(self) -> list:
        """
        Airports by coordinates in DB into list
        """
        coordinates = (self.lat_min, self.lat_max, self.lon_min, self.lon_max)
        match = [re.match("^-?\d+$", item) for item in coordinates]
        if None in match:
            self.lat_min, self.lat_max, self.lon_min, self.lon_max = ("0", "0", "0", "0")
        db_connection = self.db.db_connect()
        cursor = db_connection.cursor()
        cursor.execute(f"SELECT country, city, airport, latitude, longitude FROM airports WHERE"
                       f" latitude BETWEEN {self.lat_min} and {self.lat_max} and"
                       f" longitude BETWEEN {self.lon_min} and {self.lon_max}")
        return cursor.fetchall()

    def search_routes(self) -> list:

        if None in (self.src_city, self.dst_city):
            self.src_city, self.dst_city = ("0", "0")
        db_connection = self.db.db_connect()
        cursor = db_connection.cursor()
        cursor.execute(f"SELECT src_airport, dst_airport, airplane FROM routes WHERE "
                       f"src_airport_id IN (SELECT id FROM airports WHERE city = '{self.src_city}') AND "
                       f"dst_airport_id IN (SELECT id FROM airports WHERE city = '{self.dst_city}')")
        return cursor.fetchall()


class View(ttk.Notebook):
    def __init__(self, parent):
        super().__init__(parent)
        self.controller = None
        self.data_extractor = DBFetch()
        self.frame1 = ttk.Frame(self)
        self.add(self.frame1, text="Airlines locator")
        self.grid()
        self.lat_min_entry = ttk.Entry(self.frame1, width=40)
        self.lat_min_entry.insert(0, "0")
        self.lat_max_entry = ttk.Entry(self.frame1, width=40)
        self.lat_max_entry.insert(0, "0")
        self.lon_min_entry = ttk.Entry(self.frame1, width=40)
        self.lon_min_entry.insert(0, "0")
        self.lon_max_entry = ttk.Entry(self.frame1, width=40)
        self.lon_max_entry.insert(0, "0")
        self.lat_min_label = ttk.Label(self.frame1, text="Min latitude:")
        self.lat_max_label = ttk.Label(self.frame1, text="Max latitude:")
        self.lon_min_label = ttk.Label(self.frame1, text="Min longitude:")
        self.lon_max_label = ttk.Label(self.frame1, text="Max longitude:")
        self.tree = ttk.Treeview(self.frame1, columns=("country", "city", "airport", "latitude", "longitude"),
                                 show="headings", height=25)
        self.tree.heading("city", text="city", anchor=W)
        self.tree.heading("country", text="country", anchor=W)
        self.tree.heading("airport", text="airport", anchor=W)
        self.tree.heading("latitude", text="latitude", anchor=W)
        self.tree.heading("longitude", text="longitude", anchor=W)
        self.tree.column("#1", stretch=NO, width=100)
        self.tree.column("#2", stretch=NO, width=120)
        self.tree.column("#3", stretch=NO, width=300)
        self.tree.column("#4", stretch=NO, width=140)
        self.tree.column("#5", stretch=NO, width=140)
        self.search_airports_btn = ttk.Button(self.frame1, text="Search", width=15,
                                              command=self.clicked_show)
        self.clear_btn = ttk.Button(self.frame1, text="Clear", width=15, command=self.clicked_clear)
        self.lat_min_label.grid(row=0, column=0)
        self.lat_max_label.grid(row=0, column=2)
        self.lon_min_label.grid(row=1, column=0)
        self.lon_max_label.grid(row=1, column=2)
        self.lat_min_entry.grid(row=0, column=1)
        self.lat_max_entry.grid(row=0, column=3)
        self.lon_min_entry.grid(row=1, column=1)
        self.lon_max_entry.grid(row=1, column=3)
        self.search_airports_btn.grid(row=0, column=4)
        self.clear_btn.grid(row=1, column=4)
        self.tree.grid(row=2, column=0, columnspan=5)

    def set_controller(self, controller):
        self.controller = controller

    def clicked_show(self):
        if self.controller:
            self.controller.get_airports(self.lat_min_entry.get(),
                                         self.lat_max_entry.get(),
                                         self.lon_min_entry.get(),
                                         self.lon_max_entry.get())

    def clicked_clear(self):
        self.tree.delete(*self.tree.get_children())
        self.lat_min_entry.delete(0, END)
        self.lat_min_entry.insert(0, "0")
        self.lat_max_entry.delete(0, END)
        self.lat_max_entry.insert(0, "0")
        self.lon_min_entry.delete(0, END)
        self.lon_min_entry.insert(0, "0")
        self.lon_max_entry.delete(0, END)
        self.lon_max_entry.insert(0, "0")

    def show_airports(self, airports):
        self.tree.delete(*self.tree.get_children())
        for airport in airports:
            self.tree.insert("", END, values=airport)


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('airlines locator')
        db = DBConnect()
        model = Model()
        model.set_db(db)
        view = View(self)
        view.grid(row=0, column=0, padx=10, pady=10)
        controller = Controller(model, view)
        view.set_controller(controller)


if __name__ == '__main__':
    app = App()
    app.mainloop()
