class Vehicle:
    color = "white"
    seating_capacity = 4
    seat_price = 50

    def __init__(self, name, max_speed):
        self.name = name
        self.max_speed = max_speed

    def __str__(self):
        return f"""
            Name: {self.name}, 
            Speed: {self.max_speed}, 
            Color: {self.color}
            Seating capacity : {self.seating_capacity}
            Tarif : {self.fare()}
        """

    def fare(self):
        return self.seating_capacity * self.seat_price


class Bus(Vehicle):
    seating_capacity = 50

    def fare(self):
        amount = super().fare() * 1.1
        return amount


if __name__ == '__main__':
    veh_o = Vehicle( "Tesla", 180)
    print(veh_o)

    bus_o = Bus("Volvo", 120)
    print(bus_o)
