#   aExperimentTkinter5CalcConvert.py
#     Uses Entry widget 13.6 p651-653

import tkinter
import tkinter.messagebox  # use Messagebox widget to display results

def main():
    MyGUI()   # create object window


class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.main_window.title("Christian Ramirez-Flores's Calculator :)")
# Code to add widgets will go here...

#  create 2 frames to hold labels
        self.top_frame = tkinter.Frame(self.main_window) # top frame for label & input
        self.bottom_frame = tkinter.Frame(self.main_window) # bottom frame for buttons
        self.middle_frame = tkinter.Frame(self.main_window)
        self.result_frame = tkinter.Frame(self.main_window)

# label widgets created text & Entry Box
        self.prompt1 = tkinter.Label(self.top_frame,   #Enter prompt
                                    text='Variable 1:',
                                             borderwidth=2,
                                             relief='raised', width=15)
#                Entry box invocation
        self.self_kilo_entry = tkinter.Entry(self.top_frame,width=10)

# my newly added section for second variable
        self.prompt2 = tkinter.Label(self.bottom_frame,
                                    text='Variable 2:',
                                             borderwidth=2,
                                             relief='raised', width=15)
        self.self_kilo_entry2 = tkinter.Entry(self.bottom_frame,width=10)
##newly added section ^

# pack the labels on the top frame in window
        self.prompt1.pack(side='left', padx=20, pady=20)
        self.self_kilo_entry.pack(side='left', padx=20, pady=20)

        self.prompt2.pack(side='left', padx=20, pady=20)
        self.self_kilo_entry2.pack(side='left', padx=30, pady=30)

#   create button widgets in the bottom frame
        self.divide_button = tkinter.Button(self.bottom_frame,text='Divide', command=self.divide_click) 
        self.multiply_button = tkinter.Button(self.bottom_frame,text='Multiply', command=self.multiply_click)
        self.add_button = tkinter.Button(self.bottom_frame,text='Add', command=self.add_click)
        self.subtract_button = tkinter.Button(self.bottom_frame,text='Subtract', command=self.subtract_click)                                
        self.quit_button = tkinter.Button(self.bottom_frame,text='Quit',  # destroy method
                                            command=self.main_window.destroy)                                  

# pack the buttons on the bottom frame
        self.multiply_button.pack(side='top', padx=50, pady=50)
        self.divide_button.pack(side='top', padx=50, pady=50)
        self.add_button.pack(side='top', padx=50, pady=50)
        self.subtract_button.pack(side='top', padx=50, pady=50)
        self.quit_button.pack(side='top', padx=50, pady=50)

# results
        self.result_label = tkinter.Label (self.result_frame, text='Result: ')
        self.result_label.pack(pady=15)

# Now pack the frames in the window
        self.top_frame.pack()
        self.bottom_frame.pack()
        self.middle_frame.pack()
        self.result_frame.pack()
        tkinter.mainloop()   # infinite loop to hold window on screen




    # Methods below are class methods so the button callbacks can use them.
    def do_calc(self, operation):
        try:
            num1: float = float(self.self_kilo_entry.get())
            num2: float = float(self.self_kilo_entry2.get())

            if operation == "+":
                result = num1 + num2
            elif operation == "-":
                result = num1 - num2
            elif operation == "*":
                result = num1 * num2
            elif operation == "/":
                if num2 == 0:
                    tkinter.messagebox.showerror("Error", "Cannot divide by zero")
                    return
                result = num1 / num2
            else:
                tkinter.messagebox.showerror("Error", "Unknown operation")
                return

            self.result_label.config(text=f"Result: {result:,.2f}")
        except ValueError:
            tkinter.messagebox.showerror(
                "Invalid Input",
                "Please enter a valid floating-point number in both fields.")

    def add_click(self):
        self.do_calc('+')

    def subtract_click(self):
        self.do_calc('-')

    def multiply_click(self):
        self.do_calc('*')

    def divide_click(self):
        self.do_calc('/')


if __name__ == '__main__':
    main()   # execute main module