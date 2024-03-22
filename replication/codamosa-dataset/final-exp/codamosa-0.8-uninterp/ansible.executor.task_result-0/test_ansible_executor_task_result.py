# Automatically generated by Pynguin.
import ansible.executor.task_result as module_0

def test_case_0():
    pass

def test_case_1():
    int_0 = -26
    float_0 = -3745.1269
    str_0 = "\nansible_facts:\n  description: Facts to add to ansible_facts about the services on the system\n  returned: always\n  type: complex\n  contains:\n    services:\n      description: States of the services with service name as key.\n      returned: always\n      type: complex\n      contains:\n        source:\n          description:\n          - Init system of the service.\n          - One of C(rcctl), C(systemd), C(sysv), C(upstart), C(src).\n          returned: always\n          type: str\n          sample: sysv\n        state:\n          description:\n          - State of the service.\n          - 'This commonly includes (but is not limited to) the following: C(failed), C(running), C(stopped) or C(unknown).'\n          - Depending on the used init system additional states might be returned.\n          returned: always\n          type: str\n          sample: running\n        status:\n          description:\n          - State of the service.\n          - Either C(enabled), C(disabled), C(static), C(indirect) or C(unknown).\n          returned: systemd systems or RedHat/SUSE flavored sysvinit/upstart or OpenBSD\n          type: str\n          sample: enabled\n        name:\n          description: Name of the service.\n          returned: always\n          type: str\n          sample: arp-ethers.service\n"
    task_result_0 = module_0.TaskResult(int_0, float_0, str_0)
    var_0 = task_result_0.is_changed()

def test_case_2():
    str_0 = 'failed'
    str_1 = 'failed_when_result'
    str_2 = 'results'
    bool_0 = True
    bool_1 = {str_1: bool_0}
    bool_2 = [bool_1, bool_1]
    bool_3 = {str_0: bool_0, str_1: bool_0, str_2: bool_2}
    str_3 = ''
    task_result_0 = module_0.TaskResult(str_3, str_3, bool_3)
    var_0 = task_result_0.is_unreachable()
    var_1 = task_result_0.is_skipped()
    var_2 = task_result_0.is_failed()

def test_case_3():
    int_0 = -26
    float_0 = -3745.1269
    str_0 = "\nansible_facts:\n  description: Facts to add to ansible_facts about the services on the system\n  returned: always\n  type: complex\n  contains:\n    services:\n      description: States of the services with service name as key.\n      returned: always\n      type: complex\n      contains:\n        source:\n          description:\n          - Init system of the service.\n          - One of C(rcctl), C(systemd), C(sysv), C(upstart), C(src).\n          returned: always\n          type: str\n          sample: sysv\n        state:\n          description:\n          - State of the service.\n          - 'This commonly includes (but is not limited to) the following: C(failed), C(running), C(stopped) or C(unknown).'\n          - Depending on the used init system additional states might be returned.\n          returned: always\n          type: str\n          sample: running\n        status:\n          description:\n          - State of the service.\n          - Either C(enabled), C(disabled), C(static), C(indirect) or C(unknown).\n          returned: systemd systems or RedHat/SUSE flavored sysvinit/upstart or OpenBSD\n          type: str\n          sample: enabled\n        name:\n          description: Name of the service.\n          returned: always\n          type: str\n          sample: arp-ethers.service\n"
    task_result_0 = module_0.TaskResult(int_0, float_0, str_0)
    var_0 = task_result_0.is_failed()
    tuple_0 = (str_0, int_0, float_0)
    var_1 = task_result_0.needs_debugger(tuple_0)

def test_case_4():
    float_0 = 1780.635
    dict_0 = {float_0: float_0}
    bytes_0 = b'T\xad\xf1\x89X\xe6\xad'
    task_result_0 = module_0.TaskResult(dict_0, bytes_0, dict_0)
    var_0 = task_result_0.needs_debugger()

def test_case_5():
    var_0 = {}
    var_1 = {}
    task_result_0 = module_0.TaskResult(var_0, var_0, var_0, var_1)
    var_2 = task_result_0.is_skipped()
    var_3 = task_result_0.is_skipped()
    str_0 = 'results'
    str_1 = 'skipped'
    var_4 = []
    bool_0 = True
    var_5 = {str_0: var_4, str_1: bool_0}
    var_6 = {}
    task_result_1 = module_0.TaskResult(var_5, var_5, var_5, var_6)
    var_7 = task_result_1.is_skipped()
    bool_1 = {str_1: bool_0}
    bool_2 = [bool_1]
    bool_3 = {str_0: bool_2}
    var_8 = {}
    task_result_2 = module_0.TaskResult(bool_3, bool_3, bool_3, var_8)
    var_9 = task_result_2.is_skipped()

def test_case_6():
    str_0 = 'failed'
    str_1 = 'failed_when_result'
    str_2 = 'results'
    bool_0 = True
    bool_1 = {str_1: bool_0}
    bool_2 = {str_1: bool_1}
    bool_3 = [bool_1, bool_2]
    bool_4 = {str_0: bool_0, str_1: bool_0, str_2: bool_3}
    str_3 = ''
    task_result_0 = module_0.TaskResult(str_3, str_3, bool_4)
    var_0 = task_result_0.is_failed()

def test_case_7():
    str_0 = 'failed'
    str_1 = 'results'
    bool_0 = True
    bool_1 = {str_0: bool_0}
    bool_2 = {str_1: bool_1}
    bool_3 = {str_0: bool_0, str_1: bool_0, str_1: bool_2}
    str_2 = ''
    task_result_0 = module_0.TaskResult(str_2, str_2, bool_3)
    var_0 = task_result_0.is_failed()

def test_case_8():
    bytes_0 = b'\xf1v1\x91 !\x88\xd5k\x9d\\\xd9\x0e'
    str_0 = 'results'
    bool_0 = {bytes_0: str_0, str_0: str_0}
    task_result_0 = module_0.TaskResult(bool_0, bool_0, bool_0, bool_0)
    var_0 = task_result_0.is_unreachable()
    var_1 = task_result_0.is_failed()

def test_case_9():
    var_0 = None
    str_0 = 'failed'
    bool_0 = True
    bool_1 = {str_0: bool_0}
    str_1 = 'ame'
    str_2 = 'debugger'
    str_3 = 'test'
    str_4 = 'always'
    str_5 = {str_1: str_3, str_2: str_4}
    task_result_0 = module_0.TaskResult(var_0, var_0, bool_1, str_5)
    bytes_0 = b'O\x8c\xe3\xb4\xc2f'
    var_1 = task_result_0.needs_debugger(bytes_0)

def test_case_10():
    var_0 = None
    str_0 = 'failed'
    str_1 = 'unreachable'
    bool_0 = False
    bool_1 = {str_0: bool_0, str_0: bool_0, str_1: bool_0}
    str_2 = 'debugger'
    str_3 = 'alwys'
    str_4 = {str_2: str_3}
    var_1 = None
    task_result_0 = module_0.TaskResult(var_1, var_0, bool_1, str_4)
    var_2 = task_result_0.needs_debugger(bool_0)
    str_5 = 'never'
    str_6 = {str_2: str_5}
    task_result_1 = module_0.TaskResult(var_1, var_0, bool_1, str_6)
    var_3 = task_result_1.needs_debugger(bool_1)

def test_case_11():
    bool_0 = True
    var_0 = dict(ignore_errors=bool_0)
    str_0 = 'localhost'
    str_1 = 'fake task'
    str_2 = 'changed'
    str_3 = 'invocation'
    bool_1 = False
    str_4 = 'module_name'
    str_5 = 'module_args'
    str_6 = 'ping'
    str_7 = ''
    str_8 = {str_4: str_6, str_5: str_7}
    var_1 = {str_2: bool_1, str_3: str_8}
    task_result_0 = module_0.TaskResult(str_0, str_1, var_1, var_0)
    var_2 = task_result_0.needs_debugger(bool_0)
    var_3 = task_result_0.needs_debugger(bool_0)
    str_9 = 'failed'
    str_10 = {str_4: str_6, str_5: str_7}
    var_4 = {str_9: bool_0, str_3: str_10}
    task_result_1 = module_0.TaskResult(str_0, str_1, var_4, var_0)
    var_5 = task_result_1.needs_debugger(bool_0)