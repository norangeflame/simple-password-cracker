import hashlib
import time
import os

#pass_input = input("Enter the hashed password: ")
#pass_bytes = bytes(pass_input, 'utf-8')
num = 0
total_seconds = 1
last_num = 0
total_p = 14344392*4
start_time = time.time() # Initialize start time
#ogfile = input("Input the filename of the wordlist (provide the full path if it is not located in the same directory of this script. Otherwise, just filename.txt is acceptable) > "

#read config
#0 is title
#1 is description 
#2 is filename of wordlist

line = 2
with open("config.txt", 'r', errors="ignore") as fp:
    x = fp.readlines()[line]
    x = x.strip()
    name = x
    ogfile = x + ".txt"
    print(f"Hashing {ogfile}")

#SHA1
nwfile = name + ".sha1.txt"
print(f"To file {nwfile}")

with open(ogfile, encoding='utf-8', errors='ignore') as file:
    file1 = open(nwfile, "w")
    for line in file:
        line = line.strip()
        hash_obj = hashlib.sha1(bytes(line, 'utf-8'))
        hashed = hash_obj.hexdigest()
        file1.write(f"{hashed}\n")
        
        num += 1
        success = "not found"

        if num % 100000 == 0:
            current_time = time.time()
            total_seconds = current_time - start_time
            rate = num / total_seconds / 1000
            rate = round(rate, 1)
            percent = num / total_p * 100
            time_string = time.strftime('%H:%M:%S', time.gmtime(total_seconds))
            print(f"{num} passwords hashed / {time_string} / {percent}% / {rate} kH/s.")
            last_num = num


#SHA256
nwfile = name + ".sha256.txt"
print(f"To file {nwfile}")

with open(ogfile, encoding='utf-8', errors='ignore') as file:
    file1 = open(nwfile, "w")
    for line in file:
        line = line.strip()
        hash_obj = hashlib.sha256(bytes(line, 'utf-8'))
        hashed = hash_obj.hexdigest()
        file1.write(f"{hashed}\n")
        
        num += 1
        success = "not found"

        if num % 100000 == 0:
            current_time = time.time()
            total_seconds = current_time - start_time
            rate = num / total_seconds / 1000
            rate = round(rate, 1)
            percent = num / total_p * 100
            time_string = time.strftime('%H:%M:%S', time.gmtime(total_seconds))
            print(f"{num} passwords hashed / {time_string} / {percent}% / {rate} kH/s.")
            last_num = num
#SHA512
nwfile = name + ".sha512.txt"
print(f"To file {nwfile}")

with open(ogfile, encoding='utf-8', errors='ignore') as file:
    file1 = open(nwfile, "w")
    for line in file:
        line = line.strip()
        hash_obj = hashlib.sha512(bytes(line, 'utf-8'))
        hashed = hash_obj.hexdigest()
        file1.write(f"{hashed}\n")
        
        num += 1
        success = "not found"

        if num % 100000 == 0:
            current_time = time.time()
            total_seconds = current_time - start_time
            rate = num / total_seconds / 1000
            rate = round(rate, 1)
            percent = num / total_p * 100
            time_string = time.strftime('%H:%M:%S', time.gmtime(total_seconds))
            print(f"{num} passwords hashed / {time_string} / {percent}% / {rate} kH/s.")
            last_num = num
#MD5
nwfile = name + ".md5.txt"
print(f"To file {nwfile}")

with open(ogfile, encoding='utf-8', errors='ignore') as file:
    file1 = open(nwfile, "w")
    for line in file:
        line = line.strip()
        hash_obj = hashlib.md5(bytes(line, 'utf-8'))
        hashed = hash_obj.hexdigest()
        file1.write(f"{hashed}\n")
        
        num += 1
        success = "not found"

        if num % 100000 == 0:
            current_time = time.time()
            total_seconds = current_time - start_time
            rate = num / total_seconds / 1000
            rate = round(rate, 1)
            percent = num / total_p * 100
            time_string = time.strftime('%H:%M:%S', time.gmtime(total_seconds))
            print(f"{num} passwords hashed / {time_string} / {percent}% / {rate} kH/s.")
            last_num = num

print(f"Passwords hashed.")
file1.close()
os.system("pause")
