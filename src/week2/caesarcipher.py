SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!?.'
# key = 3

message = input("What's your message? ")
givekey = input("Do you want to give a key? ")

mode = ""
while mode.lower() != "e" and mode.lower() != "d":
  mode = input("Encrypt or Decrypt? [E/D] ")
newMessage = ""

for char in message:
  if char in SYMBOLS:
    if mode.lower()== "e":
      position = SYMBOLS.find(char) + key
    else:
      position = SYMBOLS.find(char) - key
    
    if position > len(SYMBOLS):
      position = position - len(SYMBOLS) 
    elif position < 0:
      position = len(SYMBOLS)+position 
    
    newMessage = newMessage + SYMBOLS[position]
   
  else:
    newMessage = newMessage + char
    

print(newMessage)