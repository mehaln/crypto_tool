from crypto_tool.algorithms import aes
from crypto_tool.utils import key_generator
from crypto_tool import config

def main():
    # Ask user for input
    text_input = input("Enter text to encrypt: ")
    plaintext = text_input.encode()  # convert to bytes

    key = key_generator.generate_aes_key(config.DEFAULT_KEY_SIZE)
    iv = key_generator.generate_iv(config.DEFAULT_BLOCK_SIZE)

    print("Plaintext (bytes):", plaintext)

    ciphertext = aes.encrypt(plaintext, key, iv)
    print("Ciphertext (hex):", ciphertext.hex())

    decrypted = aes.decrypt(ciphertext, key, iv)
    print("Decrypted:", decrypted)

if __name__ == "__main__":
    main()