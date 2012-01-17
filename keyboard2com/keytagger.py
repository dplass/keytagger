# import WIN32API 
# import win32console 
# import win32gui 
import pythoncom, pyHook, sys, serial, time, os
import ctypes, Queue, threading
import ImageGrab, ImageDraw # PIL

def OnKeyboardEvent(event):
  print "%d\t%d\t%d\t%d\t%s\t%d\t%s\tkey"%(event.Time, event.KeyID%256, event.KeyID, event.ScanCode, event.Key, event.Window, event.WindowName)
  try:
    q.put(event.KeyID%256)
  except TypeError:
    pass
  # if event.Key == "Pause": 
    # print "EXIT"

def OnMouse(event):
  print "%d\t%d\t%d\t%s\t%d\t%d\t%s\tmouse"%(event.Time, event.Message%256, event.Message, str(event.Position), event.Wheel, event.Window, event.WindowName)
  q.put(event.Message%256)
  
  # TODO screenshots don't work in-game ...
  # img=ImageGrab.grab() # unfortunately does not grab the mouse pointer.
  # draw = ImageDraw.Draw(img) 
  # padding = 3
  # draw.rectangle([event.Position[0]-padding,event.Position[1]-padding, event.Position[0]+padding,event.Position[1]+padding], outline="red", fill="red") # draw dot in location of mouse?
  # SaveDirectory='screenshots'
  # fname = 'ScreenShot_'+time.strftime("%Y%m%d_%H%M%S")+'.jpg'
  # img.save(os.path.join(SaveDirectory,fname))
  # del draw
  
def OnMouseWheel(event):
  print "%d\t%d\t%d\t%s\t%d\t%d\t%s\tmouse"%(event.Time, event.Message%256, event.Message, str(event.Position), event.Wheel, event.Window, event.WindowName)
    
def worker():
  while True:
    item = q.get()
    ser.write(chr(item))
    
ser = serial.Serial('\\\\.\\COM6')
q = Queue.Queue()
hm = pyHook.HookManager() 

hm.KeyDown = OnKeyboardEvent
hm.HookKeyboard() 

hm.MouseAllButtons = OnMouse
hm.MouseWheel = OnMouseWheel # no mevent markers to COM port
hm.HookMouse()

threading.Thread(target=worker).start()

pythoncom.PumpMessages() 

hm.UnhookKeyboard()
hm.UnhookMouse()