from cryptography.fernet import Fernet

key = Fernet.generate_key()
ciper_suite = Fernet(key)
IBAN = b'DF232323232323232323 pass 12121212'

encrypt_data =  ciper_suite.encrypt(IBAN)

print(encrypt_data)


decrypt_data = ciper_suite.decrypt(encrypt_data)

print(decrypt_data)

