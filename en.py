import bcrypt

password = input("Input the password to hash\n>")

print("\nBCRYPT:\n")
for i in range(3):
    setpass = bytes(password, 'utf-8')
    hashed = bcrypt.hashpw(setpass, bcrypt.gensalt(10))
    print(hashed)

#https://null-byte.wonderhowto.com/how-to/use-beginner-python-build-brute-force-tool-for-sha-1-hashes-0185455/
