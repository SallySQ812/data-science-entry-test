class Car:

    def __init__(own, make, model, year):
        own.make = make
        own.model = model
        own.year = year

    def describe_car(own):
        print(f"{own.year} {own.make} {own.model}")  # print car info. as 'year make model'


if __name__ == "__main__":
    my_car = Car(make="Toyota", model="Corolla", year=2020)  # create instance of car class
    my_car.describe_car()  # call method. Expected output: 2020 Toyota Corolla 