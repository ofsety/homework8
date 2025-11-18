import pandas as pd 

df_cars = pd.read_csv("cars.csv", dtype={"id": str})

def main():
    print(df_cars)
    init_of_rent= input("If yo want to choose a car to rent pres enter")
    if init_of_rent:
        car_id= input("Please input the cars id:")
        car= Cars (id = car_id)
        if car.avaible:
            car.booking

        else:
            print("Thiss car is not avaible or not existing")
    
    else:
        print("Thank you fo visiting our web")


class Cars():
    def __init__ (self, id):
        self.id = id
    
    def booking(self):
        df_cars.loc[df_cars["id"] == self.id, "available"] = "no"
        df_cars.to_csv("cars.csv", index=False)

    def avaible (self):
        available = df_cars.loc[df_cars["id"] == self.id, "available"].squeeze()
        if available == "yes":
            return True 
        else:
            return False
        
class Reservation_Ticket():
    def generate(self):
        pass
        
        