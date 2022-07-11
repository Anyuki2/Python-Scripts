from ast import FunctionDef
import os 
import sys 
import time
import queue
import socket 
import threading
from queue import Queue

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
    {2}--Port scan 
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
          d3 = input('Enter IP or Domain# ')
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
        
        elif choice == "2":
            d4 = input('Ender Ip or Domain# ')
            os.system('cls' if os.name == 'nt' else 'clear')
            
            Scan = '''
$$\   $$\                                   
$$$\  $$ |                                  
$$$$\ $$ |$$$$$$\$$$$\   $$$$$$\   $$$$$$\  
$$ $$\$$ |$$  _$$  _$$\  \____$$\ $$  __$$\ 
$$ \$$$$ |$$ / $$ / $$ | $$$$$$$ |$$ /  $$ |
$$ |\$$$ |$$ | $$ | $$ |$$  __$$ |$$ |  $$ |
$$ | \$$ |$$ | $$ | $$ |\$$$$$$$ |$$$$$$$  |
\__|  \__|\__| \__| \__| \_______|$$  ____/ 
                                  $$ |      
                                  $$ |      
                                  \__|      
            '''
            print (Scan)
            time.sleep(1)
            print('Finding Open Ports.......')
            time.sleep(3)
            target = d4

            queue = Queue()
            open_ports = []


            def portscan(port):
                try:
                  sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                  sock.connect((target, port))
                  return True 
                except: 
                    return False

            def fill_queue(port_list): 
               for port in port_list:
                 queue.put(port)

            def worker():
                while not queue.empty():
                    port = queue.get()
                    if portscan(port):
                        print("Port {} is open!" .format(port))
                    open_ports.append(port)

            port_list = range(1, 1024)
            fill_queue(port_list)

            thread_list = []

            for t in range(100):
             thread = threading.Thread(target=worker)
             thread_list.append(thread)

            for thread in thread_list:
             thread.start()

            for thread in thread_list:
             thread.join() 

             print("Open port are: ", open_ports)
             

        elif choice == "99":
            os.system('cls' if os.name == 'nt' else 'clear')
            print("bye bye")
            quit()

    except Exception:
        print('Error')
select()
