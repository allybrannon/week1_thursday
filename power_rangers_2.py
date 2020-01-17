power_rangers = ["Jason", "Trini", "Zack", "Billy", "Kim", "Tommy"]

who_to_remove = input(f"Who would you like to remove?{power_rangers}")


if who_to_remove in power_rangers:
    power_rangers.remove(who_to_remove)
    print(power_rangers)
else:
    print("%s is gone!" % (who_to_remove))
