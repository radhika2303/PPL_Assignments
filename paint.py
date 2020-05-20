from tkinter import *
from tkinter import ttk,colorchooser


class Paint(object):

    DEFAULT_PEN_SIZE = 5.0
    DEFAULT_PEN_COLOR = 'black'
    DEFAULT_BG_COLOR  = 'white'


    def __init__(self): 
        self.root = Tk()
        
        self.pen_button = Button(self.root, text='Pen', command=self.use_pen)
        self.pen_button.grid(row=0, column=0)

        self.brush_button = Button(self.root, text='Brush', command=self.use_brush)
        self.brush_button.grid(row=0, column=1)

        self.color_fg_button = Button(self.root, text='Pen Color', command=self.choose_color_fg)
        self.color_fg_button.grid(row=0, column=2)
        
        self.color_bg_button = Button(self.root, text='Background Color', command=self.choose_color_bg)
        self.color_bg_button.grid(row=0, column=3)

        self.eraser_button = Button(self.root, text='Eraser', command=self.use_eraser)
        self.eraser_button.grid(row=0, column=4)

        self.choose_size_button = Scale(self.root, from_=1, to=10, orient=HORIZONTAL)
        self.choose_size_button.grid(row=0, column=5)
        
        self.clear_button = Button(self.root, text='Clear All', command=self.use_clear)
        self.clear_button.grid(row=0, column=6)

        self.c = Canvas(self.root, bg='white', width=1000, height=800)  
        self.c.grid(row=1, columnspan=7)

        self.setup()
        self.root.title('Draw your heart out!')   #providing title to the application
        self.root.mainloop()  # tells Python to run the Tkinter event loop

    def setup(self):
        self.old_x = None
        self.old_y = None
        self.line_width = self.choose_size_button.get()
        self.color_fg = self.DEFAULT_PEN_COLOR
        self.color_bg = self.DEFAULT_BG_COLOR
        self.eraser_on = False
        self.active_button = self.pen_button
        self.c.bind('<B1-Motion>', self.paint)   #for motion of mouse
        self.c.bind('<ButtonRelease-1>', self.reset)

    def use_pen(self):
        self.activate_button(self.pen_button)

    def use_brush(self):
        self.activate_button(self.brush_button)

    def choose_color_fg(self):
        self.eraser_on = False
        self.color_fg = colorchooser.askcolor(color=self.color_fg)[1]    #to change pen color

    def use_eraser(self):
    	self.activate_button(self.eraser_button, eraser_mode=True)
    
    def use_clear(self):
        self.c.delete(ALL)
        
    def use_undo(self):
        cur_tag = int(self.tag[1])
        if cur_tag >= 1:
            self.c.delete("tag"+str(cur_tag-1))
            self.tag = ["tag", str(cur_tag - 1)] 
            
    
    def choose_color_bg(self):  #changing the background color canvas
        self.color_bg = colorchooser.askcolor(color=self.color_bg)[1]
        self.c['bg'] = self.color_bg
     

    def activate_button(self, some_button, eraser_mode=False):
        self.active_button.config(relief=RAISED)
        some_button.config(relief=SUNKEN)
        self.active_button = some_button 
        self.eraser_on = eraser_mode   

    def paint(self, event):
        self.line_width = self.choose_size_button.get()
        paint_color = 'white' if self.eraser_on else self.color_fg
        if self.old_x and self.old_y:
            self.c.create_line(self.old_x, self.old_y, event.x, event.y,
                               width=self.line_width, fill=paint_color,
                               capstyle=ROUND, smooth=TRUE, splinesteps=36)
        self.old_x = event.x
        self.old_y = event.y

    def reset(self, event):
        self.old_x = None 
        self.old_y = None


if __name__ == '__main__':
	Paint()
	
