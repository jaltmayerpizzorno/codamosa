# Automatically generated by Pynguin.
import ansible.plugins.action.reboot as module_0

def test_case_0():
    try:
        action_module_0 = module_0.ActionModule()
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = "/v+Rl#})j'I\raEmY"
        dict_0 = {str_0: str_0}
        str_1 = 'Z"|.WGSOM'
        float_0 = -130.697
        list_0 = [float_0, float_0, dict_0, float_0, float_0, str_1]
        action_module_0 = module_0.ActionModule(*list_0)
        var_0 = action_module_0.validate_reboot(dict_0, str_1)
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = "/v+Rl#})j'IcL\rammY"
        dict_0 = {str_0: str_0}
        str_1 = 'Z"|.WGSOM'
        float_0 = -130.7
        list_0 = [float_0, float_0, dict_0, float_0, float_0, str_1]
        action_module_0 = module_0.ActionModule(*list_0)
        dict_1 = None
        var_0 = action_module_0.perform_reboot(dict_1, dict_1)
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = ';{n|_F$9-`}cPKJ0'
        dict_0 = {str_0: str_0}
        float_0 = -130.7
        list_0 = [float_0, float_0, dict_0, float_0, float_0, str_0]
        action_module_0 = module_0.ActionModule(*list_0)
        var_0 = action_module_0.deprecated_args()
        var_1 = action_module_0.get_shutdown_command_args(list_0)
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = "/v+Rl#})j'IcL\rammY"
        dict_0 = {str_0: str_0}
        str_1 = 'Z"|.WGSOM'
        float_0 = -130.7
        list_0 = [float_0, float_0, dict_0, float_0, float_0, str_1]
        action_module_0 = module_0.ActionModule(*list_0)
        var_0 = action_module_0.deprecated_args()
        timed_out_exception_0 = module_0.TimedOutException()
        int_0 = -1496
        var_1 = action_module_0.run_test_command(int_0, **dict_0)
    except BaseException:
        pass

def test_case_5():
    try:
        str_0 = ';{n|_F$9-`}cPKJ0'
        dict_0 = {str_0: str_0}
        str_1 = 'Z"|.WGSOM'
        float_0 = -130.7
        list_0 = [float_0, float_0, dict_0, float_0, float_0, str_1]
        action_module_0 = module_0.ActionModule(*list_0)
        dict_1 = {action_module_0: float_0, str_0: list_0}
        var_0 = action_module_0.check_boot_time(dict_1, dict_0)
    except BaseException:
        pass

def test_case_6():
    try:
        str_0 = ';{n|_F$9-`}cPKJ0'
        dict_0 = {str_0: str_0}
        float_0 = -130.7
        list_0 = [float_0, float_0, dict_0, float_0, float_0, str_0]
        int_0 = 13
        tuple_0 = (int_0,)
        action_module_0 = module_0.ActionModule(*list_0)
        var_0 = action_module_0.get_system_boot_time(tuple_0)
    except BaseException:
        pass

def test_case_7():
    try:
        str_0 = '<%s> %s'
        dict_0 = {str_0: str_0}
        float_0 = -130.7
        list_0 = [float_0, float_0, dict_0, float_0, float_0, str_0]
        action_module_0 = module_0.ActionModule(*list_0)
        var_0 = action_module_0.deprecated_args()
        int_0 = -108
        var_1 = action_module_0.run(int_0)
    except BaseException:
        pass

def test_case_8():
    try:
        str_0 = ';{n|_F$9-`}cPKJ0'
        dict_0 = {str_0: str_0}
        str_1 = 'Z"|.WGSOM'
        float_0 = -130.7
        list_0 = [float_0, float_0, dict_0, float_0, float_0, str_1]
        action_module_0 = module_0.ActionModule(*list_0)
        var_0 = action_module_0.get_distribution(list_0)
    except BaseException:
        pass