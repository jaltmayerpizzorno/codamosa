# Automatically generated by Pynguin.
import isort.exceptions as module_0
import builtins as module_1

def test_case_0():
    pass

def test_case_1():
    str_0 = '"xY?/,}^"z<'
    invalid_settings_path_0 = module_0.InvalidSettingsPath(str_0)

def test_case_2():
    str_0 = '\r\tEifTy'
    introduced_syntax_errors_0 = module_0.IntroducedSyntaxErrors(str_0)

def test_case_3():
    str_0 = 'l1xR3^EUw'
    file_skip_setting_0 = module_0.FileSkipSetting(str_0)

def test_case_4():
    str_0 = '1v@&kf'
    file_skip_comment_0 = module_0.FileSkipComment(str_0)

def test_case_5():
    str_0 = 'test'
    profile_does_not_exist_0 = module_0.ProfileDoesNotExist(str_0)

def test_case_6():
    str_0 = '<\x0b7o%Bd/8V7x@?J/'
    str_1 = '{?*|_9bwk21xSx.7'
    file_skipped_0 = module_0.FileSkipped(str_1, str_0)
    unsupported_encoding_0 = module_0.UnsupportedEncoding(str_1)
    formatting_plugin_does_not_exist_0 = module_0.FormattingPluginDoesNotExist(str_0)
    unsupported_encoding_1 = module_0.UnsupportedEncoding(str_1)
    unsupported_encoding_2 = module_0.UnsupportedEncoding(str_0)

def test_case_7():
    str_0 = '(G-&5#7WvEuHnE'
    str_1 = 'x<+y~uzC*uD)'
    str_2 = 'utf-8'
    file_skipped_0 = module_0.FileSkipped(str_1, str_2)
    exception_0 = module_1.Exception()
    literal_parsing_failure_0 = module_0.LiteralParsingFailure(str_0, exception_0)

def test_case_8():
    str_0 = 'Files that isort should skip over. If you want to skip multiple files you should specify twice: --skip file1 --skip file2. Values can be file names, directory names or file paths. To skip all files in a nested path use --skip-glob.'
    file_skipped_0 = module_0.FileSkipped(str_0, str_0)
    str_1 = '#U{Cs4;'
    assignments_format_mismatch_0 = module_0.AssignmentsFormatMismatch(str_1)

def test_case_9():
    str_0 = 'ab'
    str_1 = 'value'
    str_2 = 'source'
    int_0 = 1
    str_3 = 'h'
    var_0 = {str_1: int_0, str_2: str_3}
    var_1 = {str_0: var_0}
    unsupported_settings_0 = module_0.UnsupportedSettings(var_1)

def test_case_10():
    str_0 = '(~y2~YAo(v2\x0c3{\x0b=\t'
    unsupported_encoding_0 = module_0.UnsupportedEncoding(str_0)

def test_case_11():
    str_0 = 'WWEbd*Ev'
    missing_section_0 = module_0.MissingSection(str_0, str_0)