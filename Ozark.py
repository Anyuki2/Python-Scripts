from ast import FunctionDef
import os 
import sys 
import time

os.system('cls' if os.name == 'nt' else 'clear')
logo = '''
 $$$$$$\                               $$\       
$$  __$$\                              $$ |      
$$ /  $$ |$$$$$$$$\ $$$$$$\   $$$$$$\  $$ |  $$\ 
$$ |  $$ |\____$$  |\____$$\ $$  __$$\ $$ | $$  |
$$ |  $$ |  $$$$ _/ $$$$$$$ |$$ |  \__|$$$$$$  / 
$$ |  $$ | $$  _/  $$  __$$ |$$ |      $$  _$$<  
 $$$$$$  |$$$$$$$$\\$$$$$$$ |$$ |      $$ | \$$\ 
 \______/ \________|\_______|\__|      \__|  \__|

       {+}  Code By Anyuki2 {+}
      {+}  Instagram: Anyuki2 {+}                                            
{+} Github: Https://Github.com/Anyuki2 {+}  
        Copyright of Anyuki, 2022                                              
    '''
menu ='''
    {1}--Ip lookup
    {2}--
    {3}--
    {4}--
    {5}--
    {6}--
    {7}--
    {8}--
    {99}-Exit

    WARNING! THIS TOOL IS MEANT FOR LINUX DEVICES, SOME FEATURES MIGHT NOT WORK AS INTENDED 
    '''
print (logo)
print (menu)

def quit():
    con = input('Exit? [Y/n] >')
    if con[0].upper() == 'N':
        exit()
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        print (logo)
        print (menu)
        select() 

def select():
    try:
        choice = input("Ozark# ")
        if choice == "1":
          d3 = input('Enter IP or Domain ')
          os.system('cls' if os.name == 'nt' else 'clear')
          
          
          frame = '''
$$$$$$\              $$\           $$\                                    $$\     $$\                     
$$  __$$\            $$ |          $$ |                                   $$ |    \__|                    
$$ /  \__| $$$$$$\ $$$$$$\         $$ |      $$$$$$\   $$$$$$$\ $$$$$$\ $$$$$$\   $$\  $$$$$$\  $$$$$$$\  
$$ |$$$$\ $$  __$$\\_$$  _|        $$ |     $$  __$$\ $$  _____|\____$$\\_$$  _|  $$ |$$  __$$\ $$  __$$\ 
$$ |\_$$ |$$$$$$$$ | $$ |          $$ |     $$ /  $$ |$$ /      $$$$$$$ | $$ |    $$ |$$ /  $$ |$$ |  $$ |
$$ |  $$ |$$   ____| $$ |$$\       $$ |     $$ |  $$ |$$ |     $$  __$$ | $$ |$$\ $$ |$$ |  $$ |$$ |  $$ |
\$$$$$$  |\$$$$$$$\  \$$$$  |      $$$$$$$$\\$$$$$$  |\$$$$$$$\\$$$$$$$ | \$$$$  |$$ |\$$$$$$  |$$ |  $$ |
 \______/  \_______|  \____/       \________|\______/  \_______|\_______|  \____/ \__| \______/ \__|  \__/ 
 '''
          print (frame) 
          time.sleep(1)
          print('Getting Location.........')
          time.sleep(4)
          os.system("curl ip-api.com/" + d3)
          quit()
        
        elif choice == "99":
            os.system('cls' if os.name == 'nt' else 'clear')
            print("bye bye")
            quit()

    except Exception:
        print('Error')
select()