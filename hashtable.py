class HashTable: # Simple hash table implementation
    def __init__(self):
        self.table_size = 1000
        self.table = [None]*self.table_size

    def store(self, key, value):
        hash_value = self.get_hash_value(key)
        if self.table[hash_value]:
            if key in [k for k,v in self.table[hash_value]]:
                raise KeyError("key already in hash table")
            self.table[hash_value].add((key,value))
        else:
            self.table[hash_value] = {(key,value)}

    def lookup(self, key):
        hash_value = self.get_hash_value(key)
        if self.table[hash_value]:
            return [v for k,v in self.table[hash_value] if k==key][0]

    def get_hash_value(self, value):
        if isinstance(value, str):
            return ord(value[0])%self.table_size
        else:
             return value%self.table_size


ht = HashTable()
ht.store("Hello", "World")
assert ht.lookup("Hello") == "World"
ht.store("Hi", "XYZ") # same starting letter, collision
assert ht.lookup("Hi") == "XYZ"
ht.store(5, 30)
assert ht.lookup(5) == 30

try: ht.store(5, 300); assert False
except KeyError: assert True

ht.store(int(1e7), 1)
assert ht.lookup(int(1e7)) == 1
