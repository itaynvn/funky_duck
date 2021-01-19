from datetime import datetime

for i in range(100000):
    f= open("output/logme_%d.txt" %i ,"w+")
    for j in range(1000):
        f.write("This is line %d in file logme_%d at %s\r\n" % ((j+1), i, datetime.now().strftime("%d/%m/%Y %H:%M:%S")))
        f.close
