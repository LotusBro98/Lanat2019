projects = [{'name': 'Umniy dom', 'presentation':7 , 'concept':9 , 'perfomance':8},
            {'name':'Onlain Kinoteatr','presentation':8, 'concept': 9 , 'perfomance':3}]
for proj in projects:
    proj['avg'] = (proj['presentation']+proj['concept']+proj['perfomance']) / 3
projects = sorted(projects, key=lambda item: item['avg'], reverse=True)
for proj in projects:
    print(proj['name'],':',proj['avg'])
print('Luchshiy proekt:', projects[0]['name'])
