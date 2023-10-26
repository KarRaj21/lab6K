def encoder_password(pw):
    res = ""

    for i in pw:
        res += str(int(i) + 3)

    return res


def decode_pass(password):
   res = ""

   for i in password:
       res += str(int(i) - 3)

   return res


def main():
    while True:
       print('''\nMenu
-------------
1. Encode
2. Decode
3. Quit
       ''')
       menu = int(input('Please enter an option: '))

       if menu == 1:
           pw = input('Please enter your password to encode: ')
           encoded_password = encoder_password(pw)
           print("Your password has been encoded and stored!")

       elif menu == 2:
           decoded_pass = decode_pass(encoded_password)
           print(f"The encoded password is {encoded_password}, and the original password is {decoded_pass}")

       elif menu == 3:
            break

if __name__ == '__main__':
   main()

