import  struct
b = b'exp' + struct.pack('!f', 12)
print(b)
print(b[0:3])
if b[0:3] == b'exp':
    exp_id = struct.unpack('!f', b[3:7])[0]
    print(exp_id)