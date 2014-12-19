class HashMap(object): 
    def __init__(self, num_buckets = 256):
        """Initializes a Map with the given number of buckets."""
        self.aMap = []
        for i in range(0, num_buckets):
            self.aMap.append([])
        return self.aMap

    def hash_key(self, key):
        """Given a key this will create a number and then convert it to an index for the aMap's buckets."""
        return hash(key) % len(self.aMap)

    def get_bucket(self, key):
        """Given a key, find the bucket where it would go."""
        bucket_id = self.hash_key(key)
        return self.aMap[bucket_id]

    def get_slot(self, key, default = None):
        """
        Returns the index, key, and value of a slot found in a bucket.
        Returns -1, key, and default (None if not set) when not found.
        """
        bucket = self.get_bucket(key)

        for i, kv in enumerate(bucket):
            k, v = kv
            if key == k:
                return i, k, v

        return -1, key, default

    def get(self, key, default = None):
        """Gets the value in a bucket for the given key, or the default."""
        i, k, v = self.get_slot(key, default = default)
        return v 

    def set(self, key, value):
        """Sets the key to the value, replacing any existing value."""
        bucket = self.get_bucket(key)
        i, k, v = self.get_slot(key)

        if i >= 0:
            # the key exists, overwrite it
            bucket[i] = (key, value)
        else:
            # the key doesn't exist, append to create it
            bucket.append((key, value))

    def delete(self, key):
        """Deletes the given key from the Map."""
        bucket = self.get_bucket(self.aMap, key)

        for i in xrange(len(bucket)):
            k, v = bucket[i]
            if key == k:
                del bucket[i]
                break

    def list(self):
        """Prints out what's in the Map."""
        for bucket in self.aMap:
            if bucket:
                for k, v in bucket:
                    print k, v

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
