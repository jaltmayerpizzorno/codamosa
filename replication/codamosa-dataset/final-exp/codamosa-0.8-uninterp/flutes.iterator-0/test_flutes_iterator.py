# Automatically generated by Pynguin.
import flutes.iterator as module_0

def test_case_0():
    str_0 = '\r&SaTliB,+pMFX<K[ns'
    lazy_list_0 = module_0.LazyList(str_0)

def test_case_1():
    bytes_0 = b'\x7f"<\xbb\xa4\xb4y\xf1\xae'
    lazy_list_0 = module_0.LazyList(bytes_0)
    var_0 = list(lazy_list_0)

def test_case_2():
    bool_0 = False
    int_0 = -1954
    list_0 = [int_0, int_0, int_0]
    range_0 = module_0.Range(*list_0)
    var_0 = range_0.__getitem__(bool_0)

def test_case_3():
    iterable_0 = None
    float_0 = 0.1
    str_0 = 'D5'
    tuple_0 = None
    iterator_0 = None
    tuple_1 = (str_0, tuple_0, iterator_0)
    lazy_list_0 = module_0.LazyList(tuple_1)
    map_list_0 = module_0.MapList(float_0, lazy_list_0)
    iterator_1 = map_list_0.__iter__()
    iterator_2 = module_0.split_by(iterable_0, separator=iterator_1)

def test_case_4():
    dict_0 = None
    list_0 = [dict_0, dict_0, dict_0, dict_0]
    lazy_list_0 = module_0.LazyList(list_0)
    var_0 = lazy_list_0.__iter__()

def test_case_5():
    int_0 = 1000
    var_0 = range(int_0)
    lazy_list_0 = module_0.LazyList(var_0)
    int_1 = 3
    int_2 = 9
    var_1 = lazy_list_0[int_1:int_2]

def test_case_6():
    var_0 = lambda x: x * x
    int_0 = 1
    int_1 = 2
    int_2 = 3
    int_3 = 4
    int_4 = 5
    int_5 = [int_0, int_1, int_2, int_3, int_4]
    map_list_0 = module_0.MapList(var_0, int_5)
    var_1 = map_list_0[int_1]
    var_2 = map_list_0[int_2]
    var_3 = map_list_0[int_1:int_3]
    var_4 = print(var_1, var_2, var_3)

def test_case_7():
    str_0 = ' Split by: '
    bool_0 = True
    var_0 = lambda x: x.isspace()
    iterator_0 = module_0.split_by(str_0, bool_0, criterion=var_0)
    var_1 = list(iterator_0)

def test_case_8():
    int_0 = 0
    var_0 = lambda x: x % int_0 == int_0
    str_0 = ' Split by: '
    bool_0 = False
    var_1 = lambda x: x.isspace()
    iterator_0 = module_0.split_by(str_0, bool_0, criterion=var_1)
    var_2 = list(iterator_0)

def test_case_9():
    bytes_0 = b'\x7f"<\xbb\xa4\xb4y\xf1\xae'
    lazy_list_0 = module_0.LazyList(bytes_0)
    var_0 = lazy_list_0.__iter__()
    var_1 = list(var_0)

def test_case_10():
    int_0 = -1007
    var_0 = range(int_0)
    iterator_0 = module_0.drop_until(int_0, var_0)
    bytes_0 = b'\x88\xb4\x1b0hp\xd8\x98\x9c#\x92\x07\x99\xdb\xb0'
    lazy_list_0 = module_0.LazyList(bytes_0)
    var_1 = lazy_list_0.__iter__()
    var_2 = list(var_1)
    var_3 = list(var_0)
    str_0 = 'K'
    var_4 = list(iterator_0)
    var_5 = lambda x: x == var_3
    var_6 = lazy_list_0.__len__()
    iterator_1 = module_0.drop_until(var_5, str_0)
    var_7 = list(var_1)

def test_case_11():
    int_0 = 2
    var_0 = range(int_0)
    iterator_0 = module_0.drop(int_0, var_0)
    var_1 = list(iterator_0)

def test_case_12():
    int_0 = 5
    int_1 = 10
    var_0 = range(int_0)
    iterator_0 = module_0.drop(int_0, var_0)
    var_1 = list(iterator_0)
    int_2 = 27
    var_2 = range(int_1)
    iterator_1 = module_0.drop(int_2, var_2)
    var_3 = list(iterator_1)

def test_case_13():
    int_0 = -105
    int_1 = None
    iterable_0 = None
    iterator_0 = module_0.drop(int_1, iterable_0)
    var_0 = lambda x: x % int_0 == int_0
    str_0 = '(]cs'
    bool_0 = False
    var_1 = lambda x: x.isspace()
    iterator_1 = module_0.split_by(str_0, bool_0, criterion=var_1)
    var_2 = list(iterator_1)

def test_case_14():
    var_0 = lambda s, x: x + s
    str_0 = 'a'
    str_1 = 'b'
    str_2 = 'c'
    str_3 = 'd'
    str_4 = [str_0, str_1, str_2, str_3]
    var_1 = module_0.scanl(var_0, str_4)
    var_2 = list(var_1)