# Automatically generated by Pynguin.
import ansible.plugins.connection.paramiko_ssh as module_0

def test_case_0():
    try:
        float_0 = 1763.11
        dict_0 = {}
        my_add_policy_0 = module_0.MyAddPolicy(float_0, dict_0)
    except BaseException:
        pass

def test_case_1():
    try:
        int_0 = 318
        set_0 = {int_0, int_0, int_0, int_0}
        list_0 = [set_0, set_0, set_0, set_0]
        bool_0 = False
        set_1 = set()
        tuple_0 = (set_1,)
        str_0 = '%s submodule update --help'
        dict_0 = {str_0: tuple_0}
        list_1 = [set_1, dict_0]
        connection_0 = module_0.Connection(tuple_0, set_1, list_1)
        list_2 = []
        connection_1 = module_0.Connection(connection_0, list_2, tuple_0)
        var_0 = connection_1.put_file(list_0, bool_0)
    except BaseException:
        pass

def test_case_2():
    try:
        float_0 = -417.398
        set_0 = {float_0, float_0}
        str_0 = '|0'
        list_0 = []
        dict_0 = {}
        str_1 = 'V\x0c1++0Er)psR\r8'
        dict_1 = {str_0: dict_0, str_1: str_0, str_1: set_0}
        connection_0 = module_0.Connection(float_0, set_0, str_0, *list_0, **dict_1)
        var_0 = connection_0.reset()
        var_1 = connection_0.exec_command(str_0)
    except BaseException:
        pass

def test_case_3():
    try:
        float_0 = -417.398
        set_0 = {float_0, float_0}
        str_0 = '|[0|&\x0c'
        list_0 = []
        dict_0 = {}
        str_1 = 'V\x0c1++0Er)psR\r8'
        dict_1 = {str_0: dict_0, str_0: str_0, str_1: set_0}
        connection_0 = module_0.Connection(float_0, set_0, str_0, *list_0, **dict_1)
        var_0 = connection_0.reset()
        bool_0 = True
        bytes_0 = b'\x92N\xfb\x91/jEe <='
        float_1 = 0.1
        tuple_0 = (bytes_0, float_1, bool_0)
        var_1 = connection_0.fetch_file(tuple_0, set_0)
    except BaseException:
        pass

def test_case_4():
    try:
        bytes_0 = b'5=@\xca\x08\x1e\xb4\xc1]\xb2D\xab\xaf\xe5:{N'
        str_0 = '\\<p*@lukrze/"{v'
        str_1 = 'T^L,a1C5xF\r[:!B<\x0cb'
        list_0 = [bytes_0]
        connection_0 = module_0.Connection(str_0, str_1, list_0)
        var_0 = connection_0.close()
    except BaseException:
        pass

def test_case_5():
    try:
        float_0 = -417.398
        set_0 = {float_0, float_0}
        str_0 = '|0'
        connection_0 = None
        bytes_0 = b'\xc0\t\x82\xc8G\xe01\xcbH\x83\xd1\xbdl\xd6\xd9i'
        str_1 = 'ansible_os_family'
        str_2 = None
        str_3 = ":\to<&,5,p_C2'M"
        dict_0 = {}
        dict_1 = {str_1: bytes_0, str_0: bytes_0, str_2: str_3, str_1: dict_0}
        bool_0 = True
        list_0 = [str_0, bool_0, float_0, set_0]
        list_1 = [list_0, set_0]
        connection_1 = module_0.Connection(list_0, float_0, list_1)
        my_add_policy_0 = module_0.MyAddPolicy(bool_0, connection_1)
        var_0 = my_add_policy_0.missing_host_key(connection_0, bytes_0, dict_1)
    except BaseException:
        pass