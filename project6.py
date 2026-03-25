class Vehicle:
    def __init__(self, seating_capacity):
        self.seating_capacity = seating_capacity

    def fare(self):
        return self.seating_capacity * 100

class Bus(Vehicle):
    def fare(self):
        base_fare = super().fare()
        maintenance_charge = 0.10 * base_fare
        total_fare = base_fare + maintenance_charge

        print("Base Fare:", base_fare)
        print("Maintenance Charge (10%):", maintenance_charge)

        return total_fare

capacity = int(input("Enter seating capacity: "))

vehicle = Vehicle(capacity)
bus = Bus(capacity)

print("\n--- Vehicle Fare ---")
print("Total Fare:", vehicle.fare())

print("\n--- Bus Fare ---")
print("Total Fare:", bus.fare())