from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from datetime import datetime
from work_info import work

import os.path
import csv
import datetime
import sys
import time


check_path = r'text'

if not os.path.exists(check_path):
    os.makedirs(check_path)
else:
    pass

if os.path.isfile("text\congviec.txt") and os.path.isfile("text\cong_viec_da_sap_xep.txt"):
    pass
else:
    f = open("text\congviec.txt",'w+')
    f_2 = open("text\cong_viec_da_sap_xep.txt", 'w+')
    f.close()
    f_2.close()

splash_screen = Tk()
# splash_screen.geometry('750x250')

bg = PhotoImage(file = "image\welcome.png")

splash_screen_lbl = Label(splash_screen, image = bg)
splash_screen_lbl.place(x = 0, y = 0, relwidth = 1, relheight = 1)

# Center splash window on screen
app_width = 750
app_height = 250

monitor_width = splash_screen.winfo_screenwidth()
monitor_height = splash_screen.winfo_screenheight()

position_y = (monitor_height//2) - (app_height//2)
position_x = (monitor_width//2) - (app_width//2)

splash_screen.overrideredirect(True)
splash_screen.geometry(f'{app_width}x{app_height}+{position_x}+{position_y}')

# MAIN WINDOW
def main_window():
    splash_screen.destroy()

    root = Tk()

    # Title_name & icon
    root.title("Time_Management")
    root.iconbitmap('icon\logo_time.ico')

    # Window_size
    app_width_main = 710
    app_height_main = 180

    monitor_width = root.winfo_screenwidth()
    monitor_height = root.winfo_screenheight()

    position_y_main = (monitor_height//2) - (app_height//2)
    position_x_main = (monitor_width//2) - (app_width//2)

    root.geometry(f'{app_width_main}x{app_height_main}+{position_x}+{position_y}')

    #root.geometry("710x180+300+300")

    # Remove_Maximize_Window_Button
    root.resizable(0, 0)

    # No windows manager decoration
    #frame_1.overrideredirect(1)

    # define_time_day_location
    global time_info
    def time_info():
        #while True:
        current_time = time.strftime('%H:%M:%S %p')
        lbl.config(text = current_time)
        current_name_day = time.strftime('%A')
        current_year = time.strftime('%d %B %Y')
        name_day_label.config(text = current_name_day)
        year_label.config(text = current_year)
        current_tz = time.strftime('(GMT %z)')
        tz_label.config(text = current_tz)
        frame_1.after(1000, time_info)

    # Tab control
    tab_control = ttk.Notebook(root)
    tab_control.pack()

    # Frame
    frame_1 = Frame(tab_control, width = 788, height = 1000, bg = '#151a1d')
    frame_2 = Frame(tab_control, width = 788, height = 1000, bg = '#151a1d')

    frame_1.pack(fill = 'both', expand = 1)
    frame_2.pack(fill = 'both', expand = 1)

    tab_control.add(frame_1, text = 'Digital Clock')
    tab_control.add(frame_2, text = 'Configuration')


    # title_current_time
    title_time = Label(frame_1, text = 'YOUR CURRENT TIME', font = ('Calibri', 20, 'italic'), bg = '#151a1d' , fg = 'white')
    title_time.place(x = 290, y = 20)

    # digital_time_appearance
    lbl = Label(frame_1, font = ('Calibri', 60), bg = '#151a1d' , fg = 'white')
    lbl.place(x = 260, y = 50)

    # DEFINE_DAYS_YEARS, ETC
    name_day_label = Label(frame_1, font = ('Calibri', 30), bg = '#151a1d', fg = 'white')
    name_day_label.place(x = 30, y = 10)

    year_label = Label(frame_1, font = ('Calibri', 18), bg = '#151a1d', fg = 'white')
    year_label.place(x = 30, y = 60)

    tz_label = Label(frame_1, font = ('Calibri', 20, 'italic'), bg = '#151a1d', fg = 'white')
    tz_label.place(x = 540, y = 20)
    #tz_label_info = Label(frame_1, font = ('Calibri', 20), bg = '#151a1d', fg = 'white')
    #tz_label_info.place()

    # Always on top others windows
    sign = IntVar()

    # DEFINE CONFIGURATION
    def check_top_wd():
        if (sign.get() == 1):
            root.wm_attributes('-topmost', 1)
        else:
            root.wm_attributes('-topmost', 0)

    config_lbl = Label(frame_2, text = 'Confi')
    Al_Check_Box = Checkbutton(frame_2, text = "Always on top", font = ('Calibri', 13), variable = sign, onvalue = 1, offvalue = 0, command = check_top_wd)
    Al_Check_Box.place(x = 50, y = 30)

    #Open_2nd_Window = Button(frame_2, text = 'Set alarm list', font = ('Calibri', 13), command = new_Window)
    #Open_2nd_Window.place(x = 600, y = 30)

    #Open_3rd_Window = Button(frame_2, text = 'Quick note', font = ('Calibri', 13), command = Third_WD)
    #Open_3rd_Window.place(x = 600, y = 90)

    def expand_func():
        Message_label.config(text = 'Please set schedule!!!')
        frame_3.config(width = 270, height = 60)
        contract_bttn.place(x = 40, y = 105)
        hide_Alarm.place(x = 50, y = 80)
        root.geometry('710x766')
        expand_bttn.place_forget()
        set_Alarm.place_forget()

    def contract_func():
        contract_bttn.place_forget()
        hide_Alarm.place_forget()
        set_Alarm.place(x = 50, y = 80)
        expand_bttn.place(x = 40, y = 105)
        root.geometry("710x180")

    # DEFINE EXPAND + SHRINK WINDOW SIZE BUTTON
    expand_bttn = Button(frame_1, text = 'Set quick note', font = ('Calibri', 13), command = expand_func)
    expand_bttn.place(x = 40, y = 105)

    contract_bttn = Button(frame_1, text = 'Hide quick note', font = ('Calibri', 13), command = contract_func)
    contract_bttn.place_forget()

    # DEFINE QUICK NOTE WRITE DOWN FUNCTION
    Title_lbl = Label(frame_1, text = 'Note', font = ('Calibri', 30, 'italic', 'bold'), bg = '#151a1d', fg = 'white')
    Title_lbl.place(x = 50, y = 200)

    # FRAME 1
    list_content = []
    list_title = []
    temp_list = []

    # FRAME 2
    works = []
    works_temp = []
    
    schedule_temp_list = []

    # SHOW SELECTED NOTE
    #def redo():
    #    root.geometry('710x650')
    #    hd_bttn.place_forget()
    #    search_bttn.place(x = 30, y = 550)
    #    search_entry.place_forget()
    #    search_lbl.place_forget()
    #    hide_bttn_2.place_forget()

    def show_note():
        for i in listbox.curselection():
            title_note.config(text = listbox.get(i))
            content_note.config(text = list_content[i])       
            #hd_bttn.place(x = 615, y = 550)

    # Search Algorithm - Giai thuat tim kiem
    def show_note_aftersort():
        for i in listbox.curselection():
            title_note.config(text = listbox.get(i))
            repeate_title = range(0, len(list_title), 1)
            repeate_content = range(0, len(list_content), 1)
            for index in repeate_title:
                if list_title[index] == listbox.get(i):
                    for jindex in repeate_content:
                        if index == jindex:
                            content_note.config(text = list_content[jindex])
                            break     
            #hd_bttn.place(x = 615, y = 550)

    # Search Algorithm - Giai thuat tim kiem
    def check_list(list, txt):

        if title.get() in list_title:
            alert_lbl.config(text = 'Note has already been set!!')
        else:
            last_place = listbox.size()
            listbox.insert(END, title.get())
            #list_content.append(content.get())
            get_value(txt)
            list_title.append(listbox.get(last_place))
            title_entry.delete(0, 'end')
            alert_lbl.config(text = 'Set note!!!')

    #def search():
    #    repeat_list = range(0, len(list_title), 1)
    #    for i in repeat_list:
    #        if list_title[i] == title.get():
    #            show_note()
    #            break

    ttl_lbl = Label(frame_1, text = 'Title:', font = ('Calibri', 22, 'bold'), bg = '#151a1d', fg = 'white')
    ctnt_lbl = Label(frame_1, text = 'Text:', font = ('Calibri', 22, 'bold'), bg = '#151a1d', fg = 'white')
    ttl_lbl.place(x = 250, y = 625)        
    ctnt_lbl.place(x = 250, y = 670) 
    #hd_bttn = Button(frame_1, text = '^', font = ('Calibri', 17), command = redo)

    title_note = Label(frame_1, font = ('Calibri', 17), bg = '#151a1d', fg = 'white')
    title_note.place(x = 320, y = 631)
    content_note = Label(frame_1, font = ('Calibri', 17), bg = '#151a1d', fg = 'white')
    content_note.place(x = 320, y = 676)

    # DEFINE ELEMENTS OF NOTE
    title = StringVar()
    #content = StringVar()

    Lbl_title = Label(frame_1, text = 'Title', font = ('Calibri', 30,), bg = '#151a1d', fg = 'white')
    Lbl_title.place(x = 250, y = 235)

    title_entry = Entry(frame_1, textvariable = title, font = ('Calibri', 17), width = 25)
    title_entry.place(x = 250, y = 290)

    Lbl_content = Label(frame_1, text = 'Text', font = ('Calibri', 30,), bg = '#151a1d', fg = 'white')
    Lbl_content.place(x = 250, y = 326)

    #Content_entry = Entry(frame_1, textvariable = content, font = ('Calibri', 17))
    #Content_entry.place(x = 250, y = 380)

    def get_value(value):
        v = value.get('1.0', 'end-1c')
        list_content.append(v)
        txt.delete('1.0', END)

    def check_empty_content(txt):
        x = txt.get('1.0', 'end-1c')
        return x

    txt = Text(frame_1, height = 4, width = 25, font = ('Calibri', 17))
    txt.place(x = 250, y = 380)

    # DEFINE INSERT NOTE FUNCTION
    def insert_item():
        if search_entry.get() != '':
            messagebox.showinfo('Reminder', 'Clear search box first please!!!')
            #alert_lbl.config(text = 'Clear search box first please!!!')
        elif check_empty_content(txt) == '' and title.get() == '':
            messagebox.showinfo('Reminder', "Please write title and text!!!")
            #alert_lbl.config(text = "Please write title and text!!!")
        elif check_empty_content(txt) == '':
            alert_lbl.config(text = 'Please write your text!')
        elif title.get() == "":
            alert_lbl.config(text = "Set the title!!!")
        else:
            check_list(list_title, txt)

    def deletelist():
        Del_bttn.place(x = 395, y = 550)
        Del_bttn_afsort.place_forget()
        listbox.delete(0, END)
        list_title.clear()
        list_content.clear()
        temp_list.clear()

    # DEFINE ELEMENTS OF WRITE DOWN NOTE FUNCTION
    # Search Algorithm - Giai thuat tim kiem
    def delete_selected():
        for i in listbox.curselection():
            repeat_title = range(0, len(list_title), 1)
            for i_index in repeat_title:
                if list_title[i_index] == listbox.get(i):
                    list_title.remove(listbox.get(i))
                    list_content.remove(list_content[i_index])
                    listbox.delete(ANCHOR)
                    break

    # DELETE SELECTED AFTER SORT BUTTON BEING PRESSED
    # Search Algorithm - Giai thuat tim kiem
    def delete_selected_aftersort():
        content_2 = []

        for i in range(0, len(temp_list), 1):
            content_2.append(temp_list[i])
        
        #print(temp_list)
        #print(list_title)
        for i in listbox.curselection():
            #print(listbox.get(i))
            for temp_index in range(0, len(temp_list), 1):
                # compare len(content_2) vs len(temp_list)
                if len(content_2) == len(temp_list):
                    if temp_list[temp_index] == listbox.get(i):
                        for i_index in range(0, len(list_title), 1):

                            if len(content_2) == len(list_title):
                                if temp_list[temp_index] == list_title[i_index]:
                                    for j_index in range(0, len(list_content), 1):
                                        if j_index == i_index:
                                            list_title.remove(listbox.get(i))
                                            temp_list.remove(listbox.get(i))
                                            list_content.remove(list_content[j_index])
                                            listbox.delete(ANCHOR)
                                            break
                            else:
                                content_2.clear()
                                break
                else:
                    content_2.clear()
                    break

    global alert_lbl
    alert_lbl = Label(frame_1, text = 'Please set your note', font = ('Calibri', 18, 'bold'), bg ='#151a1d', fg = 'white')
    alert_lbl.place(x = 250, y = 500)

    bttn = Button(frame_1, text = 'Add', font = ('Calibri', 17), command = insert_item)
    bttn.place(x = 250, y = 550)

    Del_bttn = Button(frame_1, text = 'Delete', font = ('Calibri', 17), command = delete_selected)
    Del_bttn.place(x = 395, y = 550)

    Del_bttn_afsort = Button(frame_1, text = 'Delete', font = ('Calibri', 17), command = delete_selected_aftersort)

    Del_list_bttn = Button(frame_1, text = 'Delete List', font = ('Calibri', 17), command = deletelist)
    Del_list_bttn.place(x = 485, y = 550)

    listbox = Listbox(frame_1, font = ('Calibri', 15, 'bold'), height = 11)
    listbox.place(x = 30, y = 250)

    # DEFINE UPDATE SEARCH FUNCTION
    def update_title(data, typed):
        listbox.delete(0, END)    

        for item in data:
            listbox.insert(END, item)
        
        # Search Algorithm - Giai thuat tim kiem
        if typed != '':
            showbttn_ex.place(x = 315, y = 550)
            showbttn.place_forget()
            for i in listbox.curselection():
                if list_title[i] == listbox.get(i):
                    content.append(list_content[i])                
        else:
            showbttn.place(x = 315, y = 550)
            showbttn_ex.place_forget()

    # Search Algorithm - Giai thuat tim kiem (muon phan tich cung dc, tai cai nay ko quan trong)
    def expand_show_note_ex():
        for i in listbox.curselection():
            title_note.config(text = listbox.get(i))
            content_note.config(text = content[i])
            
    def check_search(event):
        typed = search_entry.get()
        global content

        if typed == '':
            Del_bttn.config(state = ACTIVE)
            Del_bttn_afsort.config(state = ACTIVE)
            data = list_title
            content = list_content
        else:
            # Search Algorithm - Giai thuat tim kiem
            Del_bttn.config(state = DISABLED)
            Del_bttn_afsort.config(state = DISABLED)
            data = []       
            content = []
            repeat_content = range(0, len(list_content), 1)
            repeat_title = range(0, len(list_title), 1)
            for item in repeat_title:
                if typed.lower() in list_title[item].lower():
                    data.append(list_title[item])
                    for index in repeat_content:
                        if index == item:
                            content.append(list_content[index])

        # update listbox with selected data
        update_title(data, typed)

    # EXPAND/ CONTRACT FUNCTION FOR SHOW BUTTON
    search_data = StringVar()

    def expand_show():
            # before adding another line to break program
        if not list_title:
            messagebox.showinfo('Reminder', "There's nothing to show!!!")
        
        elif list_content and list_title:
            root.geometry('710x766')
            show_note()

    def expand_show_aftersort():
        if list_content and list_title:
            root.geometry('710x766')
            show_note_aftersort()

    def search_expand():
        if '710x650' in root.winfo_geometry():
            search_bttn.place_forget()
            hide_bttn.place(x = 30, y = 550)
            root.geometry('710x765')
            search_lbl.place(x = 40, y = 615)
            search_entry.place(x = 30, y = 650)        
        else:
            search_bttn.place_forget()
            hide_bttn_2.place(x = 30, y = 550)
            search_lbl.place(x = 40, y = 615)
            search_entry.place(x = 30, y = 650)

    def hide_search():
        search_bttn.place(x = 30, y = 550)
        search_entry.place_forget()
        search_lbl.place_forget()
        hide_bttn.place_forget()
        root.geometry("710x650")

    def hid_search_2():
        search_bttn.place(x = 30, y = 550)
        hide_bttn_2.place_forget()
        hide_bttn.place_forget()
        search_lbl.place_forget()
        search_entry.place_forget()        

    # Search Algorithm - Giai thuat tim kiem ( 3 ham sort_demo(), sort_dec(), sort_inc() )
    def sort_demo():
        temp_list.clear()
        for i in range(0, listbox.size()):
            temp_list.append(listbox.get(i))

        listbox.delete(0, END)

        mergesort(temp_list)
        for i in range(0, len(temp_list), 1):
            listbox.insert(END, temp_list[i])
        
        temp_list.clear()

        for i in range(0, len(list_title), 1):
            temp_list.append(list_title[i])
        mergesort(temp_list)
        sort_button.place_forget()
        sort_bttn_dec.place(x = 120, y = 550)
        show_bttn_ex_2.place(x = 315, y = 550)
        Del_bttn.place_forget()
        Del_bttn_afsort.place(x = 395, y = 550)

    def sort_dec():
        temp_list.clear()
        for i in range(0, listbox.size()):
            temp_list.append(listbox.get(i))

        listbox.delete(0, END)

        mergesort_dec(temp_list)
        for i in range(0, len(temp_list), 1):
            listbox.insert(END, temp_list[i])

        temp_list.clear()

        for i in range(0, len(list_title), 1):
            temp_list.append(list_title[i])
        mergesort_dec(temp_list)
        sort_button.place_forget()
        sort_bttn_inc.place(x = 120, y = 550)
        sort_bttn_dec.place_forget()
        show_bttn_ex_2.place_forget()
        show_bttn_ex_2.place(x = 315, y = 550)
        Del_bttn.place_forget()
        Del_bttn_afsort.place(x = 395, y = 550)

    def sort_inc():
        temp_list.clear()
        for i in range(0, listbox.size()):
            temp_list.append(listbox.get(i))

        listbox.delete(0, END)

        mergesort(temp_list)
        for i in range(0, len(temp_list), 1):
            listbox.insert(END, temp_list[i])
        
        temp_list.clear()

        for i in range(0, len(list_title), 1):
            temp_list.append(list_title[i])
        mergesort(temp_list)
        sort_button.place_forget()
        sort_bttn_inc.place_forget()
        sort_bttn_dec.place(x = 120, y = 550)
        show_bttn_ex_2.place_forget()
        show_bttn_ex_2.place(x = 315, y = 550)
        Del_bttn.place_forget()
        Del_bttn_afsort.place(x = 395, y = 550)

    # IMPLENTMENT ALGORITHM - Giai thuat sap xep - Merge Sort
    def mergesort(templist_size):
        if len(templist_size) > 1 :
            mid = len(templist_size)//2
            left_side = templist_size[:mid]
            right_side = templist_size[mid:]
            mergesort(left_side)
            mergesort(right_side)
            i = 0
            j = 0
            k = 0
            while i < len(left_side) and j < len(right_side) :
                if left_side[i].lower() < right_side[j].lower() :
                    templist_size[k] = left_side[i]
                    i += 1
                else :
                    templist_size[k] = right_side[j]
                    j += 1
                k += 1
            while i < len(left_side) :
                templist_size[k] = left_side[i]
                k += 1
                i += 1
            while j < len(right_side) :
                templist_size[k] = right_side[j]
                k += 1
                j += 1

    def mergesort_dec(templist_size):
        if len(templist_size) > 1 :
            mid = len(templist_size)//2
            left_side = templist_size[:mid]
            right_side = templist_size[mid:]
            mergesort_dec(left_side)
            mergesort_dec(right_side)
            i = 0
            j = 0
            k = 0
            while i < len(left_side) and j < len(right_side) :
                if left_side[i].lower() > right_side[j].lower() :
                    templist_size[k] = left_side[i]
                    i += 1
                else :
                    templist_size[k] = right_side[j]
                    j += 1
                k += 1
            while i < len(left_side) :
                templist_size[k] = left_side[i]
                k += 1
                i += 1
            while j < len(right_side) :
                templist_size[k] = right_side[j]
                k += 1
                j += 1

    #def refresh_time():
    #    global time_info
    #    del time_info
    #    time_info_2()

    search_lbl = Label(frame_1, text = 'Search:', font = ('Calibri', 15, 'bold'), bg = '#151a1d', fg = 'white')
    search_entry = Entry(frame_1, textvariable = search_data, font = ('Calibri', 15, 'bold'), width = 20)
    search_entry.bind("<KeyRelease>", check_search)

    showbttn = Button (frame_1, text = "Show", font = ('Calibri', 17), command = expand_show)
    showbttn.place(x = 315, y = 550)

    showbttn_ex = Button (frame_1, text = "Show", font = ('Calibri', 17), command = expand_show_note_ex)

    show_bttn_ex_2 = Button (frame_1, text = "Show", font = ('Calibri', 17), command = expand_show_aftersort)

    search_bttn = Button(frame_1, text = "Search", font = ('Calibri', 17), command = search_expand)
    search_bttn.place(x = 30, y = 550)

    sort_button = Button (frame_1, text = "Sort", font = ('Calibri', 17), command = sort_demo)
    sort_button.place(x = 120, y = 550)

    sort_bttn_dec = Button (frame_1, text = "Sort", font = ('Calibri', 17), command = sort_dec)
    sort_bttn_inc = Button (frame_1, text = "Sort", font = ('Calibri', 17), command = sort_inc)

    hide_bttn = Button(frame_1, text = "Hide", font = ('Calibri', 17), command = hide_search)
    hide_bttn_2 = Button(frame_1, text = "Hide", font = ('Calibri', 17), command = hid_search_2)

    #if not list_title and not list_content:
    #    Del_bttn.config(state = DISABLED)
    #    Del_bttn_afsort.config(state = DISABLED)
    #    Del_list_bttn.config(state = DISABLED)

    #    showbttn.config(state = DISABLED)
    #    showbttn_ex.config(state = DISABLED)
    #    show_bttn_ex_2.config(state = DISABLED)

    #    sort_button.config(state = DISABLED)
    #    sort_bttn_dec.config(state = DISABLED)
    #    sort_bttn_inc.config(state = DISABLED)
    #elif list_title and list_content:
    #    del_bttn.config(state = ACTIVE)
    #    Del_bttn_afsort.config(state = ACTIVE)
    #    Del_list_bttn.config(state = ACTIVE)

    #    showbttn.config(state = ACTIVE)
    #    showbttn_ex.config(state = ACTIVE)
    #    showbttn_ex_2.config(state = ACTIVE)

    #    sort_button.config(state = ACTIVE)
    #    sort_bttn_dec.config(state = ACTIVE)
    #    sort_bttn_inc.config(state = ACTIVE)


    #ref_button = Button(frame_2, text = "Refresh time", font = ('Calibri', 17), command = refresh_time)
    #ref_button.place(x = 300, y = 50)

    #frame_1.config(bg = 'navy')
    #days_years()
    #time_zones_info()

    ##### CONFIGURATION TAB ######

    ### SET SCHEDULE FUNCTION
    # DEFINE SET SCHEDULE FUNCTION
    frame_4 = Frame(frame_2, width = 280, height = 440, bg = '#151a1d', highlightthickness = 1, highlightcolor = 'white')

    #frame_5 = Frame(frame_4, width = 260, height = 100, bg = '#151a1d', highlightthickness = 1, highlightcolor = 'white')

    LABEL_welcome_title = Label(frame_2, text = "Welcome to Time management!!", font = ('Calibri', 22, 'bold'), bg = '#151a1d', fg = 'white')
    LABEL_welcome_title.place(x = 280, y = 205)

    Work_label = Label(frame_2, text = 'Work', font = ('Calibri', 40, 'bold', 'italic'), bg = '#151a1d', fg = 'gold')
    Work_label.place(x = 50, y = 190)

    config_label = Label(frame_2, text = 'CONFIGURATION', font = ('Calibri', 40, 'bold'), bg = '#151a1d', fg = 'gold')
    config_label.place(x = 300, y = 30)

    set_Alarm = Button(frame_2, text = 'Set schedule list', font = ('Calibri', 13), command = expand_func)
    set_Alarm.place(x = 50, y = 80)

    hide_Alarm = Button(frame_2, text = 'Hide schedule list', font = ('Calibri', 13), command = contract_func)
    hide_Alarm.place_forget()


    #Time_limit_lbl = Label(frame_2, text = 'Time limit:', font = ('Calibri', 30, 'italic', 'bold'), bg = '#151a1d', fg = 'gold')
    #Time_limit_lbl.place(x = 315, y = 225)

    #currentday_lbl = Label(frame_2, text = '(For current day)', font = ('Calibri', 10, 'italic', 'bold'), bg = '#151a1d', fg = 'gold')
    #currentday_lbl.place(x = 350, y = 210)

    def limit_char_size_start (*arg):
        value = start_entry_txt.get()
        if value == '':
            pass
        elif value.isdigit():
            if len(value) > 5:
                start_entry_txt.set(value[:2359])
            elif int(value) > 2359:
                start_entry_txt.set(2359)
            else:
                if int(value) > 1000:
                    get_2_last_digit = int(value) % 100
                    if get_2_last_digit > 59:
                        get_2_first_digit = int(value)//100
                        set_time_last = (get_2_first_digit * 100) + 59
                        start_entry_txt.set(set_time_last)

        elif type(value) == str:
            start_entry.delete(0, 'end')

    def limit_char_size_finish (*arg):
        value = Finish_work.get()
        if value == '':
            pass
        elif value.isdigit():
            if len(value) > 5:
                Finish_work.set(value[:2359])
            elif int(value) > 2359:
                Finish_work.set(2359)
            else:
                if int(value) > 1000:
                    get_2_last_digit = int(value) % 100
                    if get_2_last_digit > 59:
                        get_2_first_digit = int(value)//100
                        set_time_last = (get_2_first_digit * 100) + 59
                        Finish_work.set(set_time_last)

        elif type(value) == str:
            Finish_entry.delete(0, 'end')

    # Greedy Algorithm Implement
    #Entry_Time_Limit = StringVar()
    #Entry_Time_Limit.trace('w', limit_char_size)

    Title_stringvar = StringVar()
    #Title_stringvar.trace('w', limit_char)

    # MergeSort for Greedy Algorithm
    def mergeSort_Greedy(works):
        if len(works) > 1 :
            mid = len(works)//2
            left_side = works[:mid]
            right_side = works[mid:]
            mergeSort_Greedy(left_side)
            mergeSort_Greedy(right_side)
            i = 0
            j = 0
            k = 0
            while i < len(left_side) and j < len(right_side) :
                if int(left_side[i].finish) < int(right_side[j].finish) :
                    works[k] = left_side[i]
                    i += 1
                else :
                    works[k] = right_side[j]
                    j += 1
                k += 1
            while i < len(left_side) :
                works[k] = left_side[i]
                k += 1
                i += 1
            while j < len(right_side) :
                works[k] = right_side[j]
                k += 1
                j += 1

    def read_file(works):
        with open("text\congviec.txt",'r') as csv_file:
            reader = csv.reader(csv_file, delimiter=',')
            for row in reader:
                works.append(work(row[0], row[1], row[2]))

    def read_file_schedule(data):
        with open("text\cong_viec_da_sap_xep.txt",'r') as csv_file:
            reader = csv.reader(csv_file, delimiter=',')
            for row in reader:
                data.append(work(row[0], row[1], row[2]))

    # Function on frame 4
    def deleted_selected_line():
        for i in listbox_work.curselection():
            listbox_file = open("text\congviec.txt", 'r')

            lines = listbox_file.readlines()
            listbox_file.close()

            del lines[i]

            new_file = open("text\congviec.txt", 'w+')

            for line in lines:
                new_file.write(line)

            new_file.close()

        for i in listbox_work.curselection():
            for j in range(0, len(works), 1):
                if listbox_work.get(i) == works[j].works:
                    works.remove(works[i])
                    listbox_work.delete(ANCHOR)
                    works_temp.clear()
                    schedule_temp_list.clear()
                    break

    def save_file(works):
        with open("text\congviec.txt", 'w') as f:
            i = 0
            for i in range(len(works)):
                f.write(''.join(works[i].works))
                f.write(',')
                f.write(''.join(str(works[i].start)))
                f.write(',')
                f.write(''.join(str(works[i].finish)))
                f.write('\n')
        f.close()

    def save_file_after_sort(data):
        with open("text\cong_viec_da_sap_xep.txt", 'w') as f:
            i = 0
            for i in range(len(data)):
                f.write(''.join(data[i].works))
                f.write(',')
                f.write(''.join(str(data[i].start)))
                f.write(',')
                f.write(''.join(str(data[i].finish)))
                f.write('\n')
        f.close()

    def show_on_frame4(event):
        for i in listbox_frame4.curselection():
            title_lbl_frame4.config(text = works_temp[i].works)

            hour_start_get = int(works_temp[i].start) // 100
            minute_start_get = int(works_temp[i].start) % 100

            hour_finish_get = int(works_temp[i].finish) // 100
            minute_finish_get = int(works_temp[i].finish) % 100

            state_hour = ''

            if int(works[i].start) < 1200:
                state_hour = 'AM'
            else:
                state_hour = 'PM'

            if hour_start_get < 12 and hour_start_get < 10 and minute_start_get < 10:
                start_lbl_frame4.config(text = f'0{hour_start_get}:0{minute_start_get} {state_hour}')
            elif hour_start_get < 12 and hour_start_get >= 10 and minute_start_get < 10:
                start_lbl_frame4.config(text = f'{hour_start_get}:0{minute_start_get} {state_hour}')
            elif hour_start_get < 12 and minute_start_get >= 10:
                start_lbl_frame4.config(text = f'0{hour_start_get}:{minute_start_get} {state_hour}')
            elif hour_start_get >= 12 and minute_start_get < 10:
                start_lbl_frame4.config(text = f'{hour_start_get}:0{minute_start_get} {state_hour}')
            elif hour_start_get >= 12 and minute_start_get >= 10:
                start_lbl_frame4.config(text = f'{hour_start_get}:{minute_start_get} {state_hour}')

            if hour_finish_get < 12 and hour_finish_get < 10 and minute_finish_get < 10:
                finish_lbl_frame4.config(text = f'0{hour_finish_get}:0{minute_finish_get} {state_hour}')
            elif hour_finish_get < 12 and hour_finish_get >= 10 and minute_finish_get < 10:
                finish_lbl_frame4.config(text = f'{hour_finish_get}:0{minute_finish_get} {state_hour}')
            elif hour_finish_get < 12 and minute_finish_get >= 10:
                finish_lbl_frame4.config(text = f'0{hour_finish_get}:{minute_finish_get} {state_hour}')
            elif hour_finish_get >= 12 and minute_finish_get < 10:
                finish_lbl_frame4.config(text = f'{hour_finish_get}:0{minute_finish_get} {state_hour}')
            elif hour_finish_get >= 12 and minute_finish_get >= 10:
                finish_lbl_frame4.config(text = f'{hour_finish_get}:{minute_finish_get} {state_hour}')

    def appearance_frame_4():
        delete_selected_bttn.config(state = DISABLED)
        open_bttn.config(state = DISABLED)
        delete_all_bttn.config(state = DISABLED)
        listbox_work.place_forget()
        refresh_button_2.place_forget()
        frame_4.place(x = 15, y = 265)
        LABEL_work_info_title.place_forget()
        LABEL_work_info_start.place_forget()
        LABEL_work_info_finish.place_forget()

        work_info_title.place_forget()
        work_info_start.place_forget()
        work_info_finish.place_forget()

        for i in range(0, len(works_temp), 1):
            listbox_frame4.insert(END, works_temp[i].works)

        listbox_frame4.place(x = 15, y = 10)
        LABEL_work_lbl_frame4.place(x = 28, y = 320)
        LABEL_start_lbl_frame4.place(x = 28, y = 355)
        LABEL_finish_lbl_frame4.place(x = 28, y = 390)

    def update_listbox():
        listbox_work.delete(0, END)
        
        mergeSort_Greedy (works)

        for i in range(0, len(works), 1):
            listbox_work.insert(END, works[i].works)

    def start_greedy_algo():
        count = 0
        index_i = 0
        if not works:
            messagebox.showinfo("Reminder", "Please insert work first!!!")
            Message_label.config(text = 'Please insert work first!!!')
            frame_3.config(width = 310)
        elif not works_temp:
            update_listbox()
            greedy_algo(works)
            appearance_frame_4()
            save_file_after_sort(works_temp)
            for index in range(0, len(works_temp), 1):
                schedule_temp_list.append(works_temp[index].works)
        else:
            while index_i < len(works_temp):
                if works_temp[index_i].works in schedule_temp_list:
                    count = count + 1
                    index_i = index_i + 1
                else:
                    index_i = index_i + 1

            if count != len(works_temp):
                works_temp.clear()
                update_listbox()
                greedy_algo(works)
                appearance_frame_4()
                save_file_after_sort(works_temp)
            else:
                messagebox.showinfo("Reminder", "Schedule has already been set!!\n\nPlease press RETURN LIST button\nbefore creating another schedule")
                #Message_label.config(text = 'Schedule already been set!!')
                #frame_3.config(width = 330)

    def greedy_algo(works):
        works_temp.clear()

        end = works[0].finish

        works_temp.append(works[0])
        for i in range(0, len(works), 1):            
            if int(works[i].start) >= int(end):
                
                end = works[i].finish                
                works_temp.append(works[i])
     
    def F5_func():
        if not works_temp:
            read_file(works)
            read_file_schedule(works_temp)
            listbox_work.delete(0, END)
            for data in range(0, len(works), 1):
                listbox_work.insert(END, works[data].works)

    def refresh_func():
        open_bttn.config(state = ACTIVE)
        delete_all_bttn.config(state = ACTIVE)
        delete_selected_bttn.config(state = ACTIVE)
        if not listbox_work:
            pass
        elif listbox_work:
            listbox_frame4.delete(0, END)
            works_temp.clear()

            listbox_work.place(x = 50, y = 280)
            frame_4.place_forget()
            LABEL_work_info_title.place(x = 37, y = 580)
            LABEL_work_info_start.place(x = 37, y = 620)
            LABEL_work_info_finish.place(x = 37, y = 660)

            work_info_title.place(x = 95, y = 580)
            work_info_start.place(x = 90, y = 621)
            work_info_finish.place(x = 120, y = 661)

            refresh_button_2.place(x = 195, y = 215)

            listbox_frame4.place_forget()
            LABEL_work_lbl_frame4.place_forget()
            LABEL_start_lbl_frame4.place_forget()
            LABEL_finish_lbl_frame4.place_forget()

    #TimeLimit_entry = Entry(frame_2, textvariable = Entry_Time_Limit, width = 3, font = ('Calibri', 25, 'italic', 'bold'))
    #TimeLimit_entry.place(x = 505, y = 230)

    create_schedule = Button(frame_2, text = 'Create schedule', font = ('Calibri', 15, 'bold'), command = start_greedy_algo)
    create_schedule.place(x = 440, y = 285)

    refresh_button = Button(frame_2, text = 'Return to list', font = ('Calibri', 15, 'bold'), command = refresh_func)
    refresh_button.place(x = 310, y = 285)

    refresh_button_2 = Button(frame_2, text = 'Import', font = ('Calibri', 12, 'bold'), command = F5_func)
    refresh_button_2.place(x = 195, y = 215)

    # Title for work
    Title_frame2 = Label(frame_2, text = 'Title:', font = ('Calibri', 23, 'italic', 'bold'), bg = '#151a1d', fg = 'white')
    Title_frame2.place(x = 305, y = 430)

    #Title_entry_frame2 = Text(frame_2, width = 21, height = 2, font = ('Calibri', 15, 'bold'))
    #Title_entry_frame2.place(x = 420, y = 390)

    Title_entry_frame2 = Entry(frame_2, textvariable = Title_stringvar, width = 20, font = ('Calibri', 20, 'bold'))
    Title_entry_frame2.place(x = 390, y = 435)

    # Time for work
    Start_frame_2 = Label(frame_2, text = 'Start at:', font = ('Calibri', 23, 'italic', 'bold'), bg = '#151a1d', fg = 'white')
    Start_frame_2.place(x = 305, y = 500)

    start_entry_txt = StringVar()
    start_entry_txt.trace('w', limit_char_size_start)

    start_entry = Entry(frame_2, textvariable = start_entry_txt, width = 4, font = ('Calibri', 25, 'italic', 'bold'))
    start_entry.place(x = 420, y = 500)

    # Priority of work
    Finish_frame_2 = Label(frame_2, text = 'Finish:', font = ('Calibri', 23, 'italic', 'bold'), bg = '#151a1d', fg = 'white')
    Finish_frame_2.place(x = 505, y = 500)

    Finish_work = StringVar()
    Finish_work.trace('w', limit_char_size_finish)

    Finish_entry = Entry(frame_2, textvariable = Finish_work, width = 4, font = ('Calibri', 25, 'italic', 'bold'))
    Finish_entry.place(x = 600, y = 500)

    #Label show work info
    LABEL_work_info_title = Label(frame_2, text = 'Work:', font = ('Calibri', 15, 'bold'), bg = '#151a1d', fg = 'white')
    LABEL_work_info_title.place(x = 37, y = 580)

    LABEL_work_info_start = Label(frame_2, text = 'Start:', font = ('Calibri', 15, 'bold'), bg = '#151a1d', fg = 'white')
    LABEL_work_info_start.place(x = 37, y = 620)

    LABEL_work_info_finish = Label(frame_2, text = 'Finish at:', font = ('Calibri', 15, 'bold'), bg = '#151a1d', fg = 'white')
    LABEL_work_info_finish.place(x = 37, y = 660)

    work_info_title = Label(frame_2, font = ('Calibri', 15), bg = '#151a1d', fg = 'gold')
    work_info_title.place(x = 95, y = 580)

    work_info_start = Label(frame_2, font = ('Calibri', 15), bg = '#151a1d', fg = 'gold')
    work_info_start.place(x = 90, y = 621)

    work_info_finish = Label(frame_2, font = ('Calibri', 15), bg = '#151a1d', fg = 'gold')
    work_info_finish.place(x = 120, y = 661)

    # Add into class function
    def check_work_list():
        temp_listbox = []
        
        for i in range(0, len(works), 1):
            temp_listbox.append(works[i].works)

        if Title_stringvar.get() in temp_listbox:
            Message_label.config(text = 'Work has already been set!!')
            frame_3.config(width = 345, height = 60)
            messagebox.showinfo('Reminder', 'Work has already been set!!')

        else:
            c_work_list()

        temp_listbox.clear()

    def c_work_list():
        start_data = start_entry_txt.get()
        finish_data = Finish_work.get()

        get_middle_start = 0
        get_middle_finish = 0

        # ONLY USE FOR start_data and finish_data both smaller than 1000 and larger 100
        get_middle_start = (int(start_data.strip() or 0) // 10) % 10
        get_middle_finish = (int(finish_data.strip() or 0) // 10) % 10

        if start_entry_txt.get() == '' and Finish_work.get() == '' and Title_stringvar.get() == '':
            Message_label.config(text = 'Please insert work!!!', font = ('Calibri', 20, 'bold'))
            frame_3.config(width = 270, height = 60)
            messagebox.showinfo('Reminder', 'Please insert work!!!')
            
        elif start_entry_txt.get() == '' and Finish_work.get() == '' and Title_stringvar.get() == '' and works:
            Message_label.config(text = 'Please insert work!!!', font = ('Calibri', 20, 'bold'))
            frame_3.config(width = 270, height = 60)
            messagebox.showinfo('Reminder', 'Please insert work!!!')
            
        elif Title_stringvar.get() == '' and Finish_work.get() == '':
            Message_label.config(text = 'Insert title and finish time please!!!', font = ('Calibri', 18, 'bold'))
            frame_3.config(width = 375, height = 60)
            messagebox.showinfo('Reminder', 'Insert title and finish time please!!!')
            
        elif Title_stringvar.get() == '' and start_entry_txt.get() == '':
            Message_label.config(text = 'Please insert titlte and start time!!!', font = ('Calibri', 18, 'bold'))
            frame_3.config(width = 375, height = 60)
            messagebox.showinfo('Reminder', 'Please insert titlte and start time!!!')
            
        elif Title_stringvar.get() == '':
            Message_label.config(text = 'Set work title please!!!', font = ('Calibri', 20, 'bold'))
            frame_3.config(width = 283, height = 60)
            messagebox.showinfo('Reminder', 'Set work title please!!!')
            
        elif start_entry_txt.get() == '' and Finish_work.get() == '':
            Message_label.config(text = 'Please insert start and finish time!!!', font = ('Calibri', 18, 'bold'))
            frame_3.config(width = 384, height = 60)
            messagebox.showinfo('Reminder', 'Please insert start and finish time!!!')
            
        elif start_entry_txt.get() == '':
            Message_label.config(text = 'We need "time" to schedule!!!', font = ('Calibri', 20, 'bold'))
            frame_3.config(width = 365, height = 60)
            messagebox.showinfo('Reminder', 'We need "time" to schedule!!!')
            
        elif Finish_work.get() == '':
            Message_label.config(text = 'Insert finish time please!!!', font = ('Calibri', 20, 'bold'))
            frame_3.config(width = 320, height = 60)
            messagebox.showinfo('Reminder', 'Insert finish time please!!!')

        elif int(start_data) > int(finish_data):
            Message_label.config(text = 'Start time > finish time??', font = ('Calibri', 20, 'bold'))
            frame_3.config(width = 310, height = 60)
            messagebox.showinfo('Reminder', 'Start time > finish time??')

        elif int(start_data) == int(finish_data):
            Message_label.config(text = 'Start time >< finish time!!', font = ('Calibri', 20, 'bold'))
            frame_3.config(width = 325, height = 60)
            messagebox.showinfo('Reminder', 'Start time >< finish time!!')
        
        elif int(start_data) > 1000 and int(finish_data) > 1000:
            insert_into_class()

        elif int(finish_data) > 1000:
            if int(start_data) > 100:
                if get_middle_start > 5:
                    Message_label.config(text = 'Invalid start time!!', font = ('Calibri', 20, 'bold'))
                    frame_3.config(width = 245, height = 60)
                    messagebox.showinfo('Reminder', 'Invalid start time!!')
                else:
                    insert_into_class()

            elif int(start_data) < 100:
                if int(start_data) > 60:
                    Message_label.config(text = 'Invalid start time!!', font = ('Calibri', 20, 'bold'))
                    frame_3.config(width = 245, height = 60)
                    messagebox.showinfo('Reminder', 'Invalid start time!!')
                else:
                    insert_into_class()

        elif int(start_data) < 100 and int(finish_data) < 100:
            if int(start_data) > 60 and int(finish_data) > 60:
                Message_label.config(text = 'Invalid start and finish time!!', font = ('Calibri', 20, 'bold'))
                frame_3.config(width = 345, height = 60)
                messagebox.showinfo('Reminder', 'Invalid start and finish time!!')

            elif int(start_data) > 60:
                Message_label.config(text = 'Invalid start time!!', font = ('Calibri', 20, 'bold'))
                frame_3.config(width = 245, height = 60)
                messagebox.showinfo('Reminder', 'Invalid start time!!')

            elif int(finish_data) > 60:
                Message_label.config(text = 'Invalid finish time!!', font = ('Calibri', 20, 'bold'))
                frame_3.config(width = 250, height = 60)
                messagebox.showinfo('Reminder', 'Invalid finish time!!')

            else:
                insert_into_class()

        elif int(start_data) < 100:
            if int(start_data) > 60:
                Message_label.config(text = 'Invalid start time!!', font = ('Calibri', 20, 'bold'))
                frame_3.config(width = 245, height = 60)
                messagebox.showinfo('Reminder', 'Invalid start time!!')

            elif get_middle_finish > 5:
                Message_label.config(text = 'Invalid finish time!!', font = ('Calibri', 20, 'bold'))
                frame_3.config(width = 250, height = 60)
                messagebox.showinfo('Reminder', 'Invalid finish time!!')

            else:
                insert_into_class()

        elif int(finish_data) < 100:
            if int(finish_data) > 60:
                Message_label.config(text = 'Invalid finish time!!', font = ('Calibri', 20, 'bold'))
                frame_3.config(width = 250, height = 60)
                messagebox.showinfo('Reminder', 'Invalid finish time!!')

            elif get_middle_start > 5:
                Message_label.config(text = 'Invalid start time!!', font = ('Calibri', 20, 'bold'))
                frame_3.config(width = 245, height = 60)
                messagebox.showinfo('Reminder', 'Invalid start time!!')

            else:
                insert_into_class()

        elif int(start_data) > 100 and int(finish_data) > 100:
            if get_middle_start > 5 and get_middle_finish > 5:
                Message_label.config(text = 'Invalid start and finish time!!', font = ('Calibri', 20, 'bold'))
                frame_3.config(width = 345, height = 60)
                messagebox.showinfo('Reminder', 'Invalid start and finish time!!')

            elif get_middle_finish > 5:
                Message_label.config(text = 'Invalid finish time!!', font = ('Calibri', 20, 'bold'))
                frame_3.config(width = 250, height = 60)
                messagebox.showinfo('Reminder', 'Invalid finish time!!')

            else:
                insert_into_class()
        else:
            insert_into_class()

    def insert_into_class():
        #title_get = Title_entry_frame2.get('1.0', 'end-1c')
        title_get = Title_stringvar.get()
        start_get = start_entry_txt.get()
        finish_get = Finish_work.get()

        works.append(work(title_get, start_get, finish_get))

        save_file(works)

        listbox_work.insert(END, title_get)
        start_entry.delete(0, 'end')
        Finish_entry.delete(0, 'end')
        Title_entry_frame2.delete(0, 'end')
        Message_label.config(text = 'Set work successfully!!!', font = ('Calibri', 20, 'bold'))
        frame_3.config(width = 290, height = 60)
        #Title_entry_frame2.delete('1.0', END)
            

    def show_on_screen(event):
        for i in listbox_work.curselection():
            #data = listbox_work.get(i)
            work_info_title.config(text = works[i].works)

            hour_start_get = int(works[i].start) // 100
            minute_start_get = int(works[i].start) % 100

            hour_finish_get = int(works[i].finish) // 100
            minute_finish_get = int(works[i].finish) % 100

            state_hour = ''

            if int(works[i].start) < 1200:
                state_hour = 'AM'
            else:
                state_hour = 'PM'

            if hour_start_get < 12 and hour_start_get < 10 and minute_start_get < 10:
                work_info_start.config(text = f'0{hour_start_get}:0{minute_start_get} {state_hour}')
            elif hour_start_get < 12 and hour_start_get >= 10 and minute_start_get < 10:
                work_info_start.config(text = f'{hour_start_get}:0{minute_start_get} {state_hour}')
            elif hour_start_get < 12 and minute_start_get >= 10:
                work_info_start.config(text = f'0{hour_start_get}:{minute_start_get} {state_hour}')
            elif hour_start_get >= 12 and minute_start_get < 10:
                work_info_start.config(text = f'{hour_start_get}:0{minute_start_get} {state_hour}')
            elif hour_start_get >= 12 and minute_start_get >= 10:
                work_info_start.config(text = f'{hour_start_get}:{minute_start_get} {state_hour}')

            if hour_finish_get < 12 and hour_finish_get < 10 and minute_finish_get < 10:
                work_info_finish.config(text = f'0{hour_finish_get}:0{minute_finish_get} {state_hour}')
            elif hour_finish_get < 12 and hour_finish_get >= 10 and minute_finish_get < 10:
                work_info_finish.config(text = f'{hour_finish_get}:0{minute_finish_get} {state_hour}')
            elif hour_finish_get < 12 and minute_finish_get >= 10:
                work_info_finish.config(text = f'0{hour_finish_get}:{minute_finish_get} {state_hour}')
            elif hour_finish_get >= 12 and minute_finish_get < 10:
                work_info_finish.config(text = f'{hour_finish_get}:0{minute_finish_get} {state_hour}')
            elif hour_finish_get >= 12 and minute_finish_get >= 10:
                work_info_finish.config(text = f'{hour_finish_get}:{minute_finish_get} {state_hour}')

        #for i in range(0, len(works), 1):
        #    print(works[i].works + ' ' + works[i].time + ' ' + works[i].priority + ' ' + str(works[i].percent_priority))

    def delected_all_schedule():
        if not works:
            open("text\congviec.txt", 'w').close()
            open("text\cong_viec_da_sap_xep.txt", 'w').close()
            Message_label.config(text = 'All schedules has already been deleted!', font = ('Calibri', 16, 'bold'))
            frame_3.config(width = 370, height = 50)
            messagebox.showinfo('Reminder', 'All schedules\nhas already been deleted!!')
        else:
            listbox_work.delete(0, END)
            works.clear()
            works_temp.clear()
            schedule_temp_list.clear()
            open("text\congviec.txt", 'w').close()
            open("text\cong_viec_da_sap_xep.txt", 'w').close()
            Message_label.config(text = 'All schedules has deleted!', font = ('Calibri', 20, 'bold'))
            frame_3.config(width = 310, height = 60)
            messagebox.showinfo('Reminder', 'All schedules has deleted!')

    listbox_work = Listbox(frame_2, font = ('Calibri', 15, 'bold'), height = 11)
    listbox_work.place(x = 50, y = 280)
    listbox_work.bind("<<ListboxSelect>>", show_on_screen)

    # Frame 3 in Frame 2
    frame_3 = Frame(frame_2, width = 270, height = 60, bg = '#151a1d', highlightbackground = 'white', highlightthickness = 1)
    frame_3.place(x = 307, y = 347)

    # Add into class and Delete/ Delete all value from class
    open_bttn = Button(frame_2, text = "Add", font = ('Calibri', 20, 'italic', 'bold'), command = check_work_list)
    open_bttn.place(x = 310, y = 580)

    delete_selected_bttn = Button(frame_2, text = "Delete", font = ('Calibri', 20, 'italic', 'bold'), command = deleted_selected_line)
    delete_selected_bttn.place(x = 381, y = 580)

    delete_all_bttn = Button(frame_2, text = "Clear all", font = ('Calibri', 20, 'italic', 'bold'), command = delected_all_schedule)
    delete_all_bttn.place(x = 480, y = 580)

    Message_label = Label(frame_2, text = 'Please set schedule!!!', font = ('Calibri', 20, 'bold'), bg ='#151a1d', fg = 'gold')
    Message_label.place(x = 315, y = 357)

    # Label appear on Frame 4
    listbox_frame4 = Listbox(frame_4, font = ('Calibri', 18, 'bold'), height = 9, bg = '#151a1d', fg = 'white')
    listbox_frame4.bind("<<ListboxSelect>>", show_on_frame4)

    LABEL_work_lbl_frame4 = Label(frame_4, text = 'Title:', font = ('Calibri', 15, 'bold'), bg = '#151a1d', fg = 'gold')

    LABEL_start_lbl_frame4 = Label(frame_4, text = 'Start:', font = ('Calibri', 15, 'bold'), bg = '#151a1d', fg = 'gold')

    LABEL_finish_lbl_frame4 = Label(frame_4, text = 'Finish:', font = ('Calibri', 15, 'bold'), bg = '#151a1d', fg = 'gold')

    title_lbl_frame4 = Label(frame_4, font = ('Calibri', 15, 'bold'), bg = '#151a1d', fg = 'white')
    title_lbl_frame4.place(x = 80, y = 320)

    start_lbl_frame4 = Label(frame_4, font = ('Calibri', 15, 'bold'), bg = '#151a1d', fg = 'white')
    start_lbl_frame4.place(x = 83, y = 355)

    finish_lbl_frame4 = Label(frame_4, font = ('Calibri', 15, 'bold'), bg = '#151a1d', fg = 'white')
    finish_lbl_frame4.place(x = 90, y = 390)

    time_info()
    #read_file()
    #text_schedule_screen = Label(frame_4, font = ('Calibri', 15, 'bold'), bg ='#151a1d', fg = 'white')

    root.config(bg = '#151a1d')

splash_screen.after(2300, main_window)

mainloop()