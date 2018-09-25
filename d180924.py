while True:
    a = input()
    try:
        b = eval(a)
        print(b)
        print(type(b))
    except:

        if a == '' or a == ' ':
            break
        else:
            print(a, '\nstr')
