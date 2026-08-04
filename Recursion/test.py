#**
#** Testharness to compute Factorial and Fibonacci using
#** iterative or recursive methods, and time their performance.
#**
import sys
import timeit
import recurtion

REPEATS = 3  # No. times to run to get mean time

def usage():
    print(" Usage: python test_harness.py n xy [xy ...]")
    print("        where")
    print("        n is the input value")
    print("        x is one of")
    print("           f - factorial")
    print("           b - fibonacci")
    print("        y is one of")
    print("           i - iterative")
    print("           r - recursive")

def doRun(n, funcType, methodType):
    try:
        if funcType == "f" and methodType == "i":
            return recurtion.factorial_iterative(n)
        elif funcType == "f" and methodType == "r":
            return recurtion.factorial_recursive(n)
        elif funcType == "b" and methodType == "i":
            return recurtion.fibo_iterative(n)
        elif funcType == "b" and methodType == "r":
            return recurtion.fibo_recursive(n)
        else:
            print("Unsupported function/method combination")
            return None
    except RecursionError:
        print("RecursionError: n too large for recursion")
        return None
    except ValueError as e:
        print(f"Error: {e}")
        return None

# main program
if len(sys.argv) < 3:
    usage()
else:
    for aa in range(2, len(sys.argv)):
        n = int(sys.argv[1])
        funcType = sys.argv[aa][0]
        methodType = sys.argv[aa][1]
        runningTotal = 0
        failed = False
        output = None

        for repeat in range(REPEATS):
            startTime = timeit.default_timer()
            result = doRun(n, funcType, methodType)
            endTime = timeit.default_timer()
            if result is None:
                failed = True
                break
            output = result
            runningTotal += (endTime - startTime)

        if failed:
            print(funcType + methodType + " " + str(n) + " FAILED")
        else:
            print(funcType + methodType + " " + str(n) + " " + str(runningTotal / (REPEATS - 1)))
            print("   Output: " + str(output))