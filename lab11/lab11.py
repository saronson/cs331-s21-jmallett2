from unittest import TestCase

def quicksort(lst,pivot_fn):
    qsort(lst,0,n-1,pivot_fn)

def qsort(lst,low,high,pivot_fn):
    ### BEGIN SOLUTION
    ### END SOLUTION

def pivot_first(lst,low,high):
    ### BEGIN SOLUTION
    ### END SOLUTION

def pivot_random(lst,low,high):
    ### BEGIN SOLUTION
    ### END SOLUTION

def pivot_median_of_three(lst,low,high):
    ### BEGIN SOLUTION
    ### END SOLUTION

################################################################################
# TEST CASES
################################################################################
def randomize_list(size):
    lst = list(range(0,size))
    for i in range(0,size):
        l = random.randint(0,size)
        r = random.randint(0,size)
        lst[l], lst[r] = lst[r], lst[l]
    return lst

def test_lists_with_pfn(pfn):
    tc = TestCase()
    exp = list(range(0,1000))

    lst = list(range(0,1000))
    quicksort(lst, pivot_first)
    tc.assertEquals(lst,exp)

    lst = list(reversed(range(0,1000)))
    quicksort(lst, pivot_first)
    tc.assertEquals(lst,exp)

    for i in range(0,100):
        lst = randomize_list(1000)
        quicksort(lst, pfn)
        tc.assertEquals(lst,exp)

# 30 points
def test_first():
    test_lists_with_pfn(pivot_first)

# 30 points
def test_random():
    test_lists_with_pfn(pivot_random)

# 40 points
def test_median():
    test_lists_with_pfn(pivot_median_of_three)

################################################################################
# TEST HELPERS
################################################################################
def say_test(f):
    print(80 * "#" + "\n" + f.__name__ + "\n" + 80 * "#" + "\n")

def say_success():
    print("----> SUCCESS")

################################################################################
# MAIN
################################################################################
def main():
    for t in [test_first,
              test_random,
              test_median]:
        say_test(t)
        t()
        say_success()
    print(80 * "#" + "\nALL TEST CASES FINISHED SUCCESSFULLY!\n" + 80 * "#")

if __name__ == '__main__':
    main()
