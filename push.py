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

while True:
    while True:
        description = input("\033[1;32;40m(%d字上限)請輸入題目\033[0m" %(int(size_description/2)))
        if len(description) > int(size_description/2):
            print("\033[1;33;40m題目請不要超過%d個字謝謝\033[0m" %(int(size_description/2)))
        else:
            break
    while True:
        answer = input("\033[1;36;40m(%d字上限)請輸入答案\033[0m" %(int(size_answer/2)))
        if len(answer) > int(size_answer/2):
            print("\033[1;33;40m答案請不要超過%d個字謝謝\033[0m" %(int(size_answer/2)))        
        else:
            break
    write_thing( paper_fd , (1+num_question)*size_question , description , size_description )
    write_thing( paper_fd , (1+num_question)*size_question+size_description , answer , size_answer )
    num_question += 1
    update_num( paper_fd , num_question)
    next = input("\033[1;33;40m繼續新增請按YES/Y/yes/y/1\033[0m")
    if next == "YES" or next == "Y" or next == "yes" or next == "y" or next == "1":
        continue
    else:
        break

print("\033[1;33;40mpush完成\033[0m")