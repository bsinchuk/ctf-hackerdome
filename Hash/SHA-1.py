import hashlib

for flag in range(10000000, 100000000):
    h = hashlib.sha1()
    h.update(str(flag).encode("utf-8"))
    if h.hexdigest() == "a58dc2cfc5a93134666c607fbc5d6e961254214a":
        print(flag)
        break

