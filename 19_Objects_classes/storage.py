class Storage:
    storage = []

    def __init__(self, capacity):
        self.capacity = capacity

    def add_product(self, product):
        if len(Storage.storage) < self.capacity and isinstance(product, str):
            Storage.storage.append(product)

    def get_products(self):
        return Storage.storage


storage = Storage(9)
storage.add_product("apple")
storage.add_product(12)
storage.add_product(3)
storage.add_product("tomato")
storage.add_product("bread")
print(storage.get_products())
