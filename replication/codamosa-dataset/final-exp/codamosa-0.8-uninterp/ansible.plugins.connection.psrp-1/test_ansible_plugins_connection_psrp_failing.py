# Automatically generated by Pynguin.
import ansible.plugins.connection.psrp as module_0

def test_case_0():
    try:
        connection_0 = module_0.Connection()
    except BaseException:
        pass

def test_case_1():
    try:
        bool_0 = True
        list_0 = [bool_0, bool_0, bool_0, bool_0]
        connection_0 = module_0.Connection(*list_0)
        var_0 = connection_0.fetch_file(list_0, bool_0)
    except BaseException:
        pass

def test_case_2():
    try:
        bool_0 = True
        int_0 = -1093
        str_0 = 'B2A!Gm}--ej\x0bW|i<&&MR'
        list_0 = [str_0, str_0, str_0, str_0]
        connection_0 = module_0.Connection(*list_0)
        var_0 = connection_0.put_file(bool_0, int_0)
    except BaseException:
        pass

def test_case_3():
    try:
        bytes_0 = b'\xc8V\xa6\x0f\x14e\xa6\x1dY\xcb\xca\x88\x07'
        list_0 = [bytes_0, bytes_0, bytes_0]
        connection_0 = module_0.Connection(*list_0)
        bytes_1 = b''
        var_0 = connection_0.exec_command(bytes_1)
    except BaseException:
        pass