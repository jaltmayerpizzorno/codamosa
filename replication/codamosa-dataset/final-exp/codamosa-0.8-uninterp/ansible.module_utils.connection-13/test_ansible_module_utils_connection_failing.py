# Automatically generated by Pynguin.
import ansible.module_utils.connection as module_0

def test_case_0():
    try:
        dict_0 = {}
        connection_0 = module_0.Connection(dict_0)
        list_0 = [connection_0, dict_0, dict_0]
        str_0 = '\n\n'
        var_0 = module_0.write_to_file_descriptor(list_0, str_0)
    except BaseException:
        pass

def test_case_1():
    try:
        list_0 = []
        var_0 = module_0.request_builder(list_0)
        str_0 = 'Ks'
        dict_0 = {str_0: list_0, str_0: list_0, str_0: list_0}
        list_1 = []
        var_1 = module_0.send_data(dict_0, list_1)
    except BaseException:
        pass

def test_case_2():
    try:
        bool_0 = False
        var_0 = module_0.recv_data(bool_0)
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = 'V5\x0c_xY\n'
        connection_0 = module_0.Connection(str_0)
        tuple_0 = (connection_0,)
        dict_0 = {tuple_0: tuple_0, tuple_0: str_0, tuple_0: connection_0, tuple_0: str_0}
        var_0 = module_0.exec_command(tuple_0, dict_0)
    except BaseException:
        pass

def test_case_4():
    try:
        bool_0 = False
        connection_0 = module_0.Connection(bool_0)
        var_0 = connection_0.__rpc__(connection_0)
    except BaseException:
        pass

def test_case_5():
    try:
        bool_0 = False
        connection_0 = module_0.Connection(bool_0)
        str_0 = '%j-Usm'
        dict_0 = {str_0: str_0}
        connection_error_0 = module_0.ConnectionError(str_0, **dict_0)
        var_0 = connection_0.__rpc__(connection_error_0)
    except BaseException:
        pass

def test_case_6():
    try:
        connection_0 = None
        connection_1 = module_0.Connection(connection_0)
    except BaseException:
        pass

def test_case_7():
    try:
        bytes_0 = b'C=\xa6'
        connection_0 = module_0.Connection(bytes_0)
        var_0 = module_0.recv_data(connection_0)
    except BaseException:
        pass

def test_case_8():
    try:
        bool_0 = False
        connection_0 = module_0.Connection(bool_0)
        var_0 = connection_0.__rpc__(bool_0)
    except BaseException:
        pass

def test_case_9():
    try:
        tuple_0 = None
        str_0 = '~-5.sO)'
        list_0 = [tuple_0, tuple_0, str_0]
        connection_error_0 = module_0.ConnectionError(tuple_0, *list_0)
        str_1 = '{\\K 2<z$SwX'
        connection_0 = module_0.Connection(str_1)
        var_0 = connection_0.send(connection_error_0)
    except BaseException:
        pass

def test_case_10():
    try:
        bytes_0 = b'4\x83x\xc2p\xd6\xa7\xbf5\xf6H\xf2\x0e'
        str_0 = 'Fb;1%Qd%_='
        str_1 = '*t`asi0;o)W&34H'
        str_2 = None
        float_0 = -321.904
        tuple_0 = (str_1, str_2, bytes_0, float_0)
        list_0 = [tuple_0, tuple_0, float_0]
        int_0 = 1127
        tuple_1 = (tuple_0, list_0, int_0)
        dict_0 = None
        bytes_1 = b'/\xbf\xdd\xf2:\x08\x96\x16\x9e\xdbV\xbeR\xe7\xd8=\xc4x'
        int_1 = -321
        float_1 = -1100.0
        tuple_2 = (int_1, float_1)
        tuple_3 = (str_0, dict_0, bytes_1, tuple_2)
        list_1 = [str_0, bytes_0, tuple_3]
        connection_error_0 = module_0.ConnectionError(list_1, *list_1)
        connection_0 = module_0.Connection(connection_error_0)
        var_0 = connection_0.__getattr__(tuple_1)
    except BaseException:
        pass

def test_case_11():
    try:
        str_0 = 'bct'
        connection_0 = module_0.Connection(str_0)
        var_0 = connection_0.__rpc__(str_0)
    except BaseException:
        pass

def test_case_12():
    try:
        float_0 = -1675.532397611316
        bool_0 = True
        bool_1 = False
        var_0 = module_0.write_to_file_descriptor(bool_1, float_0)
        connection_0 = module_0.Connection(bool_0)
        var_1 = connection_0.__rpc__(float_0)
    except BaseException:
        pass

def test_case_13():
    try:
        str_0 = 'Command "%s" found no files in archive. Empty archive files are not supported.'
        var_0 = ()
        var_1 = dict(_socket_path=var_0)
        var_2 = type(str_0, var_0, var_1)
        str_1 = 'echo ok'
        var_3 = module_0.exec_command(var_2, str_1)
    except BaseException:
        pass