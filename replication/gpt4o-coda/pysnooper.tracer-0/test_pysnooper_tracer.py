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
    bytes_0 = b'\xb4\xdf\xf8\xda\x0b;!\xe9\x1d\xc1\xa7\x8b\x8d\xfd\xa0\xb3xH\xf7'
    str_0 = '/input/pysnooper/tracer.py'
    file_writer_0 = module_0.FileWriter(bytes_0, str_0)

def test_case_4():
    tracer_0 = module_0.Tracer()
    var_0 = tracer_0.__enter__()
    var_1 = tracer_0.__enter__()

def test_case_5():
    str_0 = 'Rp9\r`Rul'
    tracer_0 = None
    list_0 = [str_0, tracer_0]
    unavailable_source_0 = module_0.UnavailableSource()
    file_writer_0 = module_0.FileWriter(list_0, unavailable_source_0)
    str_1 = "(l+I%C\x0c\ni_Xc8'|b`z+K"
    dict_0 = {str_1: tracer_0}
    file_writer_1 = module_0.FileWriter(file_writer_0, dict_0)
    tracer_1 = module_0.Tracer(file_writer_1)
    var_0 = tracer_1.__enter__()