# Automatically generated by Pynguin.
import thonny.roughparse as module_0

def test_case_0():
    try:
        bool_0 = False
        float_0 = 0.009
        rough_parser_0 = module_0.RoughParser(bool_0, float_0)
        var_0 = rough_parser_0.set_lo(bool_0)
        var_1 = rough_parser_0.compute_backslash_indent()
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = 'S);/5# 0;0\n'
        dict_0 = {}
        bytes_0 = b';y'
        rough_parser_0 = module_0.RoughParser(dict_0, bytes_0)
        var_0 = rough_parser_0.set_str(str_0)
        var_1 = rough_parser_0.find_good_parse_start(str_0)
        var_2 = rough_parser_0.get_base_indent_string()
        var_3 = rough_parser_0.get_last_open_bracket_pos()
        var_4 = rough_parser_0.is_block_closer()
        str_1 = 'k^_y'
        set_0 = set()
        rough_parser_1 = module_0.RoughParser(str_1, set_0)
        var_5 = rough_parser_0.compute_backslash_indent()
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = 'S);/#0;0\n'
        dict_0 = {}
        bytes_0 = b';y'
        rough_parser_0 = module_0.RoughParser(dict_0, bytes_0)
        var_0 = rough_parser_0.set_str(str_0)
        var_1 = rough_parser_0.get_last_open_bracket_pos()
        var_2 = rough_parser_0.compute_backslash_indent()
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = 'S);#0;0\n'
        dict_0 = {}
        bytes_0 = b';y'
        rough_parser_0 = module_0.RoughParser(dict_0, bytes_0)
        var_0 = rough_parser_0.set_str(str_0)
        var_1 = rough_parser_0.find_good_parse_start(str_0)
        var_2 = rough_parser_0.get_last_stmt_bracketing()
        var_3 = rough_parser_0.compute_backslash_indent()
    except BaseException:
        pass

def test_case_4():
    try:
        int_0 = 74
        dict_0 = {int_0: int_0}
        hyper_parser_0 = module_0.HyperParser(int_0, dict_0)
    except BaseException:
        pass

def test_case_5():
    try:
        str_0 = 'S$;#0;0\n'
        dict_0 = {}
        bytes_0 = b';y'
        rough_parser_0 = module_0.RoughParser(dict_0, bytes_0)
        var_0 = rough_parser_0.set_str(str_0)
        var_1 = rough_parser_0.find_good_parse_start(str_0)
        var_2 = rough_parser_0.get_base_indent_string()
        var_3 = rough_parser_0.get_last_open_bracket_pos()
        hyper_parser_0 = module_0.HyperParser(rough_parser_0, bytes_0)
    except BaseException:
        pass

def test_case_6():
    try:
        str_0 = '\n'
        dict_0 = {}
        bytes_0 = b'\xfd;\xa2\xfa\xd3\x13\t\xf7\x8b\x8f\xf2'
        rough_parser_0 = module_0.RoughParser(dict_0, bytes_0)
        var_0 = rough_parser_0.set_str(str_0)
        var_1 = rough_parser_0.compute_backslash_indent()
    except BaseException:
        pass

def test_case_7():
    try:
        bool_0 = True
        float_0 = 0.009
        rough_parser_0 = module_0.RoughParser(bool_0, float_0)
        var_0 = rough_parser_0.set_lo(bool_0)
    except BaseException:
        pass

def test_case_8():
    try:
        str_0 = 'S);/5\\ 0f0\n'
        dict_0 = {}
        bytes_0 = b'\xf5\xc26\x0b\xd5E'
        rough_parser_0 = module_0.RoughParser(dict_0, bytes_0)
        var_0 = rough_parser_0.set_str(str_0)
        var_1 = rough_parser_0.get_continuation_type()
        var_2 = rough_parser_0.compute_backslash_indent()
    except BaseException:
        pass

def test_case_9():
    try:
        str_0 = 'S);/\\ f\n'
        dict_0 = {}
        bytes_0 = b'{\xe9'
        rough_parser_0 = module_0.RoughParser(dict_0, bytes_0)
        var_0 = rough_parser_0.set_str(str_0)
        var_1 = rough_parser_0.compute_bracket_indent()
    except BaseException:
        pass

def test_case_10():
    try:
        str_0 = 'S);5 0;f0\n'
        dict_0 = {}
        bytes_0 = b'{\xe9'
        rough_parser_0 = module_0.RoughParser(dict_0, bytes_0)
        var_0 = rough_parser_0.set_str(str_0)
        var_1 = rough_parser_0.get_num_lines_in_stmt()
        var_2 = rough_parser_0.get_last_open_bracket_pos()
        var_3 = rough_parser_0.compute_backslash_indent()
    except BaseException:
        pass

def test_case_11():
    try:
        bool_0 = False
        bool_1 = False
        float_0 = 0.009
        rough_parser_0 = module_0.RoughParser(bool_1, float_0)
        var_0 = rough_parser_0.set_lo(bool_0)
        var_1 = rough_parser_0.is_block_opener()
    except BaseException:
        pass

def test_case_12():
    try:
        bytes_0 = b'\x15\xfd\xb8\x87.\x04\xe2\xcc~\x93\x88m\xf1\xd60\xf8\xa4v\x05'
        dict_0 = {bytes_0: bytes_0, bytes_0: bytes_0}
        string_translate_pseudo_mapping_0 = module_0.StringTranslatePseudoMapping(dict_0, bytes_0)
        string_translate_pseudo_mapping_1 = module_0.StringTranslatePseudoMapping(string_translate_pseudo_mapping_0, bytes_0)
        var_0 = string_translate_pseudo_mapping_1.__len__()
        float_0 = 4569.008
        hyper_parser_0 = module_0.HyperParser(float_0, bytes_0)
    except BaseException:
        pass

def test_case_13():
    try:
        str_0 = '8S?3>lcOe\\45z(mYM='
        bool_0 = True
        tuple_0 = (bool_0,)
        set_0 = {tuple_0, bool_0, str_0, bool_0}
        rough_parser_0 = module_0.RoughParser(set_0, bool_0)
        var_0 = rough_parser_0.set_str(str_0)
    except BaseException:
        pass

def test_case_14():
    try:
        str_0 = ''
        dict_0 = {}
        bytes_0 = b'\xceX\xc6\xe1Y\xe7\x1dL\xe9\x96"e\xae\x92\x99\xb0\xce_\xd4d'
        rough_parser_0 = module_0.RoughParser(dict_0, bytes_0)
        var_0 = rough_parser_0.set_str(str_0)
        var_1 = rough_parser_0.compute_backslash_indent()
    except BaseException:
        pass

def test_case_15():
    try:
        str_0 = 'S);/5# 0;f0\n'
        dict_0 = {}
        bytes_0 = b'{\xe9'
        rough_parser_0 = module_0.RoughParser(dict_0, bytes_0)
        var_0 = rough_parser_0.set_str(str_0)
        var_1 = rough_parser_0.find_good_parse_start()
        var_2 = rough_parser_0.compute_backslash_indent()
    except BaseException:
        pass

def test_case_16():
    try:
        str_0 = '\n'
        dict_0 = {str_0: str_0}
        bytes_0 = b'\xfd;\xa2\xfa\xd3\x13\t\xf7\x8b\x8f\xf2'
        rough_parser_0 = module_0.RoughParser(dict_0, bytes_0)
        bool_0 = True
        rough_parser_1 = module_0.RoughParser(str_0, bool_0)
        var_0 = rough_parser_0.set_str(str_0)
        var_1 = rough_parser_0.find_good_parse_start(rough_parser_0)
        var_2 = rough_parser_0.set_lo(bool_0)
        var_3 = rough_parser_0.find_good_parse_start()
        var_4 = rough_parser_1.compute_backslash_indent()
    except BaseException:
        pass

def test_case_17():
    try:
        str_0 = 'S);/5\\ 0f0\n'
        dict_0 = {}
        bytes_0 = b'{\xe9'
        rough_parser_0 = module_0.RoughParser(dict_0, bytes_0)
        var_0 = rough_parser_0.set_str(str_0)
        var_1 = rough_parser_0.compute_backslash_indent()
    except BaseException:
        pass

def test_case_18():
    try:
        str_0 = 'S)t/\\ f\n'
        dict_0 = {}
        bytes_0 = b'>\xe3\x96\x11\x88'
        rough_parser_0 = module_0.RoughParser(dict_0, bytes_0)
        var_0 = rough_parser_0.set_str(str_0)
        var_1 = rough_parser_0.is_block_opener()
        var_2 = rough_parser_0.get_base_indent_string()
        var_3 = rough_parser_0.get_last_open_bracket_pos()
        var_4 = rough_parser_0.compute_bracket_indent()
    except BaseException:
        pass

def test_case_19():
    try:
        str_0 = '\n'
        dict_0 = {}
        bytes_0 = b'\xfd;\xa2-\x1d\xfa\xd3\x13\t\xf7\xb6\x8f\xf2'
        rough_parser_0 = module_0.RoughParser(dict_0, bytes_0)
        var_0 = rough_parser_0.set_str(str_0)
        var_1 = rough_parser_0.get_base_indent_string()
        var_2 = rough_parser_0.compute_backslash_indent()
    except BaseException:
        pass

def test_case_20():
    try:
        str_0 = '\n'
        dict_0 = {}
        float_0 = -652.4142
        string_translate_pseudo_mapping_0 = module_0.StringTranslatePseudoMapping(dict_0, float_0)
        var_0 = string_translate_pseudo_mapping_0.__iter__()
        bytes_0 = b'\xfd;\xa2\xfa\xd3\x13\t\xf7\x8b\x8f\xf2'
        rough_parser_0 = module_0.RoughParser(dict_0, bytes_0)
        var_1 = rough_parser_0.set_str(str_0)
        var_2 = rough_parser_0.compute_backslash_indent()
    except BaseException:
        pass

def test_case_21():
    try:
        str_0 = 'S);#0;0\n'
        dict_0 = {}
        bytes_0 = b'\x88\x94'
        rough_parser_0 = module_0.RoughParser(dict_0, bytes_0)
        var_0 = rough_parser_0.set_str(str_0)
        var_1 = rough_parser_0.compute_backslash_indent()
    except BaseException:
        pass

def test_case_22():
    try:
        str_0 = 'S)#04t\n'
        dict_0 = {}
        bytes_0 = b'\x88\xd7'
        rough_parser_0 = module_0.RoughParser(dict_0, bytes_0)
        var_0 = rough_parser_0.set_str(str_0)
        var_1 = rough_parser_0.compute_backslash_indent()
    except BaseException:
        pass

def test_case_23():
    try:
        str_0 = 'S)t/z"f\n'
        bytes_0 = b'7>\xe3\x96\x11\x88'
        rough_parser_0 = module_0.RoughParser(bytes_0, bytes_0)
        var_0 = rough_parser_0.set_str(str_0)
        var_1 = rough_parser_0.get_base_indent_string()
        var_2 = rough_parser_0.get_base_indent_string()
        var_3 = rough_parser_0.find_good_parse_start()
        var_4 = rough_parser_0.compute_backslash_indent()
    except BaseException:
        pass