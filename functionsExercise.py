# def print_args(*args):
#   # for arg in args:
#   #   print(f'arg = {arg}')
#   print(args)
#   print(type(args))

# print_args('a')
# print_args('a', 'b')
# print_args('a', 'b', 'c')

def printKeywordArgs(**kwargs):

  print("\n")
  print(kwargs)
  print(type(kwargs))
  
  for key, value in kwargs.items():
    print(f'{key}: {value}')

  third = kwargs.get('third', None)
  if third != None:
    print('third arg =', third)

printKeywordArgs(first="a")
printKeywordArgs(first="a", second="b")
printKeywordArgs(first="a", second="b", third="c")