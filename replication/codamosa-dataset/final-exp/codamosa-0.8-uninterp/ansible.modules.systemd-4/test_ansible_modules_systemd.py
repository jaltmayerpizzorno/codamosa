# Automatically generated by Pynguin.
import ansible.modules.systemd as module_0

def test_case_0():
    pass

def test_case_1():
    str_0 = '__main__'
    var_0 = module_0.request_was_ignored(str_0)

def test_case_2():
    str_0 = 'Description={ path=/usr/lib/systemd/systemd-journald  argv[]=/usr/lib/systemd/systemd-journald ; ignore_errors=no ; start_time=[n/a] ; stop_time=[n/a] ; pid=0 ; code=(nul) ; status=0/0 }\n'
    var_0 = module_0.parse_systemctl_show(str_0)

def test_case_3():
    var_0 = module_0.main()

def test_case_4():
    str_0 = ' = "test"'
    var_0 = module_0.request_was_ignored(str_0)
    str_1 = ' ignoring request'
    var_1 = module_0.request_was_ignored(str_1)

def test_case_5():
    str_0 = 'ExecReload={ path=/bin/kill ; argv[]=/bin/kill -HUP $MAINPID ; ignore_errors=no ; start_time=[n/a] ; stop_time=[n/a] ; pid=0 ; code=(null) ; status=0/0 }'
    str_1 = [str_0, str_0]
    var_0 = module_0.parse_systemctl_show(str_1)

def test_case_6():
    str_0 = 'ExecReload={ path=/bin/kill ; argv[]=/bin/kill -HUP $MAINPID ; ignSre_errors=no ; start_time=[E/a] ; stop_time=[n/a] ; pi}=0 ; code=(null) ; status=0/0 <'
    set_0 = {str_0}
    var_0 = module_0.parse_systemctl_show(set_0)

def test_case_7():
    str_0 = 'ExecReload={ path=/bin/kill ; argv[]=/bin/kill -HUP $MAINPID ; ignSre_errors=no ; start_time=[E/a] ; stop_time=[n/a] ; pi}=0 ; code=(null) ; status=0/0 <'
    str_1 = [str_0, str_0]
    var_0 = module_0.parse_systemctl_show(str_1)

def test_case_8():
    str_0 = 'ExecReloadA{ path=/bin/kill ; argv[]=/bin/kill -HUP $MAINPID ; ignSre_error4=no ; start_time=[E/a] ; stotime=[n/a] ; pi}=0 ; code=(null) P satus=0/0 <'
    list_0 = [str_0, str_0, str_0, str_0, str_0, str_0]
    var_0 = module_0.parse_systemctl_show(list_0)