import pandas as pd
import datetime

df_cars = pd.read_csv("cars.csv", dtype={"id": str})
df_playlists = pd.read_csv("playlist.csv", dtype={"id": str})

class Car:
    def __init__(self, id):
        self.id = id
    

    def avaible(self):
        available = df_cars.loc[df_cars["id"] == self.id, "available"].squeeze()
        if available == "yes":
            return True 
        else:
            return False
        
    def booking(self):
        df_cars.loc[df_cars["id"] == self.id, "available"] = "No"
        df_cars.to_csv("cars.csv", index=False)
        
class PlaylistService:
    def __init__(self, playlist_name, ):
        self.name = playlist_name
    
    def output_playlist(self):
        self.link = df_playlists.loc[df_playlists["name"] == self.name, "Link"].squeeze()
        return self.link

class Reservation_Ticket:
    def __init__(self, name,model, link ):
        self.name = name
        self.model = model
        self.link = link

    
    def generate(self):
        print (f"""
                Your car model is: {self.model}
                Your customer name is: {self.name}
                The date of the booking is: {datetime.now()}
                Your playlist link is: {self.link}
 """)
        


def main():
    print(df_cars)
    init_of_rent= input("If yo want to choose a car to rent pres enter")
    if init_of_rent:
        car_id= input("Please input the cars id:")
        car= Car (id = car_id)
        if car.avaible():
            car.booking()
            customer_name = input ("Please input your name:")
            car_model = df_cars.loc[df_cars["id"] == car_id, "model"].squeeze()
            init_of_playlist = input ("If you want to choose playlis for your trip press enter")
            if init_of_playlist:
                print (df_playlists)
                playlist_name = input ("Please input the playlist name:")
                playlist = PlaylistService (playlist_name)
                playlist_link=playlist.output_playlist()
            else:
                pass
            rent_confirmation = Reservation_Ticket(customer_name, car_model, playlist_link)
            rent_confirmation.generate
            

        else:
            print("Thiss car is not avaible or not existing")
    
    else:
        print("Thank you fo visiting our web")

main ()     