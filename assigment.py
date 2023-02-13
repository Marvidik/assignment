def two_sum(num1,num2):
    sums=num1+num2

    print(sums)

    for i in range(2, int(sums/2)+ 1):
        if (sums% i)==0:
            print("it is an ordinary numbet")
            break
        else:
            print("This is a prime")
            break

two_sum(4,8)