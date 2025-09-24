import os
import base64

def generate_aes_key(key_size: int = 32) -> bytes:
    """Generate a random AES key (default 256-bit)."""
    return os.urandom(key_size)

def generate_iv(block_size: int = 16) -> bytes:
    """Generate a random IV for CBC mode."""
    return os.urandom(block_size)

def to_base64(data: bytes) -> str:
    return base64.b64encode(data).decode()

