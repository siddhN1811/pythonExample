#Example: Movie Database
table = {'1975': 'Holy Grail','1979': 'Life of Brian','1983': 'The Meaning of Life'}
table_res={'Holy Grail': '1975','Life of Brian': '1979','The Meaning of Life': '1983'}
name={'fname':'raju','lname':'mane'}
print('table db',table)
print('table_res db',table_res)
year='1975'
print('table[year]',table[year])
keys=name.keys()
for year in table:
    print(year+'\t'+table[year])
print()
for year in table_res:
    print(year+'\t'+table_res[year])


for (title,year) in table_res.items():
    if year=='1975':
        print(title)

