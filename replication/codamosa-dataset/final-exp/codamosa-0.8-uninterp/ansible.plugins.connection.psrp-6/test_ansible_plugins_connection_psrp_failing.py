# Automatically generated by Pynguin.
import ansible.plugins.connection.psrp as module_0
import ansible.utils.display as module_1

def test_case_0():
    try:
        connection_0 = module_0.Connection()
    except BaseException:
        pass

def test_case_1():
    try:
        bytes_0 = b'\x17r\x88\xc4\x01\x14\x8fq\x98\x98{\xe3\xfb\xce\x8eo\xed0'
        list_0 = [bytes_0, bytes_0, bytes_0]
        connection_0 = module_0.Connection(*list_0)
        var_0 = connection_0.exec_command(bytes_0)
    except BaseException:
        pass

def test_case_2():
    try:
        int_0 = -3072
        display_0 = module_1.Display()
        display_1 = module_1.Display(display_0)
        display_2 = module_1.Display()
        list_0 = [display_2, display_2, display_2, display_2]
        connection_0 = module_0.Connection(*list_0)
        var_0 = connection_0.fetch_file(int_0, display_1)
    except BaseException:
        pass

def test_case_3():
    try:
        bytes_0 = b'\x17r\x88\xc4\x01\x14\x8fq\x98\x98{\xe3\xfb\xce\x8eo\xed0'
        list_0 = [bytes_0, bytes_0, bytes_0]
        connection_0 = module_0.Connection(*list_0)
        str_0 = 'Tv\x0be_/'
        display_0 = module_1.Display()
        var_0 = connection_0.put_file(str_0, display_0)
    except BaseException:
        pass