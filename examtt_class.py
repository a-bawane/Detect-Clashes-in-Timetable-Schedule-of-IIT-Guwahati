department_dict = {'BT': "Bioscience and Bioengineering", 'CE': "Civil Engineering", 'CH': "Chemistry",
                   'CL': "Chemical", \
                   'CS': "Computer Science", 'DD': "Department of Design",
                   'EE': "Electronics and Electrical Engineering", \
                   'EN': "Energy", 'HS': "Humanities and Social Science", 'IF': "Instriments facility",
                   'MA': "Mathematics", \
                   'ME': "Mechanical", 'NT': "Nanotechnology", 'PH': "Physics", 'RT': "Rural Technology"}
input_file = open('examtt_input.txt.txt')
C_Dictionary = {}

def exam_timetable_clash_detector():
    not_exam = {}
    for key,value in department_dict.items():
        print("###############################################################")
        print("Exam clashes in Department:",value)
        print("###############################################################")


        temp_m_dict={}
        temp_e_dict={}

        for key1, value1 in C_Dictionary.items():

            if value1[2] == "***" or value1[3] =="***":
                key6 = "***"
                not_exam.setdefault(key6, [])
                if key1 not in not_exam[key6]:
                    not_exam[key6].append(key1)
                continue
            for key2, value2 in C_Dictionary.items():
                if key1 != key2 and key==key1[:2] and key==key2[:2] and value1[2] == value2[2] and value2[2] != "***":

                    key4=value1[2]

                    temp_m_dict.setdefault(key4,[])

                    if key1 not in temp_m_dict[key4]:
                        temp_m_dict[key4].append(key1)
                    if key2 not in temp_m_dict[key4]:
                        temp_m_dict[key4].append(key2)

                if key1 != key2 and key == key1[:2] and key==key2[:2]  and  value1[3] == value2[3] and value2[3] != "***":
                    key5 = value1[3]

                    temp_e_dict.setdefault(key5, [])
                    if key1 not in temp_e_dict[key5]:
                        temp_e_dict[key5].append(key1)

                    if key2 not in temp_e_dict[key5]:
                        temp_e_dict[key5].append(key2)

        #print(temp_m_dict)
        print("****************Midsem Exam*******************")
        if bool(temp_m_dict):
            for k,v in temp_m_dict.items():

                print(k)
                #l = temp_m_dict[k]
                for s in v:
                    print(s,":",C_Dictionary[s][0])
        else:
            print("No clashes")

        print("****************Endsem Exam*******************")
        if bool(temp_e_dict):
            for k, v in temp_e_dict.items():

                print(k)
                # l = temp_m_dict[k]
                for s in v:
                    print(s,":",C_Dictionary[s][0])
        else:
            print("No clashes")
    print("****************Courses which does not have exam*******************")
    if bool(not_exam):
            for k, v in not_exam.items():

                #print(k)
                # l = temp_m_dict[k]
                for s in v:
                    print(s,":",C_Dictionary[s][0])
l1 = input_file.readlines()

for i in l1:
        T_L = i.strip().split("\t")
        C_Dictionary[T_L[0]] = T_L[1:]


exam_timetable_clash_detector()
#print(C_Dictionary)

