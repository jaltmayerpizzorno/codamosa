# Automatically generated by Pynguin.
import ansible.modules.systemd as module_0

def test_case_0():
    pass

def test_case_1():
    str_0 = 'ansible_scp_extra_args'
    var_0 = module_0.request_was_ignored(str_0)

def test_case_2():
    str_0 = 'MQ ZLeL'
    var_0 = module_0.parse_systemctl_show(str_0)

def test_case_3():
    var_0 = module_0.main()

def test_case_4():
    str_0 = 'ignoring request'
    var_0 = module_0.request_was_ignored(str_0)
    var_1 = module_0.request_was_ignored(str_0)
    str_1 = '='
    var_2 = module_0.request_was_ignored(str_1)
    var_3 = module_0.main()

def test_case_5():
    str_0 = '\x0c@=^\x0bMS533TGIi Yp'
    var_0 = module_0.parse_systemctl_show(str_0)

def test_case_6():
    str_0 = 'ignoring request'
    var_0 = module_0.request_was_ignored(str_0)

def test_case_7():
    str_0 = 'ExecStart={\n  foo;\n  bar;\n}'
    str_1 = [str_0]
    var_0 = module_0.parse_systemctl_show(str_1)

def test_case_8():
    str_0 = 'Id=some-service.service'
    str_1 = 'Description=some description'
    str_2 = 'ExecStart={'
    str_3 = 'Description=another description'
    str_4 = [str_0, str_1, str_3, str_2, str_0, str_3, str_3, str_3]
    var_0 = module_0.parse_systemctl_show(str_4)
    int_0 = 2
    int_1 = 6
    var_1 = str_4[int_0:int_1]

def test_case_9():
    str_0 = 'Id=some-service.service'
    str_1 = 'Description=some description'
    str_2 = 'ExecStart={'
    str_3 = '  PathExistsGlob=/foo/*.pid'
    str_4 = '  ExecStart=/bin/rm -f /foo/*.pid'
    str_5 = '}'
    str_6 = [str_0, str_1, str_5, str_2, str_3, str_4, str_5, str_2]
    var_0 = module_0.parse_systemctl_show(str_6)
    int_0 = 2
    int_1 = 6
    var_1 = str_6[int_0:int_1]