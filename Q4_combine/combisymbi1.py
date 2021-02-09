rows=[]
Filenm=input("Enter File name for symbol Table 1: ")
f = open(Filenm,"r")

 # use readline() to read the first line
line = f.readline()
while line:
  if line.rstrip():
      #print(line)
      rows.append(line.split())
       # use realine() to read next line
  line = f.readline()
f.close()
size=int(rows[-1][5])+20
#print(size)
Filenm=input("Enter File name for symbol Table 2: ")
f = open(Filenm,"r")

#f = open('symbolT2.txt')
#rows=[]
 # use readline() to read the first line
flag=0
line = f.readline()
while line:
  if line.rstrip():
      #print(line)
      rows.append(line.split())
      if rows[-1][2].strip()=="Text" and flag==0:
          count=len(rows)-1
          #print("count=",count)
          flag=1
       # use realine() to read next line
  line = f.readline()
f.close()

for i in range(len(rows)):
    if i<len(rows):
        k=4+len(rows[i][4:-2])
        for j in range(5,k):
            rows[i][4]+=" "+rows[i][j]
        del rows[i][5:k]

l=len(rows)
for i in range(len(rows)):
    #print(i)
    if i<len(rows):
        if (len(rows[i]))==1:
            rows[i-1][4]+=" "+rows[i][0]
            del rows[i]

#print("lr=",len(rows))
rows1=[]
j=0
d=0
flag=0
for i in range(len(rows)):
    flag=0
    if(rows[i][2]=="Data"):
        if d==0:
            lc=0
        else:
            lc=int(rows1[d-1][1])+int(rows1[d-1][5])
        rows[i][1]=lc
        rows1.append(rows[i])
        d+=1
    else:
        continue
d=0
flag=0
for i in range(len(rows)):
    if(rows[i][2]=="Bss"):
        if d==0:
            lc=0
        else:
            lc=int(rows1[d-1][1])+int(rows1[d-1][5])
        rows[i][1]=lc
        rows1.append(rows[i])
        d+=1
    else:
        continue
d=0
flag=0
for i in range(len(rows)):
    if(rows[i][2]=="Text"):
        #print("i=",i)
        if d==0:
            lc=0
        if i==count:
            #print("hi")
            lc=int(rows1[d-1][1])+size
        else:
            lc=int(rows1[d-1][1])+int(rows1[d-1][5])

        if int(rows[i][1])<lc:
            rows[i][1]=lc
        rows1.append(rows[i])
    else:
        continue

for i in range(len(rows1)):
    flag=0
    if i==0:
        rows1[i].insert(0,rows1[i][0])
    else:
        for j in range(i):
            if rows1[i][0]==rows1[j][0]:
                flag=1
                rows1[i].insert(0,"new"+rows1[i][0])
        if flag==0:
            rows1[i].insert(0,rows1[i][0])
def red(text):
    print('\033[31m', text, '\033[0m', sep='')
def cyan(text):
    print('\033[36m', text, '\033[0m', sep='')
print()
print()
red("**********************COMBINED SYMBOL TABLE************************")
cyan("newName\toldName\tAddress\tSection\tType\tSize\tDefined\tValue")
for i in range(len(rows1)):
    for j in range (len(rows1[i])):
        if j==5:
            continue
        print(rows1[i][j],end="\t")
    print(rows1[i][5])
