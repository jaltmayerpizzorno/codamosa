# Automatically generated by Pynguin.
import tornado.queues as module_0

def test_case_0():
    try:
        int_0 = 50
        queue_0 = module_0.Queue()
        var_0 = queue_0.__aiter__()
        queue_1 = module_0.Queue(int_0)
        str_0 = queue_1.__str__()
        queue_2 = module_0.Queue()
        awaitable_0 = queue_2.join()
    except BaseException:
        pass

def test_case_1():
    try:
        queue_0 = module_0.Queue()
        lifo_queue_0 = module_0.LifoQueue()
        queue_iterator_0 = module_0._QueueIterator(lifo_queue_0)
        awaitable_0 = queue_iterator_0.__anext__()
    except BaseException:
        pass

def test_case_2():
    try:
        int_0 = 2682
        queue_0 = module_0.Queue(int_0)
        str_0 = queue_0.__str__()
        int_1 = -1395
        queue_1 = module_0.Queue(int_1)
    except BaseException:
        pass

def test_case_3():
    try:
        queue_0 = module_0.Queue()
        var_0 = queue_0.get_nowait()
    except BaseException:
        pass

def test_case_4():
    try:
        queue_0 = module_0.Queue()
        queue_0.task_done()
    except BaseException:
        pass

def test_case_5():
    try:
        queue_0 = module_0.Queue()
        lifo_queue_0 = module_0.LifoQueue()
        var_0 = queue_0.get_nowait()
    except BaseException:
        pass

def test_case_6():
    try:
        int_0 = None
        queue_0 = module_0.Queue(int_0)
    except BaseException:
        pass

def test_case_7():
    try:
        queue_0 = module_0.Queue()
        var_0 = queue_0.__aiter__()
        bool_0 = queue_0.full()
        priority_queue_0 = module_0.PriorityQueue()
        str_0 = queue_0.__str__()
        int_0 = queue_0.qsize()
        int_1 = 161
        bool_1 = queue_0.full()
        queue_1 = module_0.Queue()
        queue_2 = module_0.Queue()
        queue_3 = module_0.Queue()
        str_1 = queue_2.__repr__()
        var_1 = None
        queue_0.put_nowait(var_1)
        var_2 = queue_2.__aiter__()
        future_0 = queue_0.put(var_1, int_1)
    except BaseException:
        pass

def test_case_8():
    try:
        priority_queue_0 = module_0.PriorityQueue()
        int_0 = 161
        queue_0 = module_0.Queue()
        str_0 = queue_0.__repr__()
        var_0 = None
        queue_0.put_nowait(var_0)
        var_1 = queue_0.__aiter__()
        var_2 = None
        queue_0.put_nowait(var_2)
        var_3 = queue_0.__aiter__()
        queue_0.task_done()
        queue_1 = module_0.Queue()
        var_4 = queue_0.get_nowait()
        queue_2 = module_0.Queue(int_0)
        var_5 = queue_2.get_nowait()
    except BaseException:
        pass

def test_case_9():
    try:
        int_0 = 2
        queue_0 = module_0.Queue(int_0)
        int_1 = 1
        queue_0.put_nowait(int_1)
        queue_0.put_nowait(int_0)
        queue_0.put_nowait(int_1)
    except BaseException:
        pass