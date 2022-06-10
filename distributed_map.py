import hazelcast
import string
import random

KEYS_N = 1000


def main():
    """
    1) Connect to standalone Hazelcast instance
    2) Using HZ API create distributed Map
    3) Insert 1000 keys
    """

    # Start the Hazelcast Client and connect to an already running Hazelcast
    # Cluster on 127.0.0.1 through Docker
    hz = hazelcast.HazelcastClient(cluster_name="hz-cluster")

    # Get the Distributed Map from Cluster.
    map = hz.get_map("my-distributed-map").blocking()

    # Insert items
    for i in range(KEYS_N):
        rand_val = ''.join(random.choices(string.ascii_uppercase +
                                          string.digits, k=10))
        map.put(i, rand_val)

    # Shutdown this Hazelcast Client
    hz.shutdown()


if __name__ == '__main__':
    main()
