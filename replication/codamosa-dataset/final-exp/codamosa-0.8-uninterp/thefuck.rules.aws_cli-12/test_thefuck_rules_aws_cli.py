# Automatically generated by Pynguin.
import thefuck.rules.aws_cli as module_0

def test_case_0():
    pass

def test_case_1():
    str_0 = 'Command'
    var_0 = ()
    str_1 = 'output'
    str_2 = 'script'
    str_3 = "usage: blah blah blah Invalid choice: 's3', maybe you meant:\n  * s3api\n  * ls"
    str_4 = 'aws s3 ls asdf'
    str_5 = {str_1: str_3, str_2: str_4}
    var_1 = type(str_0, var_0, str_5)
    var_2 = module_0.get_new_command(var_1)