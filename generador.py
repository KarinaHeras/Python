def numerosPares(limite):
    num=1

    while   num<limite:
        yield num*2
        num=num+1
devuelvePares=numerosPares(100)    

for i in devuelvePares:
    print(i)


