import hashlib

s = input("Inform the input to be hashed: ")

menu = int(input(''' ### MENU - CHOOSE THE ENCODER FOR HASH ###
                1) MD5
                2) SHA1
                3) SHA256
                4) SHA512
                Type the corresponding number for encoder: '''))

if menu == 1:
    output = hashlib.md5(s.encode('utf-8'))
    print('The hash MD5 for: -->', s, '<-- is: ' ,output.hexdigest())
elif menu == 2:
    output = hashlib.sha1(s.encode('utf-8'))
    print('The hash SHA1 for: -->', s, '<-- is: ', output.hexdigest())
elif menu == 3:
    output = hashlib.sha256(s.encode('utf-8'))
    print('The hash SHA256 for : -->', s, '<-- is: ', output.hexdigest())
else:
    output = hashlib.sha512(s.encode('utf-8'))
    print('The hash SHA512 for: -->', s, '<-- is: ', output.hexdigest())