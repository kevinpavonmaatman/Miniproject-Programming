from functions import *
from tkinter.messagebox import showerror

def load_mainmenu():
    """Destroys all of root's children and loads the main menu."""

    destroy_slaves(root)

    # Definition of frames
    top_frame = Frame(root, width=200, height=50, pady=3, bg=bg_color)
    buttons_frame = Frame(root, width=200, height=50, bg=bg_color)
    footer_frame = Frame(root, width=200, height=50, bg=bg_color)

    # Layout of frames
    top_frame.grid(row=0)
    buttons_frame.grid(row=1)
    footer_frame.grid(row=2)

    # Definition of widgets top_frame
    title_label = Label(top_frame, text='Main Menu', bg=bg_color, fg=fg_color, width = 40, height=1, font=("Helvetica", 25, "bold"))
    photo = Label(top_frame,image=large_image, bg=bg_color)
    photo.image = large_image
    welcome_label = Label(top_frame, text='Welkom bij de NS Reisapplicatie \n Maak een keuze door te klikken op één van de onderstaande knoppen', bg=bg_color, fg=fg_color, font=("Helvetica", 10, "bold"))

    # Layout widgets of top_frame
    title_label.grid(row=0, pady=50)
    photo.grid(row=1)
    welcome_label.grid(row=2, pady=(50, 0))

    # Definition of widgets buttons_frame
    station_departure_information_button = Button(master = buttons_frame, text = 'Reisinformatie', bg=fg_color, fg=bg_color, font=font_20, command=load_reisinfomenu)
    travel_recommendation_button = Button(master = buttons_frame, text = 'Reisadvies', bg=fg_color, fg=bg_color, font=font_20, command=load_reisadviesmenu)

    # Layout of widgest button_frame
    station_departure_information_button.grid(row=0, column=0, padx=(0, 25))
    travel_recommendation_button.grid(row=0,column=1,padx=(0, 25))

    # Definition of widgets footer_frame
    copyright_label = Label(footer_frame, text='Copyright © 2017. All rights reserved', bg=bg_color, fg=fg_color, width = 50, height=5, font=font_8)
    exit_button = Button(master = footer_frame, text = 'Afsluiten', bg=fg_color, fg=bg_color, font=font_8, command=exit)

    # Layout of widgets footer_frame
    copyright_label.grid(row=0)
    exit_button.grid(row=1)

def load_reisinfomenu():
    """"Destroys all of root's children and loads the reisinfo menu."""

    def station_departure_information():
        """"Uses information_to_dict() to ask for station departure information from the NS API, and inserts the departure times from the return into a listbox."""

        global departures

        try:
            departures_dict = information_to_dict('ns-api-avt?station={}'.format(input_station_entry.get()))
            departures = [departure for departure in departures_dict['ActueleVertrekTijden']['VertrekkendeTrein']]

        except:
            return showerror(title='Foutmelding', message='Station niet gevonden. Probeer het opnieuw')

        possibilities_listbox.delete(0, END)

        for departure in departures:
            if 'VertrekVertraging' in departure:
                possibilities_listbox.insert(END, '{:<25}{:<} {:<}'.format(departure['EindBestemming'], departure['VertrekTijd'][11:16], departure['VertrekVertragingTekst']))
            else:
                possibilities_listbox.insert(END, '{:<25}{:<}'.format(departure['EindBestemming'], departure['VertrekTijd'][11:16]))

    def listbox_selection(event):
        """"Takes the event from the possibilities listbox and then replaces the information in the (empty) widgets in ctr_mid with the currently selected possibility's travel information."""

        try:
            selection_index = int(possibilities_listbox.curselection()[0])
        except IndexError:
            return

        possibilities_listbox.itemconfig(selection_index, bg=fg_color, fg=bg_color)

        for item_value in possibilities_listbox.get(0, END):
            item_index = possibilities_listbox.get(0, END).index(item_value)
            if item_index != selection_index:
                possibilities_listbox.itemconfig(item_index, bg=bg_color, fg=fg_color)

        for departure in departures:
            if departures.index(departure) == selection_index:
                if 'VertrekVertraging' in departure:
                    departure_time['text'] = '{}: {} {}'.format(('Vertrektijd'), departure['VertrekTijd'][11:16],
                                                                departure['VertrekVertragingTekst'])
                else:
                    departure_time['text'] = ('Vertrektijd:', departure['VertrekTijd'][11:16])

                ridenumber['text'] = ('{}: {}'.format(('Ritnummer'), departure['RitNummer']))
                destination['text'] = ('{}: {}'.format('Eindbestemming', departure['EindBestemming']))
                carrier['text'] = ('{}: {}'.format('Vervoerder', departure['Vervoerder']))
                train_type['text'] = '{}: {}'.format(('Type Trein'), departure['TreinSoort'])
                platform['text'] = ''

                if departure['VertrekSpoor']['@wijziging'] == 'true':
                    platform['text'] = (
                    '{}: {}'.format(('Vertrekspoor'), departure['VertrekSpoor']['#text'] + ' (wijziging)'))
                else:
                    if '#text' in departure['VertrekSpoor']:
                        platform['text'] = ('Vertrekspoor:', departure['VertrekSpoor']['#text'])
                    else:
                        platform['text'] = '-'
                if 'RouteTekst' in departure:
                    route_text['text'] = ('{}: {}'.format('Tussenhaltes', departure['RouteTekst']))
                else:
                    route_text['text'] = ''
                if 'ReisTip' in departure:
                    travel_tip['text'] = ('{}: {}'.format('Reistip', departure['ReisTip']))
                else:
                    travel_tip['text'] = ''
                if 'Comments' in departure:
                    comments['text'] = ('Mededelingen:', departure['Comments'])
                else:
                    comments['text'] = ''
                comments['text'] = ''

    destroy_slaves(root)

    # Definition of frames
    top_frame = Frame(root, pady = 3,bg=bg_color)
    center = Frame(root, padx = 3, pady = 3, bg=fg_color)

    # Layout of frames
    top_frame.grid(row = 0, sticky = "ew")
    center.grid(row = 1, sticky = "nsew")

    # Definition of widgets top_frame
    input_label = Label(top_frame, text='Vul uw gegevens in',fg=fg_color, bg=bg_color, font=font_10,bd=10)
    input_station_label = Label(top_frame, text='Station:',fg=fg_color, bg=bg_color, font=font_8)
    input_station_entry = Entry(top_frame, fg=fg_color, bg=bg_color, font=font_8)
    button = Button(master = top_frame, text = 'Toon tijden', command=station_departure_information, activeforeground=bg_color, activebackground=fg_color, bg=fg_color, fg=bg_color, font=font_8)

    # Layout of widgets top_frame
    input_label.grid(row = 0, column = 1)
    input_station_label.grid(row = 1, column = 0, padx = (15, 0))
    input_station_entry.grid(row = 1, column = 1, padx = (0, 15))
    button.grid(row = 1, column = 2, pady = (0, 5))

    # Definition of frames center and grid configuration center
    center.grid_rowconfigure(0, weight=1)
    center.grid_columnconfigure(1, weight=1)

    ctr_left = Frame(center, bg = fg_color, padx = 3, pady = 3)
    ctr_mid = Frame(center, bg = bg_color, padx = 3, pady = 3)

    # Layout of frames center
    ctr_left.grid(row = 0, column = 0, sticky = 'nsew')
    ctr_mid.grid(row = 0, column = 1, sticky = 'nsew')

    # Definition of widgets ctr_left
    possibilities_listbox = Listbox(ctr_left, height = 33, width = 40, fg=fg_color, bg=bg_color, font=('Consolas', 9, 'bold'),bd=10, highlightcolor=bg_color, selectforeground=bg_color, selectbackground=fg_color, activestyle='none')
    possibilities_listbox.bind('<<ListboxSelect>>', listbox_selection)

    # Layout of widgets ctr_left
    possibilities_listbox.grid(row = 0, column = 0)

    # Definition of widgets ctr_mid
    departure_time = Label(master = ctr_mid, bg = bg_color, fg = fg_color, font=font_9)
    ridenumber = Label(master = ctr_mid, bg = bg_color, fg = fg_color, font=font_9)
    destination = Label(master = ctr_mid, bg = bg_color, fg = fg_color, font=font_9)
    carrier = Label(master = ctr_mid, bg = bg_color, fg = fg_color, font=font_9)
    train_type = Label(master = ctr_mid, bg = bg_color, fg = fg_color, font=font_9)
    platform = Label(master = ctr_mid, bg = bg_color, fg = fg_color, font=font_9)
    route_text = Label(master = ctr_mid, bg = bg_color, fg = fg_color, font=font_9)
    travel_tip = Label(master = ctr_mid, bg = bg_color, fg = fg_color, font=font_9)
    comments = Label(master = ctr_mid, bg = bg_color, fg = fg_color, font=font_9)

    # Layout of widgets ctr_mid
    departure_time.place(x = 10, y = 10)
    ridenumber.place(x = 10, y = 30)
    destination.place(x = 10, y = 50)
    carrier.place(x = 10, y = 70)
    train_type.place(x = 10, y = 90)
    platform.place(x = 10, y = 110)
    route_text.place(x = 10, y = 130)
    travel_tip.place(x = 10, y = 150)
    comments.place(x = 10, y = 170)

    # Defenition of NS Pictures, Text and Copyright
    photo_top = Label(root,image=small_image, bg=bg_color)
    photo_bottom = Label(root,image=small_image, bg=bg_color, width=300, height=113)
    photo_top.image = small_image
    photo_bottom.image = small_image
    smalltop_text = Label(root, text='NS Stationsinformatie Interface', bg=bg_color, fg=fg_color, width = 30, height=1, font=font_8)
    copyright_text = Label(root, text='Copyright © 2017. All rights reserved', bg=bg_color, fg=fg_color, width = 50, height=1, font=font_8)

    # Layout of NS Pictures, Text and Copyright
    photo_top.place(x=1090,y=5)
    photo_bottom.place(x=4,y=600)
    smalltop_text.place(x=1040,y=49)
    copyright_text.place(x=500,y=690)

    #Back to menu button:
    backtomenu_button = Button(master = root, text = 'Terug naar het menu', bg=fg_color, fg=bg_color, font=font_10, command=load_mainmenu)
    backtomenu_button.place(x=600,y=650)

def load_reisadviesmenu():
    """"Destroys all of root's children and loads the reisadvies menu."""

    def travel_recommendation():
        """"Uses information_to_dict() to ask for travel recommendations from the NS API, and inserts the departure times from those recommendations into a listbox."""

        global travel_possibilities

        current_time = '{}-{}-{}T{}'.format(year_date_entry.get(), month_date_entry.get(), day_date_entry.get(), time_date_entry.get())
        try:
            travel_possibilities_dict = information_to_dict('ns-api-treinplanner?fromStation={}&viaStation={}&toStation={}&dateTime={}&Departure={}'.format(from_station_entry.get(), via_station_entry.get(), to_station_entry.get(), current_time, is_departure))
            travel_possibilities = [possibility for possibility in travel_possibilities_dict['ReisMogelijkheden']['ReisMogelijkheid']]
        except:
            return showerror(title='Foutmelding', message='Station bestaat niet of onjuiste tijd.')

        possibilities_listbox.delete(0, END)

        for possibility in travel_possibilities:
            possibilities_listbox.insert(END, '{:<20}{}-{}-{}'.format(possibility['ActueleVertrekTijd'][11:16], possibility['ActueleVertrekTijd'][8:10], possibility['ActueleVertrekTijd'][5:7], possibility['ActueleVertrekTijd'][0:4]))

    def times_listbox_selection(event):
        """"When triggered, saves the selected option of times_listbox."""

        global is_departure

        try:
            selection_index = int(times_listbox.curselection()[0])
        except:
            return

        selection_value = times_listbox.get(selection_index)
        if selection_value == 'Vertrek':
            is_departure = 'true'
        else:
            is_departure = 'false'

        if selection_index == 0:
            times_listbox.itemconfig(selection_index, bg=fg_color, fg=bg_color)
            times_listbox.itemconfig(1, bg=bg_color, fg=fg_color)
        else:
            times_listbox.itemconfig(selection_index, bg=fg_color, fg=bg_color)
            times_listbox.itemconfig(0, bg=bg_color, fg=fg_color)

    def possibilities_listbox_selection(event):
        """"Takes the event from the possibilities listbox and then replaces the information in the (empty) widgets in ctr_mid with the currently selected possibility's travel information."""

        try:
            selection_index = int(possibilities_listbox.curselection()[0])
        except IndexError:
            return

        possibilities_listbox.itemconfig(selection_index, bg=fg_color, fg=bg_color)

        for item_value in possibilities_listbox.get(0, END):
            item_index = possibilities_listbox.get(0, END).index(item_value)
            if item_index != selection_index:
                possibilities_listbox.itemconfig(item_index, bg=bg_color, fg=fg_color)

        for possibility in travel_possibilities:
            if travel_possibilities.index(possibility) == selection_index:
                if 'VertrekVertraging' in possibility:
                    departure_time = '{} {}'.format(possibility['ActueleVertrekTijd'][11:16],
                                                    possibility['VertrekVertraging'])
                else:
                    departure_time = possibility['ActueleVertrekTijd'][11:16]

                if 'AankomstVertraging' in possibility:
                    arrival_time = '{} {}'.format(possibility['ActueleAankomstTijd'][11:16],
                                                  possibility['AankomstVertraging'])
                else:
                    arrival_time = possibility['ActueleAankomstTijd'][11:16]

                departure_arrival_time_label['text'] = '{} <> {}'.format(departure_time, arrival_time)
                travel_time_label['text'] = 'Reistijd: {}'.format(possibility['ActueleReisTijd'])

                if possibility['AantalOverstappen'] == '0':
                    destroy_slaves(ctr_mid_travel_part)
                    too_many.place_forget()
                    part_maker(ctr_mid_travel_part, bg_color, fg_color, possibility['ReisDeel'], 0, None)

                else:
                    destroy_slaves(ctr_mid_travel_part)

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
                        part_maker(ctr_mid_travel_part, bg_color, fg_color, travel_part, column_number, part)
                        column_number += 1
                        part += 1

                notification_label_text(possibility, notification_label, fg_color)

    destroy_slaves(root)

    # Definition of frames
    top_frame = Frame(root, pady = 3, bg=bg_color)
    center = Frame(root, padx = 3, pady = 3, bg=fg_color)

    # Layout of frames
    top_frame.grid(row = 0, sticky = "ew")
    center.grid(row = 1, sticky = "nsew")

    # Definition of widgets top_frame
    from_station_label = Label(top_frame, text='Beginstation:', fg=fg_color, bg=bg_color, font=font_8)
    via_station_label = Label(top_frame, text='Via (optioneel):', fg=fg_color, bg=bg_color, font=font_8)
    to_station_label = Label(top_frame, text='Bestemming:', fg=fg_color, bg=bg_color, font=font_8)

    from_station_entry = Entry(top_frame, fg=fg_color, bg=bg_color, font=font_8)
    via_station_entry = Entry(top_frame, fg=fg_color, bg=bg_color, font=font_8)
    to_station_entry = Entry(top_frame, fg=fg_color, bg=bg_color, font=font_8)

    time_date_label= Label(top_frame, text='Tijd:', fg=fg_color, bg=bg_color, font=font_8)
    day_date_label = Label(top_frame, text='Dag:', fg=fg_color, bg=bg_color, font=font_8)
    month_date_label = Label(top_frame, text='Maand:', fg=fg_color, bg=bg_color, font=font_8)
    year_date_label = Label(top_frame, text='Jaar:', fg=fg_color, bg=bg_color, font=font_8)

    time_date_entry = Entry(top_frame, fg=fg_color, bg=bg_color, width=10, font=font_8)
    day_date_entry = Entry(top_frame, fg=fg_color, bg=bg_color, width=10, font=font_8)
    month_date_entry = Entry(top_frame, fg=fg_color, bg=bg_color, width=10, font=font_8)
    year_date_entry = Entry(top_frame, fg=fg_color, bg=bg_color, width=10, font=font_8)

    times_listbox = Listbox(top_frame, height = 2, fg=fg_color, bg=bg_color, font=font_9, bd=2, selectbackground=fg_color, selectforeground=bg_color, activestyle='none')
    times_listbox.insert(END, 'Vertrek')
    times_listbox.insert(END, 'Aankomst')
    times_listbox.bind('<<ListboxSelect>>', times_listbox_selection)
    times_listbox.select_set(0)

    button = Button(master = top_frame, text = 'Geef reismogelijkheden', command=travel_recommendation)
    button.configure(bg=fg_color, fg=bg_color, activeforeground=bg_color, activebackground=fg_color, font=font_8)

    # Layout widgets of top_frame
    from_station_label.grid(row = 1, column = 0, padx = (15, 0))
    via_station_label.grid(row = 2, column = 0)
    to_station_label.grid(row = 3, column = 0)
    from_station_entry.grid(row = 1, column = 1, padx = (0, 15))
    via_station_entry.grid(row = 2, column = 1, padx = (0, 15))
    to_station_entry.grid(row = 3, column = 1, padx = (0, 15))
    button.grid(row = 2, column = 7, padx = (20,0))

    time_date_label.grid(row = 1, column = 2)
    day_date_label.grid(row = 1, column=3)
    month_date_label.grid(row = 1, column=4)
    year_date_label.grid(row = 1, column=5)

    time_date_entry.grid(row = 2, column=2)
    day_date_entry.grid(row = 2, column=3, padx = (5, 0))
    month_date_entry.grid(row = 2, column=4, padx = (5, 0))
    year_date_entry.grid(row = 2, column=5, padx = (5, 0))

    times_listbox.grid(row = 2, column = 6, padx = (30,0))

    # Getting current time and selection ghosting
    times(time_date_entry, day_date_entry, month_date_entry, year_date_entry)
    times_listbox_selection(None)

    # Definition of frames center and grid configuration center
    center.grid_rowconfigure(0, weight=1)
    center.grid_columnconfigure(1, weight=1)

    ctr_left = Frame(center, bg = fg_color, padx = 3, pady = 3)
    ctr_mid = Frame(center, bg = bg_color, padx = 3, pady = 3)

    ctr_left.grid(row = 0, column = 0, sticky = 'nsew')
    ctr_mid.grid(row = 0, column = 1, sticky = 'nsew')

    # Definition of widgets ctr_left
    possibilities_listbox = Listbox(ctr_left, height = 30, fg=fg_color, bg=bg_color, font=font_9, bd=10, selectforeground=bg_color, selectbackground=fg_color, activestyle='none')
    possibilities_listbox.bind('<<ListboxSelect>>', possibilities_listbox_selection)

    # Layout  of widgets ctr_left
    possibilities_listbox.grid(row = 0, column = 0)

    # Definition widgets of ctr_mid
    ctr_mid_travel_part = Frame(ctr_mid, bg=bg_color)
    departure_arrival_time_label = Label(master=ctr_mid, bg=bg_color, fg=fg_color)
    travel_time_label = Label(master=ctr_mid, bg=bg_color, fg=fg_color)
    notification_label = Label(master=ctr_mid, bg=bg_color, fg=fg_color)
    too_many = Label(ctr_mid, text='Helaas worden meer dan 4 reisdelen niet ondersteund door deze applicatie.', bg=bg_color, fg=fg_color, font=('Helvetica', 18))

    # Layout of widgets ctr_mid
    ctr_mid_travel_part.pack(anchor = W, padx = (10, 0), pady = (100, 0))
    departure_arrival_time_label.place(x = 10, y = 10)
    travel_time_label.place(x = 10, y = 30)
    notification_label.place(x = 500, y = 10)

    # Definition of NS Pictures, Text and Copyright
    photo_top = Label(root, image=small_image, bg=bg_color)
    photo_top.image = small_image
    smalltop_label = Label(root, text='NS Reisadvies Interface', bg=bg_color, fg=fg_color, width=30, height=1, font=font_8)
    photo_bottom = Label(root, image=small_image, bg=bg_color, width=160, height=115)
    photo_bottom.image = small_image
    copyright_label = Label(root, text='Copyright © 2017. All rights reserved', bg=bg_color, fg=fg_color, width=50, height=1, font=font_8)

    # Layout of of NS Pictures, Text and Copyright
    photo_top.place(x=1090, y=5)
    smalltop_label.place(x=1040, y=49)
    photo_bottom.place(x=4, y=597)
    copyright_label.place(x=500, y=690)

    #Back to menu button:
    backtomenu_button = Button(master = root, text = 'Terug naar het menu', bg=fg_color, fg=bg_color, font=("Helvetica", 10, "bold"), command=load_mainmenu)
    backtomenu_button.place(x=600,y=650)

# Declaration of initial objects
bg_color = "#FFCC20"
fg_color = "#000066"

# Declaration of fonts
font_8 = ('Helvetica', 8, 'bold')
font_9 = ('Helvetica', 9, 'bold')
font_10 = ('Helvetica', 10, 'bold')
font_20 = ('Helvetica', 20, 'bold')

# Default root layout
root = Tk()
root.title('Project Programming')
root.geometry('{}x{}'.format(1280, 720))
root.resizable(width=False, height=False)
root.configure(bg=bg_color)
root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)

# Declaration of image objects
small_image = PhotoImage(file="ns_small.png")
large_image = PhotoImage(file="ns.png")

load_mainmenu()

root.mainloop()