def make_averager():
    series = []

    def averager(new_value):
        series.append(new_value)
        total = sum(series)
        return total / len(series)
    return averager


def main():
    avg = make_averager()
    print(avg(10))
    print(avg(11))
    print(avg(12))


if __name__ == '__main__':
    main()
