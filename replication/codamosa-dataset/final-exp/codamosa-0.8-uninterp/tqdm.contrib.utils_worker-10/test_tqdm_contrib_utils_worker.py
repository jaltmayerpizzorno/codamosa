# Automatically generated by Pynguin.
import tqdm.contrib.utils_worker as module_0

def test_case_0():
    pass

def test_case_1():
    mono_worker_0 = module_0.MonoWorker()

def test_case_2():
    set_0 = None
    mono_worker_0 = module_0.MonoWorker()
    var_0 = mono_worker_0.submit(set_0)
    var_1 = mono_worker_0.submit(set_0)
    var_2 = mono_worker_0.submit(mono_worker_0)
    var_3 = mono_worker_0.submit(mono_worker_0)

def test_case_3():
    bytes_0 = b'd\xed%p\xf5#\xabl>\xa3\xb53\xe2zdB\xd2\xf7\x81'
    mono_worker_0 = module_0.MonoWorker()
    var_0 = mono_worker_0.submit(bytes_0)