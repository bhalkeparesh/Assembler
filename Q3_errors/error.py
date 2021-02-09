reg32=["eax","ecx","edx","ebx","esp","ebp","esi","edi"]
reg16=["ax","cx","dx","bx","sp","bp","si","di"]
reg8=["al","cl","dl","bl","ah","ch","dh","bh"]
reg=["eax","ecx","edx","ebx","esp","ebp","esi","edi","ax","cx","dx","bx","sp","bp","si","di","al","cl","dl","bl","ah","ch","dh","bh"]
ins2=["mov","add","adc","sub","sbb","xor","cmp"]
ins1=["push","inc","dec","pop","jmp"]
keywords=["eax","ecx","edx","ebx","esp","ebp","esi","edi","ax","cx","dx","bx","sp","bp","si",\
"di","al","cl","dl","bl","ah","ch","dh","bh","mov","add","adc","sub","sbb","xor","cmp",\
"push","inc","dec","pop","jmp","dword"]
lc=0
class Node:
    def __init__(self, name=None):
        self.name=name
        self.nextval = None

class SLinkedList:
    def __init__(self):
        self.headval = None

# Function to add newnode
    def AtEnd(self, a):
        NewNode = Node(a)
        if self.headval is None:
            self.headval = NewNode
            return
        laste = self.headval
        while(laste.nextval):
            laste = laste.nextval
        laste.nextval=NewNode

# Print the linked list
    def listprint(self):
        printval = self.headval
        while printval is not None:
            print("%s"%(printval.name))
            #print()
            printval = printval.nextval
#search
    def search(self,symbol):
        temp = self.headval
        while temp is not None:
            if temp.name==symbol or temp.name==(symbol+":"):
                return True
            temp = temp.nextval
        return False
def alone_label(line,lc):
    line=line.split()
    if len(line)==1 and line[0] not in keywords:
        print("%s:%d warning: label alone on a line without a colon might be in error"%(Filenm,lc))
        return 1
    else:
        return 0
def check_redefine(symbi,lc):
    if list.search(symbi):
        print("%s:%d error: symbol %s redefined"%(Filenm,lc,symbi))
        return 1
    else:
        return 0

def proper_sib(line):
    l=line.split("[")
    #print("l=",l)
    l[0]=l[0].strip()
    #print(l[0])
    size=0
    if l[0]=="dword" or l[0]=="":
        l=l[1].strip()[:-1]
        l=l.split("+")
        esp=l[0]
        l=l[1].strip()[:-1]
        l=l.split("+")
        esp=l[0]
        if l[0] in reg and l[0] not in reg32:
            print("%s:%d error: Invalid effective address"%(Filenm,lc))
        elif l[0] not in reg and l[0]!= symbi and not list.search(l[0]):
            print("%s:%d:error:symbol %s undefined"%(Filenm,lc,l[0]))
                #print("GOOOD")
        l=l[1].split("*")
        if list.search(l[0]) and l[1]!="1":
            print("%s:%d: error: invalid effective address: impossible segment base multiplier"%(Filenm,lc))
        elif l[0]!= symbi and not list.search(l[0]) and l[0] not in keywords:
            print("%s:%d:error:symbol %s undefined"%(Filenm,lc,l[0]))
        elif l[0] in reg32 and (int(l[1])>8 or int(l[1])<0):
            print("%s:%d: error: invalid effective address: impossible segment base multiplier"%(Filenm,lc))
        elif l[0]=="esp" and (int(l[1])>1 or int(l[1])<0):
            print("%s:%d error: Invalid effective address"%(Filenm,lc))



def base(line):
    l=line.split("[")
    #print("l=",l)
    l[0]=l[0].strip()
    print(l[0])
    size=0
    #l[0]=l[0].strip()
    if l[0]=="dword" or l[0]=="":
        l[1]=l[1].strip()[:-1]
        if l[1] in reg and l[1] not in reg32:
            print("%s:%d error: Invalid effective address"%(Filenm,lc))

        elif l[1] not in reg32 and not list.search(l[1]) and l[1]!=symbi:
            print("%s:%d:error:symbol %s undefined"%(Filenm,lc,l[1]))

def base_index(line):
    l=line.split("[")
    #print("l=",l)
    l[0]=l[0].strip()
    #print(l[0])
    size=0
    if l[0]=="dword" or l[0]=="":
        l[1]=l[1].strip()[:-1]
        l=l[1].split("+")
        if l[0].strip() in reg and l[0].strip() not in reg32:
            print("%s:%d error: Invalid effective address"%(Filenm,lc))
        elif l[0].strip() not in reg32 and list.search(l[0].strip()) and (int(l[1].strip())>1 or int(l[1].strip())<0):
            print("%s:%d: error: invalid effective address: impossible segment base multiplier"%(Filenm,lc))
        elif l[0].strip() in reg32 and not l[1].strip().isdecimal() or (l[1].strip() in reg32 and not l[0   ].strip().isdecimal()):
            print("%s:%d:error:unable to multiply two non scalar objects"%(Filenm,lc))
        elif not list.search(l[0].strip()):
            print("%s:%d:error:symbol %s undefined"%(Filenm,lc,l[0].strip()))

def base_scale(line):
    l=line.split("[")
    #print("l=",l)
    l[0]=l[0].strip()
    #print(l[0])
    size=0
    if l[0]=="dword" or l[0]=="":
        l[1]=l[1].strip()[:-1]
        l=l[1].split("*")
        if l[0].strip() in reg32 and l[1].strip().isdecimal():
            if int(l[1].strip())>9 or int(l[1].strip())<0:
                print("%s:%d error: Invalid effective address"%(Filenm,lc))
        elif l[0].strip() not in reg32 and list.search(l[0].strip()) and (int(l[1].strip())>1 or int(l[1].strip())<0):
            print("%s:%d: error: invalid effective address: impossible segment base multiplier"%(Filenm,lc))
        elif l[0].strip() in reg32 and not l[1].strip().isdecimal() or (l[1].strip() in reg32 and not l[0   ].strip().isdecimal()):
            print("%s:%d:error:unable to multiply two non scalar objects"%(Filenm,lc))
        elif not list.search(l[0].strip()):
            print("%s:%d:error:symbol %s undefined"%(Filenm,lc,l[0].strip()))


def txt(f,lc):
    #print("hi")
    adcount=0
    padcount=0
    pos=f.tell()
    line=f.readline()
    line=line.strip()

    #print(line)
    while(True):
        newpos = f.tell()
        if newpos == pos:  # stream position hasn't changed -> EOF
            break
        else:
            pos = newpos
        flag=0

        if not line:
            line=f.readline()
            line=line.strip()
            continue

        flag=0
        if "global main" in line:
            line=f.readline()
            line=line.strip()
            lc+=1
            continue
        pos=line.find(';')
        if pos==-1:
            pos=len(line)
        i=0
        size=0
        while(i<pos):
            alone_label(line,lc)
            w=""
            while i<pos and (line[i]!=" "):
                w+=line[i]
                i+=1
            if ":" in line and flag==0:
                if ":" in w:
                    symbi=w[:-1]
                else:
                    symbi=w
                w=""
                flag=1
                i+=1
                continue

                if not symbi[0].isalpha() or symbi in keywords:
                    print("%s:%d error: label or instruction expected at start of line "%(Filenm,lc))
                elif list.search(symbi):
                    print("%s:%d:error:symbol %s redefined",Filenm,lc,symbi)

            if w not in ins2 and w not in ins1:
                print("%s:%d:error: parser: instruction expected"%(Filenm,lc))

            if w in ins2:
                w=""
                count=i
                #i=pos-1
                #print(line[count:pos])
                line=line[count:pos]
                if ',' not in line:
                    print("%s:%d: error: comma, colon, decorator or end of line expected after operand"%(Filenm,lc))
                line=line.split(",")
                if line[0].strip() in reg32 and line[1].strip() in reg and line[1].strip() not in reg32:
                    print("%s:%d: error:Invalid combination of opcode and operands"%(Filenm,lc))
                elif line[0].strip() in reg16 and line[1].strip() in reg and line[1].strip() not in reg16:
                    print("%s:%d: error:Invalid combination of opcode and operands"%(Filenm,lc))
                elif line[0].strip() in reg8 and line[1].strip() in reg and line[1].strip() not in reg8:
                    print("%s:%d: error:Invalid combination of opcode and operands"%(Filenm,lc))
                elif (line[0].strip() in reg32 or line[0].strip() in reg8) and line[1].strip().isdecimal():
                    flag1=1
                    value=line[1].strip()
                elif line[0].strip() in reg16 and line[1].strip().isdecimal():
                    flag1=1
                    value=line[1].strip()

                elif "dword" in line[1].strip() and list.search(line[0].strip()):
                    print("%s:%d: error:Invalid combination of opcode and operands"%(Filenm,lc))
                elif "dword" in line[0].strip()  and (line[1].strip() in reg and line[1].strip() not in reg32):
                    print("%s:%d: error: mismatch in operand sizes"%(Filenm,lc))

                elif "dword" in line[0].strip() and line[1].strip() not in reg32 and line[1].strip()!=symbi and not list.search(line[1].strip())\
                or ("dword" in line[1].strip() and line[0].strip() not in reg32):
                     print("%s:%d: error: symbol %s undefined"%(Filenm,lc,line[0].strip()))


                elif line[0].strip() in reg32 and "dword" in line[1].strip() and "+" in line[1].strip() and "*" in line[1].strip()\
                or "dword" in line[0].strip() and "+" in line[0].strip()and "*" in line[0].strip() and line[1].strip() in reg32:
                    #print("OKKK")
                    if "dword" in line[1].strip():
                        l=line[1].split("[")
                    elif "dword" in line[0].strip():
                        l=line[0].split("[")
                    #print("l=",l)
                    l[0]=l[0].strip()
                    #print(l[0])
                    if l[0]=="dword":
                        l=l[1].strip()[:-1]
                        l=l.split("+")
                        esp=l[0]
                        if l[0] in reg and l[0] not in reg32:
                            print("%s:%d error: Invalid effective address"%(Filenm,lc))
                        elif l[0] not in reg and l[0]!= symbi and not list.search(l[0]):
                            print("%s:%d:error:symbol %s undefined"%(Filenm,lc,l[0]))
                            #print("GOOOD")
                        l=l[1].split("*")
                        if list.search(l[0]) and l[1]!="1":
                            print("%s:%d: error: invalid effective address: impossible segment base multiplier"%(Filenm,lc))
                        elif l[0]!= symbi and not list.search(l[0]) and l[0] not in keywords:
                            print("%s:%d:error:symbol %s undefined"%(Filenm,lc,l[0]))
                        elif l[0] in reg32 and (int(l[1])>8 or int(l[1])<0):
                            print("%s:%d: error: invalid effective address: impossible segment base multiplier"%(Filenm,lc))
                        elif l[0]=="esp" and (int(l[1])>1 or int(l[1])<0):
                                print("%s:%d error: Invalid effective address"%(Filenm,lc))

                elif ("dword" in line[0].strip() and not "+" in line[0].strip() and not "*" in line[0].strip()and line[1].strip() in reg32)\
                or("dword" in line[1].strip() and  not "+" in line[1].strip()and not "*" in line[1].strip() and line[0].strip() in reg32):
                    if "dword" in line[0].strip():
                        l=line[0].split("[")
                    elif "dword" in line[1].strip():
                        l=line[1].split("[")
                    l[0]=l[0].strip()
                    if l[0]=="dword":
                        l[1]=l[1].strip()[:-1]
                        #print("l[1]= ",l[1])
                        if l[1] in reg and l[1] not in reg32:
                            print("%s:%d error: Invalid effective address"%(Filenm,lc))

                        elif l[1] not in reg32 and not list.search(l[1]) and l[1]!=symbi:
                            print("%s:%d:error:symbol %s undefined"%(Filenm,lc,l[1]))

                elif "dword" in line[0].strip() and "+" in line[0].strip() and line[1].strip() in reg32\
                or ("dword" in line[1].strip() and "+" in line[1].strip() and line[0].strip() in reg32):
                    #print("THATS>>>")
                    if "dword" in line[0].strip():
                        l=line[0].split("[")
                    elif "dword" in line[1].strip():
                        l=line[1].split("[")
                    l[0]=l[0].strip()
                    if l[0]=="dword":
                        l[1]=l[1].strip()[:-1]
                        l=l[1].split("+")
                        if l[0].strip() in reg and l[0].strip() not in reg32:
                            print("%s:%d error: Invalid effective address"%(Filenm,lc))
                        elif list.search(l[0].strip()) and list.search(l[1].strip()):
                            print("%s:%d: error: invalid effective address"%(Filenm,lc))
                        elif not list.search(l[0].strip()) and l[0].strip() not in reg32:
                            print("%s:%d:error:symbol %s undefined"%(Filenm,lc,l[0].strip()))
                        elif not list.search(l[1].strip()) and l[1].strip() not in reg32:
                            print("%s:%d:error:symbol %s undefined"%(Filenm,lc,l[1].strip()))


                elif ("dword" in line[0].strip() and "*" in line[0].strip() and line[1].strip() in reg32)\
                or ("dword" in line[1].strip() and "*" in line[1].strip() and line[0].strip() in reg32):
                    if "dword" in line[0].strip():
                        l=line[0].split("[")
                    elif "dword" in line[1].strip():
                        l=line[1].split("[")
                    l[0]=l[0].strip()
                    if l[0]=="dword":
                        l[1]=l[1].strip()[:-1]
                        l=l[1].split("*")
                        if l[0].strip() in reg32 and l[1].strip().isdecimal():
                            if int(l[1].strip())>9 or int(l[1].strip())<0:
                                print("%s:%d error: Invalid effective address"%(Filenm,lc))
                        elif l[0].strip() not in reg32 and list.search(l[0].strip()) and (int(l[1].strip())>1 or int(l[1].strip())<0):
                            print("%s:%d: error: invalid effective address: impossible segment base multiplier"%(Filenm,lc))
                        elif l[0].strip() in reg32 and not l[1].strip().isdecimal() or (l[1].strip() in reg32 and not l[0   ].strip().isdecimal()):
                            print("%s:%d:error:unable to multiply two non scalar objects"%(Filenm,lc))
                        elif not list.search(l[0].strip()):
                            print("%s:%d:error:symbol %s undefined"%(Filenm,lc,l[0].strip()))

                elif ("[" in line[0].strip() and line[1].strip() in reg )or ("[" in line[1].strip() and\
                line[0].strip() in reg):
                    #print("HUUUUU")
                    if "[" in line[0].strip():
                        l=line[0].split("[")
                        l[1]=l[1].strip()[:-1]
                        #print("l[1]= ",l[1])
                        if list.search(l[1]):
                            if line[1].strip() not in reg:
                                print("%s:%d:error: operation size not specified"%(Filenm,lc))


            elif w in ins1:
                ins=w
                w=""
                count=i
                #print(line[count:pos])
                line=line[count:pos]
                if "dword" in line:
                    if "+" in line and "*" in line:
                        size=proper_sib(line)
                    elif "+" in line:
                        size=base_index(line)
                    elif "*" in line:
                        size=base_scale(line)
                    else:
                        size=base(line)
                if ins=="inc" or ins=="dec":
                    if line.strip().isdecimal() or line.strip() not in keywords:
                        print("%s:%d: error:Invalid combination of opcode and operands"%(Filenm,lc))

                elif not line.strip().isdecimal():
                    if not line.strip()[0].isalpha():
                        print("%s:%d error:expression syntax error"%(Filenm,lc))
            i=pos-1
            break
        if flag==1:
            list.AtEnd(symbi)
        line=f.readline()
        line=line.strip()
        lc+=1

def bss(f,lc):
    flag2=0
    i=0
    line = f.readline()
    line.rstrip()
    count=0
    countp=0
    address="00000000"
    while(line):
        if "section .data" in line:
            data(f,lc)
            break
        elif "section .text" in line:
            lc+=1
            txt(f,lc)
            break
        i=0
        while(line[i]==" "or line[i]=="\t"):
            i+=1
        #print(line)
        section="bss"
        word=""
        for j in range(i,len(line)):
            if line[j]!=" ":
                word+=line[j]
            else:
                symbi=word
                ch=check_redefine(symbi,lc)
                word=""
                break

        while(j<len(line) and line[j]==" "):
            j+=1
        while(j<len(line) and line[j]!=" "):
            word+=line[j]
            j+=1

        if word=="resd" or word =="resb" or word=="resw":

            address="0"*(8-len(address))+address
            addr=address
                #print("address=",address)
            if word=="resd":
                type="Double"
            elif word=="resw":
                type="Word"
            else:
                type="Byte"
            if j<len(line):
                value=line[j:len(line)]
                flag2=1
                value=value.strip()
            if flag2==0:
                print("%s:%d error: Invalid combination of opcode and operand"%(Filenm,lc))
            #print("value=",value)
            if value=="" or value=="\n":
                print("%s:%d error: Invalid combination of opcode and operand"%(Filenm,lc))
            elif '"' not in value  and not value.isdecimal():
                if list.search(value):
                    print("%s:%d error: attempt to reserve non-constant quantity of BSS space"%(Filenm,lc))
                else:
                    print("%s:%d warning: forward reference in RESx can have unpredictable results"%(Filenm,lc))
                    print("%s:%d error: symbol %s undefined"%(Filenm,lc,value))

        elif word=="dd" or word=="dw" or word=="db":
            print("%s:%d  warning: attempt to initialize memory in BSS section `.bss': ignored"%(Filenm,lc))
        else:
            print("%s:%d: error: parser: instruction expected"%(Filenm,lc))

        list.AtEnd(symbi)
        line = f.readline()
        line.rstrip()
        lc+=1

def data(f,lc):
    i=0
    line = f.readline()
    line.rstrip()
    count=0
    countp=0
    address="00000000"
    lc+=1
    while(line):
        if "section .bss" in line:
            lc+=1
            bss(f,lc)

            break
        elif "section .txt" in line:
            txt(f,lc)
            break
        section="data"
        i=0
        line= line.strip()
        #print(line)
        check=alone_label(line,lc)
        if check==1:
            continue
        else:
            pass

        word=""
        for j in range(len(line)):
            if line[j]!=" ":
                word+=line[j]
            else:
                break

        symbi=word
        #print("symbi=",symbi)
        if not symbi[0].isalpha() or symbi in keywords:
            print("%s:%d error: label or instruction expected at start of line "%(Filenm,lc))

                #print("symbi=",symbi)word=""
        word=""
        while(j<len(line) and line[j]==" "):
            j+=1
        while(j<len(line) and line[j]!=" "):
            word+=line[j]
            j+=1
        #print("word[0]=",word[0])
        #print("word=",word)
        if word!="db" and word!="dd" and word!="dw":
            print("%s:%d: error: parser: instruction expected"%(Filenm,lc))

        elif word=="db" or word =="dd" or word=="dw":
            while(j<len(line) and line[j]==" "):
                j+=1
            if ',' in line:
                word=line[j:len(line)].split(',')
                #print(word)
                for i in range(len(word)):
                #word[i]=word[i].strip()
                    if not word[i].strip().isdecimal():
                        word[i]=word[i].strip()
                        if word[i][0]!='"' and word[i][-1]!='"':
                            if word[i][0]!="'" and word[i][-1]!="'":
                                print("%s:%d: error:symbol %s undefined"%(Filenm,lc,word[i]))
            else:
                word=""
                while(j<len(line) and line[j]!=" "):
                    word+=line[j]
                    j+=1
                if not word.isdecimal():
                    if word[0]!='"' or word[-1]!='"':
                        print("%s:%d: error:symbol %s undefined"%(Filenm,lc,word))

        list.AtEnd(symbi)
        line = f.readline()
        line.rstrip()
        lc+=1
def red(text):
    print('\033[31m', text, '\033[0m', sep='')
def cyan(text):
    print('\033[36m', text, '\033[0m', sep='')


list = SLinkedList()
Filenm=input("Enter  Assembly file name :")
f = open(Filenm,"r")

while True:
    line = f.readline()
    line=line.strip()
    lc+=1
    check=alone_label(line,lc)
    if check==1:
        continue
    else:
        break
if "section .data" in line:
    data(f,lc)
elif "section .bss" in line:
    bss(f,lc)
