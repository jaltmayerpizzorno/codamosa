# Automatically generated by Pynguin.
import ansible.modules.systemd as module_0

def test_case_0():
    try:
        str_0 = 'n_b\nfy*E/j1'
        var_0 = module_0.is_running_service(str_0)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = 'ExecReload={ path=/bid/kill ; argv[]=/bin/kill -HUP $MAINPID ; inore_errors=no ; start_time=[n/a] ; stop_time=[n/a] ; pid=0 ; code=(null) ; status=0/0 }'
        str_1 = [str_0, str_0, str_0]
        var_0 = module_0.parse_systemctl_show(str_1)
        list_0 = [var_0]
        var_1 = module_0.is_deactivating_service(list_0)
    except BaseException:
        pass

def test_case_2():
    try:
        int_0 = None
        var_0 = module_0.request_was_ignored(int_0)
    except BaseException:
        pass

def test_case_3():
    try:
        bytes_0 = b'\xe7\x9c\x8c\xf1\x9f\xf8\x9e\xb3\x11o\xf8\xb8\xe2:@'
        var_0 = module_0.parse_systemctl_show(bytes_0)
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = "=$%:'E"
        var_0 = module_0.request_was_ignored(str_0)
        str_1 = '1;d'
        var_1 = module_0.is_running_service(str_1)
    except BaseException:
        pass