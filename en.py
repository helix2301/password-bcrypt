import bcrypt

password = input("Input the password to hash\n>")

print("\nBCRYPT:\n")
for i in range(3):
    setpass = bytes(password, 'utf-8')
    hashed = bcrypt.hashpw(setpass, bcrypt.gensalt(10))
    print(hashed)
