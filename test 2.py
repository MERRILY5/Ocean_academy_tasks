##Convert string to uppercase

##string=input("Enter the string: ")
##count=0
##for i in string:
##    if i.isupper():
##        count+=1
##print(count)


##Covert string to capitalize

##string=input("Enter the string: ")
##word=""
##for i in string.split():
##    word+=i.capitalize()
##    word+=" "
##print(word)



##Password checker

##pre="Tall$%"
##pwd=input("Enter your password: ")
##if pre==pwd:
##    print("Password correct")
##else:
##    print("Password incorrect")



##VOWEL REPLACED BY STAR

##string=input("Enter your string: ")
##vowel="aeiouAEIOU"
##newstring=""
##for i in string:
##    if i in vowel :
##        newstring+='*'
##    elif " " == i:
##        print(end="")
##    else:
##        newstring+=i
##print(newstring)





##Replace words by keys in dict

##string=input("Enter your string: ")
##string=string.split()
##d={
##    "geeks":"all CS aspirants"
##    }
##j=0
##for i in string:
##    if i in d:
##        string.remove(i)
##        string.insert(j,d[i])
##    j+=1
##for i in string:
##    print(i,end=" ")



##Bubble sort

##def sort(l):
##    n=len(l)
##    for i in range(n):
##        for j in range(0,n-i-1):
##            if l[j]>l[j+1]:
##                l[j],l[j+1]=l[j+1],l[j]
##    print(l)
##
##l=[1,5,7,3,9,8,4]
        



##Armstrong number

##num=int(input("Enter a number: "))
##result=0
##length=len(str(num))
##org=num
##while(num > 0):
##    m = num % 10
##    result += pow(m,length)
##    num=num//10
##if result==org:
##    print("YES, it is an armstrong number")
##else:
##    print("NO, it is not an armstrong number")



##Happy number

##num=int(input("Enter a number: "))
##def happy(num):
##    res=0
##    while(num >= 1):
##        m=num%10
##        res+=(m**2)
##        num=num//10
##    return res
##
##res=num
##while(res!=1 and res != 4):
##    res=happy(res)
##
##if res==1:
##    print("It is a happy number")    
##else:
##    print("It is not a happy number")   



##Spy number

##num=int(input("Enter your number: "))
##summer=0
##multi=1
##while(num > 0):
##    m=num%10
##    summer+=m
##    multi*=m
##    num=num//10
##if summer==multi:
##    print("It is a spy number")
##else:
##    print("It is not a spy number")



##Neon number

##num=int(input("Enter your number: "))
##multi=(num**2)
##summer=0
##while(multi > 0):
##    m=multi%10
##    summer+=m
##    multi=multi//10
##if summer==num:
##    print("It is a neon number")
##else:
##    print("It is not a neon number")
    


##Rotate an array

##num=int(input("Enter the number of elements needed: "))
##l=[int(input("Enter an element: ")) for i in range(0,num)]
##rotate=int(input("Enter the number for rotations: "))
##length=len(l)
##rotate %= length
##rotated = l[-rotate:] + l[:-rotate]
##print(rotated)
        
  

##List number split and checker
  
##l=[21,101,30501,450]
##summ=0
##mul=1
##def check(summ,mul):
##    l1=[]
##    l=[21,101,30501,450]
##    for i in range(0,len(l)):
##        if summ % l[i]==0 and mul % l[i]==0:
##            l1.append(0)
##        else:
##            l1.append(1)
##    return l1
##
##for i in range(0,len(l)):
##    while(l[i] > 0):
##        m = l[i] % 10
##        if m == 0:
##            mul = mul * 1
##        else:
##            summ = summ + m
##            mul = mul * m
##            l[i]=l[i]//10
##    print(check(summ,mul))
            


##Parathesis Checker

##l=list(input("Enter your string: "))
##start="{[("
##end="}])"
##checker={
##    ")":"(",
##    "}":"{",
##    "]":"["
##    }
##def expression(l):
##    check=[]
##    for i in l:
##        if i in start:
##            check.append(i)
##        elif i in end:
##            if not check or check[-1] != checker[i]:
##                return False
##            check.pop()
##    return not check
##
##if expression(l):
##    print(True)
##else:
##    print(False)




##input [9,9] output: [1,0,0]

##num=int(input("Enter the length of the array: "))
##l=[input("Enter the elements: ") for i in range(num)]
##check=""
##for i in l:
##    check+=i
##a=int(check)
##l=a+1
##string=str(l)
##final=[]
##for i in string:
##    final.append(i)
##print(final)


    















































































