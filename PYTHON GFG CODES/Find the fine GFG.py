def calculate_fine(car, fine, date):
    if date % 2 == 0:
        total_fine = 0
        for i in range(len(car)):
            if car[i] % 2 == 1:
                total_fine = total_fine +fine[i]
        return total_fine
    else:
        total_fine = 0
        for i in range(len(car)):
            if car[i] % 2 == 0:
                total_fine = total_fine + fine[i]
        return total_fine


car = [2375, 7682, 2325, 2352]
fine = [250, 500, 350, 200]
date = 21
print(calculate_fine(car, fine, date))