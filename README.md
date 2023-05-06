# simple-password-cracker
Simple password cracker written in python. Requires your own wordlist, and can crack SHA1, SHA256, SHA512 and MD5 passwords.
This is a dictionary-based password cracker, which means it hashes a list of known common passwords, and compares your inputted password hash to see if it is a match. If it is, then the cracker will know which hash corresponds to which password, and will give you your result.
Obviously, this will be nowhere near as fast as specialised password crackers such as Hashcat and John the Ripper, which utilise your GPU power as well as your processing power.

This was more just a fun project.

To set up: 
1. Download the files
2. Download a wordlist (a common one: https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt)
3. Place the wordlist TXT file in the directory of the cracker files.
4. Modify the config.txt file to have the name of the wordlist file on line 3. DO NOT INCLUDE THE .txt EXTENSION.
5. If its the first time running the cracker, run PRE_HASH_FILES.exe.
6. When complete, run CRACKER.exe. Input the password hash, and then the type of hash. To identify: https://hashes.com/en/tools/hash_identifier (Shown in possible algorithms after inputting hash)
7. In future, you will not need to run PRE_HASH_FILES.exe again, UNLESS YOU WANT TO USE A NEW WORDLIST. IN THAT CASE, GO OVER THESE STEPS AGAIN IN A NEW FOLDER, WITH YOUR NEW WORLIST.
8. Wait for CRACKER to detect the password. Whether it cracks the password is dependent on the complexity and the scope of the wordlist. The rockyou wordlist contains 14 million of the most common passwords, while crackstation has a wordlist with 1.5 billion entries.


Note: CRACKER.exe may be flagged as a virus. If you want, compile it from the source CRACKER.py file. Requires installing hashlib library.
