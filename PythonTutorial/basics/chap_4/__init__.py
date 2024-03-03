class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def whereIsThePoint(self, point):
        match point:
            case Point(x=0, y=0):
                print('center')
            case Point(x=x, y=0):
                print(f"x axis {x}")
            case Point(x=0, y=y):
                print(f"y axis {y}")
            case Point(x=x, y=y):
                print(f"x axis is : {x} and y axis is : {y}")
            case _:
                print("invalid input")


class CirclePoints:
    __match_args__ = ('x', 'y')

    def __int__(self):
        pass

    def __init__(self, x, y):
        self.x = x
        self.y = y


match CirclePoints:
    case [CirclePoints()]:
        print("center")
    case [CirclePoints(x=x, y=y)]:
        print(f"x axis {x} and y axis {y}")
    case [CirclePoints(x=x, y=0)]:
        print(f"x axis is {x}")
    case [CirclePoints(x=0, y=y)]:
        print(f"y axis is {y}")
    case _:
        print("invalid input")
