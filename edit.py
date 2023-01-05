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
show_paper( paper_fd , num_question )
if num_question == 0:
    exit()

while num_question > 0:
    operation_question = input("\033[1;33;40m請選擇你想要編輯的題目，輸入[]的數字即可\033[0m")
    operation_question = int(operation_question)
    if operation_question >= num_question:
        print("\033[1;33;40m沒有那麼多題目\033[0m")
        exit()
    paper_fd.seek((1+operation_question)*size_question)
    description = paper_fd.read((int)(size_description/2))
    paper_fd.seek((1+operation_question)*size_question+size_description)
    answer = paper_fd.read((int)(size_answer/2))
    print("\033[1;32;40m題目: %s\033[0m" %description )
    print("\033[1;36;40m答案: %s\033[0m" %answer )
    new_description = input("\033[1;32;40m(%d字上限)請輸入新題目\033[0m" %(int(size_description/2)))
    new_answer      = input("\033[1;36;40m(%d字上限)請輸入新答案\033[0m" %(int(size_answer/2)))
    write_thing( paper_fd , (1+operation_question)*size_question , new_description , size_description )
    write_thing( paper_fd , (1+operation_question)*size_question+size_description , new_answer , size_answer )
    next = input("\033[1;33;40m繼續新增請按YES/Y/yes/y/1\033[0m")
    if next == "YES" or next == "Y" or next == "yes" or next == "y" or next == "1":
        continue
    else:
        break
print("\033[1;33;40m編輯完成\033[0m")
