# Automatically generated by Pynguin.
import ansible.module_utils.common.parameters as module_0

def test_case_0():
    try:
        dict_0 = {}
        str_0 = 'sXaNFG`1c: 9W'
        list_0 = [dict_0, dict_0, str_0]
        var_0 = module_0.sanitize_keys(list_0, list_0)
        list_1 = [str_0]
        var_1 = module_0.env_fallback(*list_1)
    except BaseException:
        pass

def test_case_1():
    try:
        var_0 = module_0.env_fallback()
    except BaseException:
        pass

def test_case_2():
    try:
        int_0 = -878
        list_0 = [int_0, int_0]
        var_0 = module_0.env_fallback(*list_0)
    except BaseException:
        pass

def test_case_3():
    try:
        tuple_0 = ()
        list_0 = [tuple_0]
        var_0 = module_0.set_fallbacks(tuple_0, list_0)
    except BaseException:
        pass

def test_case_4():
    try:
        bytes_0 = b'Z>S\xb0\x82wk\xeb=o\xd0\x1e\xb7\xb6~\xd2bM\x9a'
        float_0 = 0.2
        dict_0 = {bytes_0: bytes_0, bytes_0: float_0}
        str_0 = '2Qjx+|Pq4W'
        str_1 = 'Up'
        str_2 = '($_8t_!!PD7}\t'
        dict_1 = {str_2: dict_0, str_1: float_0, str_2: float_0, str_0: dict_0}
        str_3 = "hostname %r doesn't match %r"
        int_0 = -448
        dict_2 = {str_3: int_0}
        var_0 = module_0.sanitize_keys(dict_1, dict_2, str_2)
    except BaseException:
        pass

def test_case_5():
    try:
        str_0 = '<S84e`@'
        dict_0 = {str_0: str_0, str_0: str_0}
        str_1 = 'Role name, URL or tar file'
        list_0 = []
        tuple_0 = (dict_0, str_1, list_0)
        set_0 = set()
        var_0 = module_0.sanitize_keys(tuple_0, set_0)
        str_2 = "3R8lPEIy@<d|N>'Z("
        float_0 = 1173.0033
        var_1 = module_0.sanitize_keys(str_2, float_0)
    except BaseException:
        pass

def test_case_6():
    try:
        str_0 = '!z%E+Nmh -x\r^v'
        set_0 = set()
        dict_0 = {}
        bytes_0 = b'\xfa\x87\xb1\xbf\xeb\x1d\x07\xf5\x86\xa2C\x89'
        str_1 = 'sXaNFG`1c: 9W'
        dict_1 = {str_1: str_1, str_0: set_0, str_0: dict_0, str_1: str_0, str_1: str_1, str_0: bytes_0}
        list_0 = [dict_1, dict_1, str_1]
        var_0 = module_0.sanitize_keys(list_0, list_0)
        list_1 = [str_1]
        var_1 = module_0.env_fallback(*list_1)
    except BaseException:
        pass

def test_case_7():
    try:
        tuple_0 = ()
        dict_0 = {tuple_0: tuple_0, tuple_0: tuple_0}
        float_0 = 62.3
        var_0 = module_0.set_fallbacks(dict_0, float_0)
    except BaseException:
        pass

def test_case_8():
    try:
        float_0 = 60.0
        dict_0 = {float_0: float_0, float_0: float_0, float_0: float_0}
        dict_1 = {}
        int_0 = 20
        bool_0 = False
        list_0 = [dict_1, dict_0, float_0, int_0]
        var_0 = module_0.remove_values(bool_0, list_0)
        bytes_0 = b'\x11U\xe6\rX\xf6\x1e\xd9\xc0J\x05q{\xf6\x8e;{\xd4;>'
        var_1 = module_0.sanitize_keys(int_0, bytes_0)
        var_2 = module_0.remove_values(dict_0, dict_1)
        var_3 = module_0.env_fallback()
    except BaseException:
        pass

def test_case_9():
    try:
        bytes_0 = b'Z>S\xb0\x82wk\xeb=o\xd0\x1e\xb7\xb6~\xd2bM\x9a'
        float_0 = -9.824546868637757
        dict_0 = {bytes_0: bytes_0, bytes_0: float_0}
        str_0 = '2Qjx+|Pq4W'
        str_1 = '($_8t_!!PD7}\t'
        str_2 = "hostname %r doesn't match %r"
        int_0 = -448
        dict_1 = {str_2: int_0}
        var_0 = module_0.sanitize_keys(dict_1, dict_1, str_1)
        var_1 = module_0.remove_values(dict_1, str_1)
        var_2 = module_0.set_fallbacks(dict_0, str_0)
    except BaseException:
        pass

def test_case_10():
    try:
        float_0 = -283.0
        dict_0 = {}
        var_0 = module_0.set_fallbacks(dict_0, dict_0)
        dict_1 = {float_0: float_0, float_0: float_0, float_0: float_0}
        dict_2 = {}
        var_1 = module_0.remove_values(dict_1, dict_2)
        var_2 = module_0.env_fallback()
    except BaseException:
        pass

def test_case_11():
    try:
        bytes_0 = b'Z>S\xb0\x82wk\xeb=o\xd0\xb7\xb6~\xd2bM\x9a'
        float_0 = -9.824546868637757
        str_0 = 'x6|w%#'
        dict_0 = {bytes_0: bytes_0, bytes_0: float_0}
        str_1 = '2Qjx+|Pq4W'
        str_2 = 'I?eH\ndM#LF'
        dict_1 = {str_2: dict_0, str_1: bytes_0}
        list_0 = [str_0]
        var_0 = module_0.set_fallbacks(dict_1, list_0)
    except BaseException:
        pass

def test_case_12():
    try:
        str_0 = 'D+_ax3V*/ysO\r'
        str_1 = 'j-X!r'
        dict_0 = {str_0: str_1, str_1: str_1}
        dict_1 = {str_0: str_0, str_1: str_0, str_0: dict_0}
        bool_0 = False
        var_0 = module_0.set_fallbacks(dict_1, bool_0)
    except BaseException:
        pass

def test_case_13():
    try:
        str_0 = 'a'
        str_1 = 'foo'
        str_2 = {str_0: str_1}
        str_3 = 'b'
        str_4 = 'type'
        str_5 = 'fallback'
        str_6 = 'str'
        str_7 = 'bar'
        var_0 = lambda : str_7
        str_8 = 'prefix'
        str_9 = 'testing '
        str_10 = {str_8: str_9}
        var_1 = (var_0, str_10)
        var_2 = {str_4: str_6, str_5: var_1}
        var_3 = {str_3: var_2}
        var_4 = module_0.set_fallbacks(var_3, str_2)
    except BaseException:
        pass