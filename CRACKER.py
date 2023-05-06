import hashlib
import time
import os
import linecache

def file_len(filename):
    with open(filename, errors='ignore') as f:
        for i, _ in enumerate(f):
            pass
    return i + 1

pass_input = input("Enter the hashed password: ")

line = 2
with open("config.txt", 'r', errors="ignore") as fp:
    x = fp.readlines()[line]
    x = x.strip()
    name = x
    ogfile = x + ".txt"
    length = file_len(ogfile)
    
K = "$"
N = 3
res = pass_input.split(K, N)[-1]
pass_input = str(res)
pass_input = pass_input.lower()
pass_bytes = bytes(pass_input, 'utf-8')
num = 0
total_seconds = 1
last_num = 0
total_p = 63941069
start_time = time.time() # Initialize start time
hashtype = input("Select hash type: sha1, sha256. sha512, md5. > ")

if hashtype == "sha1":
    name2 = name + ".sha1.txt"
    with open(name2, encoding='utf-8', errors='ignore') as file:
        for line in file:
            line = line.strip()        
            num += 1
            success = "not found"

            if line == pass_input:
                print("Password found...please wait...")
                break

            if num % 10000000 == 0:
                current_time = time.time()
                total_seconds = current_time - start_time
                rate = num / total_seconds / 1000000
                rate = round(rate, 4)
                percent = num / total_p * 100
                time_string = time.strftime('%H:%M:%S', time.gmtime(total_seconds))
                print(f"{num} combinations tested / {time_string} / {percent}% / {rate} Million Passwords/s.")
                last_num = num
                
if hashtype == "sha256":
    name2 = name + ".sha256.txt"
    with open(name2, encoding='utf-8', errors='ignore') as file:
        for line in file:
            line = line.strip()        
            num += 1
            success = "not found"

            if line == pass_input:
                print("Password found...please wait...")
                break

            if num % 10000000 == 0:
                current_time = time.time()
                total_seconds = current_time - start_time
                rate = num / total_seconds / 1000000
                rate = round(rate, 4)
                percent = num / total_p * 100
                time_string = time.strftime('%H:%M:%S', time.gmtime(total_seconds))
                print(f"{num} combinations tested / {time_string} / {percent}% / {rate} Million Passwords/s.")
                last_num = num
                
if hashtype == "sha512":
    name2 = name + ".sha512.txt"
    with open(name2, encoding='utf-8', errors='ignore') as file:
        for line in file:
            line = line.strip()        
            num += 1
            success = "not found"

            if line == pass_input:
                print("Password found...please wait...")
                break

            if num % 10000000 == 0:
                current_time = time.time()
                total_seconds = current_time - start_time
                rate = num / total_seconds / 1000000
                rate = round(rate, 4)
                percent = num / total_p * 100
                time_string = time.strftime('%H:%M:%S', time.gmtime(total_seconds))
                print(f"{num} combinations tested / {time_string} / {percent}% / {rate} Million Passwords/s.")
                last_num = num

                
if hashtype == "md5":
    name2 = name + ".md5.txt"
    with open(name2, encoding='utf-8', errors='ignore') as file:
        for line in file:
            line = line.strip()        
            num += 1
            success = "not found"

            if line == pass_input:
                print("Password found...please wait...")
                break

            if num % 10000000 == 0:
                current_time = time.time()
                total_seconds = current_time - start_time
                rate = num / total_seconds / 1000000
                rate = round(rate, 4)
                percent = num / total_p * 100
                time_string = time.strftime('%H:%M:%S', time.gmtime(total_seconds))
                print(f"{num} combinations tested / {time_string} / {percent}% / {rate} Million Passwords/s.")
                last_num = num






with open(ogfile, 'r', errors="ignore") as fp:
    num2 = num - 1
    try:
        x = fp.readlines()[num2]
        x = x.strip()
        if num == length:
            x = "NOT FOUND"
            print(f"The password was not found. Check you entered the correct hash and hash type.")
        else:
            print(f"The password is '{x}'.")
    except:
        x = "NOT FOUND"
        print(f"The password was not found. Check you entered the correct hash and hash type.")
    
os.system("pause")


