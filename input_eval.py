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
'''input为int或float型时，可以直接用eval，
为str时则应加' '，或直接不加eval，input本身为str型
'''