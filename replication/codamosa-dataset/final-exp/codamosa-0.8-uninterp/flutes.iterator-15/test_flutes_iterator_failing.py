# Automatically generated by Pynguin.
import flutes.iterator as module_0

def test_case_0():
    try:
        bool_0 = False
        str_0 = '2^'
        var_0 = module_0.scanr(bool_0, str_0)
    except BaseException:
        pass

def test_case_1():
    try:
        iterable_0 = None
        lazy_list_0 = module_0.LazyList(iterable_0)
    except BaseException:
        pass

def test_case_2():
    try:
        set_0 = set()
        lazy_list_0 = module_0.LazyList(set_0)
        var_0 = lazy_list_0.__len__()
    except BaseException:
        pass

def test_case_3():
    try:
        range_0 = module_0.Range()
    except BaseException:
        pass

def test_case_4():
    try:
        int_0 = 3
        tuple_0 = ()
        list_0 = [int_0]
        range_0 = module_0.Range(*list_0)
        var_0 = range_0.__getitem__(tuple_0)
    except BaseException:
        pass

def test_case_5():
    try:
        int_0 = 3
        list_0 = [int_0, int_0, int_0]
        range_0 = module_0.Range(*list_0)
        int_1 = range_0.__next__()
    except BaseException:
        pass

def test_case_6():
    try:
        float_0 = 1844.81
        int_0 = 857
        list_0 = [float_0]
        range_0 = module_0.Range(*list_0)
        var_0 = range_0.__getitem__(int_0)
        bytes_0 = None
        list_1 = [bytes_0]
        lazy_list_0 = module_0.LazyList(list_1)
        int_1 = range_0.__len__()
        lazy_list_1 = module_0.LazyList(lazy_list_0)
        iterable_0 = None
        lazy_list_2 = module_0.LazyList(iterable_0)
    except BaseException:
        pass

def test_case_7():
    try:
        int_0 = -425
        iterable_0 = None
        iterator_0 = module_0.drop(int_0, iterable_0)
        int_1 = -3962
        str_0 = 'x/d2"'
        str_1 = '$)?\rT'
        map_list_0 = module_0.MapList(str_0, str_1)
        var_0 = map_list_0.__getitem__(int_1)
    except BaseException:
        pass

def test_case_8():
    try:
        int_0 = 3
        str_0 = 'A3g8o'
        str_1 = '*7 .'
        map_list_0 = module_0.MapList(str_0, str_1)
        iterator_0 = map_list_0.__iter__()
        tuple_0 = ()
        list_0 = [int_0]
        range_0 = module_0.Range(*list_0)
        var_0 = range_0.__getitem__(tuple_0)
    except BaseException:
        pass

def test_case_9():
    try:
        int_0 = 3
        str_0 = '{`_seM'
        dict_0 = {str_0: int_0, str_0: int_0, str_0: str_0, str_0: str_0}
        lazy_list_0 = module_0.LazyList(dict_0)
        map_list_0 = module_0.MapList(int_0, lazy_list_0)
        int_1 = map_list_0.__len__()
    except BaseException:
        pass

def test_case_10():
    try:
        set_0 = None
        str_0 = 'fzHGE^\\2\\<8Si\\F'
        lazy_list_0 = module_0.LazyList(str_0)
        var_0 = lazy_list_0.__getitem__(set_0)
    except BaseException:
        pass

def test_case_11():
    try:
        int_0 = 1
        iterator_0 = module_0.drop(int_0, int_0)
        str_0 = ')%!'
        dict_0 = {iterator_0: int_0, iterator_0: iterator_0}
        lazy_list_0 = module_0.LazyList(dict_0)
        var_0 = lazy_list_0.__getitem__(str_0)
    except BaseException:
        pass

def test_case_12():
    try:
        str_0 = '#KeeSmiWu@Yt)oUTg2'
        list_0 = [str_0, str_0, str_0, str_0]
        range_0 = module_0.Range(*list_0)
    except BaseException:
        pass

def test_case_13():
    try:
        str_0 = "Z9''P?a*Ox\x0bkjPn"
        list_0 = [str_0, str_0]
        iterable_0 = None
        str_1 = "\x0b'\nzVh,(/xl,A.fQI\x0c"
        dict_0 = {str_1: list_0, str_1: str_0}
        iterator_0 = module_0.split_by(iterable_0, criterion=dict_0)
        bytes_0 = b'\x88\xd4\x7f\xc9\x8f'
        var_0 = module_0.scanr(dict_0, bytes_0, *list_0)
    except BaseException:
        pass

def test_case_14():
    try:
        float_0 = 1844.81
        bytes_0 = None
        list_0 = [bytes_0]
        lazy_list_0 = module_0.LazyList(list_0)
        lazy_list_1 = module_0.LazyList(lazy_list_0)
        var_0 = lazy_list_1.__getitem__(float_0)
    except BaseException:
        pass

def test_case_15():
    try:
        float_0 = -2066.759925
        list_0 = [float_0, float_0]
        lazy_list_0 = module_0.LazyList(list_0)
        lazy_list_1 = module_0.LazyList(lazy_list_0)
        var_0 = lazy_list_1.__getitem__(float_0)
    except BaseException:
        pass

def test_case_16():
    try:
        int_0 = -3388
        str_0 = '|kT\r<L63^>bO&XPm'
        str_1 = '|2oVlhI|Z=H0?)NnR{6'
        str_2 = 'GWN'
        dict_0 = {str_0: str_0, str_1: str_1, str_2: str_1}
        iterator_0 = module_0.chunk(int_0, dict_0)
        lazy_list_0 = module_0.LazyList(iterator_0)
        bool_0 = False
        var_0 = lazy_list_0.__getitem__(bool_0)
    except BaseException:
        pass

def test_case_17():
    try:
        int_0 = 10
        var_0 = range(int_0)
        int_1 = 3
        int_2 = 0
        var_1 = lambda x: x % int_1 == int_2
        iterator_0 = module_0.split_by(var_0, criterion=var_1)
        var_2 = list(iterator_0)
    except BaseException:
        pass

def test_case_18():
    try:
        int_0 = 1
        iterator_0 = module_0.drop(int_0, int_0)
        var_0 = list(iterator_0)
    except BaseException:
        pass

def test_case_19():
    try:
        int_0 = 1793
        bytes_0 = b'%g\x91/\xc0#\x04'
        str_0 = '|2oVlhI|Z=H0?)NnR{6'
        dict_0 = {str_0: str_0, str_0: str_0, str_0: str_0}
        iterator_0 = module_0.chunk(int_0, dict_0)
        lazy_list_0 = module_0.LazyList(iterator_0)
        var_0 = lazy_list_0.__iter__()
        bool_0 = False
        str_1 = '(OIFPz5afLSchz\r^Xb'
        iterator_1 = module_0.split_by(bytes_0, bool_0, separator=str_1)
        str_2 = ''
        iterator_2 = module_0.drop(int_0, str_2)
        lazy_list_1 = module_0.LazyList(iterator_2)
        var_1 = lazy_list_1.__iter__()
        tuple_0 = None
        var_2 = lazy_list_1.__getitem__(tuple_0)
    except BaseException:
        pass

def test_case_20():
    try:
        int_0 = 1793
        float_0 = 0.1
        str_0 = '|kT\r<L63^>bO&XPm'
        str_1 = '|2oVlhI|Z=H0?)NnR{6'
        dict_0 = {str_0: str_0, str_1: str_1, str_1: str_1}
        iterator_0 = module_0.chunk(int_0, dict_0)
        lazy_list_0 = module_0.LazyList(iterator_0)
        var_0 = lazy_list_0.__iter__()
        bool_0 = False
        lazy_list_1 = None
        iterator_1 = module_0.split_by(bool_0, criterion=lazy_list_1)
        lazy_list_2 = module_0.LazyList(iterator_1)
        var_1 = lazy_list_2.__iter__()
        var_2 = lazy_list_2.__getitem__(float_0)
    except BaseException:
        pass

def test_case_21():
    try:
        int_0 = 5
        var_0 = range(int_0)
        iterator_0 = module_0.take(int_0, var_0)
        var_1 = list(iterator_0)
        var_2 = range(int_0)
        var_3 = list(var_2)
        int_1 = 3
        var_4 = range(int_1)
        iterator_1 = module_0.take(int_0, var_4)
        var_5 = list(iterator_1)
        var_6 = range(int_1)
        int_2 = -5
        var_7 = range(int_1)
        iterator_2 = module_0.take(int_2, var_7)
        var_8 = list(iterator_2)
    except BaseException:
        pass

def test_case_22():
    try:
        float_0 = 1852.7239247963364
        int_0 = 922
        list_0 = [float_0]
        range_0 = module_0.Range(*list_0)
        var_0 = range_0.__getitem__(int_0)
        list_1 = []
        int_1 = range_0.__next__()
        lazy_list_0 = module_0.LazyList(list_1)
        lazy_list_1 = module_0.LazyList(lazy_list_0)
        var_1 = lazy_list_1.__getitem__(float_0)
    except BaseException:
        pass

def test_case_23():
    try:
        int_0 = 5
        int_1 = 114
        var_0 = range(int_1)
        iterator_0 = module_0.take(int_0, var_0)
        var_1 = list(iterator_0)
        int_2 = 10
        int_3 = 1
        list_0 = [int_2, int_3, int_2]
        str_0 = 'wxfn!5:N].<3h'
        list_1 = [int_1, var_0, str_0]
        iterator_1 = module_0.drop_until(list_0, list_1)
        iterator_2 = module_0.take(int_2, int_3)
        var_2 = list(iterator_2)
    except BaseException:
        pass

def test_case_24():
    try:
        str_0 = '(A.;1{b_t;-ov~~d'
        str_1 = 'P}J'
        dict_0 = {str_0: str_0, str_1: str_0, str_0: str_0}
        list_0 = None
        map_list_0 = module_0.MapList(dict_0, list_0)
        dict_1 = {str_0: str_0, str_0: str_0, str_0: str_0, str_0: str_0}
        bytes_0 = b'\xd11\xa1\xf0\xbaD\xb5'
        list_1 = [dict_1]
        var_0 = module_0.scanr(dict_1, bytes_0, *list_1)
    except BaseException:
        pass

def test_case_25():
    try:
        int_0 = -16
        int_1 = None
        iterator_0 = module_0.drop(int_0, int_1)
        var_0 = list(iterator_0)
    except BaseException:
        pass

def test_case_26():
    try:
        int_0 = 10
        var_0 = range(int_0)
        iterator_0 = module_0.drop_until(int_0, var_0)
        var_1 = list(iterator_0)
    except BaseException:
        pass

def test_case_27():
    try:
        int_0 = 10
        var_0 = range(int_0)
        lazy_list_0 = module_0.LazyList(var_0)
        var_1 = list(lazy_list_0)
        var_2 = lazy_list_0.__len__()
        int_1 = 3
        var_3 = range(int_1)
        var_4 = LazyList(var_3)[int_1:]
    except BaseException:
        pass

def test_case_28():
    try:
        int_0 = 10
        var_0 = range(int_0)
        lazy_list_0 = module_0.LazyList(var_0)
        var_1 = list(lazy_list_0)
        int_1 = 3
        var_2 = lazy_list_0.__len__()
        var_3 = range(int_1)
        lazy_list_1 = module_0.LazyList(lazy_list_0)
        var_4 = LazyList(var_3)[int_1:]
    except BaseException:
        pass