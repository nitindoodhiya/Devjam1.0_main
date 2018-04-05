import os
def geary():
    print("Install Geary?   y/n:")
    char a = input()
    if a is 'y':
        os.system("sudo add-apt-repository ppa:geary-team/releases")
        os.system("sudo apt update")
        os.system("sudo apt install geary")
