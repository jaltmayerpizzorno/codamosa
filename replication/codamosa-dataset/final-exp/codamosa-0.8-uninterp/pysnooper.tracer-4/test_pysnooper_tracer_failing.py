# Automatically generated by Pynguin.
import pysnooper.tracer as module_0
import datetime as module_1
import pysnooper.variables as module_2

def test_case_0():
    try:
        str_0 = 'yRM.<2s=/}3?b8EP0YqD'
        tuple_0 = (str_0,)
        var_0 = module_0.get_write_function(tuple_0, tuple_0)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = 'gF\tz'
        tuple_0 = ()
        list_0 = [str_0, tuple_0, str_0, tuple_0]
        tracer_0 = module_0.Tracer(str_0, tuple_0, list_0, tuple_0, str_0)
    except BaseException:
        pass

def test_case_2():
    try:
        bytes_0 = b'5\xf6!\x0cw\x04\xd3\xc3\xe9\x10\xda9\x9d\x00\xfa\xec\xfb\x16'
        list_0 = [bytes_0, bytes_0]
        bool_0 = True
        str_0 = 'PathLike'
        tracer_0 = module_0.Tracer(list_0, bool_0, str_0)
    except BaseException:
        pass

def test_case_3():
    try:
        tracer_0 = module_0.Tracer()
        tracer_1 = module_0.Tracer(tracer_0)
        var_0 = tracer_1.__enter__()
    except BaseException:
        pass

def test_case_4():
    try:
        dict_0 = {}
        unavailable_source_0 = module_0.UnavailableSource(**dict_0)
        set_0 = set()
        unavailable_source_1 = module_0.UnavailableSource(**dict_0)
        str_0 = None
        int_0 = -2083
        file_writer_0 = module_0.FileWriter(str_0, int_0)
        list_0 = []
        tracer_0 = module_0.Tracer(file_writer_0, unavailable_source_1, set_0, list_0)
    except BaseException:
        pass

def test_case_5():
    try:
        tracer_0 = module_0.Tracer()
        tuple_0 = ()
        bytes_0 = b''
        file_writer_0 = module_0.FileWriter(tuple_0, bytes_0)
        var_0 = file_writer_0.write(tracer_0)
    except BaseException:
        pass

def test_case_6():
    try:
        str_0 = 'def'
        float_0 = 84.232634
        tracer_0 = module_0.Tracer(str_0, float_0)
    except BaseException:
        pass

def test_case_7():
    try:
        str_0 = 'b;N>\r6e'
        str_1 = '/input/pysnooper/tracer.py'
        dict_0 = {str_1: str_1, str_0: str_1}
        file_writer_0 = module_0.FileWriter(str_0, dict_0)
        str_2 = '#\x0bme[&\'"Z-0 V@'
        tracer_0 = module_0.Tracer(str_2)
        var_0 = tracer_0.write(file_writer_0)
        str_3 = 'r'
        bytes_0 = b'}\x96\xb4\xdb6\xf7\xed\x05\xc9\x07w\xbdy\xd3\xe8H'
        file_writer_1 = module_0.FileWriter(str_3, bytes_0)
        tracer_1 = module_0.Tracer(file_writer_1)
        str_4 = 'jV0]#I!@j1'
        var_1 = module_0.get_write_function(str_4, bytes_0)
        tuple_0 = ()
        var_2 = file_writer_0.write(tuple_0)
    except BaseException:
        pass

def test_case_8():
    try:
        tuple_0 = ()
        float_0 = 285.1185
        list_0 = [float_0]
        file_writer_0 = module_0.FileWriter(list_0, list_0)
        var_0 = file_writer_0.write(tuple_0)
    except BaseException:
        pass

def test_case_9():
    try:
        tracer_0 = module_0.Tracer()
        dict_0 = {tracer_0: tracer_0, tracer_0: tracer_0, tracer_0: tracer_0}
        var_0 = tracer_0.__call__(dict_0)
    except BaseException:
        pass

def test_case_10():
    try:
        tracer_0 = module_0.Tracer()
        float_0 = -1606.92503
        var_0 = tracer_0.__exit__(float_0, tracer_0, float_0)
    except BaseException:
        pass

def test_case_11():
    try:
        tracer_0 = module_0.Tracer()
        var_0 = tracer_0.__enter__()
        str_0 = 'P{ cthL\rke'
        tuple_0 = ()
        bytes_0 = b''
        file_writer_0 = module_0.FileWriter(tuple_0, bytes_0)
        timedelta_0 = module_1.timedelta()
        var_1 = tracer_0.__exit__(tuple_0, str_0, timedelta_0)
    except BaseException:
        pass

def test_case_12():
    try:
        tracer_0 = module_0.Tracer()
        var_0 = tracer_0.__enter__()
        var_1 = tracer_0.__enter__()
        float_0 = 173.939
        var_2 = tracer_0.__call__(float_0)
    except BaseException:
        pass

def test_case_13():
    try:
        str_0 = 'r'
        bytes_0 = b'\x9f3\xbc0\xb8\xceQQ'
        file_writer_0 = module_0.FileWriter(str_0, bytes_0)
        tracer_0 = module_0.Tracer(file_writer_0)
        var_0 = tracer_0.__enter__()
        var_1 = tracer_0.__enter__()
        exploding_0 = None
        var_2 = tracer_0.__call__(exploding_0)
    except BaseException:
        pass

def test_case_14():
    try:
        tracer_0 = module_0.Tracer()
        str_0 = 'exception'
        common_variable_0 = module_2.CommonVariable(str_0)
        tracer_1 = module_0.Tracer(tracer_0, common_variable_0)
        var_0 = tracer_0.__enter__()
        bool_0 = False
        var_1 = tracer_0.__call__(bool_0)
    except BaseException:
        pass