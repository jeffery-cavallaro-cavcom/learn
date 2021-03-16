def func(arg1=1, arg2=2, arg3=3, arg4=None):
    values = {'arg1': arg1, 'arg2': arg2, 'arg3': arg3}
    if arg4:
        values['arg4'] = arg4
    return values


print(func())
print(func(100, 200, 300, 42))
print(func(arg2=20, arg1=10, arg4=40))

args = [-1, -2, -3]
print(func(*args))

args = {'arg3': 33, 'arg2': 22, 'arg4': 44}
print(func(**args))
