# Automatically generated by Pynguin.
import tornado.concurrent as module_0
import builtins as module_1
import concurrent.futures._base as module_2

def test_case_0():
    pass

def test_case_1():
    float_0 = -3521.20621
    dummy_executor_0 = module_0.DummyExecutor()
    future_0 = dummy_executor_0.submit(float_0)
    bool_0 = module_0.is_future(dummy_executor_0)
    dummy_executor_1 = module_0.DummyExecutor()

def test_case_2():
    callable_0 = None
    dummy_executor_0 = module_0.DummyExecutor()
    future_0 = dummy_executor_0.submit(callable_0)

def test_case_3():
    bool_0 = True
    dummy_executor_0 = module_0.DummyExecutor()
    dummy_executor_0.shutdown(bool_0)

def test_case_4():
    str_0 = 'Gz(^@*8[n\x0cK+I'
    list_0 = [str_0]
    callable_0 = module_0.run_on_executor(*list_0)
    base_exception_0 = module_1.BaseException()

def test_case_5():
    callable_0 = module_0.run_on_executor()

def test_case_6():
    future_0 = module_2.Future()
    float_0 = -4941.25565
    module_0.future_set_result_unless_cancelled(future_0, float_0)