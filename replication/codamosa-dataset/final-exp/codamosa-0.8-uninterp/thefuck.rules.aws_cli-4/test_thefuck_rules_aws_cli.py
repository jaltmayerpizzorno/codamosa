# Automatically generated by Pynguin.
import thefuck.rules.aws_cli as module_0

def test_case_0():
    pass

def test_case_1():
    str_0 = 'Command'
    var_0 = ()
    str_1 = 'output'
    str_2 = 'script'
    str_3 = "usage: aws [options] <command> <subcommand> [<subcommand> ...] [parameters]\nTo see help text, you can run:\n  $ aws help\n  $ aws <command> help\n  $ aws <command> <subcommand> help\naws: error: argument subcommand: Invalid choice: 's3api', maybe you meant: \n* s3\n\nInvalid choice: 's3api', maybe you meant: \n* s3"
    str_4 = 'aws s3api'
    str_5 = {str_1: str_3, str_2: str_4}
    var_1 = type(str_0, var_0, str_5)
    var_2 = module_0.get_new_command(var_1)