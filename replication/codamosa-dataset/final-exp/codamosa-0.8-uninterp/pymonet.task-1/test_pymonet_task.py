# Automatically generated by Pynguin.
import pymonet.task as module_0

def test_case_0():
    pass

def test_case_1():
    bytes_0 = b'MW\x0b!\xdcn\x7f\x1e\x1a\x99\t$'
    task_0 = module_0.Task(bytes_0)

def test_case_2():
    bytes_0 = b'\xdf\xc3v,\x94\x15\xdd)\xa99'
    task_0 = module_0.Task(bytes_0)
    bytes_1 = b'Zi'
    var_0 = task_0.map(bytes_1)

def test_case_3():
    str_0 = "7 N+cWQ^.px\r>'cpE"
    float_0 = 942.1
    bool_0 = True
    task_0 = module_0.Task(bool_0)
    float_1 = -2428.353224
    task_1 = module_0.Task(float_1)
    task_2 = module_0.Task(float_0)
    var_0 = task_2.bind(str_0)
    tuple_0 = ()
    var_1 = task_2.map(tuple_0)