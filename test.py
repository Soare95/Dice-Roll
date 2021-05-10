from tkinter import *
import tkinter
from PIL import Image, ImageTk


root = tkinter.Tk()
root.geometry('400x400')
root.resizable(0,0)
root.title('Dice rolling')

dice = ['dice1.png', 'dice2.png', 'dice3.png', 'dice4.png', 'dice5.png', 'dice6.png']
roll_dice1 = Image.open(r'C:\Users\so4re\Desktop\Applications\Programs\Dice roll\dice1.JPG')
roll_dice2 = Image.open(r'C:\Users\so4re\Desktop\Applications\Programs\Dice roll\dice2.JPG')
roll_dice3 = Image.open(r'C:\Users\so4re\Desktop\Applications\Programs\Dice roll\dice3.JPG')
roll_dice4 = Image.open(r'C:\Users\so4re\Desktop\Applications\Programs\Dice roll\dice4.JPG')
roll_dice5 = Image.open(r'C:\Users\so4re\Desktop\Applications\Programs\Dice roll\dice5.JPG')
roll_dice6 = Image.open(r'C:\Users\so4re\Desktop\Applications\Programs\Dice roll\dice6.JPG')

render1 = ImageTk.PhotoImage(roll_dice1)
image1 = Label(image=render1)
image1.image = render1
image1.place(x=0, y=0)



root.mainloop()

