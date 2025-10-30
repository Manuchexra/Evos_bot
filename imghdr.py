# imghdr.py
import struct

def what(file, h=None):
    if h is None:
        if isinstance(file, str):
            f = open(file, 'rb')
            h = f.read(32)
            f.close()
        else:
            h = file.read(32)
    if h.startswith(b'\211PNG\r\n\032\n'):
        return 'png'
    if h[6:10] in (b'JFIF', b'Exif'):
        return 'jpeg'
    return None
