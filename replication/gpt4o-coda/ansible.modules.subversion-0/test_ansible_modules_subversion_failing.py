# Automatically generated by Pynguin.
import ansible.modules.subversion as module_0

def test_case_0():
    try:
        bool_0 = True
        float_0 = 3448.6855
        int_0 = 1173
        subversion_0 = module_0.Subversion(float_0, bool_0, float_0, bool_0, float_0, bool_0, float_0, int_0)
        var_0 = subversion_0.checkout()
    except BaseException:
        pass

def test_case_1():
    try:
        bool_0 = False
        float_0 = 2.0
        int_0 = 1186
        subversion_0 = module_0.Subversion(float_0, bool_0, float_0, bool_0, float_0, bool_0, float_0, int_0)
        var_0 = subversion_0.checkout()
    except BaseException:
        pass

def test_case_2():
    try:
        bool_0 = False
        float_0 = 3448.7
        int_0 = 1184
        subversion_0 = module_0.Subversion(float_0, bool_0, float_0, bool_0, int_0, bool_0, float_0, bool_0)
        var_0 = subversion_0.checkout()
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = '$$SN'
        bool_0 = False
        set_0 = set()
        bytes_0 = b'\xea\xbf\xfc\x8aP\x08\t\xbd\x83)\x1d\x11\x01|\xe8'
        str_1 = '[o&ZhnI.{d${x hbwK'
        list_0 = [set_0]
        dict_0 = {bool_0: set_0, bool_0: list_0}
        bytes_1 = b'\x17J\xc0\xab@\xb5\xa2X\x80\xe1\xc6'
        subversion_0 = module_0.Subversion(bool_0, set_0, bytes_0, str_1, list_0, bytes_0, dict_0, bytes_1)
        float_0 = -1629.9
        set_1 = {str_0, bool_0}
        bool_1 = False
        subversion_1 = module_0.Subversion(str_0, str_0, subversion_0, float_0, set_1, bool_1, str_1, bool_0)
        var_0 = subversion_1.is_svn_repo()
    except BaseException:
        pass

def test_case_4():
    try:
        bool_0 = True
        float_0 = 3448.7
        int_0 = 1173
        subversion_0 = module_0.Subversion(float_0, bool_0, float_0, bool_0, float_0, bool_0, float_0, int_0)
        var_0 = subversion_0.export()
    except BaseException:
        pass

def test_case_5():
    try:
        str_0 = None
        bytes_0 = b'\xceVu\xfb\xc2\xdb\x9a'
        str_1 = 'O6&S9'
        list_0 = [bytes_0]
        str_2 = '6X^\ty=_'
        dict_0 = {str_2: str_2, str_2: str_0}
        bool_0 = True
        str_3 = '0V/s!3- jZUV%-I^9Ny'
        subversion_0 = module_0.Subversion(list_0, str_2, dict_0, dict_0, dict_0, bool_0, str_3, str_3)
        var_0 = subversion_0.export(str_1)
    except BaseException:
        pass

def test_case_6():
    try:
        bool_0 = True
        float_0 = 2.0
        int_0 = 1173
        subversion_0 = module_0.Subversion(float_0, bool_0, float_0, bool_0, float_0, bool_0, float_0, int_0)
        var_0 = subversion_0.switch()
    except BaseException:
        pass

def test_case_7():
    try:
        int_0 = 1176
        str_0 = '=BP0\\|b|)'
        set_0 = {int_0}
        list_0 = [set_0, str_0, set_0]
        str_1 = '#t5Mkhq3D'
        int_1 = -2912
        int_2 = -1640
        dict_0 = {}
        subversion_0 = module_0.Subversion(str_0, set_0, list_0, str_1, int_1, int_2, dict_0, set_0)
        var_0 = subversion_0.update()
    except BaseException:
        pass

def test_case_8():
    try:
        bool_0 = True
        float_0 = 9.39832300801554
        int_0 = 1168
        subversion_0 = module_0.Subversion(float_0, bool_0, float_0, bool_0, int_0, bool_0, float_0, bool_0)
        var_0 = subversion_0.revert()
    except BaseException:
        pass

def test_case_9():
    try:
        bool_0 = True
        float_0 = 3448.6855
        int_0 = 1173
        subversion_0 = module_0.Subversion(float_0, bool_0, float_0, bool_0, float_0, bool_0, float_0, int_0)
        var_0 = subversion_0.needs_update()
    except BaseException:
        pass

def test_case_10():
    try:
        bool_0 = False
        float_0 = 2.0
        int_0 = 1186
        subversion_0 = module_0.Subversion(float_0, bool_0, float_0, bool_0, float_0, bool_0, float_0, int_0)
        var_0 = subversion_0.get_remote_revision()
    except BaseException:
        pass

def test_case_11():
    try:
        float_0 = -1664.166
        int_0 = 1079
        bytes_0 = b''
        bool_0 = True
        str_0 = '__main__'
        bool_1 = None
        tuple_0 = (bool_1,)
        list_0 = [str_0, tuple_0, bool_0, tuple_0]
        set_0 = set()
        tuple_1 = (tuple_0, list_0, set_0)
        int_1 = -1340
        bytes_1 = b'\xe9\x9b@\xc0\xcf\x14\xba'
        dict_0 = {str_0: bool_0, bytes_1: set_0}
        int_2 = -1691
        int_3 = 1800
        subversion_0 = module_0.Subversion(int_1, dict_0, dict_0, dict_0, int_0, dict_0, int_2, int_3)
        subversion_1 = module_0.Subversion(float_0, int_0, bytes_0, float_0, bool_0, str_0, tuple_1, subversion_0)
        var_0 = subversion_1.has_local_mods()
    except BaseException:
        pass

def test_case_12():
    try:
        bool_0 = False
        float_0 = -1129.6527
        int_0 = 0
        subversion_0 = module_0.Subversion(float_0, bool_0, float_0, bool_0, int_0, bool_0, float_0, bool_0)
        var_0 = subversion_0.checkout(subversion_0)
    except BaseException:
        pass

def test_case_13():
    try:
        bool_0 = False
        float_0 = 3448.7
        int_0 = 1184
        subversion_0 = module_0.Subversion(float_0, bool_0, float_0, bool_0, int_0, bool_0, float_0, bool_0)
        var_0 = subversion_0.checkout(int_0)
    except BaseException:
        pass