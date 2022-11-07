#from  random keyword
import random
#printing 1st diceroll
p=random.randint(1,6)
print("Rolling dice...\nnumber rolled on dice is::",p,"\n")
#while loop to play multiple times
while True:
    q=random.randint(1,6)
    #asking user to play again
    ans=input("Do you want to play again\nif yes press y: ")
    if ans == "y" or ans=="Y": # executes if user interested
        print("Rolling dice...\nnumber rolled on dice is::",q,"\n")
    else:
        #break loop if user don't want to play more 
        break