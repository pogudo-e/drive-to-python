from pprint import pprint

names = ['Максим', 'Ибрагим', 'Ярослав', 'Мирослав', 'Себастиан']
salaries = [50000, 547547, 24234, 789789, 35000]
bonus = ['10.5%', '11.5%', '15.3%', '11%', '10.8%']

premium = {names[i]: format(salaries[i] * float(bonus[i][:-1]) / 100, '.2f') for i in
           range(len(names))}

pprint(premium)
