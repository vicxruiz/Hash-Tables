# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

    def __str__(self):
        return f"{{{self.key}, {self.value}}}"

    def __repr__(self):
        next = None
        if self.next:
            next = self.next.key
        return f"{{key: {self.key}, value: {self.value}, next_key: {next}}}"

    # These little helpers keep our hash methods clean

    # append an item at the end of our linked pair chain. if the item exists overwrite it
    def append(self, key, value):
        if self.key == key:
            self.value = value
        elif not self.next:
            self.next = LinkedPair(key, value)
        else:
            self.next.append(key, value)

    # retrieve an item from our linked list chain
    def retrieve(self, key):
        if self.key == key:
            return self.value
        elif not self.next:
            print(f"Hash[{key}] is undefined")
            return None
        else:
            return self.next.retrieve(key)

class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''
    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity


    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return hash(key)


    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        pass


    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity


    def insert(self, key, value):
        '''
        Store the value with the given key.

        # Part 1: Hash collisions should be handled with an error warning. (Think about and
        # investigate the impact this will have on the tests)

        # Part 2: Change this so that hash collisions are handled with Linked List Chaining.

        Fill this in.
        '''
        if not None in self.storage:
            self.resize()
        hash_mod = self._hash_mod(key)
        # if we have something at the hash_mod index, append this value. Using LinkedPair.append will overwrite a value if that value already exists, and traverse over all the values
        if self.storage[hash_mod]:
            self.storage[hash_mod].append(key, value)
        else:
            self.storage[hash_mod] = LinkedPair(key, value)



    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        hash_mod = self._hash_mod(key)
        if not self.storage[hash_mod]:
            print(f'Hash[{key}] cannot be deleted: it does not exist')
            return
        current_node = self.storage[hash_mod]
        prev_node = None
        if current_node.key == key and not current_node.next:
            self.storage[hash_mod] = None
        elif current_node.key == key:
            self.storage[hash_mod] = self.storage[hash_mod].next
        else:
            while current_node:
                if current_node.key == key:
                    prev_node.next = current_node.next
                    return
                prev_node = current_node
                current_node = current_node.next


    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        hash_mod = self._hash_mod(key)
        if self.storage[hash_mod]:
            return self.storage[hash_mod].retrieve(key)
        else:
            print(f"Hash[{key}] is undefined")
            return None


    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''

        self.capacity *= 2
        old_storage = self.storage
        self.storage = [None] * self.capacity
        for node in old_storage:
            if node:
                current_node = node
                while current_node:
                    self.insert(current_node.key, current_node.value)
                    current_node = current_node.next



if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")
