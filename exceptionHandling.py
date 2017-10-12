print('Trail on exception handling')

try:
    print('Execution starts inside try block')
    name = input('What is your name: ')
    print('Hello,',name)
    age = input('What is your age: ')
    age = int(age)
    print('hello'+10)
    import mars

except TypeError as t:
    print(str(t))
except NameError as n:
    print('NameError triggered')
except Exception as e:
    print('***Some general exception occured***')
    print(str(e))

print('Execution continues on')
