# Automatically generated by Pynguin.
import pysnooper.tracer as module_0
import inspect as module_1
import pysnooper.variables as module_2

def test_case_0():
    pass

def test_case_1():
    tracer_0 = module_0.Tracer()
    var_0 = tracer_0.__enter__()

def test_case_2():
    tracer_0 = module_0.Tracer()

def test_case_3():
    str_0 = '{indent}Call ended by exception'
    tracer_0 = module_0.Tracer()
    var_0 = tracer_0.__enter__()
    list_0 = []
    tuple_0 = (list_0,)
    file_writer_0 = module_0.FileWriter(str_0, tuple_0)
    set_0 = None
    dict_0 = {}
    file_writer_1 = module_0.FileWriter(set_0, dict_0)

def test_case_4():
    var_0 = module_1.currentframe()
    var_1 = var_0.f_back
    str_0 = 'x'
    int_0 = 7
    common_variable_0 = module_2.CommonVariable(str_0, int_0)
    common_variable_1 = (common_variable_0,)
    var_2 = module_0.get_local_reprs(var_1, common_variable_1)