import io
import time
from collections import namedtuple


def timer_rev():
    counter = 3
    for i in reversed(range(counter)):
        print(i)
        time.sleep(1)


def dummy_file_io():
    dummy_file = io.StringIO()
    print("Dummy file", file=dummy_file)
    print(dummy_file.getvalue())


def sep_print():
    a = 10
    b = 20
    c = 30
    print(a, b, c, sep='-')


def car_builder():
    Car = namedtuple('Car', ('make', 'model', 'year'))
    car = Car(make='Ford', model='Mustang', year=2023)
    print(repr(car))


if __name__ == '__main__':
    # timer_rev()
    #sep_print()
    #dummy_file_io()
    car_builder()