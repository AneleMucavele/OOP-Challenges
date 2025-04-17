from pet import Pet

def main():
    my_pet = Pet("Frisky")

    my_pet.get_status()

    my_pet.eat()
    my_pet.sleep()
    my_pet.play()
    my_pet.train("Roll Over")
    my_pet.train("Shake Hands")

    my_pet.get_status()
    my_pet.show_tricks()

if __name__ == "__main__":
    main()
