# Automatically generated by Pynguin.
import flutes.iterator as module_0

def test_case_0():
    try:
        bool_0 = False
        iterator_0 = None
        var_0 = module_0.scanr(bool_0, iterator_0)
    except BaseException:
        pass

def test_case_1():
    try:
        int_0 = -4
        bool_0 = False
        iterator_0 = module_0.drop(int_0, bool_0)
        lazy_list_0 = module_0.LazyList(iterator_0)
        var_0 = list(lazy_list_0)
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = '\\fNrd\nlp`'
        set_0 = {str_0, str_0}
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
        float_0 = 440.703
        str_0 = 'd{}'
        str_1 = 'M:1?>w$YEk1W_{T1j ]H'
        dict_0 = {str_1: float_0, str_0: float_0, str_1: str_1}
        map_list_0 = module_0.MapList(float_0, dict_0)
        var_0 = map_list_0.__getitem__(dict_0)
    except BaseException:
        pass

def test_case_5():
    try:
        bytes_0 = b'$!\x94\xa9\xb8C\xfd\x06\xa2\xab\xcc\x05f'
        list_0 = [bytes_0, bytes_0, bytes_0]
        str_0 = ''
        int_0 = 645
        str_1 = '[>@{1O_\rc>'
        iterator_0 = module_0.drop(int_0, str_1)
        map_list_0 = module_0.MapList(str_0, list_0)
        int_1 = map_list_0.__len__()
        iterator_1 = module_0.split_by(list_0)
        iterator_2 = map_list_0.__iter__()
        lazy_list_0 = module_0.LazyList(iterator_2)
        var_0 = lazy_list_0.__iter__()
        range_0 = module_0.Range()
    except BaseException:
        pass

def test_case_6():
    try:
        bytes_0 = b'\x85&\x1f\xde\xd7\xef.E\xc3\xfd\xf2\xb1\x88\xb0\xbf'
        list_0 = [bytes_0, bytes_0, bytes_0, bytes_0]
        range_0 = module_0.Range(*list_0)
    except BaseException:
        pass

def test_case_7():
    try:
        bool_0 = False
        int_0 = 1837
        int_1 = 905
        list_0 = [int_1, bool_0]
        range_0 = module_0.Range(*list_0)
        map_list_0 = module_0.MapList(bool_0, int_0)
        iterator_0 = map_list_0.__iter__()
    except BaseException:
        pass

def test_case_8():
    try:
        range_0 = None
        str_0 = 'x\n#La|j%rW,\t:|5Q<Ct/'
        list_0 = [range_0]
        bool_0 = None
        iterator_0 = module_0.split_by(list_0, bool_0)
        bytes_0 = b'\x00D\x89ox\x93\x8f4Z\xac\xf6j\xdd\x1c'
        map_list_0 = module_0.MapList(iterator_0, bytes_0)
        list_1 = []
        var_0 = module_0.scanr(str_0, map_list_0, *list_1)
    except BaseException:
        pass

def test_case_9():
    try:
        int_0 = 261
        bytes_0 = None
        iterator_0 = module_0.take(int_0, bytes_0)
        list_0 = [iterator_0]
        str_0 = '  F`M,/j'
        str_1 = None
        str_2 = 'Linux'
        dict_0 = {str_0: iterator_0, str_1: iterator_0, str_2: int_0, str_1: int_0}
        var_0 = module_0.scanr(list_0, dict_0)
    except BaseException:
        pass

def test_case_10():
    try:
        bool_0 = False
        int_0 = 905
        list_0 = [int_0, bool_0]
        float_0 = 61.741
        range_0 = module_0.Range(*list_0)
        iterator_0 = module_0.split_by(float_0, separator=range_0)
        bool_1 = None
        iterator_1 = module_0.split_by(iterator_0, bool_1)
        int_1 = range_0.__next__()
    except BaseException:
        pass

def test_case_11():
    try:
        str_0 = 'J}?b<k,#<\x0b;'
        lazy_list_0 = module_0.LazyList(str_0)
        bool_0 = True
        var_0 = lazy_list_0.__getitem__(bool_0)
        float_0 = -2634.47257
        map_list_0 = module_0.MapList(bool_0, float_0)
        iterator_0 = module_0.split_by(map_list_0)
        list_0 = [iterator_0, map_list_0, lazy_list_0]
        range_0 = module_0.Range(*list_0)
    except BaseException:
        pass

def test_case_12():
    try:
        int_0 = 9
        list_0 = [int_0]
        range_0 = module_0.Range(*list_0)
        iterator_0 = range_0.__iter__()
        str_0 = '{v]=&-MP\x0c>._kwD '
        dict_0 = {str_0: int_0, str_0: str_0, str_0: str_0}
        bytes_0 = b'9F?M6\xbf\xb4\x82\x07%\x1c5[\xfa\xdf\x0b'
        list_1 = [int_0, int_0, int_0, int_0]
        iterator_1 = module_0.split_by(list_1, criterion=bytes_0)
        var_0 = range(int_0)
        bool_0 = True
        iterator_2 = module_0.drop(int_0, bool_0)
        lazy_list_0 = module_0.LazyList(iterator_2)
        var_1 = lazy_list_0.__iter__()
        iterator_3 = module_0.drop_until(dict_0, var_0)
        var_2 = list(iterator_3)
    except BaseException:
        pass

def test_case_13():
    try:
        bytes_0 = b'H\xe5\xf9\x8c\x18\xbd\xbc}\xba\xda\xdb*'
        str_0 = "/\x0bUXKaIiJ%RX;x3:'|E"
        list_0 = [bytes_0, bytes_0, str_0]
        var_0 = module_0.scanr(bytes_0, str_0, *list_0)
    except BaseException:
        pass

def test_case_14():
    try:
        int_0 = -9
        var_0 = lambda x: x > int_0
        bool_0 = True
        iterator_0 = module_0.drop(int_0, bool_0)
        lazy_list_0 = module_0.LazyList(iterator_0)
        var_1 = lazy_list_0.__iter__()
        float_0 = -3099.716988934681
        var_2 = lazy_list_0.__getitem__(float_0)
    except BaseException:
        pass

def test_case_15():
    try:
        bool_0 = None
        str_0 = '~['
        lazy_list_0 = module_0.LazyList(str_0)
        var_0 = lazy_list_0.__getitem__(bool_0)
    except BaseException:
        pass

def test_case_16():
    try:
        str_0 = '@++"eqY)J"S3\\KF'
        dict_0 = {str_0: str_0}
        list_0 = [dict_0]
        var_0 = module_0.scanr(dict_0, dict_0, *list_0)
    except BaseException:
        pass

def test_case_17():
    try:
        int_0 = 5
        iterable_0 = None
        iterator_0 = module_0.take(int_0, iterable_0)
        lazy_list_0 = module_0.LazyList(iterator_0)
        var_0 = lazy_list_0.__iter__()
        bool_0 = False
        var_1 = lazy_list_0.__getitem__(bool_0)
    except BaseException:
        pass

def test_case_18():
    try:
        int_0 = 9
        bool_0 = True
        iterator_0 = module_0.drop(int_0, bool_0)
        lazy_list_0 = module_0.LazyList(iterator_0)
        var_0 = lazy_list_0.__iter__()
        var_1 = list(lazy_list_0)
    except BaseException:
        pass

def test_case_19():
    try:
        str_0 = '\r)m\x0c7$u\x0b'
        int_0 = -11
        dict_0 = {str_0: str_0}
        map_list_0 = module_0.MapList(int_0, dict_0)
        iterator_0 = map_list_0.__iter__()
        list_0 = [str_0, int_0, str_0]
        iterator_1 = module_0.chunk(int_0, list_0)
        iterable_0 = None
        iterator_2 = module_0.drop(int_0, iterable_0)
        iterator_3 = module_0.take(int_0, iterable_0)
        lazy_list_0 = module_0.LazyList(iterator_3)
        var_0 = lazy_list_0.__iter__()
        bool_0 = False
        var_1 = lazy_list_0.__getitem__(bool_0)
    except BaseException:
        pass

def test_case_20():
    try:
        int_0 = 5
        var_0 = range(int_0)
        iterator_0 = module_0.drop_until(int_0, var_0)
        var_1 = list(iterator_0)
    except BaseException:
        pass

def test_case_21():
    try:
        int_0 = 1
        int_1 = 2
        int_2 = 3
        int_3 = 4
        int_4 = 5
        int_5 = [int_0, int_1, int_2, int_3, int_4]
        map_list_0 = module_0.MapList(int_5, int_5)
        var_0 = map_list_0[:int_1]
    except BaseException:
        pass

def test_case_22():
    try:
        int_0 = 10
        list_0 = [int_0, int_0, int_0, int_0]
        iterator_0 = module_0.split_by(list_0)
        var_0 = list(iterator_0)
    except BaseException:
        pass

def test_case_23():
    try:
        int_0 = -7
        int_1 = 10
        var_0 = range(int_1)
        int_2 = 7
        var_1 = range(int_2)
        iterator_0 = module_0.chunk(int_0, var_1)
        var_2 = list(iterator_0)
    except BaseException:
        pass

def test_case_24():
    try:
        str_0 = ' Split by: '
        bool_0 = True
        str_1 = ' '
        iterator_0 = module_0.split_by(str_0, bool_0, separator=str_1)
        var_0 = list(iterator_0)
        bool_1 = False
        var_1 = list(iterator_0)
        iterator_1 = module_0.split_by(str_0, bool_0, criterion=bool_1)
        var_2 = list(iterator_1)
    except BaseException:
        pass

def test_case_25():
    try:
        str_0 = ' Split by: '
        bool_0 = True
        str_1 = 'P'
        iterator_0 = module_0.split_by(str_0, bool_0, separator=str_1)
        var_0 = list(iterator_0)
        bool_1 = False
        iterator_1 = module_0.split_by(str_0, bool_1, separator=str_1)
        var_1 = list(bool_1)
    except BaseException:
        pass