text = 'абв Ура, питон крутой абвязык , очень интересные семинарабвы ДЗ! абв'
lst= ' '.join(list(filter(lambda s:'абв' not in s, text.split())))
print(lst)