from general import *
colorama.init(autoreset=True)

Paper , num_paper = Connect_To_Paper()
show_Paper( Paper , num_paper )

mode = input("\033[1;33;40m[0]增加考卷 [1]重新命名考卷 [2]刪除考卷\033[0m")
mode = int(mode)

if mode == 0:#增加考卷
    new_paper_name = input("\033[1;32;40m(%d字上限)新考卷的名字是:\033[0m" %(int(size_paper/2))) # 拿新考卷名字
    write_thing( Paper , (1+num_paper)*size_paper , new_paper_name , size_paper )              # 先 update 到 Paper
    new_paper_name = "./paper/" + new_paper_name                                               # 加工
    fd = open( new_paper_name , "w+" )
    fd.write("0\0\0\0\0\0\0\0\0\0")
    num_paper += 1
    update_num( Paper , num_paper )
    show_Paper( Paper , num_paper )
elif mode == 1:#重新命名考卷
    if num_paper == 0:
        print("\033[1;33;40m目前沒有考卷\033[0m")
        exit()
    operation_paper = input("\033[1;33;40m請選擇你想要重命名的考卷，輸入[]的數字即可\033[0m")
    operation_paper = int(operation_paper)
    if operation_paper >= num_paper:
        print("\033[1;33;40m沒有那麼多考卷\033[0m")
        exit()
    new_paper_name = input("\033[1;32;40m(%d字上限)考卷的新名字是:\033[0m" %(int(size_paper/2)))
    write_thing( Paper , (1+operation_paper)*size_paper , new_paper_name , size_paper ) # 先 update 到 Paper
    Paper.seek((1+operation_paper)*size_paper)                     # 拿舊名
    old_paper_name = Paper.read((int)(size_paper/2))
    Paper.seek((1+operation_paper)*size_paper)
    old_paper_name = Paper.read(strlen(old_paper_name,size_paper)) # 拿舊名
    old_paper_name = "./paper/" + old_paper_name                   # 舊名加工
    new_paper_name = "./paper/" + new_paper_name                   # 新名加工
    os.rename( old_paper_name , new_paper_name )
    show_Paper( Paper , num_paper )
else:#刪除考卷
    if num_paper == 0:
        print("\033[1;33;40m目前沒有考卷\033[0m")
        exit()
    operation_paper = input("\033[1;33;40m請選擇你想要刪除的考卷，輸入[]的數字即可\033[0m")
    operation_paper = int(operation_paper)
    if operation_paper >= num_paper:
        print("\033[1;33;40m沒有那麼多考卷\033[0m")
        exit()
    Paper.seek((1+operation_paper)*size_paper)                            # 拿刪除名
    delete_paper_name = Paper.read((int)(size_paper/2))
    Paper.seek((1+operation_paper)*size_paper)
    delete_paper_name = Paper.read(strlen(delete_paper_name,size_paper))  # 拿刪除名
    delete_paper_name = "./paper/" + delete_paper_name                    # 刪除名加工
    os.remove(delete_paper_name)
    for x in range(operation_paper,num_paper):
        Paper.seek((2+x)*size_paper)
        copy = Paper.read((int)(size_paper/2))
        write_thing( Paper , (1+x)*size_paper , copy , size_paper )
    num_paper -= 1
    update_num( Paper , num_paper )
    





