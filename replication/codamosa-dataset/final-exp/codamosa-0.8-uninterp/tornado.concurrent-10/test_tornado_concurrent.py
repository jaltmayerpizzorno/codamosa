# Automatically generated by Pynguin.
import tornado.concurrent as module_0
import concurrent.futures._base as module_1

def test_case_0():
    pass

def test_case_1():
    bool_0 = True
    bool_1 = module_0.is_future(bool_0)

def test_case_2():
    dummy_executor_0 = module_0.DummyExecutor()
    future_0 = dummy_executor_0.submit(dummy_executor_0)

def test_case_3():
    future_0 = module_1.Future()
    str_0 = 'fO&>$y9'
    module_0.future_set_result_unless_cancelled(future_0, str_0)
    dummy_executor_0 = module_0.DummyExecutor()
    dummy_executor_0.shutdown()
    dummy_executor_0.shutdown()

def test_case_4():
    callable_0 = module_0.run_on_executor()
    list_0 = [callable_0]
    callable_1 = module_0.run_on_executor(*list_0)
    dummy_executor_0 = module_0.DummyExecutor()

def test_case_5():
    callable_0 = module_0.run_on_executor()
    dummy_executor_0 = module_0.DummyExecutor()

def test_case_6():
    future_0 = module_1.Future()
    module_0.future_set_result_unless_cancelled(future_0, future_0)