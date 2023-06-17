from tkinter import *
import sqlite3


class Table:
    def __init__(self, root, data):
        self.data = data
        self.total_rows = len(data)
        self.total_columns = len(data)
        for i in range(self.total_rows):
            for j in range(self.total_columns):
                self.e = Entry(root, width=20, fg='black', font=('Arial', 14, 'bold'))
                self.e.grid(row=i, column=j)
                self.e.insert(END, self.data[i][j])

    def destroy(self, root):
        for widget in root.winfo_children():
            widget.destroy()


t = None


def click1():
    cursor = app.cursor()
    query = ("SELECT city, country, latitude, longitude FROM airports "
             "WHERE latitude BETWEEN " + min_lat.get() + " AND " + max_lat.get() +
             " AND longitude BETWEEN " + min_lon.get() + " AND " + max_lon.get())
    cursor.execute(query)

    lst = []
    for (city, country, latitude, longitude) in cursor:
        lst.append((city, country, latitude, longitude))

    cursor.close()
    global t
    if t is not None:
        t.destroy(bottom_frame)
    t = Table(bottom_frame, lst)


window = Tk()
window.title("Airports")
window.geometry('1000x1000')

main_frame = Frame(window)
main_frame.pack()

top_frame = Frame(main_frame)
top_frame.pack(side=TOP)

bottom_frame = Frame(main_frame)
bottom_frame.pack(side=BOTTOM)

btn = Button(top_frame, text="Apply", font=("Arial", 14), command=click1)
btn.grid(column=0, row=4, columnspan=2)

Label(top_frame, text="Min latitude:").grid(row=0, column=0, sticky=W, pady=20, padx=20)
min_lat = Entry(top_frame,width=30)
min_lat.grid(column=0, row=1)
min_lat.delete(0, END)
min_lat.insert(0, '30.0')

Label(top_frame, text="Max latitude:").grid(row=0, column=1, sticky=W, pady=20, padx=20)
max_lat = Entry(top_frame,width=30)
max_lat.grid(column=1, row=1)
max_lat.delete(0, END)
max_lat.insert(0, '70.0')

Label(top_frame, text="Min longitude:").grid(row=2, column=0, sticky=W, pady=20, padx=20)
max_lon = Entry(top_frame,width=30)
max_lon.grid(column=0, row=3)
max_lon.delete(0, END)
max_lon.insert(0, '30.0')

Label(top_frame, text="Max longitude:").grid(row=2, column=1, sticky=W, pady=20, padx=20)
min_lon = Entry(top_frame,width=30)
min_lon.grid(column=1, row=3)
min_lon.delete(0, END)
min_lon.insert(0, '70.0')

app = sqlite3.connect("airports.db")

window.mainloop()

app.close()

