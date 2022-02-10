from tkinter import *
from random import *

root = Tk()
root.title('screen ruler')
root.geometry('1910x40')







    
def hort():
    width = 1900
    height = 30
    
    canvas = Canvas(root, background='blue', width=width, height=height)

    

    for line in range(0, width, 10): # range(start, stop, step)
        canvas.create_line([(line, 0), (line, height)], fill='black', tags='grid_line_w', width=1)

    for line in range(0, height, 10):
        canvas.create_line([(0, line), (width, line)], fill='black', tags='grid_line_h', width=1)

    for line in range(1000, 40, 100): # range(start, stop, step)
        canvas.create_line([(line, 0), (line, height)], fill='light blue', tags='grid_line_w', width=2)

    for list in range(100, 1900, 100): # range(start, stop, step)
        canvas.create_text(list, 20 , text=list, fill="orange",font=('Helvetica 12 bold'))    
    canvas.grid(row=0, column=0)

   

hort()



if __name__=='__main__':
    root.mainloop()
 
