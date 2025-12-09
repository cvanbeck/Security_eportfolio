import hashlib
import datetime
import bcrypt

password = b"TestPass123!"


''' current = datetime.datetime.now()
md5 = hashlib.md5(password)
now = datetime.datetime.now() - current
print(md5, now)

current = datetime.datetime.now()
sha256 = hashlib.sha256(password)
now = datetime.datetime.now() - current
print(sha256, now)

current = datetime.datetime.now()
salt = bcrypt.gensalt()
bcryptHash = bcrypt.hashpw(password, salt)
now = datetime.datetime.now() - current
print(bcryptHash, now) '''


newPass = b"AnotherTest"

'''
salt = bcrypt.gensalt()
bcryptHash = bcrypt.hashpw(newPass, salt)
print(bcryptHash) '''

salt = bcrypt.gensalt(100)
bcryptHash = bcrypt.hashpw(newPass, salt)
print(bcryptHash)

pepper = (b"saltnpepperchicken123!")
salt = bcrypt.gensalt(100)
pepperedPass = (str(newPass) + str(pepper)).encode("utf-8")
pepperedBcryptHash = bcrypt.hashpw(pepperedPass, salt)
print(pepperedBcryptHash)


