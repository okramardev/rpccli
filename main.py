import configparser
from pypresence import Presence
import time
# Read config
config = configparser.ConfigParser()
config.read('config.ini')

client_id = config['CONNECTION']['client_id']

state = config['RPC']['state']
details = config['RPC']['details']
start = config['RPC']['start']
end = config['RPC']['end']
large_image = config['RPC']['large_image']
large_text = config['RPC']['large_text']
small_image = config['RPC']['small_image']
small_text = config['RPC']['small_text']
party_id = config['RPC']['party_id']
party_size = config['RPC']['party_size']
join = config['RPC']['join']
spectate = config['RPC']['spectate']
match = config['RPC']['match']
buttons = config['RPC']['buttons']
instance = config['RPC']['instance']

# Main
while True:
    print("""

  _____  _____   _____ _____ _      _____ 
 |  __ \|  __ \ / ____/ ____| |    |_   _|
 | |__) | |__) | |   | |    | |      | |  
 |  _  /|  ___/| |   | |    | |      | |  
 | | \ \| |    | |___| |____| |____ _| |_ 
 |_|  \_\_|     \_____\_____|______|_____|
                                          
                                          
           [ Made by okramar ]
  [ As a challenge, made in 30 minutes ]
""")
    print()
    print("""
    [1] Start RPC
    [2] Change RPC
    [3] Exit
    """)
    x = input("> ")
    if x == "1":
        if client_id == "":
            print("Please enter a client_id!")
            sys.exit(0)
        print("Connecting to Discord... To end RPC press CTRL-C")
        while True:
            RPC = Presence(client_id)
            RPC.connect()
            RPC.update(
                state=state if state != "" else None, 
                details=details if details != "" else None,
                start=start if start != "" else None, 
                end=end if end != "" else None, 
                large_image=large_image if large_image != "" else None, 
                large_text=large_text if large_text != "" else None, 
                small_image=small_image if small_image != "" else None, 
                small_text=small_text if small_text != "" else None, 
                party_id=party_id if party_id != "" else None, 
                party_size=party_size if party_size != "" else None, 
                join=join if join != "" else None, 
                spectate=spectate if spectate != "" else None, 
                match=match if match != "" else None, 
                buttons=buttons if buttons != "" else None, 
                instance = instance if instance != "" else None)
            time.sleep(10)
    elif x == "2":
        print("""
        [1] State
        [2] Details
        [3] Start
        [4] End
        [5] Large_Image
        [6] Large_Text
        [7] Small_Image
        [8] Small_text
        [9] Party_ID
        [10] Party_Size
        [11] Join
        [12] Spectate
        [13] Match
        [14] Buttons
        [15] Instance
        [16] Client_ID
        """)
        x = input("> ")
        if x == "1":
            print("Please enter the new state:")
            x = input("> ")
            config['RPC']['state'] = x
            with open('config.ini', 'w') as configfile:
                config.write(configfile)
        elif x == "2":
            print("Please enter the new details:")
            x = input("> ")
            config['RPC']['details'] = x
            with open('config.ini', 'w') as configfile:
                config.write(configfile)
        elif x == "3":
            print("Please enter the new start time (in unix timestamp):")
            x = input("> ")
            config['RPC']['start'] = x
            with open('config.ini', 'w') as configfile:
                config.write(configfile)
        elif x == "4":
            print("Please enter the new end time (in unix timestamp):")
            x = input("> ")
            config['RPC']['end'] = x
            with open('config.ini', 'w') as configfile:
                config.write(configfile)
        elif x == "5":
            print("Please enter the new large_image name:")
            x = input("> ")
            config['RPC']['large_image'] = x
            with open('config.ini', 'w') as configfile:
                config.write(configfile)
        elif x == "6":
            print("Please enter the new large_text:")
            x = input("> ")
            config['RPC']['large_text'] = x
            with open('config.ini', 'w') as configfile:
                config.write(configfile)
        elif x == "7":
            print("Please enter the new small_image name:")
            x = input("> ")
            config['RPC']['small_image'] = x
            with open('config.ini', 'w') as configfile:
                config.write(configfile)
        elif x == "8":
            print("Please enter the new small_text:")
            x = input("> ")
            config['RPC']['small_text'] = x
            with open('config.ini', 'w') as configfile:
                config.write(configfile)
        elif x == "9":
            print("Please enter the new party_id:")
            x = input("> ")
            config['RPC']['party_id'] = x
            with open('config.ini', 'w') as configfile:
                config.write(configfile)
        elif x == "10":
            print("Please enter the new party_size:")
            x = input("> ")
            config['RPC']['party_size'] = x
            with open('config.ini', 'w') as configfile:
                config.write(configfile)
        elif x == "11":
            print("Please enter the new join hash:")
            x = input("> ")
            config['RPC']['join'] = x
            with open('config.ini', 'w') as configfile:
                config.write(configfile)
        elif x == "12":
            print("Please enter the new spectate hash:")
            x = input("> ")
            config['RPC']['spectate'] = x
            with open('config.ini', 'w') as configfile:
                config.write(configfile)
        elif x == "13":
            print("Please enter the new match hash:")
            x = input("> ")
            config['RPC']['match'] = x
            with open('config.ini', 'w') as configfile:
                config.write(configfile)
        elif x == "14":
            print('Please enter the new buttons (in a list, example: [{"label"}]: "My Website", "url": "https://test.com"}, ...):')
            x = input("> ")
            config['RPC']['state'] = x
            with open('config.ini', 'w') as configfile:
                config.write(configfile)
        elif x == "15":
            print("Please enter the new instance bool:")
            x = input("> ")
            config['RPC']['instance'] = x
            with open('config.ini', 'w') as configfile:
                config.write(configfile)
        elif x == "16":
            print("Please enter the new client_id:")
            x = input("> ")
            config['CONNECTION']['client_id'] = x
            with open('config.ini', 'w') as configfile:
                config.write(configfile)
