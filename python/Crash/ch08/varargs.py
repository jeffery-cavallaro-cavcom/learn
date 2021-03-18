def func(posarg, *listargs, **keyargs):
    print(posarg)
    print(listargs)
    print(keyargs)


func('hello', 1, 2, 'xyz', key1=42, key2='xyzzy')
