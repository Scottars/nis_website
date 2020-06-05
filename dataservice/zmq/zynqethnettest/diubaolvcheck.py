import  pymysql

if __name__ =="__main__":

    db = pymysql.connect(host='localhost', user='scottar', password='wangsai', db='nis_hsdd', port=3306, charset='utf8')
    cur = db.cursor()
    msgResult = ''

    sql = "SELECT v_data,v_data_time FROM v_data_monitor"
    cur.execute(sql)
    numinbase = 0
    last=0
    packagelost=0;

    for col in (cur):
        # print(col)
        if numinbase==0:
            last=col[0]
            numinbase += 1
            continue
        if col[0]!=last+1:
            if last==10 and col[0]:
                numinbase += 1
                continue
            else:
                print('numinbash',numinbase,'last',last,'col[0]',col[0])
                packagelost+=1
        numinbase += 1
        last = col[0]
    # numinbase +=7
    print('Total package:',numinbase)
    print('Lost packages:',packagelost)
    print("Package loss rate",packagelost/numinbase)

