from termcolor import colored
import time
from colors import colors

colors = colors * 4


def gradient():
    while True:
        for start_point in range(len(colors)):
            color_str = colored('')
            for color in colors[start_point:]:
                color_str = color_str + colored('***', f'{color}', f'on_{color}')
            for color in colors[0:start_point]:
                color_str = color_str + colored('***', f'{color}', f'on_{color}')
            print(color_str)
            time.sleep(0.1)


if __name__ == '__main__':
    gradient()


