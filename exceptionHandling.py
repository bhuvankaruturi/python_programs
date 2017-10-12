print('Trail on exception handling')

try:
    print('Execution starts inside try block')
    print('hello'+10)
    import mars

except TypeError as t:
    print(str(t))
except NameError as n:
    print('NameError triggered')
except Exception as e:
    print(str(e))

print('Execution continues on')
