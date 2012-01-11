# import WIN32API 
# import win32console 
# import win32gui 
import pythoncom, pyHook, sys, serial, time
import ctypes, Queue, threading

def OnKeyboardEvent(event):
  print "%d\t%d\t%s\t%d\t%s"%(event.KeyID, event.ScanCode, event.Key, event.Window, event.WindowName)
  try:
    q.put(event.KeyID)
  except TypeError:
    pass
  # if event.Key == "Pause": 
    # print "EXIT"

def worker():
  while True:
    item = q.get()
    ser.write(chr(item))
    
ser = serial.Serial('\\\\.\\COM6')
q = Queue.Queue()
hm = pyHook.HookManager() 
hm.KeyDown = OnKeyboardEvent 
hm.HookKeyboard() 

threading.Thread(target=worker).start()

pythoncom.PumpMessages() 