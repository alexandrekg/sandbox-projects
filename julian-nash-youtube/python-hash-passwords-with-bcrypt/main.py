import bcrypt


password = b"piar250322"
hashed = bcrypt.hashpw(password, bcrypt.gensalt())

print(password)
print(hashed)

# b'$2b$12$eQDqBOkA37WWeIwHpAxwD.IhfdFaqvwAwN6AhDT/riDsiOj9OchqC'
# b'$2b$12$S1.QrZKBony95I.kRzrJ0eg5EXfnAWE6gkpowXBo1C1m4YAMbAT.W'

# Comparing plain text with hashed password
if bcrypt.checkpw(password, hashed):
    print('It matches!')
else:
    print('it doesnt matches!')
