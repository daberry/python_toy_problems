# A hash table that utilizes chaining (linked lists) to handle collisions

class HashTable(object):
    def __init__(self, num_buckets=256):
        self.aMap = []
        for i in range(0, num_buckets):
            self.aMap.append([])
        return self.aMap

    def hash_key(self, key):
        return hash(key) % len(self.aMap)

    def get_bucket(self, key):
        bucket_id = self.hash_key(key)
        return self.aMap[bucket_id]

    def get_slot(self, key):
        bucket = sefl.get_bucket(key)
        for i, kv in enumerate(bucket):
            k, v = kv
            if key == k:
                return i, k, v
        return -1, key, default

    def get(self, key, default=None):
        i, k, v = self.get_slot(key, default=default)
        return v

    def set(self, key, value):
        bucket = self.get_bucket(key)
        i, k, v = self.get_slot(key)
        if i >= 0:
            bucket[i] = (key, value.insert(value))
        else:
            value = LinkedList(value)
            bucket.append((key, value))

    def delete(self, key):
        bucket = self.get_bucket(key)
        for i in xrange(bucket.length):
            k, v = bucket[i]
            if key == k:
                del bucket[i]
                break

    def resize(self, newSize):
        oldStorage = self.aMap
        self.aMap = []
        for i in range(0, newSize):
            self.aMap.append([])
        for bucket in oldStorage:
            if not bucket: return
            for i in range(0, len(bucket)):
                pair = bucket[i]
                self.insert(pair[0], pair[1])

