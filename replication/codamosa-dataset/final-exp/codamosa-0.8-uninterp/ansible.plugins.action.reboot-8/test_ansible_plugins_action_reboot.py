# Automatically generated by Pynguin.
import ansible.plugins.action.reboot as module_0

def test_case_0():
    pass

def test_case_1():
    timed_out_exception_0 = module_0.TimedOutException()
    list_0 = [timed_out_exception_0, timed_out_exception_0, timed_out_exception_0, timed_out_exception_0, timed_out_exception_0, timed_out_exception_0]
    action_module_0 = module_0.ActionModule(*list_0)
    var_0 = action_module_0.deprecated_args()