'''
byteData = bytearray()
print(type(byteData)) # <class 'bytearray'>
'''

msg = 'adminesp32messa1234567890'
print(type(msg),msg)
bytesMsg = msg.encode()
print(type(bytesMsg),bytesMsg)

bytesMsg2 = 'haha'.encode()

bytesMsg3 = bytesMsg+bytesMsg2

print(type(bytesMsg3),bytesMsg3)