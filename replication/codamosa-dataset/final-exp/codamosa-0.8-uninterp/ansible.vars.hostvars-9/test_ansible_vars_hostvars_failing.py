# Automatically generated by Pynguin.
import ansible.vars.hostvars as module_0

def test_case_0():
    try:
        str_0 = 'A+8B2/h3@L/tb'
        bytes_0 = b'Wd\x11B\xd1\x03y\t\x06Q\x1f\xdc\xccS\x99'
        host_vars_0 = module_0.HostVars(bytes_0, str_0, bytes_0)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = ':]gf&^{zr('
        str_1 = 'scp_extra_args'
        bytes_0 = b'\x18\xac?\xcc\xdfN}\x8aO\xfb\x08\xa1\xc3p\xf3v\xb2\xcd\xcb'
        list_0 = [str_1, str_1, str_1, bytes_0]
        host_vars_vars_0 = module_0.HostVarsVars(str_1, list_0)
        var_0 = host_vars_vars_0.__getitem__(str_0)
    except BaseException:
        pass

def test_case_2():
    try:
        float_0 = -460.5102
        bool_0 = True
        set_0 = {bool_0, bool_0}
        host_vars_vars_0 = module_0.HostVarsVars(bool_0, set_0)
        var_0 = host_vars_vars_0.__contains__(float_0)
    except BaseException:
        pass

def test_case_3():
    try:
        int_0 = 4096
        bool_0 = True
        set_0 = {int_0, int_0}
        host_vars_vars_0 = module_0.HostVarsVars(bool_0, set_0)
        var_0 = host_vars_vars_0.__len__()
    except BaseException:
        pass

def test_case_4():
    try:
        list_0 = []
        host_vars_vars_0 = module_0.HostVarsVars(list_0, list_0)
        str_0 = 'p/@wJWerx>IQk'
        host_vars_vars_1 = module_0.HostVarsVars(host_vars_vars_0, str_0)
        var_0 = host_vars_vars_1.__repr__()
    except BaseException:
        pass

def test_case_5():
    try:
        str_0 = '!Brzb:'
        bool_0 = True
        str_1 = 'Az|bn[\tjI'
        dict_0 = {str_1: str_1, str_1: str_1, str_1: str_1}
        tuple_0 = (str_1, dict_0, dict_0)
        host_vars_vars_0 = module_0.HostVarsVars(tuple_0, str_1)
        list_0 = []
        host_vars_0 = module_0.HostVars(host_vars_vars_0, host_vars_vars_0, list_0)
        var_0 = host_vars_0.set_host_facts(str_0, bool_0)
    except BaseException:
        pass

def test_case_6():
    try:
        str_0 = 'Az|bn[\tjI'
        dict_0 = {str_0: str_0, str_0: str_0, str_0: str_0}
        tuple_0 = (str_0, dict_0, dict_0)
        host_vars_vars_0 = module_0.HostVarsVars(tuple_0, str_0)
        list_0 = []
        host_vars_0 = module_0.HostVars(host_vars_vars_0, host_vars_vars_0, list_0)
        float_0 = -757.0
        host_vars_1 = module_0.HostVars(float_0, host_vars_0, float_0)
        var_0 = host_vars_1.__len__()
    except BaseException:
        pass

def test_case_7():
    try:
        str_0 = 'Az|bn[\tjI'
        dict_0 = {str_0: str_0, str_0: str_0, str_0: str_0}
        tuple_0 = (str_0, dict_0, dict_0)
        host_vars_vars_0 = module_0.HostVarsVars(tuple_0, str_0)
        list_0 = []
        host_vars_0 = module_0.HostVars(host_vars_vars_0, host_vars_vars_0, list_0)
        float_0 = -757.0
        var_0 = host_vars_0.__setstate__(dict_0)
        host_vars_1 = module_0.HostVars(float_0, host_vars_0, float_0)
        bool_0 = False
        host_vars_2 = module_0.HostVars(bool_0, host_vars_1, dict_0)
        var_1 = host_vars_1.__getitem__(str_0)
    except BaseException:
        pass

def test_case_8():
    try:
        str_0 = 'Az|bn[\tjI'
        dict_0 = {str_0: str_0, str_0: str_0, str_0: str_0}
        tuple_0 = (str_0, dict_0, dict_0)
        host_vars_vars_0 = module_0.HostVarsVars(tuple_0, str_0)
        list_0 = []
        host_vars_0 = module_0.HostVars(host_vars_vars_0, host_vars_vars_0, list_0)
        float_0 = -757.0
        var_0 = host_vars_0.set_variable_manager(host_vars_0)
        host_vars_1 = module_0.HostVars(float_0, host_vars_0, float_0)
        var_1 = host_vars_vars_0.__repr__()
    except BaseException:
        pass

def test_case_9():
    try:
        set_0 = set()
        str_0 = 'Usp$/r0llEZ1&J)4'
        bytes_0 = b'`u/\xa1'
        host_vars_vars_0 = module_0.HostVarsVars(str_0, bytes_0)
        list_0 = [set_0, set_0]
        host_vars_0 = module_0.HostVars(set_0, host_vars_vars_0, list_0)
        host_vars_vars_1 = module_0.HostVarsVars(str_0, set_0)
        var_0 = host_vars_vars_1.__repr__()
        tuple_0 = ()
        float_0 = -1687.638
        int_0 = -837
        var_1 = host_vars_0.set_host_variable(tuple_0, float_0, int_0)
    except BaseException:
        pass

def test_case_10():
    try:
        set_0 = set()
        str_0 = 'Usp$/r0llEZ1&J)4'
        bytes_0 = b'`u/\xa1'
        host_vars_vars_0 = module_0.HostVarsVars(str_0, bytes_0)
        list_0 = [set_0, set_0]
        host_vars_0 = module_0.HostVars(set_0, host_vars_vars_0, list_0)
        host_vars_vars_1 = module_0.HostVarsVars(str_0, set_0)
        var_0 = host_vars_vars_1.__repr__()
        var_1 = host_vars_0.set_inventory(host_vars_0)
        bool_0 = False
        var_2 = host_vars_0.set_nonpersistent_facts(host_vars_0, bool_0)
    except BaseException:
        pass

def test_case_11():
    try:
        str_0 = 'Az|bn[\tjI'
        dict_0 = {str_0: str_0, str_0: str_0, str_0: str_0}
        tuple_0 = (str_0, dict_0, dict_0)
        host_vars_vars_0 = module_0.HostVarsVars(tuple_0, str_0)
        list_0 = []
        host_vars_0 = module_0.HostVars(host_vars_vars_0, host_vars_vars_0, list_0)
        float_0 = -757.0
        var_0 = host_vars_0.__setstate__(dict_0)
        host_vars_1 = module_0.HostVars(float_0, host_vars_0, float_0)
        bool_0 = False
        host_vars_2 = module_0.HostVars(bool_0, host_vars_1, dict_0)
        var_1 = host_vars_1.__repr__()
    except BaseException:
        pass

def test_case_12():
    try:
        str_0 = 'Tz|bn[\tj['
        dict_0 = {str_0: str_0, str_0: str_0, str_0: str_0}
        tuple_0 = (str_0, dict_0, dict_0)
        host_vars_vars_0 = module_0.HostVarsVars(tuple_0, str_0)
        var_0 = host_vars_vars_0.__contains__(host_vars_vars_0)
    except BaseException:
        pass

def test_case_13():
    try:
        str_0 = 'Az|bn[\tjI'
        dict_0 = {str_0: str_0, str_0: str_0, str_0: str_0}
        tuple_0 = (str_0, dict_0, dict_0)
        host_vars_vars_0 = module_0.HostVarsVars(tuple_0, str_0)
        list_0 = []
        host_vars_0 = module_0.HostVars(host_vars_vars_0, host_vars_vars_0, list_0)
        var_0 = host_vars_vars_0.__contains__(host_vars_0)
    except BaseException:
        pass

def test_case_14():
    try:
        str_0 = ']?'
        host_vars_vars_0 = None
        host_vars_vars_1 = module_0.HostVarsVars(str_0, host_vars_vars_0)
        int_0 = 106
        var_0 = host_vars_vars_1.__getitem__(int_0)
    except BaseException:
        pass

def test_case_15():
    try:
        str_0 = 'Az|bn[\tjI'
        dict_0 = {str_0: str_0, str_0: str_0, str_0: str_0}
        tuple_0 = (str_0, dict_0, dict_0)
        host_vars_vars_0 = module_0.HostVarsVars(tuple_0, str_0)
        list_0 = []
        host_vars_0 = module_0.HostVars(host_vars_vars_0, host_vars_vars_0, list_0)
        float_0 = -757.0
        var_0 = host_vars_0.__setstate__(dict_0)
        host_vars_1 = module_0.HostVars(float_0, host_vars_0, float_0)
        var_1 = host_vars_1.__contains__(host_vars_0)
    except BaseException:
        pass