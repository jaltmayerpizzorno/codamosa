# Automatically generated by Pynguin.
import tqdm.contrib.utils_worker as module_0

def test_case_0():
    pass

def test_case_1():
    mono_worker_0 = module_0.MonoWorker()

def test_case_2():
    mono_worker_0 = module_0.MonoWorker()
    bytes_0 = b'\x82s~[\x04XO\xfa\xdbYI\xb9\xe0\x15\xf8\xca'
    var_0 = mono_worker_0.submit(mono_worker_0)
    var_1 = mono_worker_0.submit(mono_worker_0)
    var_2 = mono_worker_0.submit(bytes_0)
    var_3 = mono_worker_0.submit(mono_worker_0)

def test_case_3():
    mono_worker_0 = module_0.MonoWorker()
    int_0 = -1909
    var_0 = mono_worker_0.submit(int_0)
    mono_worker_1 = module_0.MonoWorker()