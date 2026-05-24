def carFleet(target: int, position: list[int], speed: list[int]) -> int:
    if len(position) == 1:
        return 1
    
    # create position, speed pairs for each car and sort in descending order
    cars = [(p, s) for p, s in zip(position, speed)]
    cars = sorted(cars, key=lambda car: car[0], reverse=True)
    fleets = []

    for car in cars:
        time = (target - car[0]) / car[1]

        # if time to target of curr car > top of stack time, then curr car will 
        # never meet fleet at top of stack
        if not fleets or time > fleets[-1]:
            fleets.append(time)
    
    return len(fleets)

if __name__ == "__main__":
    print(carFleet(12, [10,8,0,5,3], [2,4,1,1,3]))
