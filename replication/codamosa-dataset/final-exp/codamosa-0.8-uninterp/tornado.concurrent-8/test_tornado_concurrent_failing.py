# Automatically generated by Pynguin.
import tornado.concurrent as module_0
import builtins as module_1
import concurrent.futures._base as module_2

def test_case_0():
    try:
        return_value_ignored_error_0 = module_0.ReturnValueIgnoredError()
        list_0 = [return_value_ignored_error_0]
        dict_0 = {}
        callable_0 = module_0.run_on_executor(*list_0, **dict_0)
        dummy_executor_0 = module_0.DummyExecutor()
        future_0 = dummy_executor_0.submit(callable_0, *list_0, **dict_0)
        base_exception_0 = module_1.BaseException()
        module_0.future_set_exception_unless_cancelled(future_0, base_exception_0)
    except BaseException:
        pass

def test_case_1():
    try:
        callable_0 = module_0.run_on_executor()
        future_0 = None
        str_0 = 'Set-Cookie'
        module_0.future_set_result_unless_cancelled(future_0, str_0)
    except BaseException:
        pass

def test_case_2():
    try:
        future_0 = None
        module_0.chain_future(future_0, future_0)
    except BaseException:
        pass

def test_case_3():
    try:
        future_0 = module_2.Future()
        callable_0 = module_0.run_on_executor()
        dummy_executor_0 = module_0.DummyExecutor()
        future_1 = None
        module_0.future_add_done_callback(future_0, future_1)
        module_0.chain_future(future_1, future_1)
    except BaseException:
        pass

def test_case_4():
    try:
        future_0 = module_2.Future()
        callable_0 = module_0.run_on_executor()
        module_0.future_set_result_unless_cancelled(future_0, callable_0)
        str_0 = "RVfw'hVmu{]8."
        dummy_executor_0 = module_0.DummyExecutor()
        future_1 = dummy_executor_0.submit(str_0)
        base_exception_0 = module_1.BaseException()
        module_0.future_add_done_callback(future_1, base_exception_0)
    except BaseException:
        pass

def test_case_5():
    try:
        return_value_ignored_error_0 = module_0.ReturnValueIgnoredError()
        callable_0 = module_0.run_on_executor()
        future_0 = module_2.Future()
        base_exception_0 = module_1.BaseException()
        list_0 = [return_value_ignored_error_0, future_0]
        dict_0 = {}
        callable_1 = module_0.run_on_executor(*list_0, **dict_0)
    except BaseException:
        pass

def test_case_6():
    try:
        str_0 = 'Implement this method to handle streamed request data.\n\n        Requires the `.stream_request_body` decorator.\n\n        May be a coroutine for flow control.\n        '
        bytes_0 = b'\x85\xdb\xc58\xfc^=|[j\xc8\xbe\xff\x91\xc2'
        dict_0 = {str_0: bytes_0}
        future_0 = module_2.Future()
        callable_0 = module_0.run_on_executor()
        module_0.future_set_result_unless_cancelled(future_0, callable_0)
        str_1 = "RVfw'hVmu{]8."
        dummy_executor_0 = module_0.DummyExecutor()
        future_1 = dummy_executor_0.submit(str_1)
        list_0 = [str_1, dummy_executor_0]
        callable_1 = module_0.run_on_executor(*list_0, **dict_0)
    except BaseException:
        pass

def test_case_7():
    try:
        future_0 = module_2.Future()
        none_type_0 = None
        list_0 = []
        dummy_executor_0 = module_0.DummyExecutor(*list_0)
        future_1 = module_2.Future()
        callable_0 = module_0.run_on_executor()
        future_2 = dummy_executor_0.submit(list_0)
        return_value_ignored_error_0 = module_0.ReturnValueIgnoredError()
        dummy_executor_1 = module_0.DummyExecutor()
        future_3 = dummy_executor_1.submit(future_0, *list_0)
        dummy_executor_2 = module_0.DummyExecutor()
        future_4 = None
        module_0.future_add_done_callback(future_1, future_4)
        tuple_0 = (future_0, none_type_0, return_value_ignored_error_0)
        dummy_executor_3 = module_0.DummyExecutor()
        base_exception_0 = module_1.BaseException(*list_0)
        module_0.future_set_exc_info(future_3, tuple_0)
    except BaseException:
        pass