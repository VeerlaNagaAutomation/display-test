# display_test.py
import sys

def run_test(width=1024, height=768):
    print(f"Running display resolution test with {width}x{height}")
    # Here you can later add actual resolution change logic

if __name__ == "__main__":
    if len(sys.argv) == 3:
        width = sys.argv[1]
        height = sys.argv[2]
        run_test(width, height)
    else:
        print("No resolution passed, using default 1024x768")
        run_test()

