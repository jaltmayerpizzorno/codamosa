# Automatically generated by Pynguin.
import ansible.plugins.become.sudo as module_0

def test_case_0():
    try:
        become_module_0 = module_0.BecomeModule()
        list_0 = None
        var_0 = become_module_0.build_become_command(become_module_0, list_0)
    except BaseException:
        pass

def test_case_1():
    try:
        become_module_0 = module_0.BecomeModule()
        list_0 = None
        str_0 = 'b4wnmcWDg+x`\\r]@.<x'
        var_0 = become_module_0.build_become_command(list_0, str_0)
        var_1 = become_module_0.build_become_command(become_module_0, list_0)
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = '-H -S -n'
        str_1 = 'sudo'
        str_2 = ''
        str_3 = 'ping -c2'
        become_module_0 = module_0.BecomeModule()
        str_4 = 'become_flags'
        var_0 = become_module_0.set_option(str_4, str_0)
        str_5 = 'become_exe'
        var_1 = become_module_0.set_option(str_5, str_5)
        float_0 = 60.0
        dict_0 = {var_0: str_1, str_3: str_2, str_2: str_5, str_4: str_4}
        tuple_0 = (dict_0, become_module_0, str_1)
        var_2 = become_module_0.build_become_command(float_0, tuple_0)
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = '-H -S -n'
        str_1 = 'root'
        str_2 = ''
        set_0 = set()
        bytes_0 = b''
        become_module_0 = module_0.BecomeModule()
        var_0 = become_module_0.build_become_command(set_0, bytes_0)
        become_module_1 = module_0.BecomeModule()
        str_3 = 'become_flags'
        var_1 = become_module_1.set_option(str_3, str_0)
        str_4 = 'become_exe'
        var_2 = become_module_1.set_option(str_4, str_2)
        var_3 = become_module_1.set_option(str_1, str_1)
        become_module_2 = module_0.BecomeModule()
        bytes_1 = b'ao!K\xef\xef\xcb\xa7\x852\xdbNs0 '
        str_5 = '8ugB</kL\r'
        var_4 = become_module_1.build_become_command(bytes_1, str_5)
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = 'sudo'
        str_1 = 'root'
        str_2 = ''
        set_0 = set()
        bytes_0 = b''
        become_module_0 = module_0.BecomeModule()
        var_0 = become_module_0.build_become_command(set_0, bytes_0)
        str_3 = 'ping -c2'
        str_4 = 'sh'
        str_5 = 'become_flags'
        var_1 = become_module_0.set_option(str_5, str_2)
        str_6 = 'become_exe'
        var_2 = become_module_0.set_option(str_6, str_0)
        var_3 = become_module_0.set_option(str_1, str_1)
        dict_0 = {var_1: str_1, str_3: var_2, str_4: str_6, str_5: str_5}
        str_7 = 'Y&c>Xi^\x0bK*= GvAv+Qu'
        tuple_0 = (dict_0, become_module_0, str_7)
        bytes_1 = b'ao!K\xef\xef\xcb\xa7\x852\xdbNs0 '
        var_4 = become_module_0.build_become_command(bytes_1, tuple_0)
    except BaseException:
        pass