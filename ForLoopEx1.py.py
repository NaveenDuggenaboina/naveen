#program for generating 1 to n numbers where n is +ve
#forloopex1.py
n=int(input("eneter how many nunmbers u want to generate:"))
if(n<=0):
    print("{} is invalid".format(n))
else:
    print("*"*50)
    print("eneter within {}".format(n))
    print("*" * 50)
    for i in range(1,n+1):
        print("\t\t{}".format(i))
    else:
        print("*" * 50)