#Storing Packed Binary Data: struct
f1 = open('data.bin', 'wb')
import struct
data = struct.pack('>i4ss', 7, b'spam', b'8')
print(data)
f1.write(data)
f1.close()
f2=open('data.bin', 'rb')
data = f2.read()
values = struct.unpack('>i4s1s', data)
print(values)

