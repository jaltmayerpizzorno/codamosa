# Automatically generated by Pynguin.
import thonny.jedi_utils as module_0

def test_case_0():
    try:
        int_0 = None
        str_0 = None
        str_1 = '\nY'
        str_2 = 'Try performing a web search for\n\n``Python %s: %s``'
        float_0 = 0.1
        list_0 = []
        bytes_0 = b'\n\xa2\x9e\xa9x\xcc\xea#\x10\xb5u0O\xd0'
        str_3 = 'xn29f@<\nS-h'
        tuple_0 = ()
        tuple_1 = (bytes_0, int_0, str_3, tuple_0)
        thonny_completion_0 = module_0.ThonnyCompletion(str_0, str_1, str_2, float_0, list_0, tuple_1)
        str_4 = None
        float_1 = -2094.0
        str_5 = '#2ca02c'
        list_1 = [float_1, str_4]
        thonny_completion_1 = module_0.ThonnyCompletion(str_4, str_4, float_1, str_5, int_0, list_1)
        var_0 = module_0.get_statement_of_position(int_0, thonny_completion_1)
    except BaseException:
        pass

def test_case_1():
    try:
        bytes_0 = None
        var_0 = module_0.parse_source(bytes_0)
    except BaseException:
        pass

def test_case_2():
    try:
        int_0 = -1876
        str_0 = '\t2'
        var_0 = module_0.get_script_completions(str_0, int_0, int_0, str_0)
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = 'def f(a): pass\nf('
        var_0 = module_0.get_interpreter_completions(str_0, str_0)
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = 'Z=dZe9r(c0"~TK?'
        int_0 = 497
        var_0 = module_0.get_definitions(str_0, int_0, int_0, str_0)
    except BaseException:
        pass

def test_case_5():
    try:
        bytes_0 = b'U0{\xa4J\x1f\x05\x169 [(\xc2\x13N\xc2'
        str_0 = "ERROR: This back-end requires a Python package named 'ptyprocess'.\n"
        float_0 = 2095.7
        list_0 = []
        tuple_0 = ()
        str_1 = 'M}v-V*D^OpF'
        thonny_completion_0 = module_0.ThonnyCompletion(str_0, str_0, float_0, list_0, tuple_0, str_1)
        var_0 = thonny_completion_0.__getitem__(bytes_0)
    except BaseException:
        pass