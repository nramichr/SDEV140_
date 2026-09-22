#   aExperimentTkinter5CalcConvert.py
#     Uses Entry widget 13.6 p651-653
import tkinter
import tkinter.messagebox     # use Messagebox widget to display results

def main():
    MyWindow=MyGUI()   # create object window
class MyGUI:
    def __init__(self):
        self.top = tkinter.Tk()     # Create main window object top
        self.top.title('Conver Kilmeters to miles')  # top title
# Code to add widgets will go here...
#  create 2 frames to hold labels
        self.top_frame = tkinter.Frame(self.top) # top frame for label & input
        self.bottom_frame = tkinter.Frame(self.top) # bottom frame for buttons
        self.middle_frame = tkinter.Frame(self.top)
# label widgets created text & Entry Box
        self.prompt1 = tkinter.Label(self.top_frame,   #Enter prompt
                                    text='Enter a floating number(test1)',
                                             borderwidth=2,
                                             relief='raised'  )
#                Entry box invocation
        self.kilo_entry = tkinter.Entry(self.top_frame,width=10)
# my newly added section
        self.prompt2 = tkinter.Label(self.bottom_frame,
                                    text='Enter a floating number(test2)',
                                             borderwidth=2,
                                             relief='raised'  )
        self.kilo_entry2 = tkinter.Entry(self.top_frame,width=10)
##newly added section ^
# pack the labels on the top frame in window
        self.prompt1.pack(side='left',ipadx=20, ipady=20,  #inside padding
                         padx=25 , pady=35)   #outside padding
        self.prompt2.pack(side='left',ipadx=20, ipady=20,  #inside padding  #newentry
                                 padx=25 , pady=35)   #outside padding
        self.kilo_entry.pack(side='left',ipadx=30, ipady=30,
                         padx=20 , pady=20 )
        self.kilo_entry2.pack(side='left',ipadx=30, ipady=30, #newentry
                                 padx=20 , pady=20 )
#   create button widgets in the bottom frame
        self.calc_button = tkinter.Button(self.bottom_frame,text='Multiply',command=self.do_calc) 
        self.divide_button = tkinter.Button(self.bottom_frame,text='Divide',command=self.do_calc) 
        self.multiply_button = tkinter.Button(self.bottom_frame,text='Multiply',command=self.do_calc)
        self.add_button = tkinter.Button(self.bottom_frame,text='Add',command=self.do_calc)
        self.subtract_button = tkinter.Button(self.bottom_frame,text='Subtract',command=self.do_calc)                                
        self.quit_button = tkinter.Button(self.bottom_frame,text='Quit',  # destroy method
                                            command=self.top.destroy)                                  
# pack the buttons on the bottom frame
        self.calc_button.pack(ipadx=20, ipady=20,  #inside padding
                         padx=25 , pady=35)   #outside padding
        
        self.quit_button.pack(ipadx=10, ipady=10,  #inside padding
                         padx=30 , pady=20)   #outside paddin
# Now pack the frames in the window
        self.top_frame.pack()
        self.bottom_frame.pack()
        self.middle_frame.pack()

        tkinter.mainloop()   # infinite loop to hold window on screen

# Code to add widgets will go here...
# methods below...
    def do_calc(self): ###program name
        # Calculate from data entered
        kilo = float(self.kilo_entry.get())  # get from entry box
        cm = kilo * 100000
        miles = cm / 2.54 / 12 / 5280 
        # Display an information dialog box
        tkinter.messagebox.showinfo('Result',
                                    f'Calculated result is {miles:10.2f} miles.')
if __name__ == '__main__':
    main()   # execute main module
