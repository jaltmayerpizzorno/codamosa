# Automatically generated by Pynguin.
import ansible.modules.command as module_0

def test_case_0():
    pass

def test_case_1():
    str_0 = ' n |1.'
    var_0 = module_0.check_command(str_0, str_0)

def test_case_2():
    str_0 = 'sn'
    bytes_0 = b'\x95\x03\xe4R\xe7\x8d;p{\xe8{\xd7\xa6\xce\xb5\xe8'
    list_0 = [bytes_0]
    var_0 = module_0.check_command(bytes_0, list_0)
    var_1 = module_0.check_command(str_0, str_0)
    var_2 = module_0.main()

def test_case_3():
    var_0 = module_0.main()