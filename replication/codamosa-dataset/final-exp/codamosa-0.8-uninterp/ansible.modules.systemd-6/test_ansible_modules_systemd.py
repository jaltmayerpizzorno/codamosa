# Automatically generated by Pynguin.
import ansible.modules.systemd as module_0

def test_case_0():
    pass

def test_case_1():
    str_0 = "d'O7\r8R"
    var_0 = module_0.request_was_ignored(str_0)

def test_case_2():
    str_0 = "d'O7\r8R"
    var_0 = module_0.parse_systemctl_show(str_0)

def test_case_3():
    str_0 = 'ExecStart=/bin/true'
    str_1 = [str_0, str_0, str_0, str_0, str_0, str_0, str_0]
    var_0 = module_0.parse_systemctl_show(str_1)

def test_case_4():
    var_0 = module_0.main()

def test_case_5():
    str_0 = 'ignoring request'
    var_0 = module_0.request_was_ignored(str_0)
    str_1 = 'ignoring command'
    var_1 = module_0.request_was_ignored(str_1)
    var_2 = module_0.main()