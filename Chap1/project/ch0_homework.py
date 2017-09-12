import random
set_number=random.randint(1,20)
#生成1-10间的随机数
for i in range(0,10):
    num=input("请输入你猜的数字:\n>")
    if num.isdigit()==True:
        if (int(num)<1 or int(num)>20):
            print("请输入1-20间的数字！")
        elif (int(num)>=1 and int(num)<=20):


            if (int(num) < set_number)  :
                print("你猜的太小了！")
                print("你已经猜了%d次" %(i+1) )
            elif( int( num )> set_number):
                print("你猜的太大了！")
                print("你已经猜了%d次" %(i+1) )
            else:
                break
            if (i==9):
                print("你在 %d 次内没能猜出结果" %(i+1) )
                break

        elif num.isdigit()==False:
            print("请输入数字！")



if (int(num)== set_number):
    print("答案是：%d" %set_number)
    print( "你猜对了，你在第 %d 次猜中了数字 ！" %(i+1))
