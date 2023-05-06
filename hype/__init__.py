import os
from hype.gradient import Colorate, Colors, Center, Box
import discord
from hype import presence

def init(debug=False,
         mobile=False):
    if(os.name == 'posix'):
        os.system('clear')
    else:
        os.system('cls')
    
    print(Colorate.Horizontal(Colors.green_to_white, Center.XCenter("""

  .d88         o              o         88b.
 d88P"        d8b            d8b        "Y88b
d88P         d888b          d888b         Y88b
888         d8P"Y8b        d8P"Y8b         888
888                                        888
Y88b                                      d88P
 Y88b.                                  .d88P
  "Y88             88888888             88P"


""")))

    if mobile == True:
        print(Colorate.Horizontal(Colors.green_to_white, "Disocrd iOS Payload\n".center(os.get_terminal_size().columns)))
        presence.enable()
    elif mobile == False:
        return

    if debug == False:
        return
    elif debug == True:
        print(Colorate.Horizontal(Colors.green_to_white, "Debug Mode\n".center(os.get_terminal_size().columns)))