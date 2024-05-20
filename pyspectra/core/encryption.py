def xor_cipher(data, key):
    key_length = len(key)
    return ''.join(chr(ord(data[i]) ^ ord(key[i % key_length])) for i in range(len(data)))
