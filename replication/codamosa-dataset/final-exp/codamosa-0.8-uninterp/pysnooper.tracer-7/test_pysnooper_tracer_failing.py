# Automatically generated by Pynguin.
import pysnooper.tracer as module_0

def test_case_0():
    try:
        tracer_0 = module_0.Tracer()
        bytes_0 = b'w\xdaQ\xd6\xa5\xaa\xd7\x8a\x0cK\xc4)'
        var_0 = tracer_0.write(bytes_0)
        var_1 = tracer_0.__enter__()
        tuple_0 = None
        bool_0 = False
        file_writer_0 = module_0.FileWriter(tuple_0, bool_0)
        var_2 = tracer_0.__call__(file_writer_0)
    except BaseException:
        pass

def test_case_1():
    try:
        file_writer_0 = None
        var_0 = module_0.get_path_and_source_from_frame(file_writer_0)
    except BaseException:
        pass

def test_case_2():
    try:
        bool_0 = False
        tuple_0 = None
        dict_0 = {}
        tracer_0 = module_0.Tracer(tuple_0, dict_0)
        var_0 = module_0.get_write_function(bool_0, tracer_0)
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = 'Ya72'
        tracer_0 = module_0.Tracer(str_0, str_0)
        set_0 = {tracer_0, str_0}
        tracer_1 = module_0.Tracer(set_0)
    except BaseException:
        pass

def test_case_4():
    try:
        float_0 = -15.787667
        list_0 = []
        list_1 = [list_0, float_0, list_0, list_0]
        list_2 = [list_0, list_0, list_1]
        int_0 = -2248
        bool_0 = True
        tuple_0 = (int_0, bool_0)
        file_writer_0 = module_0.FileWriter(list_2, tuple_0)
        bytes_0 = b'\xc3m\xb7\xe0a\xb4<\x0b\xa5\xda\x99\x03\x0f6\x01'
        bytes_1 = b'\xb5\x9a \x87\xce\x8b\xe9%\x19\\qq'
        tracer_0 = module_0.Tracer(file_writer_0, bytes_0, bytes_1, bytes_1)
    except BaseException:
        pass

def test_case_5():
    try:
        str_0 = '@'
        list_0 = []
        list_1 = [str_0, list_0, str_0, list_0]
        tracer_0 = module_0.Tracer(str_0, list_0, list_1)
    except BaseException:
        pass

def test_case_6():
    try:
        file_writer_0 = None
        tracer_0 = module_0.Tracer()
        var_0 = tracer_0.__call__(file_writer_0)
    except BaseException:
        pass

def test_case_7():
    try:
        str_0 = '[R/2'
        str_1 = '\r(%3Q\t?rfM\x0bYm2B4aBF,'
        dict_0 = {str_0: str_1}
        file_writer_0 = None
        int_0 = 3
        str_2 = '&G'
        tracer_0 = module_0.Tracer(str_2)
        list_0 = [file_writer_0, dict_0, dict_0]
        tuple_0 = (int_0, tracer_0, str_2, list_0)
        tracer_1 = module_0.Tracer(str_0, str_1, dict_0, file_writer_0, tuple_0, str_1)
    except BaseException:
        pass

def test_case_8():
    try:
        tracer_0 = None
        bytes_0 = None
        file_writer_0 = module_0.FileWriter(tracer_0, bytes_0)
        unavailable_source_0 = module_0.UnavailableSource()
        var_0 = file_writer_0.write(unavailable_source_0)
    except BaseException:
        pass

def test_case_9():
    try:
        tracer_0 = module_0.Tracer()
        var_0 = tracer_0.__enter__()
        var_1 = tracer_0.__enter__()
        tuple_0 = None
        bool_0 = False
        file_writer_0 = module_0.FileWriter(tuple_0, bool_0)
        var_2 = tracer_0.__call__(tracer_0)
    except BaseException:
        pass

def test_case_10():
    try:
        tracer_0 = module_0.Tracer()
        var_0 = tracer_0.__enter__()
        bool_0 = None
        file_writer_0 = module_0.FileWriter(var_0, bool_0)
        set_0 = set()
        tracer_1 = module_0.Tracer(tracer_0, set_0)
        bytes_0 = b'l\xd8,4@@\x01\xff\x12$tN\xcc\xf0\x058'
        float_0 = -2917.49
        bytes_1 = None
        var_1 = tracer_0.__exit__(bytes_0, float_0, bytes_1)
    except BaseException:
        pass

def test_case_11():
    try:
        tracer_0 = module_0.Tracer()
        var_0 = tracer_0.__enter__()
        bytes_0 = b'o'
        list_0 = []
        var_1 = tracer_0.__exit__(list_0, tracer_0, bytes_0)
    except BaseException:
        pass

def test_case_12():
    try:
        file_writer_0 = None
        str_0 = '}a)C1@cDW a'
        str_1 = '$R*3'
        file_writer_1 = module_0.FileWriter(str_0, str_1)
        unavailable_source_0 = module_0.UnavailableSource()
        tracer_0 = module_0.Tracer(file_writer_1)
        var_0 = tracer_0.__enter__()
        tuple_0 = None
        tracer_1 = module_0.Tracer(tuple_0, file_writer_0)
    except BaseException:
        pass