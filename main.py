from crypto_tool.algorithms import aes
from crypto_tool.utils import key_generator
from crypto_tool import config
from crypto_tool.simulation.simulator import run_simulation
from crypto_tool.simulation.gui_simulator import AESGuiSimulator
import tkinter as tk

def main():
    choice = input("Choose mode:\n1. Command-line Simulation\n2. GUI Simulation\nEnter 1 or 2: ")

    if choice == "2":
        # Run GUI simulation
        root = tk.Tk()
        gui = AESGuiSimulator(root)
        root.mainloop()
        return

    # Command-line simulation
    text_input = input("Enter text to encrypt: ")
    plaintext = text_input.encode()

    key = key_generator.generate_aes_key(config.DEFAULT_KEY_SIZE)
    iv = key_generator.generate_iv(config.DEFAULT_BLOCK_SIZE)

    print("\n=== AES Encryption/Decryption ===")
    print("Plaintext (bytes):", plaintext)

    ciphertext = aes.encrypt(plaintext, key, iv)
    print("Ciphertext (hex):", ciphertext.hex())

    decrypted = aes.decrypt(ciphertext, key, iv)
    print("Decrypted:", decrypted)

    print("\n=== Command-line Block Simulation ===")
    run_simulation(plaintext, key, iv)

if __name__ == "__main__":
    main()
