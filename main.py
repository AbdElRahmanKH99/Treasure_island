#Welcome messege, doors (red/blue), not others
print("""

░██╗░░░░░░░██╗███████╗██╗░░░░░░█████╗░░█████╗░███╗░░░███╗███████╗  ████████╗░█████╗░  ███╗░░░███╗██╗░░░██╗
░██║░░██╗░░██║██╔════╝██║░░░░░██╔══██╗██╔══██╗████╗░████║██╔════╝  ╚══██╔══╝██╔══██╗  ████╗░████║╚██╗░██╔╝
░╚██╗████╗██╔╝█████╗░░██║░░░░░██║░░╚═╝██║░░██║██╔████╔██║█████╗░░  ░░░██║░░░██║░░██║  ██╔████╔██║░╚████╔╝░
░░████╔═████║░██╔══╝░░██║░░░░░██║░░██╗██║░░██║██║╚██╔╝██║██╔══╝░░  ░░░██║░░░██║░░██║  ██║╚██╔╝██║░░╚██╔╝░░
░░╚██╔╝░╚██╔╝░███████╗███████╗╚█████╔╝╚█████╔╝██║░╚═╝░██║███████╗  ░░░██║░░░╚█████╔╝  ██║░╚═╝░██║░░░██║░░░
░░░╚═╝░░░╚═╝░░╚══════╝╚══════╝░╚════╝░░╚════╝░╚═╝░░░░░╚═╝╚══════╝  ░░░╚═╝░░░░╚════╝░  ╚═╝░░░░░╚═╝░░░╚═╝░░░

██╗░██████╗██╗░░░░░░█████╗░███╗░░██╗██████╗░
██║██╔════╝██║░░░░░██╔══██╗████╗░██║██╔══██╗
██║╚█████╗░██║░░░░░███████║██╔██╗██║██║░░██║
██║░╚═══██╗██║░░░░░██╔══██║██║╚████║██║░░██║
██║██████╔╝███████╗██║░░██║██║░╚███║██████╔╝
╚═╝╚═════╝░╚══════╝╚═╝░░╚═╝╚═╝░░╚══╝╚═════╝░

There are two doors in front of you. 🚪 a red and 🚪 a blue door""")
door = input("Which door do you want to open? ").lower()

#blue to crocodiles
if door == "blue":
    print("""Oops! You chose the crocodile door.
Game over! 🐊🐊🐊""")

#red to a room that have three boxes (white/black/green), not others
elif door == "red":
    print("""Great! now you entered a room.
you found three boxes: 🎁 white, 🎁 black, 🎁 green""")
    box = input("Which box do you open? ").lower()

#white to snakes
    if box == "white":
        print("Oops! You opened a box filled with snakes 🐍🐍🐍")

#black to spiders
    elif box == "black":
        print("Oops! You opened a box filled with spiders 🕸️ 🕸️ 🕸️")

#green to the treasure
    elif box == "green":
        print("Congrats! You found the treasure! 💰💰💰")
    else:
        print("Invalid choice! 🤷‍♂️🤷‍♂️🤷‍♂️")

else:
    print("Invalid choice! 🤷‍♂️🤷‍♂️🤷‍♂️")
