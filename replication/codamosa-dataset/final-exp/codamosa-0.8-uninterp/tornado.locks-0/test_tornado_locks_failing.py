# Automatically generated by Pynguin.
import tornado.locks as module_0
import builtins as module_1
import datetime as module_2

def test_case_0():
    try:
        condition_0 = module_0.Condition()
    except BaseException:
        pass

def test_case_1():
    try:
        event_0 = module_0.Event()
        event_1 = module_0.Event()
        str_0 = event_0.__repr__()
        event_0.set()
        event_2 = module_0.Event()
        event_1.set()
        semaphore_0 = module_0.Semaphore()
        semaphore_0.release()
        bounded_semaphore_0 = module_0.BoundedSemaphore()
        bounded_semaphore_0.release()
    except BaseException:
        pass

def test_case_2():
    try:
        event_0 = module_0.Event()
        event_0.clear()
        event_0.clear()
        bool_0 = event_0.is_set()
        int_0 = -1467
        awaitable_0 = event_0.wait(int_0)
    except BaseException:
        pass

def test_case_3():
    try:
        event_0 = module_0.Event()
        awaitable_0 = event_0.wait()
    except BaseException:
        pass

def test_case_4():
    try:
        timeout_garbage_collector_0 = module_0._TimeoutGarbageCollector()
        releasing_context_manager_0 = module_0._ReleasingContextManager(timeout_garbage_collector_0)
        releasing_context_manager_0.__enter__()
        lock_0 = module_0.Lock()
        lock_0.release()
    except BaseException:
        pass

def test_case_5():
    try:
        int_0 = 1338
        releasing_context_manager_0 = module_0._ReleasingContextManager(int_0)
        releasing_context_manager_0.__enter__()
        releasing_context_manager_1 = module_0._ReleasingContextManager(releasing_context_manager_0)
        event_0 = module_0.Event()
        list_0 = [releasing_context_manager_0, event_0, int_0]
        base_exception_0 = module_1.BaseException(*list_0)
        traceback_0 = None
        releasing_context_manager_1.__exit__(event_0, base_exception_0, traceback_0)
    except BaseException:
        pass

def test_case_6():
    try:
        int_0 = -549
        semaphore_0 = module_0.Semaphore(int_0)
    except BaseException:
        pass

def test_case_7():
    try:
        semaphore_0 = module_0.Semaphore()
        awaitable_0 = semaphore_0.acquire()
    except BaseException:
        pass

def test_case_8():
    try:
        event_0 = module_0.Event()
        semaphore_0 = module_0.Semaphore()
        str_0 = semaphore_0.__repr__()
        semaphore_0.__enter__()
    except BaseException:
        pass

def test_case_9():
    try:
        bounded_semaphore_0 = module_0.BoundedSemaphore()
        bounded_semaphore_0.release()
    except BaseException:
        pass

def test_case_10():
    try:
        timedelta_0 = module_2.timedelta()
        lock_0 = module_0.Lock()
        str_0 = lock_0.__repr__()
        semaphore_0 = module_0.Semaphore()
        semaphore_0.release()
        awaitable_0 = lock_0.acquire(timedelta_0)
    except BaseException:
        pass

def test_case_11():
    try:
        lock_0 = module_0.Lock()
        lock_0.release()
    except BaseException:
        pass

def test_case_12():
    try:
        timeout_garbage_collector_0 = module_0._TimeoutGarbageCollector()
        lock_0 = module_0.Lock()
        none_type_0 = None
        none_type_1 = None
        list_0 = [timeout_garbage_collector_0, timeout_garbage_collector_0, timeout_garbage_collector_0]
        lock_0.__exit__(none_type_0, none_type_1, list_0)
    except BaseException:
        pass

def test_case_13():
    try:
        event_0 = module_0.Event()
        event_0.set()
        str_0 = event_0.__repr__()
        semaphore_0 = module_0.Semaphore()
        str_1 = semaphore_0.__repr__()
        event_0.set()
        event_0.set()
        semaphore_1 = module_0.Semaphore()
        semaphore_2 = module_0.Semaphore()
        semaphore_2.release()
        bounded_semaphore_0 = module_0.BoundedSemaphore()
        bounded_semaphore_0.release()
    except BaseException:
        pass

def test_case_14():
    try:
        type_0 = None
        base_exception_0 = module_1.BaseException()
        optional_0 = None
        semaphore_0 = module_0.Semaphore()
        semaphore_0.__exit__(type_0, base_exception_0, optional_0)
    except BaseException:
        pass

def test_case_15():
    try:
        event_0 = module_0.Event()
        event_0.set()
        event_1 = module_0.Event()
        event_0.set()
        event_1.clear()
        event_2 = module_0.Event()
        str_0 = event_1.__repr__()
        lock_0 = module_0.Lock()
        str_1 = lock_0.__repr__()
        bounded_semaphore_0 = module_0.BoundedSemaphore()
        timeout_garbage_collector_0 = module_0._TimeoutGarbageCollector()
        bool_0 = event_1.is_set()
        bounded_semaphore_0.release()
    except BaseException:
        pass

def test_case_16():
    try:
        event_0 = module_0.Event()
        event_0.set()
        event_1 = module_0.Event()
        event_0.clear()
        event_2 = module_0.Event()
        lock_0 = module_0.Lock()
        lock_1 = module_0.Lock()
        str_0 = lock_1.__repr__()
        int_0 = 3866
        semaphore_0 = module_0.Semaphore(int_0)
        semaphore_0.release()
        int_1 = 0
        semaphore_1 = module_0.Semaphore(int_1)
        str_1 = semaphore_1.__repr__()
        lock_1.release()
    except BaseException:
        pass