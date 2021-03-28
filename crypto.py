import hashlib

print(hashlib.md5(b"hello").hexdigest())
print(hashlib.sha256(b"hello").hexdigest())
