# Automatically generated by Pynguin.
import tempfile as module_0
import cookiecutter.zipfile as module_1

def test_case_0():
    pass

def test_case_1():
    var_0 = module_0.mkdtemp()
    str_0 = 'https://github.com/audreyr/cookiecutter-pypackage/archive/master.zip'
    var_1 = module_1.unzip(str_0, str_0, var_0)