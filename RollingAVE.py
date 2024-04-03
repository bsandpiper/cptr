from plotter import Plotter

file = "covid.txt"

def read_data(filename: str) -> list[int]:
    output = []
    
    with open(file) as f:
        for line in f:
            output.append(int(line.strip()))

    return output

def rolling_average(a: list[int]) -> list[int]:
    rolling = []
    for i in range(len(a)-4):
        number = 0
        for n in range(5):
            number += a[i+n]
        number /=5
        rolling.append(number)
    return rolling

rolling_average(read_data(file))
data = read_data('covid.txt')
roll_avg = rolling_average(data)
plotter = Plotter()
plotter.new(data, 50, 50, 400, 200)
plotter.new(roll_avg, 50, 325, 400, 200)
plotter.plot()