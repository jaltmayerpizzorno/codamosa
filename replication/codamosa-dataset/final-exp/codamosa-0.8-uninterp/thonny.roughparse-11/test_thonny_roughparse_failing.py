# Automatically generated by Pynguin.
import thonny.roughparse as module_0

def test_case_0():
    try:
        str_0 = 'dict-iter-method'
        dict_0 = {}
        list_0 = []
        list_1 = [list_0, list_0, str_0]
        string_translate_pseudo_mapping_0 = module_0.StringTranslatePseudoMapping(dict_0, list_1)
        bool_0 = False
        string_translate_pseudo_mapping_1 = module_0.StringTranslatePseudoMapping(string_translate_pseudo_mapping_0, bool_0)
        var_0 = string_translate_pseudo_mapping_1.__iter__()
        var_1 = string_translate_pseudo_mapping_1.__len__()
        rough_parser_0 = module_0.RoughParser(str_0, string_translate_pseudo_mapping_1)
        var_2 = rough_parser_0.get_base_indent_string()
    except BaseException:
        pass

def test_case_1():
    try:
        bool_0 = True
        list_0 = [bool_0]
        rough_parser_0 = module_0.RoughParser(bool_0, list_0)
        var_0 = rough_parser_0.compute_bracket_indent()
    except BaseException:
        pass

def test_case_2():
    try:
        bool_0 = True
        list_0 = [bool_0, bool_0, bool_0]
        rough_parser_0 = module_0.RoughParser(bool_0, list_0)
        bool_1 = False
        var_0 = rough_parser_0.set_lo(bool_1)
        dict_0 = {}
        var_1 = rough_parser_0.set_str(dict_0)
        var_2 = rough_parser_0.get_num_lines_in_stmt()
    except BaseException:
        pass

def test_case_3():
    try:
        bool_0 = True
        rough_parser_0 = module_0.RoughParser(bool_0, bool_0)
        str_0 = ''
        var_0 = rough_parser_0.set_str(str_0)
        var_1 = rough_parser_0.compute_backslash_indent()
    except BaseException:
        pass

def test_case_4():
    try:
        dict_0 = {}
        str_0 = 'cmp-method'
        rough_parser_0 = module_0.RoughParser(dict_0, str_0)
        var_0 = rough_parser_0.is_block_opener()
    except BaseException:
        pass

def test_case_5():
    try:
        str_0 = 'Initial submit_mode: %s, block_size: %s, block_delay: %s'
        int_0 = -817
        rough_parser_0 = module_0.RoughParser(str_0, int_0)
        var_0 = rough_parser_0.get_last_stmt_bracketing()
    except BaseException:
        pass

def test_case_6():
    try:
        str_0 = '|<|o\x0b7z#N{?E'
        hyper_parser_0 = module_0.HyperParser(str_0, str_0)
    except BaseException:
        pass

def test_case_7():
    try:
        bool_0 = False
        float_0 = 0.05
        rough_parser_0 = module_0.RoughParser(bool_0, float_0)
        hyper_parser_0 = module_0.HyperParser(rough_parser_0, float_0)
    except BaseException:
        pass

def test_case_8():
    try:
        bytes_0 = b'\x9eG3\x8bq\x81S\x80n\xa8'
        int_0 = 2441
        rough_parser_0 = module_0.RoughParser(bytes_0, int_0)
        var_0 = rough_parser_0.get_continuation_type()
    except BaseException:
        pass

def test_case_9():
    try:
        bool_0 = False
        rough_parser_0 = module_0.RoughParser(bool_0, bool_0)
        str_0 = ''
        var_0 = rough_parser_0.set_str(str_0)
        var_1 = rough_parser_0.get_base_indent_string()
        var_2 = rough_parser_0.is_block_closer()
        float_0 = 1274.0
        var_3 = rough_parser_0.find_good_parse_start(float_0, float_0)
    except BaseException:
        pass

def test_case_10():
    try:
        bool_0 = False
        list_0 = [bool_0, bool_0, bool_0, bool_0]
        rough_parser_0 = module_0.RoughParser(bool_0, list_0)
        var_0 = rough_parser_0.set_lo(bool_0)
        var_1 = rough_parser_0.set_str(rough_parser_0)
    except BaseException:
        pass

def test_case_11():
    try:
        bool_0 = True
        list_0 = []
        rough_parser_0 = module_0.RoughParser(bool_0, list_0)
        str_0 = "2>VubGyn's/\\L);P=aZ"
        var_0 = rough_parser_0.set_str(str_0)
    except BaseException:
        pass

def test_case_12():
    try:
        float_0 = None
        bool_0 = True
        list_0 = [bool_0, bool_0, bool_0, bool_0]
        rough_parser_0 = module_0.RoughParser(bool_0, list_0)
        var_0 = rough_parser_0.set_lo(float_0)
    except BaseException:
        pass

def test_case_13():
    try:
        bool_0 = False
        rough_parser_0 = module_0.RoughParser(bool_0, bool_0)
        str_0 = 'Z]3#fC\n'
        var_0 = rough_parser_0.set_str(str_0)
        var_1 = rough_parser_0.get_base_indent_string()
        var_2 = rough_parser_0.get_continuation_type()
        var_3 = rough_parser_0.compute_backslash_indent()
    except BaseException:
        pass

def test_case_14():
    try:
        bytes_0 = b'\x1b\x04'
        float_0 = 1736.0
        list_0 = []
        dict_0 = {float_0: bytes_0}
        float_1 = 556.6
        string_translate_pseudo_mapping_0 = module_0.StringTranslatePseudoMapping(dict_0, float_1)
        var_0 = string_translate_pseudo_mapping_0.get(list_0)
    except BaseException:
        pass

def test_case_15():
    try:
        bool_0 = True
        list_0 = [bool_0, bool_0, bool_0, bool_0]
        rough_parser_0 = module_0.RoughParser(bool_0, list_0)
        dict_0 = {}
        var_0 = rough_parser_0.set_str(dict_0)
        int_0 = 2426
        var_1 = rough_parser_0.find_good_parse_start(int_0, int_0)
    except BaseException:
        pass

def test_case_16():
    try:
        bool_0 = True
        rough_parser_0 = module_0.RoughParser(bool_0, bool_0)
        bool_1 = False
        var_0 = rough_parser_0.set_lo(bool_1)
        str_0 = ''
        var_1 = rough_parser_0.set_str(str_0)
        var_2 = rough_parser_0.get_num_lines_in_stmt()
    except BaseException:
        pass

def test_case_17():
    try:
        bool_0 = True
        rough_parser_0 = module_0.RoughParser(bool_0, bool_0)
        bool_1 = False
        var_0 = rough_parser_0.set_lo(bool_1)
        str_0 = ''
        var_1 = rough_parser_0.set_str(str_0)
        var_2 = rough_parser_0.is_block_opener()
        var_3 = rough_parser_0.compute_backslash_indent()
    except BaseException:
        pass

def test_case_18():
    try:
        bool_0 = True
        list_0 = [bool_0, bool_0, bool_0]
        rough_parser_0 = module_0.RoughParser(bool_0, list_0)
        bool_1 = False
        var_0 = rough_parser_0.set_lo(bool_1)
        dict_0 = {}
        var_1 = rough_parser_0.set_str(dict_0)
        str_0 = ''
        var_2 = rough_parser_0.set_str(str_0)
        var_3 = rough_parser_0.get_continuation_type()
        var_4 = rough_parser_0.get_last_stmt_bracketing()
        var_5 = rough_parser_0.compute_bracket_indent()
    except BaseException:
        pass