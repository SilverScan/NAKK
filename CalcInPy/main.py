from turtle import *
from tkinter import *
from tkinter import ttk
import tkinter.messagebox
from graphing import Screen, num_derive, tangent_line, derivative_function, calculate_integral, round_to_thousandths
import math

def mathematical_function(x):
    #print(f"x{x}")
    return math.sin(x)

def reject_closing():
    pass

#TODO: Adjust UI to be at least a little less hardcoded than it currently is



def ui_derive_button():       
    derive_button["state"] = "disabled"
    pop_up = Toplevel()
    pop_up.geometry("300x300+800+150")
    pop_up.wm_title("NAKK")
    # pop_up.protocol("WM_DELETE_WINDOW", reject_closing)
    drv_choice = tkinter.IntVar()
    loc_input = tkinter.StringVar()

     #TODO: add error if x_coord is offscreen (11:30 rn, will do tmr should be easy enough)
    def set_loc():
        disable_popup_inputs()
        try:
            x_coord = float(loc_input.get())
            derivative = float(num_derive(x_coord,mathematical_function))
            if drv_choice.get() == 1:
                y_coord = mathematical_function(x_coord)
                t.pencolor("red")
                screen.graph_function(tangent_line(derivative, x_coord, y_coord))
                enable_popup_inputs()
            else:
                drv_loc_lbl.config(text=f"Derivative at x = {x_coord}: {round_to_thousandths(derivative)}", fg="black")
                drv_loc_lbl.place(x=90, y=200)
                enable_popup_inputs()
        except ValueError:
            drv_loc_lbl.config(text="error: not a number", fg="red")
            enable_popup_inputs()
        
    
    drv_tan_rbtn = Radiobutton(pop_up, text="Plot derivative tangent line", variable=drv_choice, value=1, background="lightblue",
                              indicatoron=0, width=25)
    drv_show_rbtn = Radiobutton(pop_up, text="Print derivative of point", variable=drv_choice, value=2, background="lightblue", 
                               indicatoron=0, width=25)
    
    # drv_options_kill_btn = 
    input_box = Entry(pop_up, textvariable=loc_input)
    x_equals_lbl = Label(pop_up, text="x =")
    confirm_btn = Button(pop_up, text="Confirm x", width = 15 ,background="lightblue", command=set_loc)
    drv_loc_lbl = Label(pop_up)
    drv_tan_rbtn.place(x=55, y=30)
    drv_show_rbtn.place(x=55, y=90)
    x_equals_lbl.place(x=100, y=130)
    input_box.place(x=125, y = 130)
    confirm_btn.place(x=90, y=165)

    def disable_popup_inputs():
        drv_tan_rbtn["state"] = "disabled"
        drv_show_rbtn["state"] = "disabled"
        input_box["state"] = "disabled"
        confirm_btn["state"] = "disabled"
    def enable_popup_inputs():
        drv_tan_rbtn["state"] = "normal"
        drv_show_rbtn["state"] = "normal"
        input_box["state"] = "normal"
        confirm_btn["state"] = "normal"

def graph_drv_func():
    t.pencolor("blue")
    screen.graph_function(derivative_function(mathematical_function))
        

def ui_integrate_button():
    lower_limit = float(input("X coord A?\n"))
    upper_limit = float(input("X coord B?\n"))
    print(calculate_integral(lower_limit, upper_limit, mathematical_function))
# https://tenor.com/view/kriziebizie-krizziebuoy-magmastuff-magstok-pootisman-gif-1255252459385296217
def screen_render():
    try:
        xmin = float(x_min_entry.get())
        xmax = float(x_max_entry.get())
        ymin = float(y_min_entry.get())
        ymax = float(y_max_entry.get())
        screen.set_screen(xmin, xmax, ymin, ymax)
        screen.render()
    except ValueError:
        print("bruh")

def alter_input_states(functions: list, state: str):
    for i in range(len(functions)):
        functions[i]["state"] = state
        

main_ui = Tk()
main_ui.geometry("800x600")
main_ui.title("nakk (Nathan's Awesome Kalculus Kalculator)")

frame = ttk.Frame(main_ui)
frame.pack(expand=True, fill="both")
graphsidebar = ttk.Frame(frame)
graphsidebar.pack(side=LEFT, expand=True, fill='both')
sidebar = ttk.Frame(frame)
sidebar.pack(side=RIGHT, expand=True, fill='both')

graphsidebar.columnconfigure(0, pad = 5, weight = 1, minsize=5)
graphsidebar.columnconfigure(1, pad = 5, weight = 3, minsize=30)
graphsidebar.columnconfigure(2, pad = 5, weight = 1, minsize=6)

f1_lbl = Label(graphsidebar, anchor=W, text="f1(x)=")
f1_lbl.grid(column=0, row = 0)
f2_lbl = Label(graphsidebar, anchor=W, text="f2(x)=")
f2_lbl.grid(column=0, row = 1)
f3_lbl = Label(graphsidebar, anchor=W, text="f3(x)=")
f3_lbl.grid(column=0, row = 2)
f4_lbl = Label(graphsidebar, anchor=W, text="f4(x)=")
f4_lbl.grid(column=0, row = 3)
f5_lbl = Label(graphsidebar, anchor=W, text="f5(x)=")
f5_lbl.grid(column=0, row = 4)

f1 = StringVar()
f1_entry = Entry(graphsidebar,textvariable=f1)
f1_entry.grid(column=1, row = 0)
f2 = StringVar()
f2_entry = Entry(graphsidebar, textvariable=f2)
f2_entry.grid(column=1, row = 1)
f3 = StringVar()
f3_entry = Entry(graphsidebar, textvariable=f3)
f3_entry.grid(column=1, row = 2)
f4 = StringVar()
f4_entry = Entry(graphsidebar, textvariable=f4)
f4_entry.grid(column=1, row = 3)
f5 = StringVar()
f5_entry = Entry(graphsidebar, textvariable=f5)
f5_entry.grid(column=1, row = 4)

f1_show = BooleanVar(value=True)
f1_show_button = Checkbutton(graphsidebar, textvariable=f1_show, width=5, text = "Show?")
f1_show_button.grid(column=2, row=0)
f2_show = BooleanVar(value=True)
f2_show_button = Checkbutton(graphsidebar, textvariable=f2_show, width = 5, text ="Show?")
f2_show_button.grid(column=2, row=1)
f3_show = BooleanVar(value=True)
f3_show_button = Checkbutton(graphsidebar, textvariable=f3_show, width=5, text="Show?")
f3_show_button.grid(column=2, row=2)
f4_show = BooleanVar(value=True)
f4_show_button = Checkbutton(graphsidebar, textvariable=f4_show, width =5, text="Show?")
f4_show_button.grid(column=2, row=3)
f5_show = BooleanVar(value=True)
f5_show_button = Checkbutton(graphsidebar, textvariable=f5_show, width=5, text="Show?")
f5_show_button.grid(column=2, row=4)

canvas = ScrolledCanvas(frame)
canvas.pack(side = RIGHT, expand=True, fill = 'both')

sidebar.columnconfigure(0, pad=5, weight=2, minsize=30)
sidebar.columnconfigure(1,pad=5, weight=2, minsize=5)
x_min_lbl = Label(sidebar, anchor=W, text="X Minimum")
x_min_lbl.grid(column=0, row=0)
x_max_lbl = Label(sidebar, anchor=W, text="X Maximum")
x_max_lbl.grid(column=0, row=1)
y_min_lbl = Label(sidebar, anchor=W, text="Y Minimum")
y_min_lbl.grid(column=0, row=2)
y_max_lbl = Label(sidebar, anchor=W, text="Y Maximum")
y_max_lbl.grid(column=0, row=3)

x_min_ui = DoubleVar(value=-10)
x_min_entry = Entry(sidebar, textvariable=x_min_ui, width=5)
x_min_entry.grid(row=0, column=1)
x_max_ui = DoubleVar(value=10)
x_max_entry = Entry(sidebar, textvariable=x_max_ui, width=5)
x_max_entry.grid(row=1, column=1)
y_min_ui = DoubleVar(value=-10)
y_min_entry = Entry(sidebar, textvariable=y_min_ui, width=5)
y_min_entry.grid(row=2, column=1)
y_max_ui = DoubleVar(value=10)
y_max_entry = Entry(sidebar, textvariable=y_max_ui, width=5)
y_max_entry.grid(row=3, column=1)



t = RawTurtle(canvas)
tscreen = TurtleScreen(canvas)

resize_button = Button(sidebar, text="Resize graph", background="lightblue", command=screen_render) 
resize_button.grid(column=0, row=4, columnspan=2, pady=5)

derive_button = Button(sidebar,text="Derive at a Point", command=ui_derive_button, background="lightblue")
derive_button.grid(column=0, row = 5, columnspan=2)

drv_func_btn = Button(sidebar, text="Plot derivative of function", command=graph_drv_func, background="lightblue")
drv_func_btn.grid(column=0, row=6, columnspan=2, pady=5)

integral_calc_btn = Button(sidebar, text="Calculate integral between two points", command=ui_integrate_button, background="lightblue" )
integral_calc_btn.grid(column=0, row=7, columnspan=2)

alter_input_states([derive_button, drv_func_btn, resize_button, integral_calc_btn], "disabled")


SCREEN_WIDTH = canvas.winfo_width()
SCREEN_HEIGHT = canvas.winfo_height()
SCREEN_DOWN_Y = float(-10)
SCREEN_UP_Y = float(10)
SCREEN_LEFT_X = float(-10)
SCREEN_RIGHT_X = float(10)

screen = Screen(t, SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_DOWN_Y, SCREEN_UP_Y, SCREEN_LEFT_X, SCREEN_RIGHT_X)

screen.add_function(mathematical_function)
screen.render()
alter_input_states([derive_button, drv_func_btn, resize_button, integral_calc_btn], "normal")


main_ui.mainloop()