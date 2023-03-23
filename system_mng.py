from ping3 import ping, verbose_ping
import socket, time
from wakeonlan import send_magic_packet


#Shutdown def with mce
def mce_shutdown(ip):
    HOST = ip
    PORT = 5150
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((HOST, PORT))
            message='shutdown\n'
            message_bytes = message.encode('utf-8')
            s.send(message_bytes)
            s.close()
            print('~~~~\nDone')
    except:
        print("Shutdon Failed🚫, No connection with Station's MCE")



#Dataton Control    
def watchout(ip):
    print('Watchout Control')
    HOST = ip
    PORT = 5150
    menu1='0'
    while menu_watchout!='x':
        com=input('Select:\nrun for Start the show\nKill to Stop\nhalt to Pause')
        menu=com
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect((HOST, PORT))
                message_bytes = com.encode('utf-8')
                s.send(message_bytes)
                s.close()
                print('~~~~\nDone')
        except:
            print("Connect Refuse!")
            menu_watchout='x'

        

#create List
ip=[]
station=[]
mac=[]
total_station=0

#close TXT Files
ip_file=open('ip.txt','r')
station_file=open('station.txt','r')
mac_file=open('mac_pc.txt','r')


#Insert & Cleaning Data
print('Loading Stations...')
for line in ip_file:
    Line=line.replace('\n','')
    ip.append(Line)
    total_station +=1

for line in station_file:
    Line=line.replace('\n','')   
    station.append(Line)

for line in mac_file:
    Line=line.replace('\n','')  
    mac.append(Line)

#closing Files
ip_file.close()
station_file.close()
mac_file.close()

print('Done!')


menu="A"
while menu!='x':
    print('-----------Menu-----------')
    print('1|Check Station Connaction Status & Wake_On_lan')
    print('2|Shutdown all Stations Via MCE')
    print('3|Watchout Dataton|Coming Soon!')

    print('Press x for Exit')
    
    menu=input("~> ")


#Check Status
    prog_status=''
    if menu=="1":
        print("Checking connection status....")
        for x in range (0,total_station):
            #Print Status prog
            response=ping(ip[x])
            print('|IP:'+ip[x]+'📃'+'\n|Station:'+station[x]+'💻'+'\n|MAC:'+mac[x]+'🌐')
            #Check Status and wake up
            if str(response)=='None':    
                print('|Status:Offline🚫 trying to WOL 🔄️')
                send_magic_packet(mac[x])
                print("|Sending 🔮🪄 to ➡️  "+station[x])
                prog_status+='❎'

            else:
                print('|Status:Online✅')
                prog_status +='✅'
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            prog_total=(total_station-x-1)*"☑️ "
            print("Progress: "+prog_status+""+prog_total)
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                

    if menu=='2':
        print('Shutdown Starting now')
        for x in range(0,total_station):
            print(' Sending Shutdown Command ➡️   '+station[x])
            time.sleep(2)
            mce_shutdown(ip[x])


    if menu=='george':
        print('-------------------------')
        print('Version 0.2')
        print('Author|George Frazeskaros')
        print('-------------------------')



    if menu=='3':
        print('not ready!')
        #watchout('1.1.1.1')






#quiting       
time.sleep(1)