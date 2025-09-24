from crypto_tool.algorithms import aes
from crypto_tool.utils import key_generator
from crypto_tool import config
from crypto_tool.simulation.simulator import run_simulation

def main():
    # 1️⃣ Ask user for input
    text_input = input("Enter text to encrypt: ")
    plaintext = text_input.encode()  # convert to bytes

    # 2️⃣ Generate key and IV
    key = key_generator.generate_aes_key(config.DEFAULT_KEY_SIZE)
    iv = key_generator.generate_iv(config.DEFAULT_BLOCK_SIZE)

    print("\n=== AES Encryption/Decryption ===")
    print("Plaintext (bytes):", plaintext)

    # 3️⃣ Encrypt and decrypt using aes.py
    ciphertext = aes.encrypt(plaintext, key, iv)
    print("Ciphertext (hex):", ciphertext.hex())
    decrypted = aes.decrypt(ciphertext, key, iv)
    print("Decrypted:", decrypted.decode())

    # 4️⃣ Run block-by-block simulation with same plaintext, key, and IV
    print("\n=== Block-by-Block Simulation ===")
    run_simulation(plaintext, key, iv)

if __name__ == "__main__":
    main()
