import multiprocessing
import hazelcast
import time

KEYS_N = 1000


def racy_process(pid):
    hz = hazelcast.HazelcastClient(cluster_name="hz-cluster")
    map = hz.get_map("distributed-map-with-locks").blocking()

    start = time.time()

    key = "1"
    print("Starting racy process")
    for k in range(KEYS_N):
        if k % 250 == 0:
            print(f"pid {pid}. k: {k}")
        value = map.get(key)
        # time.sleep(1)
        value += 1
        map.put(key, value)

    print(f"Finished! Result = {map.get(key)}. Time: {int(time.time() - start)}")

    hz.shutdown()


def optimistic_locking(pid):
    hz = hazelcast.HazelcastClient(cluster_name="hz-cluster")
    map = hz.get_map("distributed-map-with-locks").blocking()

    start = time.time()

    key = "1"
    print("Starting optimistic locking")
    for k in range(KEYS_N):
        if k % 250 == 0:
            print(f"pid {pid}. k: {k}")

        while True:
            value = map.get(key)
            # time.sleep(1)
            new_value = value + 1
            if map.replace_if_same(key, value, new_value):
                break

    print(f"Finished! Result = {map.get(key)}. Time: {int(time.time() - start)}")

    hz.shutdown()


def pessimistic_locking(pid):
    hz = hazelcast.HazelcastClient(cluster_name="hz-cluster")
    map = hz.get_map("distributed-map-with-locks").blocking()

    start = time.time()

    key = "1"
    print("Starting pessimistic locking")
    for k in range(KEYS_N):
        map.lock(key)  # LOCK here
        try:
            value = map.get(key)
            # time.sleep(1)
            value += 1
            map.put(key, value)
        finally:
            map.unlock(key)

    print(f"Finished! Result = {map.get(key)}. Time: {int(time.time() - start)}")

    hz.shutdown()


def create_map():
    """
    Creates a map and inserts first value.
    """
    hz = hazelcast.HazelcastClient(cluster_name="hz-cluster")
    map = hz.get_map("distributed-map-with-locks").blocking()

    key = "1"
    map.put(key, 0)
    hz.shutdown()


if __name__ == "__main__":
    create_map()
    proc_nos = [1, 2, 3]
    proc_lst = []

    for no in proc_nos:
        p = multiprocessing.Process(target=racy_process, args=(no,))
        proc_lst.append(p)
        p.start()

    for proc in proc_lst:
        proc.join()
