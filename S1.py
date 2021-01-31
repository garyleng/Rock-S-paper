import random
import os
import time

def clear():
    os.system("clear")
def rps():
    global rps_t
    global win_map
    global name    
#game function:

rps_t=[[-1,1,0],[0,-1,2], [1,2,-1]]
win_map={0: 'rock', 1:'scissor' , 2: 'paper' }    
    
f=input('Enter first name:')
l=input('Enter last name:')
name=(f+l)
print()
print('Greetings' , name)
print()
print('How are you doing today?')
print()
a=input('Good or bad? ')
print()
if  a == ('good'):
    print('That\'s great!')

elif a==('bad' ):
    print('Do you want to talk about it?')
    print()
    b=input('Let\'s play a mini game! yes? no?')
    if b==('yes' ):
        print()
        print('Ok! Enter \" Rock\" Scissor\" Paper\" to play')
        #player input
        i=input('Rock\"! Scissor\"! Paper!: ')
        if i.lower()== 'rock' :
            p_m= 0
           
        elif i.lower()== 'scissor':
            p_m= 1
           
        elif i.lower()== 'paper':
            p_m= 2
           
        else:
            print('try again Rock\"! Scissor\"! Paper!')

        print(' Suprise!')
        print()
        time.sleep(0)

        com=random.randint(0,2)
        
        
        #computer choice
        print(win_map[com].upper())
        #find winner
        w=rps_t[p_m][com]
        #declare winner
        
        if w == p_m:
            print(f, 'Won!?')
        elif w== com:
            print(' Oh yeah i won')
        else:
            print('Tie')
        print()
        time.sleep(2)
        clear()
            

    

        







else :
    print('I dont get what you mean')
        
            
        
            
    

