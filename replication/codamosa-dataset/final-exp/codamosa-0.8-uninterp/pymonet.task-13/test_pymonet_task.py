# Automatically generated by Pynguin.
import pymonet.task as module_0

def test_case_0():
    pass

def test_case_1():
    list_0 = None
    task_0 = module_0.Task(list_0)

def test_case_2():
    float_0 = 2972.3
    int_0 = 70
    task_0 = module_0.Task(int_0)
    var_0 = task_0.map(float_0)

def test_case_3():
    bool_0 = False
    bytes_0 = b'U5\xd2\xddr\xecy2\x81\xaa\xe2\xc4\xd4\xb7\x12\xddH\xe62\x1e'
    task_0 = module_0.Task(bytes_0)
    var_0 = task_0.bind(bool_0)