# Automatically generated by Pynguin.
import tqdm.contrib.utils_worker as module_0

def test_case_0():
    pass

def test_case_1():
    mono_worker_0 = module_0.MonoWorker()

def test_case_2():
    mono_worker_0 = module_0.MonoWorker()
    var_0 = mono_worker_0.submit(mono_worker_0)
    dict_0 = {}
    var_1 = mono_worker_0.submit(mono_worker_0, **dict_0)
    var_2 = mono_worker_0.submit(var_1, **dict_0)
    var_3 = mono_worker_0.submit(dict_0)

def test_case_3():
    float_0 = 1339.967
    mono_worker_0 = module_0.MonoWorker()
    var_0 = mono_worker_0.submit(float_0)