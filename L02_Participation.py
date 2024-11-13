contacts = {'Jenny' : 8675309, 'James':5551212}
print(*contacts)
print('Jennys number is', contacts['Jenny'])
brian = contacts.get('James')
print('Brain has a new number',brian)