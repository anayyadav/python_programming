# print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)
print("This is the output of the screen")

a= 5
print('The value of a is ',a)

#formating the output
print('Hello {name},{greeting}'.format(greeting= 'Good morning', name = 'John'))

print('I love {0} and {1}'.format('bread','butter'))
# Output: I love bread and butter

print('I love {1} and {0}'.format('bread','butter'))
# Output: I love butter and bread