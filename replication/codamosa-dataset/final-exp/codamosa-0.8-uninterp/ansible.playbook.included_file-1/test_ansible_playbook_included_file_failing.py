# Automatically generated by Pynguin.
import ansible.playbook.included_file as module_0
import ansible.utils.display as module_1
import ansible.playbook.task_include as module_2

def test_case_0():
    try:
        bool_0 = False
        str_0 = 'An\x0bu]RODd/A?%\n)m*\x0c""'
        str_1 = '9?"iPL<zIaP5'
        bool_1 = False
        tuple_0 = ()
        bool_2 = False
        included_file_0 = module_0.IncludedFile(str_1, bool_1, tuple_0, bool_2, bool_1)
        var_0 = included_file_0.add_host(str_0)
        int_0 = 7
        bool_3 = False
        int_1 = 30
        included_file_1 = module_0.IncludedFile(str_0, int_0, bool_3, int_1)
        var_1 = included_file_1.__eq__(bool_0)
    except BaseException:
        pass

def test_case_1():
    try:
        bool_0 = False
        str_0 = 'An\x0bu]RODd/A?%\n)m*\x0c""'
        int_0 = 7
        bool_1 = False
        int_1 = 30
        included_file_0 = module_0.IncludedFile(str_0, int_0, bool_1, int_1)
        var_0 = included_file_0.__eq__(bool_0)
    except BaseException:
        pass

def test_case_2():
    try:
        bool_0 = None
        set_0 = {bool_0}
        bytes_0 = b'\x0eF#\xde\x90sn'
        str_0 = 'MxW#mZ\x0cvxH;soM=N8Z&'
        int_0 = 2331
        dict_0 = {}
        str_1 = '\n    This is a GNU Hurd specific subclass of Network. It use fsysopts to\n    get the ip address and support only pfinet.\n    '
        bytes_1 = b'\x14M\x1b\xff\xdc:\xe2H\xabT\x9c\xcfQ:\\J\xf4\x93'
        float_0 = 1.0
        included_file_0 = module_0.IncludedFile(dict_0, bytes_1, dict_0, float_0, set_0)
        included_file_1 = module_0.IncludedFile(set_0, bytes_1, dict_0, str_1, included_file_0)
        var_0 = included_file_1.process_include_results(bytes_0, set_0, str_0, int_0)
    except BaseException:
        pass

def test_case_3():
    try:
        bytes_0 = b'k(\xaf\xe8\xfa\xec\xcc8\xde\xc2'
        str_0 = '\n    This is a AIX Group manipulation class.\n\n    This overrides the following methods from the generic class:-\n      - group_del()\n      - group_add()\n      - group_mod()\n    '
        float_0 = 906.42
        included_file_0 = module_0.IncludedFile(bytes_0, bytes_0, str_0, float_0, float_0)
        tuple_0 = None
        dict_0 = {}
        str_1 = 'metadata_expire_filter'
        display_0 = module_1.Display(str_1)
        templar_0 = None
        var_0 = included_file_0.process_include_results(dict_0, str_1, display_0, templar_0)
        dict_1 = {str_0: str_0, str_0: tuple_0, str_0: str_0}
        bool_0 = False
        bytes_1 = b'\x98['
        str_2 = '~[;,<(`%lM\n\x0b'
        set_0 = {bool_0, str_2}
        tuple_1 = (bytes_1, str_2, set_0, set_0)
        int_0 = 2164
        included_file_1 = module_0.IncludedFile(dict_1, tuple_0, str_0, tuple_1)
        var_1 = included_file_1.__eq__(included_file_0)
        var_2 = included_file_0.process_include_results(dict_1, tuple_1, int_0, set_0)
    except BaseException:
        pass

def test_case_4():
    try:
        bytes_0 = b'k(\xaf\xe8\xfa\xec\xcc8\xde\xc2'
        str_0 = '\n    This is a AIX Group manipulation class.\n\n    This overrides the following methods from the generic class:-\n      - group_del()\n      - group_add()\n      - group_mod()\n    '
        bool_0 = True
        tuple_0 = None
        dict_0 = {str_0: str_0, str_0: tuple_0, str_0: str_0}
        set_0 = {bool_0, str_0}
        tuple_1 = (bytes_0, str_0, set_0, set_0)
        included_file_0 = module_0.IncludedFile(dict_0, tuple_0, str_0, tuple_1)
        var_0 = included_file_0.__eq__(included_file_0)
    except BaseException:
        pass

def test_case_5():
    try:
        bytes_0 = b'k(\xaf\xe8\xfa\xec\xcc8\xde\xc2'
        str_0 = '\n    This is a AIX Group manipulation class.\n\n    This overrides the following methods from the generic class:-\n      - group_del()\n      - group_add()\n      - group_mod()\n    '
        float_0 = 917.188538
        float_1 = 906.42
        included_file_0 = module_0.IncludedFile(bytes_0, bytes_0, str_0, float_0, float_1)
        bool_0 = True
        var_0 = included_file_0.add_host(bool_0)
        var_1 = included_file_0.__repr__()
        bool_1 = True
        var_2 = included_file_0.add_host(bool_1)
    except BaseException:
        pass

def test_case_6():
    try:
        bytes_0 = b'k(\xaf\xe8\xfa\xec\xcc8\xde\xc2'
        str_0 = '\n    This is a AIX Group manipulation class.\n\n    This overrides the following methods from the generic class:-\n      - group_del()\n      - group_add()\n      - group_mod()\n    '
        float_0 = 917.188538
        float_1 = 906.42
        included_file_0 = module_0.IncludedFile(bytes_0, bytes_0, str_0, float_0, float_1)
        var_0 = included_file_0.__repr__()
        bool_0 = True
        var_1 = included_file_0.add_host(bool_0)
        str_1 = 'metadata_expire_filter'
        display_0 = module_1.Display(str_1)
        bool_1 = True
        list_0 = [str_0, bool_1, str_0]
        bytes_1 = b'\x98['
        str_2 = '~[;,<(`%lM\n\x0b'
        set_0 = {bool_1, str_2}
        tuple_0 = (bytes_1, str_2, set_0, set_0)
        list_1 = [bool_0, var_1, tuple_0, bytes_1]
        str_3 = '}PLzf}'
        task_include_0 = module_2.TaskInclude(str_3, list_1)
        task_include_1 = module_2.TaskInclude(task_include_0, included_file_0)
        included_file_1 = module_0.IncludedFile(list_1, task_include_1, list_0, task_include_0)
        var_2 = included_file_1.__eq__(included_file_1)
    except BaseException:
        pass