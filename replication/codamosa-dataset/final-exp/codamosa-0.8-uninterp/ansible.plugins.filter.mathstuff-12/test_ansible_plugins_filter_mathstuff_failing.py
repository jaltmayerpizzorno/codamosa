# Automatically generated by Pynguin.
import ansible.plugins.filter.mathstuff as module_0

def test_case_0():
    try:
        float_0 = -3672.09898
        bytes_0 = b'\xdd\xb2\xb8\x90\xda\xdbd'
        var_0 = module_0.unique(float_0, float_0, bytes_0)
    except BaseException:
        pass

def test_case_1():
    try:
        int_0 = -1601
        filter_module_0 = module_0.FilterModule()
        filter_module_1 = module_0.FilterModule()
        filter_module_2 = module_0.FilterModule()
        tuple_0 = (int_0,)
        var_0 = module_0.intersect(int_0, filter_module_1, tuple_0)
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = 'k3I>CP@S/9#I`pQ'
        filter_module_0 = module_0.FilterModule()
        str_1 = '%%'
        int_0 = None
        dict_0 = {str_1: int_0}
        var_0 = module_0.symmetric_difference(str_0, filter_module_0, dict_0)
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = None
        bool_0 = None
        int_0 = 1795
        var_0 = module_0.difference(str_0, bool_0, int_0)
    except BaseException:
        pass

def test_case_4():
    try:
        tuple_0 = ()
        set_0 = {tuple_0, tuple_0}
        var_0 = module_0.rekey_on_member(tuple_0, set_0)
        bool_0 = True
        var_1 = module_0.logarithm(bool_0)
        float_0 = 0.2
        str_0 = "de+>\n{K'\x0cOB&\n4/\n"
        list_0 = [var_1, str_0]
        var_2 = module_0.difference(str_0, list_0, set_0)
        list_1 = []
        list_2 = [list_1]
        var_3 = module_0.symmetric_difference(float_0, list_1, list_2)
        int_0 = -1693
        list_3 = [set_0, int_0, var_0]
        dict_0 = {str_0: var_0, str_0: list_0}
        var_4 = module_0.unique(tuple_0, tuple_0)
        var_5 = module_0.max(int_0, list_3, **dict_0)
    except BaseException:
        pass

def test_case_5():
    try:
        bool_0 = False
        set_0 = {bool_0, bool_0, bool_0}
        dict_0 = {bool_0: bool_0}
        bool_1 = True
        tuple_0 = ()
        bytes_0 = b'\xed\xe8jjP\x81:\xab\xec\x1f'
        var_0 = module_0.symmetric_difference(bool_1, tuple_0, bytes_0)
        str_0 = "4WiWj'12<@}r0"
        int_0 = 358
        var_1 = module_0.inversepower(int_0)
        filter_module_0 = module_0.FilterModule()
        dict_1 = {}
        var_2 = module_0.unique(filter_module_0, dict_1, set_0)
        var_3 = module_0.max(dict_0, str_0)
        var_4 = module_0.min(set_0, str_0)
        str_1 = 'name'
        str_2 = {str_1: str_1, str_1: str_0}
        str_3 = {str_1: str_0, str_0: str_0}
        str_4 = 'e'
        float_0 = -760.3
        tuple_1 = (dict_0,)
        var_5 = module_0.unique(float_0, tuple_1)
        bytes_1 = b'6t\rA\xae\xc6jAX\x91\x85'
        var_6 = module_0.unique(float_0, bytes_1)
        str_5 = {str_1: str_1, str_1: str_4}
        str_6 = [str_2, str_3, str_2, str_5]
        var_7 = module_0.rekey_on_member(str_6, str_3)
    except BaseException:
        pass

def test_case_6():
    try:
        bytes_0 = b'X\x9caXJ\xbe\xfb4\n\xb2-\x00o\xe90n;vX\xff'
        float_0 = -275.7
        var_0 = module_0.min(bytes_0, float_0)
    except BaseException:
        pass

def test_case_7():
    try:
        dict_0 = {}
        filter_module_0 = module_0.FilterModule(**dict_0)
        var_0 = module_0.max(dict_0, filter_module_0)
    except BaseException:
        pass

def test_case_8():
    try:
        dict_0 = {}
        var_0 = module_0.logarithm(dict_0)
    except BaseException:
        pass

def test_case_9():
    try:
        list_0 = None
        bool_0 = False
        var_0 = module_0.power(list_0, bool_0)
    except BaseException:
        pass

def test_case_10():
    try:
        int_0 = -507
        dict_0 = {int_0: int_0, int_0: int_0}
        var_0 = module_0.inversepower(dict_0)
    except BaseException:
        pass

def test_case_11():
    try:
        dict_0 = {}
        bytes_0 = b'X-\xf1&\xc4x\xa6\x1c\x10\xf3E'
        list_0 = [bytes_0, dict_0, bytes_0, bytes_0]
        var_0 = module_0.human_readable(bytes_0, list_0)
    except BaseException:
        pass

def test_case_12():
    try:
        int_0 = -717
        var_0 = module_0.human_to_bytes(int_0)
    except BaseException:
        pass

def test_case_13():
    try:
        int_0 = -2175
        str_0 = '!gO)N^}'
        var_0 = module_0.rekey_on_member(int_0, str_0)
    except BaseException:
        pass

def test_case_14():
    try:
        bytes_0 = b'\xd8\x7fmY4\xa1'
        tuple_0 = (bytes_0,)
        float_0 = 433.0
        var_0 = module_0.rekey_on_member(tuple_0, float_0)
    except BaseException:
        pass

def test_case_15():
    try:
        filter_module_0 = module_0.FilterModule()
        var_0 = filter_module_0.filters()
        var_1 = filter_module_0.filters()
        str_0 = '\x0b\x0b8~WZ#%-bN*Sn]0\tR'
        str_1 = 'dark gray'
        dict_0 = {str_0: var_0, str_1: filter_module_0}
        bool_0 = False
        var_2 = module_0.rekey_on_member(dict_0, bool_0)
    except BaseException:
        pass

def test_case_16():
    try:
        bool_0 = False
        set_0 = {bool_0, bool_0, bool_0}
        str_0 = '5g}'
        dict_0 = {bool_0: bool_0}
        str_1 = "Unable to retrieve documentation from '%s' due to: %s"
        filter_module_0 = module_0.FilterModule()
        dict_1 = {}
        var_0 = module_0.unique(filter_module_0, dict_1, set_0)
        var_1 = module_0.max(dict_0, str_1)
        var_2 = module_0.min(set_0, str_0)
        str_2 = 'name'
        str_3 = {str_2: str_2, str_2: str_1}
        str_4 = {str_2: var_1, str_2: str_1, str_1: str_1}
        str_5 = 'e'
        float_0 = 673.601
        tuple_0 = ()
        bool_1 = True
        list_0 = [dict_0, var_2, tuple_0, bool_1]
        var_3 = module_0.difference(float_0, tuple_0, list_0)
        str_6 = {str_2: str_2, str_2: str_5}
        str_7 = [str_3, str_4, str_6]
        var_4 = module_0.rekey_on_member(str_7, str_4)
    except BaseException:
        pass

def test_case_17():
    try:
        int_0 = 1315
        float_0 = -466.671
        int_1 = 1375
        set_0 = {float_0, int_1}
        str_0 = 'OKZYiJ5El`@1w#\\0M'
        list_0 = [int_0, set_0]
        var_0 = module_0.union(set_0, str_0, list_0)
    except BaseException:
        pass

def test_case_18():
    try:
        float_0 = -1817.2
        var_0 = module_0.logarithm(float_0)
    except BaseException:
        pass

def test_case_19():
    try:
        bool_0 = False
        set_0 = {bool_0, bool_0, bool_0}
        str_0 = '5g}'
        dict_0 = {bool_0: bool_0}
        str_1 = "Unable to retrieve documentation from '%s' due to: %s"
        var_0 = module_0.max(dict_0, str_1)
        var_1 = module_0.min(set_0, str_0)
        str_2 = 'r'
        var_2 = module_0.unique(set_0, dict_0)
        str_3 = ''
        var_3 = module_0.rekey_on_member(str_3, str_2)
    except BaseException:
        pass

def test_case_20():
    try:
        filter_module_0 = module_0.FilterModule()
        set_0 = {filter_module_0, filter_module_0}
        var_0 = module_0.unique(set_0, set_0)
        var_1 = filter_module_0.filters()
        var_2 = filter_module_0.filters()
        bool_0 = False
        filter_module_1 = module_0.FilterModule()
        list_0 = [filter_module_1]
        var_3 = module_0.rekey_on_member(bool_0, list_0)
    except BaseException:
        pass

def test_case_21():
    try:
        int_0 = 1240
        tuple_0 = ()
        var_0 = module_0.inversepower(int_0, tuple_0)
    except BaseException:
        pass

def test_case_22():
    try:
        tuple_0 = ()
        set_0 = {tuple_0, tuple_0}
        bool_0 = True
        var_0 = module_0.logarithm(bool_0)
        float_0 = 0.2
        list_0 = []
        list_1 = []
        var_1 = module_0.symmetric_difference(float_0, list_0, list_1)
        filter_module_0 = module_0.FilterModule()
        str_0 = '&LDvN{Ts\x0bWt9%?Q)Mfqn'
        int_0 = 2
        var_2 = module_0.rekey_on_member(set_0, str_0, int_0)
    except BaseException:
        pass

def test_case_23():
    try:
        str_0 = 's~IJBZb|,['
        dict_0 = {str_0: str_0, str_0: str_0, str_0: str_0}
        filter_module_0 = module_0.FilterModule()
        float_0 = 825.0199
        list_0 = [dict_0, dict_0, dict_0]
        var_0 = module_0.unique(float_0, list_0, list_0)
        var_1 = module_0.rekey_on_member(dict_0, str_0)
    except BaseException:
        pass

def test_case_24():
    try:
        tuple_0 = ()
        set_0 = {tuple_0, tuple_0}
        var_0 = module_0.rekey_on_member(tuple_0, set_0)
        bool_0 = True
        var_1 = module_0.logarithm(bool_0)
        float_0 = 0.2
        str_0 = "de+>\n{K'\x0cOB&\n4/\n"
        list_0 = [tuple_0, bool_0, var_1, float_0, str_0]
        var_2 = module_0.difference(str_0, list_0, set_0)
        list_1 = []
        list_2 = [list_0, tuple_0]
        filter_module_0 = module_0.FilterModule(*list_1)
        var_3 = filter_module_0.filters()
        var_4 = module_0.symmetric_difference(float_0, list_1, list_2)
        str_1 = 'e\n~Y*mtK_Z`5\x0c\rp'
        filter_module_1 = module_0.FilterModule()
        list_3 = [filter_module_1, str_1, str_1]
        var_5 = module_0.power(str_1, list_3)
    except BaseException:
        pass

def test_case_25():
    try:
        str_0 = '4q'
        set_0 = {str_0}
        list_0 = [str_0, str_0, set_0, set_0]
        list_1 = [str_0, set_0, list_0, str_0]
        var_0 = module_0.unique(str_0, set_0, list_0, list_1)
    except BaseException:
        pass

def test_case_26():
    try:
        tuple_0 = ()
        set_0 = {tuple_0, tuple_0}
        bool_0 = False
        var_0 = module_0.inversepower(set_0, bool_0)
    except BaseException:
        pass

def test_case_27():
    try:
        bytes_0 = b'\xf3\x87'
        str_0 = 'HG^iT*O&7>>W\x0cpW\x0c(1'
        filter_module_0 = module_0.FilterModule()
        float_0 = 0.1
        var_0 = module_0.human_readable(bytes_0, str_0, float_0)
    except BaseException:
        pass

def test_case_28():
    try:
        tuple_0 = ()
        set_0 = {tuple_0, tuple_0}
        var_0 = module_0.rekey_on_member(tuple_0, set_0)
        bool_0 = True
        var_1 = module_0.logarithm(bool_0)
        bytes_0 = b'J\xf6(\x97\x02\x9c\xaa\xd7L\xda\xb5'
        var_2 = module_0.min(tuple_0, bytes_0)
        float_0 = 0.2
        str_0 = "de+>\n{K'\x0cOB&\n4/\n"
        list_0 = [var_1, str_0]
        var_3 = module_0.difference(str_0, list_0, set_0)
        list_1 = []
        float_1 = 1818.731617
        list_2 = [list_1]
        var_4 = module_0.symmetric_difference(float_0, list_1, list_2)
        var_5 = module_0.human_to_bytes(float_1, float_0)
    except BaseException:
        pass

def test_case_29():
    try:
        str_0 = 'key'
        str_1 = {str_0: str_0, str_0: str_0}
        str_2 = [str_1, str_1, str_0]
        var_0 = module_0.rekey_on_member(str_2, str_0)
    except BaseException:
        pass

def test_case_30():
    try:
        str_0 = '=9'
        str_1 = {str_0: str_0, str_0: str_0, str_0: str_0, str_0: str_0, str_0: str_0}
        str_2 = [str_1, str_1, str_0]
        var_0 = module_0.rekey_on_member(str_2, str_1)
    except BaseException:
        pass

def test_case_31():
    try:
        float_0 = 649.7
        var_0 = module_0.power(float_0, float_0)
    except BaseException:
        pass

def test_case_32():
    try:
        tuple_0 = ()
        float_0 = -389.51066
        set_0 = {tuple_0, float_0, tuple_0}
        bool_0 = False
        str_0 = 'v\x0c2oCDAg]\\wJ'
        var_0 = module_0.unique(float_0, set_0, bool_0, str_0)
    except BaseException:
        pass