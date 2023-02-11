#set is a collection of objects (iterable)
{1, 2, 'a', 'b', True, False}
set([1, 2, 'a', 'b', True, False])

#creating empty set - only one option: set(); {} == dict{}
set()

set('Kotek')
set([1, 2, 34, 'Kotek'])

#set is unordered - order of items is resolved by Python
digits = {3, 2, 1, 0} # {0, 1,  2, 3}
digits[0] #error

#set cannot contain duplicated items
digits = {0, 0, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9} #{0, 1, 2, 3, 4, 5, 6, 7, 8, 9}

#set is a common way to removing duplicates ftrom list
letters = ['a', 'b', 'b', 'c']
letters = list(set(letters))

#set cannot contain mutable items
body = {'head', ['left hand', 'right hand'], 'belly'} #error
body = {'head', ('left hand', 'right hand'), 'belly'} #ok - tuple

#checking if set contains given object
'head' in body
'leg' not in body

#checking set's lenght
len(body)

#operating on set
letters_1 = {'a', 'b', 'c'}
letters_2 = {'b', 'c', 'd', 'e'}

letters_1.union(letters_2) #suma
letters_1.intersection(letters_2) #przeciecie = czesc wspolna
letters_1.difference(letters_2) #roznica 1-2
letters_1.symmetric_difference(letters_2) #roznica symetryczna - odwrotne do czesci wspolnej; ktore elementy nie sa wspolne

#set is mutable
letters_1.update(letters_2) #produkuje nowy zbior, ale działeanie jak suma; kompletnie nowy obiekt
letters_1.add('f')
letters_1.remove('a') #not del[i]


