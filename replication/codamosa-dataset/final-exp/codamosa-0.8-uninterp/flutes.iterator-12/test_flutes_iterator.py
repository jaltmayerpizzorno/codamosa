# Automatically generated by Pynguin.
import flutes.iterator as module_0

def test_case_0():
    pass

def test_case_1():
    bytes_0 = b'\x05\xe9'
    lazy_list_0 = module_0.LazyList(bytes_0)
    var_0 = list(lazy_list_0)

def test_case_2():
    int_0 = -949
    list_0 = [int_0, int_0, int_0]
    iterator_0 = module_0.chunk(int_0, list_0)
    str_0 = '.'
    bool_0 = True
    range_0 = module_0.Range(*list_0)
    iterator_1 = module_0.split_by(str_0, bool_0, separator=str_0)
    var_0 = list(iterator_1)
    var_1 = list(iterator_1)

def test_case_3():
    int_0 = -1706
    list_0 = [int_0]
    range_0 = module_0.Range(*list_0)
    var_0 = range_0.__getitem__(int_0)

def test_case_4():
    int_0 = 1499
    str_0 = 'E_'
    map_list_0 = module_0.MapList(int_0, str_0)
    iterator_0 = map_list_0.__iter__()
    list_0 = []
    iterator_1 = module_0.split_by(iterator_0, separator=list_0)
    bytes_0 = b'\n_'
    iterator_2 = module_0.split_by(iterator_1, criterion=bytes_0)

def test_case_5():
    bool_0 = True
    str_0 = 'KU$wk%^mM<'
    lazy_list_0 = module_0.LazyList(str_0)
    var_0 = lazy_list_0.__getitem__(bool_0)

def test_case_6():
    int_0 = 4
    list_0 = [int_0]
    range_0 = module_0.Range(*list_0)
    var_0 = range_0.__getitem__(int_0)
    int_1 = range_0.__next__()

def test_case_7():
    int_0 = -949
    list_0 = [int_0, int_0, int_0]
    iterator_0 = module_0.chunk(int_0, list_0)
    str_0 = '.'
    bool_0 = True
    range_0 = module_0.Range(*list_0)
    int_1 = range_0.__len__()
    iterator_1 = module_0.split_by(str_0, bool_0, separator=str_0)
    var_0 = list(iterator_1)
    var_1 = list(iterator_1)

def test_case_8():
    bytes_0 = b'\xd9\x9f\x01'
    lazy_list_0 = module_0.LazyList(bytes_0)
    var_0 = lazy_list_0.__iter__()
    str_0 = ''
    bool_0 = True
    var_1 = lazy_list_0.__getitem__(bool_0)
    bool_1 = True
    iterator_0 = module_0.split_by(str_0, bool_1, separator=str_0)
    var_2 = list(lazy_list_0)
    var_3 = list(iterator_0)

def test_case_9():
    int_0 = 0
    iterable_0 = None
    iterator_0 = module_0.take(int_0, iterable_0)
    int_1 = 1
    var_0 = range(int_0)
    iterator_1 = module_0.take(int_0, var_0)
    var_1 = list(iterator_1)
    var_2 = range(int_0)
    iterator_2 = module_0.take(int_0, var_2)
    var_3 = list(iterator_2)
    var_4 = range(int_0)
    iterator_3 = module_0.take(int_1, var_4)
    var_5 = list(iterator_3)
    var_6 = range(int_1)
    iterator_4 = module_0.take(int_1, var_6)
    list_0 = [var_4]
    list_1 = []
    var_7 = module_0.scanr(list_0, list_1, *list_0)
    var_8 = list(iterator_4)
    int_2 = 2
    var_9 = range(int_1)
    iterator_5 = module_0.take(int_2, var_9)
    var_10 = list(iterator_5)
    var_11 = range(int_2)
    iterator_6 = module_0.take(int_2, var_11)
    var_12 = list(iterator_6)
    int_3 = 3
    var_13 = range(int_2)
    iterator_7 = module_0.take(int_3, var_13)
    var_14 = list(iterator_7)

def test_case_10():
    var_0 = lambda s, x: s + x
    str_0 = 'a'
    str_1 = 'b'
    str_2 = 'c'
    str_3 = 'd'
    str_4 = [str_0, str_1, str_2, str_3]
    var_1 = module_0.scanl(var_0, str_4)
    var_2 = list(var_1)
    var_3 = lambda s, x: s + x

def test_case_11():
    int_0 = 4
    list_0 = [int_0]
    range_0 = module_0.Range(*list_0)
    var_0 = range_0.__getitem__(int_0)

def test_case_12():
    int_0 = 32
    var_0 = range(int_0)
    iterator_0 = module_0.drop(int_0, var_0)
    var_1 = list(var_0)
    int_1 = 3
    var_2 = range(int_0)
    var_3 = range(int_0)
    iterator_1 = module_0.drop(int_1, var_3)
    var_4 = list(iterator_1)
    var_5 = range(int_0)
    iterator_2 = module_0.drop(int_0, iterator_0)
    var_6 = list(iterator_2)

def test_case_13():
    str_0 = '.'
    bool_0 = True
    iterator_0 = module_0.split_by(str_0, bool_0, separator=str_0)
    var_0 = list(iterator_0)

def test_case_14():
    str_0 = ' Split by: '
    bool_0 = True
    iterator_0 = module_0.split_by(str_0, bool_0, separator=str_0)
    var_0 = list(iterator_0)
    var_1 = list(iterator_0)

def test_case_15():
    int_0 = 0
    var_0 = range(int_0)
    iterator_0 = module_0.chunk(int_0, var_0)
    var_1 = list(var_0)
    int_1 = 1
    var_2 = range(int_1)
    iterator_1 = module_0.chunk(int_1, var_2)
    var_3 = list(iterator_1)
    int_2 = 2
    var_4 = range(int_2)
    iterator_2 = module_0.chunk(int_2, var_4)
    var_5 = list(iterator_2)
    int_3 = 3
    var_6 = range(int_3)
    iterator_3 = module_0.chunk(int_3, var_6)
    var_7 = list(iterator_3)
    int_4 = 4
    var_8 = range(int_4)
    iterator_4 = module_0.chunk(int_4, var_8)
    var_9 = list(iterator_4)
    int_5 = 5
    var_10 = range(int_5)
    iterator_5 = module_0.chunk(int_5, var_10)
    var_11 = list(iterator_5)
    var_12 = range(int_2)
    iterator_6 = module_0.chunk(int_1, var_12)
    var_13 = list(iterator_6)
    var_14 = range(int_3)
    iterator_7 = module_0.chunk(int_2, var_14)
    var_15 = list(iterator_7)
    var_16 = range(int_4)
    iterator_8 = module_0.chunk(int_3, var_16)
    var_17 = list(iterator_8)

def test_case_16():
    str_0 = 'd'
    bool_0 = False
    iterator_0 = module_0.split_by(str_0, bool_0, separator=str_0)
    var_0 = list(iterator_0)

def test_case_17():
    bytes_0 = b'\x05\xe9'
    lazy_list_0 = module_0.LazyList(bytes_0)
    var_0 = lazy_list_0.__iter__()
    var_1 = list(lazy_list_0)
    var_2 = lazy_list_0.__len__()

def test_case_18():
    bytes_0 = b''
    lazy_list_0 = module_0.LazyList(bytes_0)
    var_0 = lazy_list_0.__iter__()
    str_0 = '^~Bgve'
    bool_0 = False
    iterator_0 = module_0.split_by(str_0, bool_0, separator=str_0)
    var_1 = list(lazy_list_0)
    var_2 = list(lazy_list_0)

def test_case_19():
    bytes_0 = b''
    lazy_list_0 = module_0.LazyList(bytes_0)
    var_0 = lazy_list_0.__iter__()
    str_0 = '.'
    bool_0 = True
    iterator_0 = module_0.split_by(str_0, bool_0, separator=str_0)
    var_1 = list(lazy_list_0)
    var_2 = list(var_0)

def test_case_20():
    int_0 = 5
    var_0 = range(int_0)
    iterator_0 = module_0.take(int_0, var_0)
    var_1 = list(iterator_0)

def test_case_21():
    int_0 = 0
    int_1 = 1
    var_0 = range(int_1)
    iterator_0 = module_0.take(int_0, var_0)
    var_1 = list(iterator_0)
    var_2 = range(int_0)
    iterator_1 = module_0.take(int_0, var_2)
    var_3 = list(iterator_1)
    var_4 = range(int_0)
    iterator_2 = module_0.take(int_1, var_4)
    var_5 = list(iterator_2)
    var_6 = range(int_1)
    iterator_3 = module_0.take(int_1, var_6)
    var_7 = list(iterator_3)
    int_2 = 2
    var_8 = range(int_1)
    var_9 = list(iterator_0)
    var_10 = list(iterator_1)
    var_11 = range(int_2)
    var_12 = list(iterator_3)

def test_case_22():
    int_0 = 10000
    var_0 = range(int_0)
    lazy_list_0 = module_0.LazyList(var_0)
    int_1 = 1
    var_1 = lazy_list_0[int_1]
    int_2 = -1
    var_2 = lazy_list_0[int_2]
    int_3 = 10
    var_3 = lazy_list_0[int_1:int_3]
    int_4 = 0
    var_4 = var_3[int_4]
    int_5 = -1
    var_5 = var_3[int_5]
    var_6 = lazy_list_0[int_4]