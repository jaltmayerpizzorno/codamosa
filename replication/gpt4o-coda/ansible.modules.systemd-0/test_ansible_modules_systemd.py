# Automatically generated by Pynguin.
import ansible.modules.systemd as module_0

def test_case_0():
    pass

def test_case_1():
    str_0 = '{,\\v'
    var_0 = module_0.parse_systemctl_show(str_0)

def test_case_2():
    var_0 = module_0.main()

def test_case_3():
    str_0 = 'l@!sL\t6Bc^/qxP_hQ \t!'
    var_0 = module_0.request_was_ignored(str_0)
    str_1 = 'ignoring request'
    var_1 = module_0.request_was_ignored(str_1)

def test_case_4():
    str_0 = 'ignoring request'
    var_0 = module_0.request_was_ignored(str_0)

def test_case_5():
    str_0 = 'ExecReload={ path=/bin/kill ; argv[]=/bin/kill -HUP $MAINPID ; ignore_errors=no ; start_time=[n/a] ; stop_time=[n/a] ; pid=0 ; code=(null) ; status=0/0 }'
    list_0 = [str_0]
    var_0 = module_0.parse_systemctl_show(list_0)

def test_case_6():
    str_0 = '6=oK'
    var_0 = module_0.parse_systemctl_show(str_0)
    var_1 = module_0.main()
    var_2 = module_0.parse_systemctl_show(str_0)

def test_case_7():
    str_0 = 'ExecReload=j pa,h=/bin/kill ; argv[]=/bin/kill -HUP $MAINPID ; ignore_errors=no ; suart_time=[n/a] ; stop_time=[n/a] ; pid=0 ; code=(null) ; status=0/0 }'
    list_0 = [str_0]
    var_0 = module_0.parse_systemctl_show(list_0)