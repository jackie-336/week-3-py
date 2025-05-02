
class Smartphone:
    def __init__(self, brand, model, storage, battery_life):
        self._brand = brand  # Encapsulated attribute
        self._model = model
        self._storage = storage  # in GB
        self._battery_life = battery_life  # in hours

    def display_info(self):
        return f"{self._brand} {self._model} with {self._storage}GB storage and {self._battery_life}h battery"

    # Encapsulation: Getter and Setter for storage
    def get_storage(self):
        return self._storage

    def set_storage(self, new_storage):
        if new_storage > 0:
            self._storage = new_storage
        else:
            print("Error: Storage must be a positive value.")


# Subclass: AndroidPhone
class AndroidPhone(Smartphone):
    def __init__(self, brand, model, storage, battery_life, android_version):
        super().__init__(brand, model, storage, battery_life)
        self.android_version = android_version

    def display_info(self):
        base_info = super().display_info()
        return f"{base_info} running Android {self.android_version}"


# Subclass: iPhone
class iPhone(Smartphone):
    def __init__(self, model, storage, battery_life, ios_version):
        super().__init__("Apple", model, storage, battery_life)
        self.ios_version = ios_version

    def display_info(self):
        base_info = super().display_info()
        return f"{base_info} running iOS {self.ios_version}"


# --- MAIN PROGRAM ---

# Create instances
android_phone = AndroidPhone("Samsung", "Galaxy S24", 256, 24, "13")
iphone = iPhone("iPhone 15 Pro", 512, 20, "17.3")

# Display info using polymorphism
print("=== Smartphone Details ===")
print(android_phone.display_info())
print(iphone.display_info())

# Test Encapsulation
print("\n=== Testing Encapsulation ===")
print(f"Original Android Storage: {android_phone.get_storage()} GB")
android_phone.set_storage(512)
print(f"Updated Android Storage: {android_phone.get_storage()} GB")

# Try setting invalid storage
android_phone.set_storage(-100)  # Should show an error
