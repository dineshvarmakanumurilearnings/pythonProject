#f=open('C:\\Users\\LENOVO\\Desktop\\TechWithTim.txt','r')
#(line for line in f)
#newf=open('C:\\Users\\LENOVO\\Desktop\\Copyof.txt','x')
#for line in (line for line in f):
    #newf.write(line)
#f.close()
#newf.close()



def readfilegen(filename):
    f= open(filename)
    while True:
        line =f.readline()
        if line!='':
            yield line
        else:break

for line in readfilegen('C:\\Users\\LENOVO\\Desktop\\TechWithTim.txt'):
    print(line,end='')








