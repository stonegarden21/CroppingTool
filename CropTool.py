from pynput.mouse import Listener, Controller, Button
from PIL import Image, ImageGrab, ImageTk
import tkinter as tk
import time

root = tk.Tk()


########################## Set Variables ##########################
ix = None
iy = None

#Get the current screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()


#Get and print coordinates
def on_move(x, y):
    print('Pointer moved to {0}'.format( (x, y) ))

#Start and End mouse position
def on_click(x, y, button, pressed):
    global ix, iy
    if button == button.left:              
        #Left button pressed then continue
        if pressed:
            ix = x
            iy = y
            print('left button pressed at {0}'.format( (x, y) ))
        else:                
            print('left button released at {0}'.format( (x, y) ))
            canvas.create_rectangle(ix, iy, x, y, outline="red", width=5)#Draw a rectangle
            canvas.pack()
            img = ImageGrab.grab(bbox = (ix, iy, x, y))#Take the screenshot
            img.save('screenshot.png')#Save screenshot
            time.sleep(1)
            root.quit()#Quit tkinter window

    if not pressed:
        # Stop listener
        root.quit()#Quit tkinter window
        return False


#Print the screen width and height
print(screen_width, screen_height)


root_geometry = str(screen_width) + 'x' + str(screen_height) #Creates a geometric string argument
root.geometry(root_geometry) #Sets the geometry string value

root.overrideredirect(True)
root.wait_visibility(root)
root.wm_attributes("-alpha", 0.1)#Set window transparent


canvas = tk.Canvas(root, width=screen_width, height=screen_height)#Crate canvas
canvas.config(cursor="cross")#Change mouse pointer to cross
canvas.pack()
time.sleep(1)

# Collect events until released
with Listener(on_move=on_move, on_click=on_click) as listener:
    root.mainloop()#Loop tkinter
    listener.join()
    
