
data_pgpower=[1,2,3]
output = open('data.xls','w',encoding='gbk')
output.write('id\tdata\n')
for i in range(len(data_pgpower)):

    output.write(str(i))
    output.write('\t')
    output.write(str(data_pgpower[i]))
    output.write('\n')
output.close()
