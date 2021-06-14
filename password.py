#Create by Charlie////////////////////////////////
#Test by Charlie
#            ///
#            /// 
#START
#input()
import easygui

print("Please input your username and password")

myname = input()

if myname == 'Charlie':
    print(myname)
    print("hello"+myname)
else:
    print("None Access")
password = input()

#if words
if myname == 'Charlie'or'zhanglan':
    print("hello,please chack your password")
    print(password)

#input twice
    password = input()

#if words
    if password == '123456':
        print('Access granted')
#else words
else:
    print("Wrong password,please try again")

#gui print////////////////////
easygui.msgbox(msg="Welcome",title="Welcome",ok_button='OK')
easygui.choicebox(msg="Enter",title="Enter",choices=None)


    #           OVER           #
    #////////////////////////////#
