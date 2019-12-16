from pynng import Pair0,Pair1



address='ws://127.0.0.1:7789'
pair=Pair0(listen=address)
print(pair.recv())
pair.send(b'world')






