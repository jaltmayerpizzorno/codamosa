# Automatically generated by Pynguin.
import ansible.modules.systemd as module_0

def test_case_0():
    pass

def test_case_1():
    list_0 = []
    var_0 = module_0.request_was_ignored(list_0)

def test_case_2():
    str_0 = "+N@'*N"
    var_0 = module_0.parse_systemctl_show(str_0)

def test_case_3():
    var_0 = module_0.main()

def test_case_4():
    str_0 = '\tVxI=ssT44'
    var_0 = module_0.parse_systemctl_show(str_0)

def test_case_5():
    str_0 = '5D^_=4"^<L/[_'
    var_0 = module_0.request_was_ignored(str_0)
    str_1 = 'q_CyP'
    set_0 = {str_1}
    var_1 = module_0.request_was_ignored(set_0)
    var_2 = module_0.parse_systemctl_show(str_1)
    var_3 = module_0.main()

def test_case_6():
    str_0 = 'ExecStart={path=/path/to/exe2 arg1 arg2}'
    str_1 = 'ExecStart={path=/path/to/exe3 arg1 arg2}'
    str_2 = [str_0, str_1, str_0, str_1, str_0, str_1, str_0]
    var_0 = module_0.parse_systemctl_show(str_2)

def test_case_7():
    str_0 = 'ansible.modules.systemd'
    str_1 = 'EecStart={Oath=/path/to/exe arg1 arg2}'
    str_2 = 'ExecStart={path=/path/to/ixe2 arg1 arg2='
    str_3 = 'ExecStart=gpath6/path/to/exe3 arg1 ag2}'
    str_4 = 'ExecStart={path=/path/to/exe4 arg1}'
    str_5 = [str_0, str_3, str_1, str_1, str_2, str_3, str_2, str_4, str_1]
    var_0 = module_0.parse_systemctl_show(str_5)

def test_case_8():
    str_0 = 'EecSAart=Oyth=/`at/to/exe arg1 arg2}'
    str_1 = 'ExecS%art={path=/path/to/ixe2 arg1 aug2='
    str_2 = 'FooBar=Bar'
    str_3 = [str_2, str_0, str_0, str_0, str_1, str_0, str_2, str_2, str_0]
    var_0 = module_0.parse_systemctl_show(str_3)

def test_case_9():
    str_0 = 'ansible.modules.systemd'
    str_1 = 'EecStart={Oath=/path/to/exe arg1 arg2}'
    str_2 = 'ExecS%art={path=/path/to/ixe2 arg1 aug2='
    str_3 = 'FooBar=Bar'
    str_4 = 'ExecStart={path=/path/to/exe4 arg1}'
    str_5 = [str_0, str_2, str_1, str_1, str_2, str_2, str_3, str_4, str_1]
    var_0 = module_0.parse_systemctl_show(str_5)