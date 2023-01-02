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
    operation_question = input("\033[1;33;40m請選擇你想要刪除的題目，輸入[]的數字即可\033[0m")
    operation_question = int(operation_question)
    if operation_question >= num_question:
        print("\033[1;33;40m沒有那麼多題目\033[0m")
        exit()
    for x in range(operation_question,num_question):
        paper_fd.seek((2+x)*size_question)
        description = paper_fd.read((int)(size_description/2))
        paper_fd.seek((2+x)*size_question+size_description)
        answer = paper_fd.read((int)(size_answer/2))
        write_thing( paper_fd , (1+x)*size_question , description , size_description )
        write_thing( paper_fd , (1+x)*size_question+size_description , answer , size_answer )
    num_question -= 1
    update_num( paper_fd , num_question )
    show_paper( paper_fd , num_question )
    next_operation = input("\033[1;33;40m繼續刪除請按YES/Y/yes/y\033[0m")
    if next_operation == "YES" or next_operation == "Y" or next_operation == "yes" or next_operation == "y":
        continue
    else:
        break

print("\033[1;33;40mdelete完成\033[0m")