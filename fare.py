# Liting Zhou
# this is a calculator,
# which takes the distance as input,
# and returns the fare as output.


def fare(distance):
    base = 2.55
    ladder = [0.2, 0.1, 0.05]
    zone3fare = 4.8
    if distance <= 0:
        return 0
    elif distance <= 5:
        return base
    elif distance <= 10:
        return base + (distance - 5) * ladder[0]
    elif distance <= 15:
        return base + 5 * ladder[0] + (distance - 10) * ladder[1]
    elif distance <= 22:
        return base + 5 * ladder[0] + 5 * ladder[1] + (distance - 15) * ladder[2]
    else:
        return zone3fare


if __name__ == "__main__":
    while True:
        distance = input("Enter the distance (or 'q' to exit): ")
        if distance.lower() == 'q':
            break
        else:
            distance = float(distance)
            print(fare(distance))
