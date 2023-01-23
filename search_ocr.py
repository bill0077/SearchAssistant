import sys
if sys.version_info[0] == 2:  # Just checking your Python version to import Tkinter properly.
    import Tkinter as tk
else:
    import tkinter as tk
    
try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract

from PIL import ImageGrab
import pyautogui

#from selenium import webdriver
import webbrowser

import time

#import cv2
#print(cv2.__version__)

    
def draw_rect(event):
    global x0, y0
    global start_x, start_y
    global rect
    x0=event.x
    y0=event.y
    canvas.delete(rect)
    rect = canvas.create_rectangle( start_x, start_y, x0, y0, outline = "green", width = "5" )
    #print("draw", start_x, start_y, x0, y0)

def mouse_down(event):
    global x0, y0
    global start_x, start_y
    global rect
    start_x, start_y = event.x, event.y
    rect = canvas.create_rectangle( 0,0,0,0, outline = "green", width = "0" )

def mouse_up(event):
    global start_x, start_y
    global x0, y0
    global text_from_image
    #x0=event.x
    #y0=event.y
    #canvas.delete("all")
    #pytesseract.pytesseract.tesseract_cmd = r'C:\Users\bill0\anaconda3\envs\search_assist\Library\bin\tesseract.exe'
    
    rect_img = pyautogui.screenshot('rect.jpg', region=(min(start_x, x0), min(start_y, y0), max(start_x, x0)-min(start_x, x0), max(start_y, y0)-min(start_y, y0)))

    text_from_image = pytesseract.image_to_string(rect_img)
    print(text_from_image)
    
    url="https://www.google.com/search?q="+text_from_image
    webbrowser.get().open(url)
    
    canvas.delete("all")
    mainframe.destroy()
    
    #mainframe.destroy()
    
def return_event(event):
    global text_from_image
    '''driver = webdriver.Chrome() 
    options=webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    url="https://www.google.com/search?q="+text_from_image
    driver.get(url)
    #time.sleep(10)
    driver.implicitly_wait(60)'''
    #time.sleep(60)
    url="https://www.google.com/search?q="+text_from_image
    webbrowser.get().open(url)
    
    #mainframe.attributes("-fullscreen", False)
    #mainframe.attributes("-alpha", 1)
    mainframe.destroy()
    
    
    #element = driver.find_element_by_name("q")
    #element.send_keys(text_from_image)
    #element.submit()
    
def escape_event(event):
    global state
    if state==True:
        canvas.delete("all")
        mainframe.attributes("-fullscreen", False)
        mainframe.attributes("-alpha", 1)
    else:
        mainframe.attributes("-fullscreen", True)
        mainframe.attributes("-alpha", 0.3)
    
    
global state    
state=True

mainframe = tk.Tk()
mainframe.attributes("-alpha", 0.3)
mainframe.attributes("-fullscreen", True)

canvas = tk.Canvas(mainframe)
canvas.pack(fill=tk.BOTH, expand=True)

mainframe.bind("<B1-Motion>", draw_rect)
mainframe.bind("<Button-1>", mouse_down)
mainframe.bind("<ButtonRelease-1>", mouse_up)
mainframe.bind('<Return>', return_event)
mainframe.bind("<Escape>", escape_event)

mainframe.bind("<F11>", lambda event: mainframe.attributes("-fullscreen", not root.attributes("-fullscreen")))

#root.attributes("-alpha", 0)

mainframe.mainloop()