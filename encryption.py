from Crypto.Cipher import Blowfish
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes


def encrypt_message(message, shared_key):
    iv = get_random_bytes(8)
    cipher = Blowfish.new(shared_key.encode("utf-8"), Blowfish.MODE_CBC, iv)
    encrypted_message = cipher.encrypt(pad(message.encode("utf-8"), Blowfish.block_size))
    return iv + encrypted_message

def decrypt_message(ciphertext, shared_key):
    iv = ciphertext[:8]
    encrypted_message = ciphertext[8:]
    cipher = Blowfish.new(shared_key.encode("utf-8"), Blowfish.MODE_CBC, iv)
    decrypted_message = unpad(cipher.decrypt(encrypted_message), Blowfish.block_size)
    return decrypted_message.decode("utf-8")
