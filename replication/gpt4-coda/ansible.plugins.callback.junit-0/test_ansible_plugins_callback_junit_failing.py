# Automatically generated by Pynguin.
import ansible.plugins.callback.junit as module_0

def test_case_0():
    try:
        list_0 = []
        bytes_0 = b'y\n,\x08\xdc'
        str_0 = 'N"RhTn'
        set_0 = None
        str_1 = None
        tuple_0 = (str_0, bytes_0, set_0, str_1)
        int_0 = 1459
        float_0 = 3730.42
        str_2 = 'tvS1_b%0S\\=a72y*+,5('
        host_data_0 = module_0.HostData(tuple_0, int_0, float_0, str_2)
        float_1 = 2071.9
        bool_0 = False
        host_data_1 = module_0.HostData(tuple_0, host_data_0, float_1, bool_0)
        tuple_1 = (list_0, bytes_0, str_0, host_data_1)
        callback_module_0 = module_0.CallbackModule()
        var_0 = callback_module_0.v2_runner_on_no_hosts(tuple_1)
    except BaseException:
        pass

def test_case_1():
    try:
        bool_0 = True
        callback_module_0 = module_0.CallbackModule()
        var_0 = callback_module_0.v2_playbook_on_cleanup_task_start(bool_0)
    except BaseException:
        pass

def test_case_2():
    try:
        list_0 = []
        callback_module_0 = module_0.CallbackModule()
        var_0 = callback_module_0.v2_playbook_on_include(list_0)
    except BaseException:
        pass

def test_case_3():
    try:
        bool_0 = True
        int_0 = -2141
        dict_0 = {}
        list_0 = [int_0]
        host_data_0 = module_0.HostData(bool_0, int_0, dict_0, list_0)
        callback_module_0 = module_0.CallbackModule()
        var_0 = callback_module_0.v2_playbook_on_start(host_data_0)
    except BaseException:
        pass

def test_case_4():
    try:
        bool_0 = False
        list_0 = [bool_0, bool_0, bool_0, bool_0]
        str_0 = '9\x0bS@ilf\r\t2'
        tuple_0 = (list_0, str_0)
        callback_module_0 = module_0.CallbackModule()
        var_0 = callback_module_0.v2_playbook_on_play_start(tuple_0)
    except BaseException:
        pass

def test_case_5():
    try:
        callback_module_0 = module_0.CallbackModule()
        dict_0 = {callback_module_0: callback_module_0, callback_module_0: callback_module_0, callback_module_0: callback_module_0, callback_module_0: callback_module_0}
        var_0 = callback_module_0.v2_runner_on_no_hosts(dict_0)
    except BaseException:
        pass

def test_case_6():
    try:
        float_0 = 0.001
        dict_0 = {float_0: float_0, float_0: float_0, float_0: float_0}
        callback_module_0 = module_0.CallbackModule()
        callback_module_1 = module_0.CallbackModule()
        var_0 = callback_module_1.v2_playbook_on_task_start(dict_0, callback_module_0)
    except BaseException:
        pass

def test_case_7():
    try:
        callback_module_0 = module_0.CallbackModule()
        str_0 = ';pw\x0c}YH-d>&d\r'
        var_0 = callback_module_0.v2_playbook_on_handler_task_start(str_0)
    except BaseException:
        pass

def test_case_8():
    try:
        bool_0 = False
        str_0 = '+\\>9K@9'
        callback_module_0 = module_0.CallbackModule()
        var_0 = callback_module_0.v2_runner_on_failed(bool_0, str_0)
    except BaseException:
        pass

def test_case_9():
    try:
        int_0 = 2253
        bytes_0 = b'\xb9\x84\x01\x99\xa1\xdd\xb9\x18Q'
        str_0 = '0'
        bool_0 = True
        list_0 = [bool_0, bytes_0, bytes_0, str_0]
        host_data_0 = module_0.HostData(int_0, bytes_0, str_0, list_0)
        callback_module_0 = module_0.CallbackModule()
        var_0 = callback_module_0.v2_runner_on_failed(host_data_0)
    except BaseException:
        pass

def test_case_10():
    try:
        set_0 = set()
        callback_module_0 = module_0.CallbackModule()
        var_0 = callback_module_0.v2_runner_on_ok(set_0)
    except BaseException:
        pass

def test_case_11():
    try:
        complex_0 = None
        callback_module_0 = module_0.CallbackModule()
        var_0 = callback_module_0.v2_playbook_on_stats(callback_module_0)
        var_1 = callback_module_0.v2_runner_on_skipped(complex_0)
    except BaseException:
        pass

def test_case_12():
    try:
        bytes_0 = b'h\x8e\xb6'
        bool_0 = True
        set_0 = {bool_0, bool_0, bool_0, bool_0}
        list_0 = []
        int_0 = True
        bytes_1 = b'b\x14\xa1" E8\xa5>P\xc4\x16\x9b\x8f\xe0'
        task_data_0 = module_0.TaskData(bool_0, set_0, list_0, int_0, bytes_1)
        var_0 = task_data_0.add_host(bytes_0)
    except BaseException:
        pass

def test_case_13():
    try:
        callback_module_0 = module_0.CallbackModule()
        set_0 = {callback_module_0, callback_module_0}
        str_0 = 'G%7("}0g`nKpK'
        list_0 = [callback_module_0]
        float_0 = None
        bool_0 = False
        task_data_0 = module_0.TaskData(list_0, float_0, bool_0, list_0, set_0)
        str_1 = 'uG'
        dict_0 = {str_1: str_0}
        task_data_1 = module_0.TaskData(set_0, str_0, task_data_0, bool_0, dict_0)
        bytes_0 = b'\x9bh\x10y\xaa\x0c^\xe3\xd2'
        list_1 = [float_0, float_0, str_0, set_0]
        callback_module_1 = module_0.CallbackModule()
        host_data_0 = module_0.HostData(bytes_0, dict_0, list_1, bool_0)
        str_2 = '(<\nmQd_cP#\x0cq [ap6&qV'
        task_data_2 = module_0.TaskData(bool_0, bool_0, host_data_0, str_2, bool_0)
        var_0 = task_data_2.add_host(host_data_0)
        var_1 = task_data_2.add_host(host_data_0)
    except BaseException:
        pass