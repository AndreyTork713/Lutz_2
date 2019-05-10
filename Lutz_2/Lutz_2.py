bob = dict(name = 'Bob Smith',age = 42,pay = 30000,job = 'dev')
sue = dict(name = 'Sue Jonson',age = 44,pay = 40000,job = 'hdw')
andy = dict(name = 'Andy Near',age = 48,pay = 45000,job = 'dev')

db ={}
db['bob'] = bob
db['sue'] = sue
db['andy'] = andy

print(db['sue']['name'])
print(db['andy']['pay'])
print(db['bob']['job'])

print(db)
print()
print()

import pprint

pprint.pprint(db)

for key in db: 
   print(key, '=>', db[key]['name'])

for key in db: print(key, '=>',db[key]['pay'])

db['tom'] = dict(name = 'Tom Swallow', age = 47, pay = 38000, job = 'swe')
pprint.pprint(db)