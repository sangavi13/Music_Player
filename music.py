from tkinter import *

from PIL import ImageTk, Image
import pygame
#from pygame import mixer
from tkinter import filedialog
from tkinter import messagebox
window=Tk()
window['bg'] = 'blue'
window.geometry('300x250')
window.title('music player')
pygame.init()
pygame.mixer.init()

pause_music=False
def browse():
    global file_name
    file_name=filedialog.askopenfile_name()
def ply_button():
    if pause_music==False:
        pygame.mixer.music.load(file_name)
        pygame.mixer.music.play()
        img_label=label(window,bg='#faf6e1',text='file_name',fg='#00267d',anchor=CENTER,height=10,width=30,justify=CENTER,wraplength=90,font=("Helivetica",10,"bold"))
        img_label.place(x=12,y=15)
    else:
        img_label = label(window, bg='#faf6e1', text='file_name', fg='#00267d', anchor=CENTER, height=10, width=30,
                          justify=CENTER, wraplength=90, font=("Helivetica", 10, "bold"))
        img_label.place(x=12, y=15)
        pygame.mixer.music.unpause()
def stop_button():
    global pause_music
    pause_music=False
    pygame.mixer.music.stop()

def pause_button():
    global pause_music
    pause_music = True
    pygame.mixer.music.pause()
def set_volume(value):
    vol=int(value)/100
    pygame.mixer.music.set_volume(vol)
def rewind_button():
    play_btn()

img_play=PhotoImage(file= "D:/")
play_btn=Button(window,image=img_play,borderwidth=0,bg='black',command=ply_button)
play_btn.place(anchor=S,X=170,y=230).pack()
img_pause=PhotoImage(file=r"C:\Users\NEW\Desktop\music py")
pause_btn=Button(window,image=img_pause,borderwidth=0,bg='black',command=pause_button)
play_btn.place(anchor=SE,X=200,y=230)
img_stop=PhotoImage(file="stop.png")
play_btn=Button(window,image=img_stop,borderwidth=0,bg='black',command=stop_button)
play_btn.place(anchor=SW,X=85,y=230)
img_rewind=PhotoImage(file="rewind.png")
rewind_btn=Button(window,image=img_rewind,borderwidth=0,bg='black',command=rewind_button)
rewind_btn.place(anchor=SE,X=140,y=230)
volume= Scale(window,from_=100,to=0,bg='blue',showvalue=0,orient=VERTICAL,command=set_volume)
volume.set=(65)
volume.place(x=260,y=54)
menu_bar=Menu(window)
window.config(menu=menu_bar)
sub_menu=Menu(menu_bar,tearoff=0)
menu_bar.add_cascade(label='file',menu=sub_menu)
menu_bar.add_cascade(label='open',commmand=browse)
menu_bar.add_cascade(label='exit',command=window.destroy)
sub_menu1=Menu(menu_bar,tearoff=0)
menu_bar.add_cascade(label='about us',command=about)

menu_bar.add_cascade(label='help',commmand=help)
Photo=ImageTK.PhotoImage(Image.open('music.jpg'))
img_label=label(window,image=photo)
img_label.place(x=20,y=25)
mainloop()






