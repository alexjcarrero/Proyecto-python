x = int(input("ingrese un numero: ")) 
if(x >= 0 and x <= 365):

    if (x % 7 == 0) :
        print(0)
    elif(x % 7 == 1) :
        print(1) 
    elif(x % 7 == 2) :
        print(2)
    elif(x % 7 == 3):
        print(3)    
    elif(x % 7 == 4):
        print(4)
    elif(x % 7 == 5):    
        print(5) 
    elif(x % 7 == 6): 
        print(6)   
    elif (x % 7 == 7):
        print(7)
        pass    

else:
    
    print('Ha ingresado un numero mal')
    
    pass 





