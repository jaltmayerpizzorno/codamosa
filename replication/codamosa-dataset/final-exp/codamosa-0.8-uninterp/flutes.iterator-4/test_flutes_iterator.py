# Automatically generated by Pynguin.
import flutes.iterator as module_0

def test_case_0():
    pass

def test_case_1():
    str_0 = '&CX\nn4\t)#&*+&<\toW'
    lazy_list_0 = module_0.LazyList(str_0)
    var_0 = list(lazy_list_0)

def test_case_2():
    int_0 = 2
    list_0 = [int_0]
    range_0 = module_0.Range(*list_0)
    range_1 = module_0.Range(*list_0)
    int_1 = range_1.__next__()

def test_case_3():
    dict_0 = None
    bytes_0 = b'l\xa3\xb9\x9b\x11\x05\x15\x98\xc5.\xb2'
    map_list_0 = module_0.MapList(dict_0, bytes_0)

def test_case_4():
    str_0 = '+^\x0bVF+jE '
    iterator_0 = None
    dict_0 = {str_0: str_0, iterator_0: str_0, iterator_0: iterator_0}
    iterator_1 = module_0.drop_until(str_0, dict_0)
    int_0 = None
    bool_0 = True
    str_1 = 'Multiprocessing stateless worker pool. See :class:`StatefulPoolType` for a pool with stateful workers.\n\n    .. note::\n        This class is only a stub for type annotation and documentation purposes only, and should not be used directly.\n        Please refer to :meth:`safe_pool` for a user-facing API for constructing pool instances.\n    '
    map_list_0 = module_0.MapList(bool_0, str_1)
    bytes_0 = None
    iterator_2 = map_list_0.__iter__()
    iterator_3 = module_0.take(int_0, bytes_0)

def test_case_5():
    int_0 = 1
    bool_0 = False
    iterator_0 = module_0.drop(int_0, bool_0)
    bool_1 = True
    list_0 = [bool_1, bool_1, bool_1]
    map_list_0 = None
    iterator_1 = module_0.chunk(int_0, map_list_0)
    int_1 = -1567
    float_0 = 1494.41
    iterator_2 = module_0.chunk(int_1, float_0)
    range_0 = module_0.Range(*list_0)
    int_2 = range_0.__len__()

def test_case_6():
    int_0 = 1
    list_0 = [int_0, int_0, int_0]
    range_0 = module_0.Range(*list_0)
    iterator_0 = range_0.__iter__()
    lazy_list_0 = module_0.LazyList(iterator_0)
    var_0 = lazy_list_0.__iter__()
    bool_0 = False
    iterator_1 = module_0.drop(int_0, bool_0)
    bool_1 = True
    list_1 = [bool_1, bool_1, bool_1]
    map_list_0 = None
    iterator_2 = module_0.chunk(int_0, map_list_0)
    int_1 = -1567
    float_0 = 1494.41
    iterator_3 = module_0.chunk(int_1, float_0)
    range_1 = module_0.Range(*list_1)
    int_2 = range_1.__len__()

def test_case_7():
    int_0 = 2
    int_1 = 1
    int_2 = 3
    int_3 = 4
    int_4 = 6
    int_5 = [int_1, int_1, int_0, int_2, int_3, int_0, int_4]
    iterator_0 = module_0.chunk(int_0, int_5)
    var_0 = list(iterator_0)
    int_6 = 7
    int_7 = [int_2, int_1, int_0, int_2, int_3, int_6, int_4, int_6]
    iterator_1 = module_0.chunk(int_2, int_7)

def test_case_8():
    bool_0 = True
    str_0 = 'G'
    iterator_0 = module_0.split_by(str_0, bool_0, separator=str_0)
    var_0 = list(iterator_0)

def test_case_9():
    int_0 = 10
    var_0 = range(int_0)
    lazy_list_0 = module_0.LazyList(var_0)
    int_1 = -1
    int_2 = -5
    int_3 = -1
    var_1 = lazy_list_0[int_1:int_2:int_3]
    var_2 = list(var_1)
    int_4 = -2
    int_5 = -5
    int_6 = -1
    var_3 = lazy_list_0[int_4:int_5:int_6]
    var_4 = list(var_3)

def test_case_10():
    int_0 = 1
    int_1 = 3
    int_2 = [int_0, int_0, int_0, int_1, int_0, int_0]
    str_0 = '/2S\tDXEDUa!kS&-Q*J'
    dict_0 = {str_0: str_0, str_0: int_0, str_0: int_2, str_0: int_1}
    lazy_list_0 = module_0.LazyList(dict_0)
    int_3 = 6
    int_4 = [int_0, int_0, int_2, int_1, int_2, int_2, int_3]
    iterator_0 = module_0.chunk(int_0, int_4)
    var_0 = list(iterator_0)
    int_5 = [int_3, int_0, int_3, int_1, int_3, int_3, int_3]
    var_1 = lazy_list_0.__iter__()
    iterator_1 = module_0.chunk(int_1, int_5)
    var_2 = list(iterator_1)
    iterator_2 = module_0.chunk(int_1, int_4)
    var_3 = list(iterator_2)

def test_case_11():
    str_0 = ' Split by: '
    bool_0 = True
    str_1 = '.'
    iterator_0 = module_0.split_by(str_0, bool_0, separator=str_1)
    var_0 = list(iterator_0)

def test_case_12():
    int_0 = -8
    str_0 = '&C>\nn4)#&*+&<)\toW'
    lazy_list_0 = module_0.LazyList(str_0)
    var_0 = lambda x: x % int_0 == int_0
    var_1 = list(lazy_list_0)
    var_2 = lazy_list_0.__len__()

def test_case_13():
    str_0 = '&C>\nn4)#&*\n&<)\toW'
    lazy_list_0 = module_0.LazyList(str_0)
    var_0 = list(lazy_list_0)
    bool_0 = True
    var_1 = lazy_list_0.__iter__()
    str_1 = '.'
    iterator_0 = module_0.split_by(str_0, bool_0, separator=str_1)
    var_2 = list(iterator_0)

def test_case_14():
    bool_0 = False
    str_0 = 'G'
    iterator_0 = module_0.split_by(str_0, bool_0, separator=str_0)
    var_0 = list(iterator_0)

def test_case_15():
    iterable_0 = None
    int_0 = 3
    str_0 = '&C>\nn4)#&*+&<)\toW'
    lazy_list_0 = module_0.LazyList(str_0)
    iterator_0 = module_0.split_by(iterable_0)
    var_0 = lazy_list_0.__iter__()
    var_1 = lambda x: x % int_0 == int_0
    var_2 = list(lazy_list_0)
    dict_0 = {int_0: int_0}
    var_3 = module_0.scanr(iterator_0, dict_0)

def test_case_16():
    iterable_0 = None
    iterator_0 = module_0.split_by(iterable_0)
    int_0 = -10
    str_0 = '&C>\nn4)#&*+&<)\toW'
    lazy_list_0 = module_0.LazyList(str_0)
    iterator_1 = module_0.split_by(iterable_0)
    var_0 = lazy_list_0.__iter__()
    var_1 = lambda x: x % int_0 == int_0
    var_2 = list(var_0)
    var_3 = lazy_list_0.__iter__()
    bool_0 = True
    str_1 = '.'
    iterator_2 = module_0.split_by(str_1, bool_0, separator=str_1)
    dict_0 = {var_0: int_0}
    var_4 = module_0.scanr(iterator_1, dict_0)
    var_5 = list(iterator_2)