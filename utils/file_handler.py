def read_file_bytes(path: str) -> bytes:
    """Read bytes from a file."""
    with open(path, "rb") as f:
        return f.read()

def write_file_bytes(path: str, data: bytes):
    """Write bytes to a file."""
    with open(path, "wb") as f:
        f.write(data)
