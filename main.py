from functions import *

def travel_recommendation():
    """"Uses information_to_dict() to ask for a travel recommendation from the NS API, and inserts the departure times from those recommendations into a listbox."""

    global travel_possibilities

    travel_possibilities_dict = information_to_dict('ns-api-treinplanner?fromStation={}&viaStation={}&toStation={}'.format(from_station_entry.get(), via_station_entry.get(), to_station_entry.get()))
    travel_possibilities = [possibility for possibility in travel_possibilities_dict['ReisMogelijkheden']['ReisMogelijkheid']]

    possibilities_listbox.delete(0, END)

    for possibility in travel_possibilities:
        possibilities_listbox.insert(END, possibility['ActueleVertrekTijd'][11:16])

def listbox_selection(event):
    """"Takes the event from the possibilities listbox and then replaces the information in the (empty) widgets in ctr_mid with the currently selected possibility's travel information."""
    try:
        selection_index = int(possibilities_listbox.curselection()[0])
    except IndexError:
        return

    for possibility in travel_possibilities:
        if travel_possibilities.index(possibility) == selection_index:
            if 'VertrekVertraging' in possibility:
                departure_time = '{} {}'.format(possibility['ActueleVertrekTijd'][11:16], possibility['VertrekVertraging'])
            else:
                departure_time = possibility['ActueleVertrekTijd'][11:16]

            if 'AankomstVertraging' in possibility:
                arrival_time = '{} {}'.format(possibility['ActueleAankomstTijd'][11:16], possibility['AankomstVertraging'])
            else:
                arrival_time = possibility['ActueleAankomstTijd'][11:16]

            departure_arrival_time_label['text'] = '{} <> {}'.format(departure_time, arrival_time)
            travel_time_label['text'] = 'Reistijd: {}'.format(possibility['ActueleReisTijd'])

            if possibility['AantalOverstappen'] == '0':
                remove_grid_slaves(ctr_mid_stops)
                too_many.place_forget()
                part_maker(ctr_mid_stops, bg_color, fg_color, possibility['ReisDeel'], 0, None)

            else:
                remove_grid_slaves(ctr_mid_stops)

                if len(possibility['ReisDeel']) > 4:
                    departure_arrival_time_label['text'] = ''
                    travel_time_label['text'] = ''
                    notification_label['text'] = ''
                    too_many.place_forget()
                    too_many.place(x=10, y=100)
                    return
                else:
                    too_many.place_forget()

                part = 1
                column_number = 0
                for travel_part in possibility['ReisDeel']:
                    part_maker(ctr_mid_stops, bg_color, fg_color, travel_part, column_number, part)
                    column_number += 1
                    part += 1

            notification_label_text(possibility, notification_label, fg_color)

bg_color = "#FFCC20"
fg_color = "#000066"

root = Tk()
root.title('Project Progamming')
root.geometry('{}x{}'.format(1280, 720))
root.resizable(width = False, height = False)

# create all of the main containers
top_frame = Frame(root, pady = 3)
center = Frame(root, padx = 3, pady = 3)

# layout main containers
root.grid_rowconfigure(1, weight = 1)
root.grid_columnconfigure(0, weight = 1)

top_frame.grid(row = 0, sticky = "ew")
center.grid(row = 1, sticky = "nsew")

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
invoer_label.grid(row = 0, column = 0)
from_station_label.grid(row = 1, column = 0, padx = (15, 0))
via_station_label.grid(row = 1, column = 2)
to_station_label.grid(row = 1, column = 4)
from_station_entry.grid(row = 1, column = 1, padx = (0, 15))
via_station_entry.grid(row = 1, column = 3, padx = (0, 15))
to_station_entry.grid(row = 1, column = 5, padx = (0, 15))
button.grid(row = 1, column = 7, pady = (0, 5))

# create widgets center
center.grid_rowconfigure(0, weight=1)
center.grid_columnconfigure(1, weight=1)

ctr_left = Frame(center, bg = 'blue', padx = 3, pady = 3)
ctr_mid = Frame(center, bg = bg_color, padx = 3, pady = 3)

ctr_left.grid(row = 0, column = 0, sticky = 'nsew')
ctr_mid.grid(row = 0, column = 1, sticky = 'nsew')

# layout widgets ctr_mid
ctr_mid_stops = Frame(ctr_mid, bg = bg_color)
departure_arrival_time_label = Label(master = ctr_mid, text = '', bg = bg_color, fg = fg_color)
travel_time_label = Label(master = ctr_mid, text = '', bg = bg_color, fg = fg_color)
notification_label = Label(master = ctr_mid, text = '', bg = bg_color, fg = fg_color)
too_many = Label(ctr_mid, text = 'Helaas worden meer dan 4 reisdelen niet ondersteund door deze applicatie.', bg = bg_color, fg = fg_color, font = ('Helvetica', 18))

# layout widgets ctr_left
possibilities_listbox = Listbox(ctr_left, height = 30)
possibilities_listbox.grid(row = 0, column = 0)
possibilities_listbox.bind('<<ListboxSelect>>', listbox_selection)

# layout widgets ctr_mid
ctr_mid_stops.pack(anchor = W, padx = (10, 0), pady = (100, 0))
departure_arrival_time_label.place(x = 10, y = 10)
travel_time_label.place(x = 10, y = 30)
notification_label.place(x = 500, y = 10)

root.mainloop()

# travel_recommendation = information_to_dict('ns-api-treinplanner?fromStation={}&viaStation={}&toStation={}&previousAdvices=0'.format(from_station, via_station, to_station))
# station_list = information_to_dict('ns-api-stations-v2')
# station_departure_information = information_to_dict('ns-api-avt?station=${}'.format(input_station))

