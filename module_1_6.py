my_dict = {'honda' : 2010, 'nissan' : 2011, 'mazda' : 2012, 'subaru' : 2014, }
print(my_dict)
print(my_dict['honda'])
print(my_dict.get('suzuki', 'Такая марка отсутствует'))
my_dict.update({'suzuki' : 2013,
 'audi' : 2016,})
print(my_dict)
au = my_dict.pop('audi')
print(my_dict)
print(au)




my_set = {'honda', 2010, 'nissan', 2011, 'mazda', 2012, 'subaru', 2014,
 'honda', 2010, 'nissan', 2011, 'mazda', 2012, 'subaru', 2014,
 'honda', 2010, 'nissan', 2011, 'mazda', 2012, 'subaru', 2014,}
print(my_set)
car_ = 'suzuki',2013, 'audi',2016,
my_set.add(car_,)
my_set.discard('honda')
print(my_set)