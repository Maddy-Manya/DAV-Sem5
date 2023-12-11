dict_height = {'Boys': [72, 68, 70, 69, 74], 'Girls': [63, 65, 69, 62, 61]}
l = []
dict_boys = dict_height['Boys']
dict_girls = dict_height['Girls']

for i in range(len(dict_boys)):
    x = {'Boys': dict_boys[i], 'Girls': dict_girls[i]}
    l.append(x)

print(l)
