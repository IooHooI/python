import argparse


def task(whs, mph, prm):
    return whs * mph + prm


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Get an input information.')

    # whs, mph, prm - Working HourS, Money Per Hour, PRemiuM
    parser.add_argument('-whs', type=int, help='Working hours')
    parser.add_argument('-mph', type=int, help='Money per hour')
    parser.add_argument('-prm', type=int, help='Premium')

    args = parser.parse_args()

    print("Результат: {}".format(task(getattr(args, 'whs'), getattr(args, 'mph'), getattr(args, 'prm'))))

