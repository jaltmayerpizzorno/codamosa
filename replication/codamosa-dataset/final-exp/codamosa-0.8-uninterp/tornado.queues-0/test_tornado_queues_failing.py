# Automatically generated by Pynguin.
import tornado.queues as module_0

def test_case_0():
    try:
        float_0 = -2172.0
        queue_iterator_0 = module_0._QueueIterator(float_0)
        awaitable_0 = queue_iterator_0.__anext__()
    except BaseException:
        pass

def test_case_1():
    try:
        int_0 = None
        queue_0 = module_0.Queue()
        var_0 = queue_0.__aiter__()
        priority_queue_0 = module_0.PriorityQueue(int_0)
    except BaseException:
        pass

def test_case_2():
    try:
        queue_0 = module_0.Queue()
        int_0 = -1324
        queue_1 = module_0.Queue(int_0)
    except BaseException:
        pass

def test_case_3():
    try:
        lifo_queue_0 = module_0.LifoQueue()
        queue_0 = module_0.Queue()
        var_0 = None
        queue_0.put_nowait(var_0)
        bool_0 = queue_0.empty()
        queue_0.task_done()
        queue_0.task_done()
    except BaseException:
        pass

def test_case_4():
    try:
        queue_0 = module_0.Queue()
        awaitable_0 = queue_0.get()
    except BaseException:
        pass

def test_case_5():
    try:
        queue_0 = module_0.Queue()
        var_0 = queue_0.get_nowait()
    except BaseException:
        pass

def test_case_6():
    try:
        int_0 = 771
        queue_0 = module_0.Queue(int_0)
        str_0 = queue_0.__str__()
        queue_0.task_done()
    except BaseException:
        pass

def test_case_7():
    try:
        queue_0 = module_0.Queue()
        awaitable_0 = queue_0.join()
    except BaseException:
        pass

def test_case_8():
    try:
        var_0 = None
        queue_0 = module_0.Queue()
        queue_0.put_nowait(var_0)
        queue_1 = module_0.Queue()
        bool_0 = queue_1.full()
        str_0 = queue_1.__repr__()
        future_0 = queue_0.put(var_0)
    except BaseException:
        pass

def test_case_9():
    try:
        var_0 = None
        queue_0 = module_0.Queue()
        queue_0.put_nowait(var_0)
        int_0 = 1477
        queue_1 = module_0.Queue()
        queue_2 = module_0.Queue(int_0)
        bool_0 = queue_1.full()
        str_0 = queue_0.__repr__()
        queue_3 = module_0.Queue()
        lifo_queue_0 = module_0.LifoQueue()
        queue_4 = module_0.Queue()
        queue_5 = module_0.Queue()
        int_1 = queue_5.qsize()
        float_0 = -4046.945
        awaitable_0 = queue_3.join(float_0)
    except BaseException:
        pass

def test_case_10():
    try:
        lifo_queue_0 = module_0.LifoQueue()
        queue_0 = module_0.Queue()
        var_0 = None
        queue_0.put_nowait(var_0)
        queue_0.task_done()
        queue_0.task_done()
    except BaseException:
        pass

def test_case_11():
    try:
        var_0 = None
        queue_0 = module_0.Queue()
        queue_0.put_nowait(var_0)
        var_1 = queue_0.get_nowait()
        queue_1 = module_0.Queue()
        str_0 = queue_1.__repr__()
        queue_0.put_nowait(var_1)
        queue_full_0 = module_0.QueueFull()
        str_1 = queue_1.__repr__()
        queue_0.task_done()
        lifo_queue_0 = module_0.LifoQueue()
        queue_2 = module_0.Queue()
        int_0 = queue_0.qsize()
        var_2 = queue_0.get_nowait()
        queue_3 = module_0.Queue()
        lifo_queue_1 = module_0.LifoQueue()
        list_0 = [queue_1]
        dict_0 = {str_1: queue_0}
        queue_empty_0 = module_0.QueueEmpty(*list_0, **dict_0)
    except BaseException:
        pass

def test_case_12():
    try:
        int_0 = 2
        queue_0 = module_0.Queue(int_0)
        int_1 = 10
        queue_0.put_nowait(int_1)
        int_2 = 20
        queue_0.put_nowait(int_2)
        bool_0 = queue_0.full()
        int_3 = 57
        bool_1 = queue_0.full()
        queue_0.put_nowait(int_3)
    except BaseException:
        pass