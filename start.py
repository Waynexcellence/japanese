from general import *
colorama.init(autoreset=True)

fp , num_question = init()
print("\033[1;33;40m目前有 %d 個考題\033[0m" % num_question)
if num_question == 0:
    exit()

while True:
    position = random.randint(0,num_question-1)
    fp.seek((1+position)*size_question)
    # print("現在在:",fp.tell())
    chinese = fp.read((int)(size_description/2))
    # print("現在在:",fp.tell())
    print("\033[1;32;40m翻譯 %s\033[0m" %chinese)
    option = {}
    messy_ever = [False,False,False,False]
    messy = 0
    correct_answer = None
    for x in range(4):
        fp.seek((1+position)*size_question+(1+x)*size_description)
        # print("現在在:",fp.tell())
        option[x] = fp.read((int)(size_description/2))
        # print("現在在:",fp.tell())

    while messy < 4:
        rand = random.randint(0,3)
        if messy_ever[rand] == True:
            continue
        print("\033[1;33;40m[%d] \033[1;34;40m%s\033[0m" %(messy,option[rand]))
        if rand == 0:
            correct_answer = messy
        messy += 1
        messy_ever[rand] = True
    buf = input("Choose an option.")
    user_answer = int(buf)
    if user_answer != correct_answer:
        print("\033[1;31;40mWA\n%s = %s\n\033[0m" %(chinese,option[0]) )
    else:
        print("\033[1;32;40mAC\n\033[0m")

