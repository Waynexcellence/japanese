from general import *
colorama.init(autoreset=True)

sure = input("\033[1;33;40m確定要重置?(YES/Y/yes/y/1)\033[0m")
if sure != "YES" and sure != "Y" and sure != "yes" and sure != "y" and sure != 1:
    exit()

if not os.path.isdir("paper"):
    os.mkdir("paper")
    print("\033[1;33;40m已新增paper資料夾\033[0m")
    Paper = open("./paper/Paper" , "w+" )
    print("\033[1;33;40m已新增Paper檔案\033[0m")
else:
    Paper , num_paper = Connect_To_Paper()
    for x in range(num_paper):
        Paper.seek((1+x)*size_paper)                                    #拿刪除名
        delete_paper_name = Paper.read((int)(size_paper/2))
        Paper.seek((1+x)*size_paper)
        delete_paper_name = Paper.read(strlen(delete_paper_name,size_paper))
        print("\033[1;33;40m刪除 %s\033[0m" %delete_paper_name )
        delete_paper_name = "./paper/" + delete_paper_name              #拿刪除名
        os.remove(delete_paper_name)
update_num( Paper , 0 )