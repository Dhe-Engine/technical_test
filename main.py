def sort(width, height, length, mass):
    """
    this method helps to classify the package based on the size and weight

    :param width: width
    :param height: height
    :param length: length
    :param mass: mass
    :return: string (standard | special | rejected)
    """

    #checks for each input
    for each_value in (width, height, length, mass):
        #check when it is not numeric
        if not isinstance(each_value,(int,float)):
            raise TypeError("only accept numeric values  (int or float) ")

        #check when the numeric value is less than zero
        if each_value < 0:
            raise ValueError("dimensions and mass must be positive")

    #si unit is cm³
    volume = width * height * length

    #bulky conditions
    bulky = (
        volume >= 1000000
        or width >= 150
        or height >= 150
        or length >= 150
    )

    #heavy condition
    heavy = mass >= 20

    #check when bulky and heavy
    if bulky and heavy:
        return "REJECTED"

    #check when it is either bulky or heavy
    if bulky or heavy:
        return "SPECIAL"

    #display the right result if both condition above are false
    return "STANDARD"


# Tests
if __name__ == "__main__":
    print(sort(10, 10, 10, 1))
    print(sort(100, 100, 100, 5))
    print(sort(150, 10, 10, 5))
    print(sort(10, 10, 10, 20))
    print(sort(200, 200, 200, 25))