# dictionaty is a collection of hey-value pairs
{'Name': 'John',
 'Age': 34,
 "Height": 175.5}

# whether dictionary is ordered or not is irrelevant because items are retrived not wia index but via key
student = {'Name': 'John',
            'Age': 34,
            "Height": 175.5}
student[0] #KeyError: 0
student['Name'] #John
student['Weight'] #KeyError: 'Weight'

#integer can be used as idctioinary keys but it doens't mean that they can be trated as indexes
digist = {0: 'zerp',
          1: 'one'}
digits[0] #'zero'

#dictionary is mutable - it can be changes
student['Email'] = 'john@gmail.com'
student['Age'] = 26
del student['Height']

#meging two dictionaries
digits.update({2: 'two', 3: 'three'})

#dictionary keys can't be mutable
cars = {['Seat', 'Ibiza']: 'KR1J465',
         ['Ford', 'Focus']: 'KRA5499M'} # TypeError: unhashable type: 'list'

cars = {('Seat', 'Ibiza'): 'KR1J465',
        ('Ford', 'Focus'): 'KRA5499M'}

#checking if dicrionary contains (or not) given hey
'Name' in student # True
'Address' not in student # True

#checking dictionary's lenght
len(student)

#other way of getting vaue from dictionary
student.get('Name') # == Student['Name']
student.get('Address', 0) # nie rzuci wyjątkiem, tylko da 0

#getting all kays, values and key-value pairs from dictionaty
student.keys() #all keys - canbe write to list
list(student.keys())

student.values()  #all values - can write to list
list(student.values())

student.items() #all items - dict_items could be write to list

student = {'Name': 'John', 'Age': 34, 'Email': 'john@wp.pl', 0: 'zero', 1: 'one', 2: 'two'}

for key in student:
    print('Klucz: ', key)

for value in student.values():
    print('Klucz: ', value)

for key, value in student.items():
    print('Klucz: ', key, ' wartosc: ', value)