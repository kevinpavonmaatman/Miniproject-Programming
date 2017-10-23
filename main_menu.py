from functions import *
from tkinter.messagebox import showerror

def station_departure_information():
    global departures
    try:
        departures_dict = information_to_dict('ns-api-avt?station={}'.format(input_station_entry.get()))
        departures = [departure for departure in departures_dict['ActueleVertrekTijden']['VertrekkendeTrein']]

    except:
        showerror(title='Foutmelding', message='Station niet gevonden. Probeer het opnieuw')

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
                departure_time['text'] = '{}: {} {}'.format(('Vetrektijd'), departure['VertrekTijd'][11:16], departure['VertrekVertragingTekst'])
            else:
                departure_time['text'] = ('Vetrektijd:',departure['VertrekTijd'][11:16])

            ridenumber['text'] = ('{}: {}'.format(('Ritnummer'), departure['RitNummer']))
            destination['text'] = ('{}: {}'.format('Eindbestemming',departure['EindBestemming']))
            carrier['text'] = ('{}: {}'.format('Vervoerder',departure['Vervoerder']))
            train_type['text'] = '{}: {}'.format(('Type Trein'),departure['TreinSoort'])
            platform['text'] = ''

            if departure['VertrekSpoor']['@wijziging'] == 'true':
                platform['text'] = ('{}: {}'.format(('Vertrekspoor'),departure['VertrekSpoor']['#text'] + ' (wijziging)'))
            else:
                if '#text' in departure['VertrekSpoor']:
                    platform['text'] = ('Vertrekspoor:',departure['VertrekSpoor']['#text'])
                else:
                    platform['text'] = '-'
            if 'RouteTekst' in departure:
                route_text['text'] = ('{}: {}'.format('Tussenhaltes',departure['RouteTekst']))
            else:
                route_text['text'] = ''
            if 'ReisTip' in departure:
                travel_tip['text'] = ('{}: {}'.format('Reistip',departure['ReisTip']))
            else:
                travel_tip['text'] = ''
            if 'Comments' in departure:
                comments['text'] = ('Mededelingen:',departure['Comments'])
            else:
                comments['text'] = ''
            comments['text'] = ''

def load_mainmenu(event):

    #Loading global frames
    global top_frame
    global buttons_frame
    global footer_frame

    #Removal of previous frames.
    buttons_frame.destroy()
    top_frame.destroy()
    footer_frame.destroy()
    center.destroy()
    root.geometry('{}x{}'.format(800, 400))


    #Definition of Frames
    top_frame = Frame(root, width=200, height=50, pady=3, bg=bg_color)
    buttons_frame = Frame(root, width=200, height=50, bg=bg_color)
    footer_frame = Frame(root, width=200, height=50, bg=bg_color)

    #Position of New Frames
    top_frame.grid(row=0)
    buttons_frame.grid(row=1)
    footer_frame.grid(row=2)

    #Information in top_frame:
    title = Label(top_frame, text='NS Main Menu Interface')
    title.configure(bg=bg_color, fg=fg_color, width = 40, height=1, font=("Helvetica", 25, "bold"))
    img = PhotoImage(file="ns.png")
    foto = Label(top_frame,image=img, bg=bg_color)
    foto.image = (img)
    welcometext = Label(top_frame, text='Welkom bij de NS Reisadvies applicatie \n Maak een keuze door te klikken op één van de onderstaande knoppen')
    welcometext.configure(bg=bg_color, fg=fg_color, width = 100, height=2, font=("Helvetica", 10, "bold"))

    #Position of objects in top_frame
    title.grid(row=0)
    foto.grid(row=1)
    welcometext.grid(row=2)

    #Information in buttons_frame:
    reisinfo_button = Button(master = buttons_frame, text = 'Reisinformatie', bg=fg_color, fg=bg_color, font=("Helvetica", 20, "bold"))
    reisinfo_button.grid(row=0,column=0,padx=50)
    reisadvies_button = Button(master = buttons_frame, text = 'Reisadvies', bg=fg_color, fg=bg_color, font=("Helvetica", 20, "bold"))
    reisadvies_button.grid(row=0,column=1, padx=20)

    #Information in footer_frame
    copyright_text = Label(footer_frame, text='Copyright © 2017. All rights reserved')
    copyright_text.configure(bg=bg_color, fg=fg_color, width = 50, height=5, font=("Helvetica", 8, "bold"))
    exit_button = Button(master = footer_frame, text = 'Afsluiten')
    exit_button.configure(bg=fg_color, fg=bg_color, font=("Helvetica", 8, "bold"))
    copyright_text.grid(row=0)
    exit_button.grid(row=1)

    #Button Bindings
    reisinfo_button.bind("<Button-1>", load_reisinfomenu)
    reisadvies_button.bind("<Button-1>", load_reisadviesmenu)
    exit_button.bind("<Button-1>", exit)

def load_reisinfomenu(event):

    #Loading global variables
    global top_frame
    global buttons_frame
    global footer_frame
    global center
    global possibilities_listbox
    global input_station_entry
    global departure_time
    global ridenumber
    global destination
    global carrier
    global train_type
    global platform
    global route_text
    global travel_tip
    global comments

    #Removal of previous frames.
    buttons_frame.destroy()
    top_frame.destroy()
    footer_frame.destroy()

    root.geometry('{}x{}'.format(1280, 720))
    # create all of the main containers
    top_frame = Frame(root, pady = 3,bg=bg_color)
    center = Frame(root, padx = 3, pady = 3, bg=fg_color)

    # layout main containers
    root.grid_rowconfigure(1, weight = 1)
    root.grid_columnconfigure(0, weight = 1)

    top_frame.grid(row = 0, sticky = "ew")
    center.grid(row = 1, sticky = "nsew")

    # create widgets top frame
    invoer_label = Label(top_frame, text='Vul uw gegevens in',fg=fg_color, bg=bg_color, font=("Helvetica", 10, "bold"),bd=10)
    input_label = Label(top_frame, text='Station:',fg=fg_color, bg=bg_color, font=("Helvetica", 8, "bold"))
    input_station_entry = Entry(top_frame, fg=fg_color, bg=bg_color, font=("Helvetica", 8, "bold"))
    button = Button(master = top_frame, text = 'Toon tijden', command=station_departure_information, activeforeground=bg_color, activebackground=fg_color, bg=fg_color, fg=bg_color, font=("Helvetica", 8, "bold"))

    # layout widgets of top frame
    invoer_label.grid(row = 0, column = 1)
    input_label.grid(row = 1, column = 0, padx = (15, 0))
    input_station_entry.grid(row = 1, column = 1, padx = (0, 15))
    button.grid(row = 1, column = 2, pady = (0, 5))

    # create widgets center
    center.grid_rowconfigure(0, weight=1)
    center.grid_columnconfigure(1, weight=1)

    ctr_left = Frame(center, bg = fg_color, padx = 3, pady = 3)
    ctr_mid = Frame(center, bg = bg_color, padx = 3, pady = 3)

    ctr_left.grid(row = 0, column = 0, sticky = 'nsew')
    ctr_mid.grid(row = 0, column = 1, sticky = 'nsew')

    # layout widgets ctr_mid
    departure_time = Label(master = ctr_mid, text = '', bg = bg_color, fg = fg_color, font=("Helvetica", 9, "bold"))
    ridenumber = Label(master = ctr_mid, text = '', bg = bg_color, fg = fg_color, font=("Helvetica", 9, "bold"))
    destination = Label(master = ctr_mid, text = '', bg = bg_color, fg = fg_color, font=("Helvetica", 9, "bold"))
    carrier = Label(master = ctr_mid, text = '', bg = bg_color, fg = fg_color, font=("Helvetica", 9, "bold"))
    train_type = Label(master = ctr_mid, text = '', bg = bg_color, fg = fg_color, font=("Helvetica", 9, "bold"))
    platform = Label(master = ctr_mid, text = '', bg = bg_color, fg = fg_color, font=("Helvetica", 9, "bold"))
    route_text = Label(master = ctr_mid, text = '', bg = bg_color, fg = fg_color, font=("Helvetica", 9, "bold"))
    travel_tip = Label(master = ctr_mid, text = '', bg = bg_color, fg = fg_color, font=("Helvetica", 9, "bold"))
    comments = Label(master = ctr_mid, text = '', bg = bg_color, fg = fg_color, font=("Helvetica", 9, "bold"))

    # layout widgets ctr_left
    possibilities_listbox = Listbox(ctr_left, height = 33, width = 40)
    possibilities_listbox.grid(row = 0, column = 0)
    possibilities_listbox.bind('<<ListboxSelect>>', listbox_selection)
    possibilities_listbox.configure(fg=fg_color, bg=bg_color, font=("Consolas", 9, "bold"),bd=10, highlightcolor=bg_color, selectforeground=bg_color, selectbackground=fg_color, activestyle="none")

    # layout widgets ctr_mid
    departure_time.place(x = 10, y = 10)
    ridenumber.place(x = 10, y = 30)
    destination.place(x = 10, y = 50)
    carrier.place(x = 10, y = 70)
    train_type.place(x = 10, y = 90)
    platform.place(x = 10, y = 110)
    route_text.place(x = 10, y = 130)
    travel_tip.place(x = 10, y = 150)
    comments.place(x = 10, y = 170)

    #Position of NS Pictures, Text and Copyright
    img = PhotoImage(file="ns_small.png")
    foto_top = Label(root,image=img, bg=bg_color)
    foto_bottom = Label(root,image=img, bg=bg_color, width=300, height=113)
    foto_top.image = (img)
    foto_top.place(x=700,y=10)
    foto_bottom.image = (img)
    foto_bottom.place(x=4,y=600)
    smalltop_text = Label(root, text='NS Stationsinformatie Interface')
    smalltop_text.configure(bg=bg_color, fg=fg_color, width = 30, height=1, font=("Helvetica", 8, "bold"))
    smalltop_text.place(x=650,y=54)
    copyright_text = Label(root, text='Copyright © 2017. All rights reserved')
    copyright_text.configure(bg=bg_color, fg=fg_color, width = 50, height=1, font=("Helvetica", 8, "bold"))
    copyright_text.place(x=500,y=690)

    #Back to menu button:
    backtomenu_button = Button(master = root, text = 'Terug naar het menu', bg=fg_color, fg=bg_color, font=("Helvetica", 10, "bold"))
    backtomenu_button.place(x=600,y=650)
    backtomenu_button.bind("<Button-1>", load_mainmenu)

def load_reisadviesmenu(event):

    #Loading global frames
    global top_frame
    global buttons_frame
    global footer_frame
    #Removal of previous frames.
    buttons_frame.destroy()
    top_frame.destroy()
    footer_frame.destroy()

    #Definition of Frames
    top_frame = Frame(root, width=200, height=50, pady=3, bg=bg_color)
    buttons_frame = Frame(root, width=200, height=50, bg=bg_color)
    footer_frame = Frame(root, width=200, height=50, bg=bg_color)

    #Position of Frames
    top_frame.grid(row=0)
    buttons_frame.grid(row=1)
    footer_frame.grid(row=2)

    #Information in top_frame:
    title = Label(top_frame, text='NS Reisadvies Interface')
    title.configure(bg=bg_color, fg=fg_color, width = 40, height=1, font=("Helvetica", 25, "bold"))
    title.grid(row=0)
    img = PhotoImage(file="ns.png")
    foto = Label(top_frame,image=img, bg=bg_color)
    foto.image = (img)
    foto.grid(row=1)

    #Information in buttons_frame:
    backtomenu_button = Button(master = buttons_frame, text = 'Terug naar het menu', bg=fg_color, fg=bg_color, font=("Helvetica", 10, "bold"))
    backtomenu_button.grid(row=0,column=0,padx=50)

    #Information in footer_frame
    copyright_text = Label(footer_frame, text='Copyright © 2017. All rights reserved')
    copyright_text.configure(bg=bg_color, fg=fg_color, width = 50, height=5, font=("Helvetica", 8, "bold"))
    copyright_text.grid(row=0)
    exit_button = Button(master = footer_frame, text = 'Afsluiten', bg=fg_color, fg=bg_color, font=("Helvetica", 8, "bold"))
    exit_button.grid(row=1)


    #Button Bindings
    exit_button.bind("<Button-1>", exit)
    backtomenu_button.bind("<Button-1>", load_mainmenu)

#Initialization of Tkinter root and color configuration.
root = Tk()
root.title('Project Progamming')
root.geometry('{}x{}'.format(800, 400))
root.resizable(width=False, height=False)
bg_color = "#FFCC20"
fg_color = "#000066"
root.configure(bg=bg_color)
root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)

#Definition of Frames
top_frame = Frame(root, width=200, height=50, pady=3, bg=bg_color)
buttons_frame = Frame(root, width=200, height=50, bg=bg_color)
footer_frame = Frame(root, width=200, height=50, bg=bg_color)

#Position of Frames
top_frame.grid(row=0)
buttons_frame.grid(row=1)
footer_frame.grid(row=2)

#Information in top_frame:
title = Label(top_frame, text='NS Main Menu Interface')
title.configure(bg=bg_color, fg=fg_color, width = 40, height=1, font=("Helvetica", 25, "bold"))
img = PhotoImage(file="ns.png")
foto = Label(top_frame,image=img, bg=bg_color)
foto.image = (img)
welcometext = Label(top_frame, text='Welkom bij de NS Reisadvies applicatie \n Maak een keuze door te klikken op één van de onderstaande knoppen')
welcometext.configure(bg=bg_color, fg=fg_color, width = 100, height=2, font=("Helvetica", 10, "bold"))

#Position of objects in top_frame
title.grid(row=0)
foto.grid(row=1)
welcometext.grid(row=2)

#Information in buttons_frame:
reisinfo_button = Button(master = buttons_frame, text = 'Reisinformatie', bg=fg_color, fg=bg_color, font=("Helvetica", 20, "bold"))
reisinfo_button.grid(row=0,column=0,padx=50)
reisadvies_button = Button(master = buttons_frame, text = 'Reisadvies', bg=fg_color, fg=bg_color, font=("Helvetica", 20, "bold"))
reisadvies_button.grid(row=0,column=1, padx=20)

# #Information in footer_frame
copyright_text = Label(footer_frame, text='Copyright © 2017. All rights reserved')
copyright_text.configure(bg=bg_color, fg=fg_color, width = 50, height=5, font=("Helvetica", 8, "bold"))
copyright_text.grid(row=0)
exit_button = Button(master = footer_frame, text = 'Afsluiten', bg=fg_color, fg=bg_color, font=("Helvetica", 8, "bold"))
exit_button.grid(row=1)

#Button Bindings
reisinfo_button.bind("<Button-1>", load_reisinfomenu)
reisadvies_button.bind("<Button-1>", load_reisadviesmenu)
exit_button.bind("<Button-1>", exit)

#Execute
root.mainloop()
