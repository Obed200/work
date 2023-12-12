print("______________________1______________________")

ChemicalElement={'H':'Hydrogen','He':'Helium','Li':'Lithium','Be':'Beryllium', 
'B':'Boron','C':'Carbon','N':'Nitrogen','O':'Oxygen','F':'Fluorine','Ne':'Neon'}
ChemicalElement.update({'Na':'sodium','Mg':'magnesium'})
print(ChemicalElement.get("C")) 
print(ChemicalElement.get("H"))
print(ChemicalElement.get("B"))
print(ChemicalElement.get("N"))
print(ChemicalElement.get("Ne"))
print(ChemicalElement)
for keys,values in ChemicalElement.items():
  print(keys,values)
print("______________________2______________________________________")
temperatureCountries = {'Rwanda': 29, 'Nigeria':28 , 'Kenya':
23, 'Egypt':37 ,'Morocco': 41 ,'South Africa': 25, 'Mali': 33, 'Ghana':28,}
print('Nigeria ',temperatureCountries.get('Nigeria'))
print('Egypt ',temperatureCountries.get('Egypt'))
print("South Africa ",temperatureCountries.get('South Africa'))
temperatureCountries.update({'togo':20,'zambia':19,'Morocco':38})
print(temperatureCountries)
#keys=temperatureCountries.keys()
for keys,values in temperatureCountries.items():
    if values>30:
        print(keys,temperatureCountries.get(keys),'it\'s to  hot')
    elif values<25:
        print(keys,temperatureCountries.get(keys,),"it's to cold")
        