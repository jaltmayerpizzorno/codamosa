# Automatically generated by Pynguin.
import thefuck.types as module_0

def test_case_0():
    try:
        set_0 = None
        int_0 = 1186
        str_0 = 'y3X\\!@}LF|V`#UXy]m'
        bytes_0 = b''
        command_0 = module_0.Command(str_0, bytes_0)
        var_0 = command_0.__repr__()
        dict_0 = {}
        corrected_command_0 = module_0.CorrectedCommand(set_0, int_0, dict_0)
    except BaseException:
        pass

def test_case_1():
    try:
        bytes_0 = b"\x15'>\xf6\x98$\xc4\xec"
        list_0 = [bytes_0]
        bool_0 = False
        float_0 = 439.28
        int_0 = 5
        corrected_command_0 = module_0.CorrectedCommand(bool_0, float_0, int_0)
        var_0 = corrected_command_0.run(list_0)
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = ',;sCzb`x\tN'
        dict_0 = {str_0: str_0}
        str_1 = ''
        str_2 = 'Vw(gzmH\nQC'
        tuple_0 = (str_1, str_2)
        set_0 = {tuple_0, str_2}
        dict_1 = {}
        dict_2 = {tuple_0: set_0, str_1: dict_1, str_1: dict_1}
        list_0 = [dict_0]
        str_3 = '$z0E,\nS\x0cx)n#\roR'
        rule_0 = None
        corrected_command_0 = module_0.CorrectedCommand(list_0, str_3, rule_0)
        corrected_command_1 = module_0.CorrectedCommand(dict_2, set_0, str_1)
        var_0 = corrected_command_1.__eq__(corrected_command_0)
        int_0 = 869
        var_1 = corrected_command_0.run(int_0)
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = 'm'
        var_0 = None
        int_0 = 1
        bool_0 = False
        rule_0 = module_0.Rule(str_0, var_0, var_0, var_0, var_0, int_0, bool_0)
        str_1 = 'rm -rf /'
        corrected_command_0 = module_0.CorrectedCommand(str_1, var_0, int_0)
        var_1 = rule_0.get_corrected_commands(var_0)
        var_2 = [c for c in var_1]
    except BaseException:
        pass

def test_case_4():
    try:
        tuple_0 = None
        float_0 = -4638.0
        int_0 = -993
        str_0 = "{I'_k\x0b{A;U2GzG}X"
        corrected_command_0 = module_0.CorrectedCommand(int_0, tuple_0, str_0)
        var_0 = corrected_command_0.__repr__()
        str_1 = 'H'
        int_1 = 1142
        bool_0 = False
        corrected_command_1 = module_0.CorrectedCommand(str_1, int_1, bool_0)
        var_1 = corrected_command_1.__eq__(float_0)
        dict_0 = {}
        set_0 = set()
        command_0 = module_0.Command(dict_0, set_0)
        dict_1 = {}
        float_1 = 2499.26526
        command_1 = module_0.Command(dict_1, float_1)
        var_2 = command_1.__eq__(command_0)
        float_2 = -1852.26
        str_2 = '3U,"QfPqnSRZ;5{'
        int_2 = -1295
        rule_0 = module_0.Rule(float_2, command_0, dict_1, command_1, str_2, int_2, command_1)
        var_3 = rule_0.is_match(corrected_command_1)
    except BaseException:
        pass