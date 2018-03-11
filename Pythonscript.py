import csv

ifile = open('Unix-head-tail-test.csv', 'r+')
reader = csv.reader(ifile)

ofile  = open('Pytest.csv', 'a')
writer = csv.writer(ofile)

rownum = 1

for row in reader:
    flag1=False
    flag2=False
    # Save header row.
    if rownum ==1:
        header = row
        writer.writerow(row)
        print('Header row saved')
    else:
        colnum = 1
        for col in row:
            if colnum ==15 and col =='1': 
                #print('hello')
                print(rownum,header[colnum], col)
                flag1=True
            if colnum ==18 and col =='LEVEL1': 
                #print('hello')
                print(rownum,header[colnum], col)
                flag2=True
                
            colnum += 1
            if flag1==True and flag2==True:
                print(row)
                writer.writerow(row)
                break
 
    rownum += 1
#print(row) 
  
ifile.close()
ofile.close()