# Automatically generated by Pynguin.
import tornado.locks as module_0
import builtins as module_1

def test_case_0():
    try:
        condition_0 = module_0.Condition()
    except BaseException:
        pass

def test_case_1():
    try:
        event_0 = module_0.Event()
        bool_0 = event_0.is_set()
        lock_0 = module_0.Lock()
        event_0.clear()
        str_0 = event_0.__repr__()
        lock_0.release()
    except BaseException:
        pass

def test_case_2():
    try:
        list_0 = None
        none_type_0 = None
        lock_0 = None
        lock_1 = module_0.Lock()
        lock_1.__aexit__(list_0, none_type_0, lock_0)
        semaphore_0 = module_0.Semaphore()
        list_1 = []
        base_exception_0 = module_1.BaseException(*list_1)
        event_0 = module_0.Event()
        awaitable_0 = event_0.wait(lock_0)
    except BaseException:
        pass

def test_case_3():
    try:
        event_0 = module_0.Event()
        releasing_context_manager_0 = module_0._ReleasingContextManager(event_0)
        semaphore_0 = module_0.Semaphore()
        str_0 = semaphore_0.__repr__()
        traceback_0 = module_1.traceback()
    except BaseException:
        pass

def test_case_4():
    try:
        timeout_garbage_collector_0 = module_0._TimeoutGarbageCollector()
        releasing_context_manager_0 = module_0._ReleasingContextManager(timeout_garbage_collector_0)
        releasing_context_manager_0.__enter__()
        event_0 = module_0.Event()
        traceback_0 = module_1.traceback()
    except BaseException:
        pass

def test_case_5():
    try:
        int_0 = -806
        bounded_semaphore_0 = module_0.BoundedSemaphore(int_0)
    except BaseException:
        pass

def test_case_6():
    try:
        event_0 = module_0.Event()
        bool_0 = event_0.is_set()
        lock_0 = module_0.Lock()
        awaitable_0 = lock_0.acquire()
    except BaseException:
        pass

def test_case_7():
    try:
        semaphore_0 = module_0.Semaphore()
        str_0 = semaphore_0.__repr__()
        lock_0 = module_0.Lock()
        semaphore_0.__enter__()
    except BaseException:
        pass

def test_case_8():
    try:
        lock_0 = module_0.Lock()
        lock_0.release()
    except BaseException:
        pass

def test_case_9():
    try:
        semaphore_0 = module_0.Semaphore()
        semaphore_0.release()
        int_0 = -3974
        int_1 = 491
        releasing_context_manager_0 = module_0._ReleasingContextManager(int_0)
        releasing_context_manager_0.__enter__()
        semaphore_1 = module_0.Semaphore(int_1)
        event_0 = module_0.Event()
        lock_0 = module_0.Lock()
        base_exception_0 = module_1.BaseException()
        semaphore_1.__exit__(lock_0, base_exception_0, int_1)
    except BaseException:
        pass

def test_case_10():
    try:
        lock_0 = module_0.Lock()
        lock_0.__enter__()
    except BaseException:
        pass

def test_case_11():
    try:
        event_0 = module_0.Event()
        event_0.set()
        bool_0 = event_0.is_set()
        releasing_context_manager_0 = module_0._ReleasingContextManager(event_0)
        releasing_context_manager_0.__enter__()
        base_exception_0 = module_1.BaseException()
        none_type_0 = None
        lock_0 = module_0.Lock()
        lock_0.__exit__(base_exception_0, base_exception_0, none_type_0)
    except BaseException:
        pass

def test_case_12():
    try:
        semaphore_0 = module_0.Semaphore()
        event_0 = module_0.Event()
        str_0 = event_0.__repr__()
        str_1 = event_0.__repr__()
        str_2 = semaphore_0.__repr__()
        releasing_context_manager_0 = module_0._ReleasingContextManager(str_2)
        event_1 = module_0.Event()
        event_1.set()
        releasing_context_manager_0.__enter__()
        str_3 = event_1.__repr__()
        semaphore_0.release()
        lock_0 = module_0.Lock()
        lock_0.release()
    except BaseException:
        pass

def test_case_13():
    try:
        event_0 = module_0.Event()
        event_0.set()
        bool_0 = event_0.is_set()
        lock_0 = module_0.Lock()
        event_0.set()
        bool_1 = event_0.is_set()
        lock_1 = module_0.Lock()
        event_0.clear()
        str_0 = event_0.__repr__()
        lock_1.release()
    except BaseException:
        pass

def test_case_14():
    try:
        semaphore_0 = module_0.Semaphore()
        str_0 = semaphore_0.__repr__()
        str_1 = semaphore_0.__repr__()
        releasing_context_manager_0 = module_0._ReleasingContextManager(str_1)
        event_0 = module_0.Event()
        lock_0 = module_0.Lock()
        lock_1 = module_0.Lock()
        releasing_context_manager_1 = module_0._ReleasingContextManager(lock_1)
        dict_0 = {releasing_context_manager_1: semaphore_0, releasing_context_manager_0: str_1}
        none_type_0 = None
        releasing_context_manager_0.__exit__(lock_0, dict_0, none_type_0)
    except BaseException:
        pass