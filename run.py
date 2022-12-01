import sys
import importlib

def usage() -> None:
    print('python3 run.py year day part import_type')
    print('python3 run.py 20[21-22] [1-25] [1,2] [test,full]')
    print('example:')
    print('    python3 run.py 2022 1 1 full')
    print('    python3 run.py 2021 19 2 test')

def main() -> None:
    year, day, part, input_type = sys.argv[1:5]
    try:
        solver = importlib.import_module(f'year_{year}.solvers.day_{day}')
    except Exception as e:
        print(e)
        return
    ans = solver.solve(int(part), input_type)
    print(ans)

if __name__ == '__main__':
    if len(sys.argv) != 5:
        usage()
    else:
        main()

