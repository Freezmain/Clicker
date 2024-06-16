import keyboard
import mouse
import time
import tkinter
import threading
import random

isCliking = False
isOne_mouse_position = True
click_interval = 0.05
click_interval_range = 0.01
click_radius = 10
mouse_position_x = 200
mouse_position_y = 200
mouse_positions_count = 0
mouse_positions_number_need = 0
count_maximum_mouse_positions = 5
mouse_positions_array = [[0 for _ in range(count_maximum_mouse_positions)] for _ in range(2)]

def Random_value(start_value, deviation, type):
    end_value = 1
    if type == "int":
        if random.randint(0,1) == 1:
            end_value = random.randint(start_value, start_value + deviation)
        else:
            end_value = random.randint(start_value - deviation, start_value)
    if type == "float":
        if random.randint(0,1) == 1:
            end_value = random.uniform(start_value, start_value + deviation)
        else:
            end_value = random.uniform(start_value - deviation, start_value)
    return end_value

def Clicker_Start():
    global mouse_positions_number_need
    while True:
        time.sleep(0.001)
        if isCliking:
            if isOne_mouse_position:
                mouse_random_position_x = Random_value(mouse_position_x, click_radius, "int")
                mouse_random_position_y = Random_value(mouse_position_y, click_radius, "int")
                mouse.drag(mouse_position_x, mouse_position_y, mouse_random_position_x, mouse_random_position_y, duration=click_interval/10)
                mouse.click(button="left")
                click_interval_changed = Random_value(click_interval, click_interval_range, "float")
            else:
                mouse_random_position_x = Random_value(mouse_positions_array[0][mouse_positions_number_need], click_radius, "int")
                mouse_random_position_y = Random_value(mouse_positions_array[1][mouse_positions_number_need], click_radius, "int")
                mouse.drag(mouse_positions_array[0][mouse_positions_number_need], mouse_positions_array[1][mouse_positions_number_need], mouse_random_position_x, mouse_random_position_y, duration=click_interval/10)
                mouse.click(button="left")
                click_interval_changed = Random_value(click_interval, click_interval_range, "float")
                mouse_positions_number_need = mouse_positions_number_need + 1
                if mouse_positions_number_need == mouse_positions_count:
                    mouse_positions_number_need = 0

            time.sleep(click_interval_changed)

def Set_One_Mouse_Position():
    global isOne_mouse_position, mouse_positions_array, mouse_positions_count, mouse_positions_number_need
    isOne_mouse_position = True
    mouse_positions_array = [[0 for _ in range(count_maximum_mouse_positions)] for _ in range(2)]
    mouse_positions_count = 0
    mouse_positions_number_need = 0

def Set_Many_Mouse_Positions():
    global isOne_mouse_position
    isOne_mouse_position = False

def Set_Clicker():
    global isCliking
    if isCliking:
        isCliking = False
        print("Cliker is OFF")
    else:
        isCliking = True
        print("Cliker is ON")
        print(mouse_positions_array, mouse_positions_count)

def Set_Click_Interval():
    global click_interval
    click_interval = int(Click_interval_entry.get())
    click_interval = click_interval/1000

def Set_Click_Interval_Range():
    global click_interval_range
    click_interval_range = int(Click_interval_range_entry.get())
    click_interval_range = click_interval_range/1000

def Set_Click_Radius():
    global click_radius
    click_radius = int(Click_radius_entry.get())

def Set_Mouse_Position():
    global mouse_position_x, mouse_position_y, mouse_positions_array, mouse_positions_count
    if isOne_mouse_position:
        mouse_position_x, mouse_position_y = mouse.get_position()
    else:
        mouse_position_x, mouse_position_y = mouse.get_position()
        if mouse_positions_count < count_maximum_mouse_positions:
            mouse_positions_array[0][mouse_positions_count] = mouse_position_x
            mouse_positions_array[1][mouse_positions_count] = mouse_position_y
            mouse_positions_count = mouse_positions_count + 1

keyboard.add_hotkey('Alt + Z', Set_Clicker)
keyboard.add_hotkey('Alt + X', Set_Mouse_Position)

prog = tkinter.Tk()

prog.title("Cliker")
prog.geometry('300x300')
prog.configure(bg='#333333')

frame = tkinter.Frame(bg='#333333')

Name_label = tkinter.Label(frame, text="AutoCliker", bg='#333333', fg='#FFFFFF', font=("Arial", 15))
Click_panel_label = tkinter.Label(frame, text="Click control", bg='#333333', fg='#FFFFFF', font=("Arial", 12))
Click_interval_label = tkinter.Label(frame, text="Click interval", bg='#333333', fg='#FFFFFF', font=("Arial", 10))
Click_radius_label = tkinter.Label(frame, text="Click radius", bg='#333333', fg='#FFFFFF', font=("Arial", 10))
Click_interval_range_label = tkinter.Label(frame, text="Click interval range", bg='#333333', fg='#FFFFFF', font=("Arial", 10))
Mouse_panel_label = tkinter.Label(frame, text="Mouse control", bg='#333333', fg='#FFFFFF', font=("Arial", 12))
Click_interval_entry = tkinter.Entry(frame, font=("Arial", 10), width=10)
Click_radius_entry = tkinter.Entry(frame, font=("Arial", 10), width=10)
Click_interval_range_entry = tkinter.Entry(frame, font=("Arial", 10), width=10)
Set_Click_interval_button = tkinter.Button(frame, text="Set", bg='#344444', fg='#FFFFFF', font=("Arial", 8), width=3, command=Set_Click_Interval)
Set_Click_radius_button = tkinter.Button(frame, text="Set", bg='#344444', fg='#FFFFFF', font=("Arial", 8), width=3, command=Set_Click_Radius)
Set_Click_interval_range_button = tkinter.Button(frame, text="Set", bg='#344444', fg='#FFFFFF', font=("Arial", 8), width=3, command=Set_Click_Interval_Range)
One_mouse_position_button = tkinter.Button(frame, text="One position", bg='#344444', fg='#FFFFFF', font=("Arial", 8), width=12, command=Set_One_Mouse_Position)
Many_mouse_position_button = tkinter.Button(frame, text="Many position", bg='#344444', fg='#FFFFFF', font=("Arial", 8), width=12, command=Set_Many_Mouse_Positions)
Start_cliking_button = tkinter.Button(frame, text="Start",  bg='#344444', fg='#FFFFFF', font=("Arial", 8), width=2, command=Set_Clicker)
IsCliking_checkbutton = tkinter.Checkbutton(frame, text="Is Clicking", bg='#333333', fg='#FFFFFF', font=("Arial", 8))
IsSet_mouse_position_checkbutton = tkinter.Checkbutton(frame, text="Is Set Mouse Position", bg='#333333', fg='#FFFFFF', font=("Arial", 8))

Click_interval_entry.insert(0, "50")
Click_interval_range_entry.insert(0, 10)
Click_radius_entry.insert(0, 10)

Name_label.grid(row=0, column=0, columnspan=3, pady=5, sticky="news")
Click_panel_label.grid(row=1, column=0, columnspan=3, pady=2, sticky="news")
Click_interval_label.grid(row=2, column=0, pady=4)
Click_interval_entry.grid(row=2, column=1, pady=4)
Set_Click_interval_button.grid(row=2, column=2, pady=4)
Click_interval_range_label.grid(row=3, column=0, pady=4)
Click_interval_range_entry.grid(row=3, column=1, pady=4)
Set_Click_interval_range_button.grid(row=3, column=2, pady=4)
Click_radius_label.grid(row=4, column=0, pady=4)
Click_radius_entry.grid(row=4, column=1, pady=4)
Set_Click_radius_button.grid(row=4, column=2, pady=4)
IsCliking_checkbutton.grid(row=5, column=0, pady=4, padx=2)
IsSet_mouse_position_checkbutton.grid(row=5, column=1, pady=4, padx=2)
Mouse_panel_label.grid(row=6, column=0, columnspan=3, pady=2, sticky="news")
One_mouse_position_button.grid(row=7, column=0, pady=4, padx=2, sticky="e")
Many_mouse_position_button.grid(row=7, column=1, pady=4, padx=2, sticky="e")
Start_cliking_button.grid(row=8, column=0, columnspan=3, pady=10, sticky="news")

frame.pack()

click_thread = threading.Thread(target=Clicker_Start)
click_thread.daemon = True
click_thread.start()

prog.mainloop()