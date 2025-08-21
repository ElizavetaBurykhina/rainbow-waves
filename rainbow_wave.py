from termcolor import colored
import time
import math
from colors import colors


colors = colors * 4


def sine_wave(amplitude=20, step_size=0.3):
    step = 0
    while True:
        value = int((math.sin(step) + 1) * amplitude/2)
        yield value
        step += step_size

def wave():
    color_str = "".join([colored('***', f'{color}', f'on_{color}') for color in colors])
    while True:
        for offset in sine_wave():
            print(" " * offset + color_str)
            time.sleep(0.1)


if __name__ == '__main__':
    wave()
