

input_file = open('classtt_input.txt')
C_Dictionary = {}


def timetable_clash_detector():
    l1 = input_file.readline()
    print()
    print(l1)
    l1 = input_file.readline()
    temp = l1.strip().split(",")
    #print(temp)
    program_dict = {}

    for i in temp:
        t2 = C_Dictionary.get(i)
        #print(t2)
        #print(t2[-1])
        program_dict[i] = t2[-1]

    #print(program_dict)

    for i in 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday':
        t3 = []
        for k1, v1 in program_dict.items():

           # print(k1,v1)
            if not v1.get(i):
                continue
            for k2, v2 in program_dict.items():
                if not v2.get(i):
                    continue
                #print(k1,k2)
                if  k1!= k2 :

                    if v1.get(i) and v2.get(i) :
                        #print((float(v1.get(i)[0])),(float(v1.get(i)[1])))
                        #print((float(v2.get(i)[0])),(float(v2.get(i)[1])))
                        #print(k1,k2)
                        if (float(v1.get(i)[0]) <= float(v2.get(i)[0]) <= float(v1.get(i)[1]) and \
                                float(v1.get(i)[0]) <= float(v2.get(i)[1]) <= float(v1.get(i)[1])):

                            if k2 not in t3 or k1 not in t3:
                                t3.append(k1)
                                t3.append(k2)
                                print(k1,":",C_Dictionary[k1][1],"And",k2,":",C_Dictionary[k2][1],"on", i, "at",v1[i][0],"to",v1[i][1])

                        elif (float(v2.get(i)[0]) <= float(v1.get(i)[0]) <= float(v2.get(i)[1]) and \
                                float(v2.get(i)[0]) <= float(v1.get(i)[1]) <= float(v2.get(i)[1])):

                            if k2 not in t3 or k1 not in t3:
                                t3.append(k1)
                                t3.append(k2)
                                print(k1,":",C_Dictionary[k1][1],"And",k2,":",C_Dictionary[k2][1],"on", i, "at",v2[i][0],"to",v2[i][1])
        #print(t3)
    if len(t3)<1:
        print("No clashes")
    program_dict.clear()
    return

l1 = input_file.readline()
while l1:
    if l1.strip() == "#############################################################":
        break
    T_L = l1.strip().split("\t")
    l1 = input_file.readline()
    if len(T_L) < 5:
        continue
    C_Dictionary[T_L[0]] = T_L[1:]
    temp = T_L[-1].split(",")
    tt_dict = {}
    for i in temp:
        t1 = i.split("-")
        # value = i.split("-")[1]
        tt_dict[t1[0]] = t1[1:]

    C_Dictionary[T_L[0]].append(tt_dict)
#print(C_Dictionary)
print("################################################")
print("Clashes in Timetable department and program wise")
print("################################################")
l1 = input_file.readline()
while l1:
   # print("started from here")

    if l1.strip() == "***":
        timetable_clash_detector()
    l1 = input_file.readline()
    #print(l1)
