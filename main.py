from tkinter import *
from functions import *

root = Tk()
root.title('Project Progamming')
root.geometry('{}x{}'.format(1280, 720))
root.resizable(width=False, height=False)

def travel_recommendation():
    """"Uses information_to_dict() to ask for a travel recommendation from the NS API, and inserts the departure times from those recommendations into a listbox."""

    global travel_possibilities

    travel_possibilities_dict = information_to_dict('ns-api-treinplanner?fromStation={}&viaStation={}&toStation={}'.format(from_station_entry.get(), via_station_entry.get(), to_station_entry.get()))
    travel_possibilities = [possibility for possibility in travel_possibilities_dict['ReisMogelijkheden']['ReisMogelijkheid']]

    possibilities_listbox.delete(0, END)

    for possibility in travel_possibilities:
        possibilities_listbox.insert(END, possibility['GeplandeVertrekTijd'][11:16])


def listbox_selection(event):
    selection_index = int(possibilities_listbox.curselection()[0])
    for possibility in travel_possibilities:
        if travel_possibilities.index(possibility) == selection_index:
            # Code to display information of the possibility
            print(possibility) # Explanatory print

# create all of the main containers
top_frame = Frame(root, width=450, height=50, pady=3)
center = Frame(root, width=250, height=40, padx=3, pady=3)

# layout main containers
root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)

top_frame.grid(row=0, sticky="ew")
center.grid(row=1, sticky="nsew")

# create widgets top frame
invoer_label = Label(top_frame, text='Invoer')
from_station_label = Label(top_frame, text='Beginstation:')
via_station_label = Label(top_frame, text='Via (leeglaten if none):')
to_station_label = Label(top_frame, text='Bestemming:')
from_station_entry = Entry(top_frame)
via_station_entry = Entry(top_frame)
to_station_entry = Entry(top_frame)
button = Button(master = top_frame, text = 'Geef vertrekmogelijkheden', command=travel_recommendation)

# layout widgets of top frame
invoer_label.grid(row=0, column=0)
from_station_label.grid(row=1, column=0, padx=(15, 0))
via_station_label.grid(row=1, column=2)
to_station_label.grid(row=1, column=4)
from_station_entry.grid(row=1, column=1, padx=(0, 15))
via_station_entry.grid(row=1, column=3, padx=(0, 15))
to_station_entry.grid(row=1, column=5, padx=(0, 15))
button.grid(row = 1, column = 7, pady=(0, 5))

# create widgets center
center.grid_rowconfigure(0, weight=1)
center.grid_columnconfigure(1, weight=1)

ctr_left = Frame(center, bg='blue', width=250, height=190, padx=3, pady=3)
ctr_mid = Frame(center, bg='green', width=250, height=190, padx=3, pady=3)

ctr_left.grid(row=0, column=0, sticky='nsew')
ctr_mid.grid(row=0, column=1, sticky='nsew')

# layout widgets ctr_left
possibilities_listbox = Listbox(ctr_left, height=30)
possibilities_listbox.grid(row=0, column=0)
possibilities_listbox.bind('<<ListboxSelect>>', listbox_selection)

root.mainloop()

# travel_recommendation = information_to_dict('ns-api-treinplanner?fromStation={}&viaStation={}&toStation={}&previousAdvices=0'.format(from_station, via_station, to_station))
# station_list = information_to_dict('ns-api-stations-v2')
# station_departure_information = information_to_dict('ns-api-avt?station=${}'.format(input_station))

