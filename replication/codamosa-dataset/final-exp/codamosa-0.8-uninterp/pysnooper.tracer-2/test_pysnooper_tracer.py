# Automatically generated by Pynguin.
import pysnooper.tracer as module_0

def test_case_0():
    pass

def test_case_1():
    tracer_0 = module_0.Tracer()
    var_0 = tracer_0.__enter__()

def test_case_2():
    tracer_0 = module_0.Tracer()

def test_case_3():
    str_0 = 'call'
    set_0 = {str_0, str_0, str_0}
    var_0 = module_0.get_write_function(str_0, set_0)

def test_case_4():
    str_0 = '{}.x'
    dict_0 = {}
    tracer_0 = module_0.Tracer(str_0, dict_0)
    list_0 = [str_0]
    tracer_1 = module_0.Tracer(tracer_0, str_0, list_0)

def test_case_5():
    list_0 = None
    file_writer_0 = module_0.FileWriter(list_0, list_0)

def test_case_6():
    str_0 = 'original_trace_functions'
    tracer_0 = module_0.Tracer(str_0)
    var_0 = tracer_0.__enter__()

def test_case_7():
    str_0 = 'original_trace_functions'
    tracer_0 = module_0.Tracer(str_0)
    var_0 = tracer_0.__enter__()
    var_1 = tracer_0.__enter__()