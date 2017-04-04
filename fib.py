a = {'key': 'value'}
b = {'key': [1, 2, 3]}
c = {'inventory': {}}

print(a['key'])
print(b['key'][1])

inp = input('enter something  ')
b[inp] = 'we just added a key called {}'.format(inp)
print(b)

c['inventory'] = {'axe': 100}
print(c)
