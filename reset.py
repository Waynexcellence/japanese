from general import *

Paper , num_paper = Connect_To_Paper()

for x in range(num_paper):
    Paper.seek((1+x)*size_paper)                               #拿刪除名
    delete_paper_name = Paper.read((int)(size_paper/2))
    Paper.seek((1+x)*size_paper)
    delete_paper_name = Paper.read(strlen(delete_paper_name,size_paper))  #拿刪除名
    os.remove(delete_paper_name)
update_num( Paper , 0 )