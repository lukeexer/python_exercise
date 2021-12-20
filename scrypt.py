import scrypt

encrypted_text = scrypt.hash(b'abc123', b'salt')
print(encrypted_text)

# For more information
# https://pypi.org/project/scrypt/