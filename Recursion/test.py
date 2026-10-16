import sys
import timeit
import recurtion

REPEATS = 3  

def usage():
    print(" Usage: python test.py n xy [xy ...]")
    print("        python test.py gcd a b     (gcd is recursive only, 2 numbers)")
    print("        python test.py conv decimal base   (recursive only, base 2 - 8 - 16)")
    print("        python test.py hanoi n     (recursive only, n disks)")
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

#Exception handling for GCD, Conversion, and Towers of Hanoi
def doRunGcd(a, b):
    try:
        return recurtion.gcd_recursive(a, b)
    except RecursionError:
        print("RecursionError: values too large for recursion")
        return None
    except TypeError as e:
        print(f"Error: {e}")
        return None

def doRunConv(decimal, base):
    try:
        return recurtion.convert_recursive(decimal, base)
    except RecursionError:
        print("RecursionError: value too large for recursion")
        return None
    except (TypeError, ValueError) as e:
        print(f"Error: {e}")
        return None

def doRunHanoi(n):
    try:
        return recurtion.towers_of_hanoi(n)
    except RecursionError:
        print("RecursionError: too many disks for recursion")
        return None
    except (TypeError, ValueError) as e:
        print(f"Error: {e}")
        return None

#Time Calculation Functions for GCD, Conversion, and Towers of Hanoi
def runGcd(a, b):
    runningTotal = 0
    failed = False
    output = None

    for repeat in range(REPEATS):
        startTime = timeit.default_timer()
        result = doRunGcd(a, b)
        endTime = timeit.default_timer()
        if result is None:
            failed = True
            break
        output = result
        runningTotal += (endTime - startTime)

    if failed:
        print(f"gcd({a}, {b}) FAILED")
    else:
        print(f"gcd({a}, {b}) {runningTotal / REPEATS}")
        print("   Output: " + str(output))

def runConv(decimal, base):
    runningTotal = 0
    failed = False
    output = None

    for repeat in range(REPEATS):
        startTime = timeit.default_timer()
        result = doRunConv(decimal, base)
        endTime = timeit.default_timer()
        if result is None:
            failed = True
            break
        output = result
        runningTotal += (endTime - startTime)

    if failed:
        print(f"conv({decimal}, base {base}) FAILED")
    else:
        print(f"conv({decimal}, base {base}) {runningTotal / REPEATS}")
        print("   Output: " + str(output))

def runHanoi(n):
    # run once only - it prints output each time it's called
    startTime = timeit.default_timer()
    result = doRunHanoi(n)
    endTime = timeit.default_timer()

    if result is None:
        print(f"hanoi({n}) FAILED")
    else:
        print(f"hanoi({n}) {endTime - startTime}")
        print("   Total moves: " + str(result))
        print("   Expected moves (2^n - 1): " + str(2**n - 1))

# main program
if len(sys.argv) < 3:
    usage()
elif sys.argv[1] == "gcd":
    if len(sys.argv) != 4:
        print("Usage: python test_harness.py gcd a b")
    else:
        try:
            a = int(sys.argv[2])
            b = int(sys.argv[3])
        except ValueError:
            print(f"Error: '{sys.argv[2]}' and '{sys.argv[3]}' must both be integers")
        else:
            runGcd(a, b)
elif sys.argv[1] == "conv":
    if len(sys.argv) != 4:
        print("Usage: python test_harness.py conv decimal base")
    else:
        try:
            decimal = int(sys.argv[2])
            base = int(sys.argv[3])
        except ValueError:
            print(f"Error: '{sys.argv[2]}' and '{sys.argv[3]}' must both be integers")
        else:
            runConv(decimal, base)
elif sys.argv[1] == "hanoi":
    if len(sys.argv) != 3:
        print("Usage: python test_harness.py hanoi n")
    else:
        try:
            n = int(sys.argv[2])
        except ValueError:
            print(f"Error: '{sys.argv[2]}' must be an integer")
        else:
            runHanoi(n)
else:
    for a in range(2, len(sys.argv)):
        n = int(sys.argv[1])
        funcType = sys.argv[a][0]
        methodType = sys.argv[a][1]
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
            print(funcType + methodType + " " + str(n) + " " + str(runningTotal / REPEATS))
            print("   Output: " + str(output))