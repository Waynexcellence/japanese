from general import *
colorama.init(autoreset=True)

fp , num_question = init()
print("\033[1;33;40m目前有 %d 個考題\033[0m" % num_question)
if num_question == 0:
    exit()

for x in range(num_question):                            ## show info
    print("\033[1;33;40m[%d] \033[0m" %x , end='')
    fp.seek((1+x)*size_question , 0 )
    chinese = fp.read((int)(size_description/2))
    print("\033[1;32;40m中文釋義:%s    \033[0m" %chinese , end='')
    for y in range(4):
        fp.seek((1+x)*size_question+(1+y)*size_description , 0 )
        option = fp.read((int)(size_description/2))
        print("\033[1;34;40moption:%s         \033[0m" %option , end='')
    print("")
print("")                                                ## show info

buf = input("\033[1;33;40mChoose a [number] you want to delete.\033[0m")
delete_num = int(buf)
if delete_num >= num_question:
    exit()

for x in range(delete_num+1 , num_question):         ## 刪除
    fp.seek((1+x)*size_question , 0 )
    temp = fp.read(size_question)
    fp.seek((x)*size_question , 0 )
    space = '\0'*size_question
    fp.write(space)
    fp.seek((x)*size_question , 0 )
    fp.write(temp)                                   ## 刪除

num_question -= 1
fp.seek(0,0)
for x in range(10):
    fp.write('\0')
fp.seek(0,0)
fp.write(str(num_question))
print("\033[1;33;40m刪除完畢\033[0m")
    






