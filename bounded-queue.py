import multiprocessing
import hazelcast
import time

no_items = 100

def producer():
    print('Started producer')
    hz = hazelcast.HazelcastClient(cluster_name="hz-cluster")
    queue = hz.get_queue("queue-6").blocking()
    start = time.time()

    for i in range(no_items):
        queue.put(f"val {i}")
        print(f"Added val {i}. Time from start: {round(time.time() - start, 3)}")

    print(f'All items added. Time from start: {round(time.time() - start, 3)}')


def consumer():
    print('Started consumer')
    hz = hazelcast.HazelcastClient(cluster_name="hz-cluster")
    queue = hz.get_queue("queue-6").blocking()

    start = time.time()

    while True:
        item = queue.take()
        print(f"Consuming {item}. Time from start: {round(time.time() - start, 3)}")


if __name__ == "__main__":
    proc_nos = [1, 2, 3]
    proc_lst = []

    for no in proc_nos:
        if no == 1:
            p = multiprocessing.Process(target=producer)
        else:
            p = multiprocessing.Process(target=consumer)
        proc_lst.append(p)
        p.start()

    for proc in proc_lst:
        proc.join()
