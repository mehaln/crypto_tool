=== Cryptographic Algorithm Simulation (Go) ===

Plaintext (64 bytes): "The quick brown fox jumps over the lazy dog — simulate crypto!"

1) AES-GCM (256-bit) simulation
 -> Encrypted: ciphertext len=80, nonce len=12, time=43µs
 -> Decrypted: valid=true, time=19µs
 -> SHA256(plaintext) = a3f5d7...

2) RSA OAEP (2048-bit) simulation
 -> RSA keygen time: 112ms
 -> RSA encrypt: ciphertext len=256, time=1.2ms
 -> RSA decrypt: valid=true, time=4.1ms

3) ECDH (P-256) key agreement simulation
 -> Shared secret equal: true (len=32 bytes)
 -> Derived AES key SHA256 = 3f1a9d...
 -> Encrypt/Decrypt with derived key valid=true

4) Hashing benchmark (SHA-256)
 -> SHA-256 of 1 MiB computed in 7.6ms
