from pynng import Pair0



address='ws://127.0.0.1:7789'
pair=Pair0(dial=address)

pair.send(b'hello')
print(pair.recv())






