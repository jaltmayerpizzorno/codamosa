# Automatically generated by Pynguin.
import ansible.executor.playbook_executor as module_0

def test_case_0():
    try:
        str_0 = 'hahaha'
        playbook_executor_0 = module_0.PlaybookExecutor(str_0, str_0, str_0, str_0, str_0)
        var_0 = playbook_executor_0.run()
    except BaseException:
        pass

def test_case_1():
    try:
        var_0 = []
        playbook_executor_0 = module_0.PlaybookExecutor(var_0, var_0, var_0, var_0, var_0)
        var_1 = playbook_executor_0.run()
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = ''
        dict_0 = {}
        int_0 = 77
        bytes_0 = b'\xd1Yd\xdb\x18\x8cC?\x93\x9eI\xc8\x97\x99\x9f'
        playbook_executor_0 = module_0.PlaybookExecutor(str_0, dict_0, int_0, bytes_0, bytes_0)
        var_0 = playbook_executor_0.run()
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = '3'
        bool_0 = False
        dict_0 = {str_0: str_0}
        playbook_executor_0 = module_0.PlaybookExecutor(str_0, bool_0, dict_0, bool_0, dict_0)
        var_0 = playbook_executor_0.run()
    except BaseException:
        pass