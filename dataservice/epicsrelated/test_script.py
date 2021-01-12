

a= ''
for i in range(1,17,1):
    a  = a +'TIMING_END_SET'+str(i)+','

print(a)

a=''
for i in range(64):
    a  = a +'PVS['+str(i)+']'+'.value,'

print(a)


print('hello world')