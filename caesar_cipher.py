# A basic encyption and decryption program called 'Caesar Cipher'

# what is Caesae cipher?
# It's very simple and insecure:
    # Only 25 possible keys (shifts), making brute-force decryption easy.
    # Frequency analysis can easily break it by analyzing letter patterns.
# While it's not used in serious cryptography today, the Caesar Cipher provides an excellent starting point to 
# understand encryption concepts!

class Cipher :
    def do_encrypt(self, msg) :
        encrypted_msg = ""
        for m in msg : # "Hello"
            if m.isupper() :
                encrypted_msg += chr((ord(m) - ord('A') + 3) % 26 + ord('A')) # 72 - 65 + 3
                # ord() returns the ASCII value of the character passed to it
                # ord() of capital letters starts from 65 and ends at 90, whereas for small letters it is from 97 to 122
            elif m.islower() :
                encrypted_msg += chr((ord(m) - ord('a') + 3) % 26 + ord('a'))
            else :
                encrypted_msg += m


        print(f"Encryped message is '{encrypted_msg}'")
        return encrypted_msg


    def do_decrypt(self, msg) :
        decrypted_msg = ""
        for m in msg :
            if m.isupper() :
                decrypted_msg += chr((ord(m) - ord('A') - 3) % 26 + ord('A'))
            elif m.islower() :
                decrypted_msg += chr((ord(m) - ord('a') - 3) % 26 + ord('a'))
            else :
                decrypted_msg += m
        
        print(f"Decrypted message is '{decrypted_msg}'")

cipher = Cipher()
msg = input("What's the msg?\n")
want_encryption = input("You want to encrypt this msg (yes/no)")
if want_encryption.lower() == "yes" :
    encrypted_msg = cipher.do_encrypt(msg)
elif want_encryption.lower() == "no" :
    print("Hope your important messages are safe.")
else :
    print("Invalid response...")

if want_encryption == "yes" : # how is this workingg???
    want_decryption = input("You want to decrypt the msg ? (yes/no)")
    if want_decryption.lower() == "yes" : 
        cipher.do_decrypt(encrypted_msg)
    elif want_decryption.lower() == "no" :
        print("Hope you can understand it.")
    else :
        print("Invalid response...")