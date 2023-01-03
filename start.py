from general import *
colorama.init(autoreset=True)

Paper , num_paper = Connect_To_Paper()
show_Paper( Paper , num_paper )

if num_paper == 0:
    exit()

operation_paper = input("\033[1;33;40m請選擇考卷，輸入[]的數字即可\033[0m")
operation_paper = int(operation_paper)

if operation_paper >= num_paper:
    print("\033[1;33;40m沒那麼多考卷\033[0m")
    exit()

Paper.seek((1+operation_paper)*size_paper)
paper_name = Paper.read((int)(size_paper/2))
Paper.seek((1+operation_paper)*size_paper)
paper_name = Paper.read(strlen(paper_name,size_paper))

paper_fd , num_question = connect_to_paper( paper_name )
if num_question == 0:
    print("\033[1;33;40m此考卷目前沒有題目\033[0m")
    exit()
num_option = 4
if num_question < 4:
    print("\033[1;33;40m題目有點少(不到4個)，但仍可開始測驗")
    num_option = num_question
print("\033[1;33;40m考試開始:(每五題為一輪)\033[0m")
total_score = 0
correct_score = 0
while True:
    index = {}
    option = {}
    finish_index = 0
    while finish_index < num_option:            #放入index
        verify = True
        temp = random.randint(0,num_question-1)
        for x in range(0,finish_index):
            if temp == index[x]:
                verify = False
                break
        if verify:
            index[finish_index] = temp
            finish_index += 1                   #放入index
    paper_fd.seek((1+index[0])*size_question)              # 放入正確description
    description = paper_fd.read((int)(size_description/2)) # 放入正確description
    paper_fd.seek((1+index[0])*size_question+size_description) # 放入正確選項
    correction_option = paper_fd.read((int)(size_answer/2))    # 放入正確選項
    for x in range(num_option):                                    # 放入 option
        paper_fd.seek((1+index[x])*size_question+size_description)
        option[x] = paper_fd.read((int)(size_answer/2))
    random.shuffle(option)                                         # 放入 option
    correct_index = -1                     # 得到 correct_index
    for x in range(num_option):
        if correction_option == option[x]:
            correct_index = x
            break                          # 得到 correct_index
    print("\033[1;32;40m翻譯:%s    \033[0m" %description , end="")
    for x in range(num_option):
        print("\033[1;36;40m選項[%d] %s    \033[0m" %(x,option[x]) , end="")
    print("")
    user_answer = input("\033[1;33;40m請作答，輸入選項[]的數字即可\033[0m")
    user_answer = int(user_answer)
    if user_answer == correct_index:
        print("\033[1;32;40mAC\033[0m")
        correct_score += 1
    else:
        print("\033[1;31;40mWA\033[0m")
    total_score += 1
    if total_score % 5 == 0:
        print("\033[1;33;40m目前分數 %d / %d\033[0m" %(correct_score,total_score) )
        next_operation = input("\033[1;33;40m繼續請按YES/Y/yes/y\033[0m")
        if next_operation == "YES" or next_operation == "Y" or next_operation == "yes" or next_operation == "y":
            continue
        else:
            break
print("\033[1;33;40m總分 %d / %d\033[0m" %(correct_score,total_score) )

