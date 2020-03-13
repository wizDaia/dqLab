'''
Почему у меня numpy не работал на линуксе, я до сих пор без понятия

-a                  - коэффициенты ai (float, от старшего к младшему)
-x VALUE             величина x (float)
-v или --verbose     выводит вычисляемое выражение "an*xn+...+a1*x+a0*1.0=p", где
                      ai - коэффициенты
                      xi - вычисленная i-я степень числа x
                      p - итоговое значение

примеры ввода:
    ./script.py -a 1 2 3 -x 0
    ./script.py -a 1 2 3 -x 2 --verbose

примеры вывода:
    3.0
    1.0*4.0+2.0*2.0+3.0*1.0=11.0
'''

import argparse
import numpy as np

parser = argparse.ArgumentParser()
parser.add_argument('-a', nargs = '*', type = float,
                    required = False, help = 'Coefficients', dest = 'c') #dest = beta
parser.add_argument('-x', nargs = 1, type = float,
                    required = False, help = 'value', dest = 'value')
parser.add_argument('-v', '--verbose', help = 'increase output verbosity',
                    action = 'store_true')
args = parser.parse_args() #-v --verbose '-a alfa -x beta gamma delta'.split()

p = np.poly1d(args.c)
x = args.value
print(p(x[0]))
if args.verbose:
    print(p, '=', x[0])
