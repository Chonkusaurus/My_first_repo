redo = True
    
print("Hello Chonkus!")
while redo == True:
    eep = input("is the chonkus eepy y/n?  ")
    i=0
    if eep == "y":
        print("that would be correct")
    elif eep =="n":
        for i in range(3):
            print("EEPY TIME!!")
            redo = False
    else:
            
            print("I said y/n >:(")
            redo = True
