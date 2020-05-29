from tkinter import *
from tkinter import ttk
from tkinter.ttk import Scale
from tkinter import colorchooser, filedialog, messagebox
import tkinter as tk
import PIL.ImageGrab as ImageGrab
from PIL import ImageTk, Image

class Paint():
    
    def __init__(self, root):
        self.root = root
        self.root.title("Paint Application")
        self.root.geometry("900x750")
        self.root.configure(background='white')
        self.item = None

        self.old_x = None
        self.old_y = None

        self.width_val = self.root.winfo_screenwidth()
        self.height_val = self.root.winfo_screenheight()

        self.pen_color = 'black'
        self.eraser_color = 'white'
        self.save_color = self.pen_color
   
          
        self.clear_image = PhotoImage(file='signs.png')
        self.clear_button = Button(self.root, image=self.clear_image, command=self.clear, width=64)
        self.clear_button.grid(row=1, column=0, pady=(5,0))
    
      
        self.eraser_image = PhotoImage(file='eraser.png')
        self.eraser_button = Button(self.root, image = self.eraser_image, command=self.eraser, width = 64)
        self.eraser_button.grid(row=1, column=1, pady=(5, 0))
        self.eraser_button.config(cursor="hand2")
        
        self.line_image = PhotoImage(file='line.png')
        self.line_button = Button(self.root, image=self.line_image, command=self._createLine, width=64)
        self.line_button.grid(row=1, column=2, pady=(5, 0))
        self.line_button.config(cursor="hand2")
    
        self.rectangle_image = PhotoImage(file='rectangle.png')
        self.rectangle_button = Button(self.root, image=self.rectangle_image, command=self._createRectangle, width=64)
        self.rectangle_button.grid(row=1, column=3, pady=(5, 0))
        self.rectangle_button.config(cursor="hand2")
        
        self.oval_image = PhotoImage(file='oval.png')
        self.oval_button = Button(self.root, image=self.oval_image, command=self._createOval, width=64)
        self.oval_button.grid(row=1, column=4, pady=(5, 0))
        self.oval_button.config(cursor="hand2")
        
        self.pencil_image = PhotoImage(file='pencil.png')
        self.pencil_button = Button(self.root, image=self.pencil_image, command=self._pencil, width=64)
        self.pencil_button.grid(row=1, column=5, pady=(5, 0))
        self.pencil_button.config(cursor="hand2")
      
        self.pen_size_scale_frame = Frame(self.root, bd=5, relief=RIDGE)
        self.pen_size_scale_frame.grid(row=2, column=0,  pady=5)
        
        self.pen_size = Scale(self.pen_size_scale_frame, orient = VERTICAL, from_ = 30, to = 2, length=170)
        self.pen_size.set(1)
        self.pen_size.grid(row=0, column=1, padx=15, pady=5)
        self.pen_size.config(cursor="hand2")

        self.canvas = Canvas(self.root, bg='white', relief=GROOVE, height=self.height_val, width=self.width_val, cursor="crosshair")
        self.canvas.place(x=70, y=50)
        
        self.canvas.bind("<B1-Motion>", self.paint)
        self.canvas.bind("<ButtonRelease-1>", self.reset)


        menu = Menu(self.root)
        self.root.config(menu=menu)
        
        colormenu = Menu(menu)
        menu.add_cascade(label='Colors',menu=colormenu)
        colormenu.add_command(label='Brush Color',command=self.brush_color)
        
        
    def _createRectangle(self):
        self.rectx0 = 0
        self.recty0 = 0
        self.rectx1 = 0
        self.recty1 = 0
        self.rectid = None
        self.pen_color = self.save_color
        self.canvas.config(cursor="fleur")
        self.canvas.unbind("<Button-1>")
        self.canvas.unbind("<ButtonRelease-1>")
        self.canvas.unbind("<B1-Motion>")
        self.canvas.bind( "<Button-1>", self.startRect )
        self.canvas.bind( "<ButtonRelease-1>", self.stopRect )
        self.canvas.bind( "<B1-Motion>", self.movingRect )


    def startRect(self, event):
        self.rectx0 = self.canvas.canvasx(event.x)
        self.recty0 = self.canvas.canvasy(event.y) 

        self.rectid = self.canvas.create_rectangle(
            self.rectx0, self.recty0, self.rectx0, self.recty0, outline=self.pen_color, width=self.pen_size.get())

    def movingRect(self, event):
        self.rectx1 = self.canvas.canvasx(event.x)
        self.recty1 = self.canvas.canvasy(event.y)

        self.canvas.coords(self.rectid, self.rectx0, self.recty0,
                      self.rectx1, self.recty1)

    def stopRect(self, event):
        self.rectx1 = self.canvas.canvasx(event.x)
        self.recty1 = self.canvas.canvasy(event.y)
 
        self.canvas.coords(self.rectid, self.rectx0, self.recty0,
                      self.rectx1, self.recty1)


    def _createOval(self):
        self.ovalx0 = 0
        self.ovaly0 = 0
        self.ovalx1 = 0
        self.ovaly1 = 0
        self.ovalid = None
        self.pen_color = self.save_color
        self.canvas.config(cursor="fleur")
        self.canvas.unbind("<Button-1>")
        self.canvas.unbind("<ButtonRelease-1>")
        self.canvas.unbind("<B1-Motion>")
        self.canvas.bind( "<Button-1>", self.startOval )
        self.canvas.bind( "<ButtonRelease-1>", self.stopOval )
        self.canvas.bind( "<B1-Motion>", self.movingOval )


    def startOval(self, event):
        self.ovalx0 = self.canvas.canvasx(event.x)
        self.ovaly0 = self.canvas.canvasy(event.y) 
    
        self.ovalid = self.canvas.create_oval(
            self.ovalx0, self.ovaly0, self.ovalx0, self.ovaly0, outline=self.pen_color, width=self.pen_size.get())

    def movingOval(self, event):
        self.ovalx1 = self.canvas.canvasx(event.x)
        self.ovaly1 = self.canvas.canvasy(event.y)

        self.canvas.coords(self.ovalid, self.ovalx0, self.ovaly0,
                      self.ovalx1, self.ovaly1)

    def stopOval(self, event):
        self.ovalx1 = self.canvas.canvasx(event.x)
        self.ovaly1 = self.canvas.canvasy(event.y)
  
        self.canvas.coords(self.ovalid, self.ovalx0, self.ovaly0,
                      self.ovalx1, self.ovaly1)



    def _createLine(self):
        self.linex0 = 0
        self.liney0 = 0
        self.linex1 = 0
        self.liney1 = 0
        self.lineid = None
        self.pen_color = self.save_color
        self.canvas.config(cursor="tcross")
        self.canvas.unbind("<Button-1>")
        self.canvas.unbind("<ButtonRelease-1>")
        self.canvas.unbind("<B1-Motion>")
        self.canvas.bind( "<Button-1>", self.startLine )
        self.canvas.bind( "<ButtonRelease-1>", self.stopLine )
        self.canvas.bind( "<B1-Motion>", self.movingLine )

    def startLine(self, event):
        self.linex0 = self.canvas.canvasx(event.x)
        self.liney0 = self.canvas.canvasy(event.y) 
    
        self.lineid = self.canvas.create_line(
            self.linex0, self.liney0, self.linex0, self.liney0, fill=self.pen_color, width = self.pen_size.get(), smooth=True, capstyle=ROUND)

    def movingLine(self, event):
        self.linex1 = self.canvas.canvasx(event.x)
        self.liney1 = self.canvas.canvasy(event.y)
    
        self.canvas.coords(self.lineid, self.linex0, self.liney0,
                      self.linex1, self.liney1)

    def stopLine(self, event):
        self.linex1 = self.canvas.canvasx(event.x)
        self.liney1 = self.canvas.canvasy(event.y)
  
        self.canvas.coords(self.lineid, self.linex0, self.liney0,
                      self.linex1, self.liney1)
   

    def _pencil(self):
        self.pen_color = self.save_color
        self.canvas.config(cursor="crosshair")
        self.canvas.unbind("<Button-1>")
        self.canvas.unbind("<ButtonRelease-1>")
        self.canvas.unbind("<B1-Motion>")
        self.canvas.bind("<B1-Motion>", self.paint)
        self.canvas.bind("<ButtonRelease-1>", self.reset)

    def clear(self):
        self.canvas.delete(ALL)
        self.canvas.configure(background='white')

    def paint(self, event):
        if self.old_x and self.old_y:
            self.canvas.create_line(self.old_x,self.old_y,event.x,event.y,
            width=self.pen_size.get(),fill=self.pen_color,capstyle=ROUND,smooth=True)
            

        self.old_x = event.x
        self.old_y = event.y


    def reset(self,e): 
        self.old_x = None
        self.old_y = None

    

    def select_color(self, col):
        self.pen_color = col
        self.save_color = col

    def eraser(self):
        self.canvas.config(cursor="dotbox")
        self.canvas.unbind("<Button-1>")
        self.canvas.unbind("<ButtonRelease-1>")
        self.canvas.unbind("<B1-Motion>")
        self.canvas.bind("<B1-Motion>", self.paint)
        self.canvas.bind("<ButtonRelease-1>", self.reset)
        self.pen_color = self.eraser_color

    def brush_color(self):
        self.pen_color=colorchooser.askcolor(color=self.pen_color)[1]
        self.save_color = self.pen_color



if __name__ == "__main__":
    root = Tk()
    root.style = ttk.Style()
    root.style.theme_use('clam')
    p = Paint(root)
    root.mainloop()