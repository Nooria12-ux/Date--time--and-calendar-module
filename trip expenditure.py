def hotel_cost(night):
    return 300 * night

def plane_ride_cost(city):
    
    if city == "Cox's Bazar":
        return 365
    
    elif city == "Bandarban":
        return 755
    
    elif city == "Alabama":
        return 2345
    
    elif city == "Los Angeles":
        return 3567

def rental_car_cost(days):

    if days >= 7:
        return (45*days)
    
    elif days >= 3:
        return (45 * days)
    else:
        return(40*days)
    
def trip_cost(city, days):

    h_c = hotel_cost(days)
    r_c = rental_car_cost(days)
    p_c = plane_ride_cost(city)
    
    sum = h_c + r_c + p_c
    return sum

d = int(input("Enter the amount of days you wish to stay (in digit): "))
c = input("Enter the city you are going to: ")

print()
print()

print(f"Hotel cost: ${hotel_cost(d)}")
print(f"Car cost: ${rental_car_cost(d)}")
print(f"Plane cost: ${plane_ride_cost(c)}")
print(f"Total cost: ${trip_cost(c,d)}")