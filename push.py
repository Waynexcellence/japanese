from general import *
colorama.init(autoreset=True)

fp , num_question = init()
print("\033[1;33;40m目前有 %d 個考題\033[0m" %num_question )

chinese = input("\033[1;32;40m請輸入中文(不超過10個字):\033[0m")#請輸入中文(綠色)
if len(chinese) > 10:
    exit()

fp.seek((1+num_question)*size_question)
# print("現在在:",fp.tell())
fp.write(chinese)
# print("現在在:",fp.tell())
print("\033[1;34;40m請輸入四個選項(長度不超過10)\033[0m")
for x in range(4):
    option = input("\033[1;34;40moption[%d]:\033[0m" %x)       #請輸入選項(藍色)
    if len(option) > 10:
        exit()
    fp.seek((1+num_question)*size_question+(1+x)*size_description)
    # print("現在在:",fp.tell())
    fp.write(option)
    # print("現在在:",fp.tell())
print("\033[1;33;40m新增完成\033[0m")
num_question += 1
fp.seek(0,0)
fp.write(str(num_question))
    





    
