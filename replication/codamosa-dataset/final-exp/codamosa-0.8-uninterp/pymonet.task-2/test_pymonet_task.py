# Automatically generated by Pynguin.
import pymonet.task as module_0

def test_case_0():
    pass

def test_case_1():
    int_0 = -1973
    task_0 = module_0.Task(int_0)

def test_case_2():
    str_0 = None
    int_0 = -1973
    task_0 = module_0.Task(int_0)
    var_0 = task_0.map(str_0)

def test_case_3():
    bool_0 = False
    bytes_0 = b'q\x1a\x91U\x1cr/\t\x81\xd5\x07\x7f\x1a\x13\xc1\xd2q'
    task_0 = module_0.Task(bytes_0)
    var_0 = task_0.bind(bool_0)