from unittest import TestCase


################################################################################
# STACK IMPLEMENTATION (DO NOT MODIFY THIS CODE)
################################################################################
class Stack:
    class Node:
        def __init__(self, val, next=None):
            self.val = val
            self.next  = next

    def __init__(self):
        self.top = None

    def push(self, val):
        self.top = Stack.Node(val, self.top)

    def pop(self):
        assert self.top, 'Stack is empty'
        val = self.top.val
        self.top = self.top.next
        return val

    def peek(self):
        return self.top.val if self.top else None

    def empty(self):
        return self.top == None

    def __bool__(self):
        return not self.empty()

    def __repr__(self):
        if not self.top:
            return ''
        return '--> ' + ', '.join(str(x) for x in self)

    def __iter__(self):
        n = self.top
        while n:
            yield n.val
            n = n.next

################################################################################
# CHECK DELIMITERS
################################################################################
def check_delimiters(expr):
    """Returns True if and only if `expr` contains only correctly matched delimiters, else returns False."""
    delim_openers = '{([<'
    delim_closers = '})]>'

    ### BEGIN SOLUTION
    s = Stack()
    for c in expr:
        if c in delim_openers:
            s.push(c)
        elif c in delim_closers:
                try:
                    t = s.pop()
                    if delim_openers.find(t) != delim_closers.find(c):
                        return False
                except:
                    return False
    return s.empty()


    ### END SOLUTION

    
print(check_delimiters('()'))
################################################################################
# CHECK DELIMITERS - TEST CASES
################################################################################
# points: 5
def test_check_delimiters_1():
    


    tc = TestCase()
    tc.assertTrue(check_delimiters('()'))
    tc.assertTrue(check_delimiters('[]'))
    tc.assertTrue(check_delimiters('{}'))
    tc.assertTrue(check_delimiters('<>'))

# points:5
def test_check_delimiters_2():
    tc = TestCase()
    tc.assertTrue(check_delimiters('([])'))
    tc.assertTrue(check_delimiters('[{}]'))
    tc.assertTrue(check_delimiters('{<()>}'))
    tc.assertTrue(check_delimiters('<({[]})>'))

# points: 5
def test_check_delimiters_3():
    tc = TestCase()
    tc.assertTrue(check_delimiters('([] () <> [])'))
    tc.assertTrue(check_delimiters('[{()} [] (<> <>) {}]'))
    tc.assertTrue(check_delimiters('{} <> () []'))
    tc.assertTrue(check_delimiters('<> ([] <()>) <[] [] <> <>>'))

# points: 5
def test_check_delimiters_4():
    tc = TestCase()
    tc.assertFalse(check_delimiters('('))
    tc.assertFalse(check_delimiters('['))
    tc.assertFalse(check_delimiters('{'))
    tc.assertFalse(check_delimiters('<'))
    tc.assertFalse(check_delimiters(')'))
    tc.assertFalse(check_delimiters(']'))
    tc.assertFalse(check_delimiters('}'))
    tc.assertFalse(check_delimiters('>'))

# points: 5
def test_check_delimiters_5():
    tc = TestCase()
    tc.assertFalse(check_delimiters('( ]'))
    tc.assertFalse(check_delimiters('[ )'))
    tc.assertFalse(check_delimiters('{ >'))
    tc.assertFalse(check_delimiters('< )'))

# points: 5
def test_check_delimiters_6():
    tc = TestCase()
    tc.assertFalse(check_delimiters('[ ( ] )'))
    tc.assertFalse(check_delimiters('((((((( ))))))'))
    tc.assertFalse(check_delimiters('< < > > >'))
    tc.assertFalse(check_delimiters('( [] < {} )'))

################################################################################
# INFIX -> POSTFIX CONVERSION
################################################################################

def infix_to_postfix(expr):
    """Returns the postfix form of the infix expression found in `expr`"""
    # you may find the following precedence dictionary useful
    prec = {'*': 2, '/': 2,
            '+': 1, '-': 1}
    ops = Stack()
    postfix = []
    toks = expr.split()
    ### BEGIN SOLUTION
    opp = {'*', '/','+', '-'}
    for x in toks:
        if str.isdigit(x):
            postfix.append(x)
        elif ops.empty() or ops.peek() == '(':
            ops.push(x)
        elif x == '(':
            ops.push(x)
        elif x == ')':
            while not ops.empty():
                temp = ops.pop()
                if temp == '(':
                    break
                else:
                    postfix.append(temp)
        elif x in opp:
            while True:
                if prec.get(x) > prec.get(ops.peek()):
                    ops.push(x)
                    break
                elif prec.get(x) == prec.get(ops.peek()):
                    postfix.append(ops.pop())
                    ops.push(x)
                    break
                elif prec.get(x) < prec.get(ops.peek()):
                    postfix.append(ops.pop())
                    if ops.empty():
                        ops.push(x)
                        break
                elif ops.empty():
                    break

    while True:
        if not ops.empty():
            postfix.append(ops.pop())
        else:
            break

    ### END SOLUTION
    return ' '.join(str(x) for x in postfix)

################################################################################
# INFIX -> POSTFIX CONVERSION - TEST CASES
################################################################################

# points: 10
def test_infix_to_postfix_1():
    tc = TestCase()
    tc.assertEqual(infix_to_postfix('1'), '1')
    tc.assertEqual(infix_to_postfix('1 + 2'), '1 2 +')
    tc.assertEqual(infix_to_postfix('( 1 + 2 )'), '1 2 +')
    tc.assertEqual(infix_to_postfix('1 + 2 - 3'), '1 2 + 3 -')
    tc.assertEqual(infix_to_postfix('1 + ( 2 - 3 )'), '1 2 3 - +')

# points: 10
def test_infix_to_postfix_2():
    tc = TestCase()
    tc.assertEqual(infix_to_postfix('1 + 2 * 3'), '1 2 3 * +')
    tc.assertEqual(infix_to_postfix('1 / 2 + 3 * 4'), '1 2 / 3 4 * +')
    tc.assertEqual(infix_to_postfix('1 * 2 * 3 + 4'), '1 2 * 3 * 4 +')
    tc.assertEqual(infix_to_postfix('1 + 2 * 3 * 4'), '1 2 3 * 4 * +')

# points: 10
def test_infix_to_postfix_3():
    tc = TestCase()
    tc.assertEqual(infix_to_postfix('1 * ( 2 + 3 ) * 4'), '1 2 3 + * 4 *')
    tc.assertEqual(infix_to_postfix('1 * ( 2 + 3 * 4 ) + 5'), '1 2 3 4 * + * 5 +')
    tc.assertEqual(infix_to_postfix('1 * ( ( 2 + 3 ) * 4 ) * ( 5 - 6 )'), '1 2 3 + 4 * * 5 6 - *')

################################################################################
# QUEUE IMPLEMENTATION
################################################################################
class Queue:
    def __init__(self, limit=10):
        self.data = [None] * limit
        self.head = -1
        self.tail = -1

    ### BEGIN SOLUTION
    ### END SOLUTION

    def enqueue(self, val):
        ### BEGIN SOLUTION
        print('called enqueue')
        if (self.tail + 1) % len(self.data) == self.head:
            raise RuntimeError
        elif self.head == -1:
            self.tail = 0
            self.head = 0
            self.data[self.tail] = val
            print("enqueued + " + str(val) + ' at ' + str(self.tail))
        else:
            self.tail = (self.tail + 1) % len(self.data)
            self.data[self.tail] = val
            print("enqueued + " + str(val) + ' at ' + str(self.tail))
        ### END SOLUTION

    def dequeue(self):
        ### BEGIN SOLUTION
        print('called dequeue')
        if self.head == -1:
           raise RuntimeError
        elif self.head == self.tail:
            temp = self.data[self.head]
            self.data[self.head] = None
            self.head = -1
            self.tail = -1
            print("returned + " + str(temp) + ' head is : ' + str(self.head) + ' - tail is: ' + str(self.tail))
            return temp
        else:
            temp = self.data[self.head]
            self.data[self.head] = None
            self.head = (self.head + 1) % len(self.data)
            print("returned + " + str(temp) + ' head is : ' + str(self.head) + ' - tail is: ' + str(self.tail))
            return temp
        ### END SOLUTION

    def resize(self, newsize):
        assert(len(self.data) < newsize)
        ### BEGIN SOLUTION
        for x in range(len(self.data), newsize):
            self.data.append(None)
        ### END SOLUTION

    def empty(self):
        ### BEGIN SOLUTION
        if self.data[self.tail] != None  and self.tail != -1:
            return False
        for x in range(self.head, self.tail):
            if self.data[x] != None:
                return False
        return True
        ### END SOLUTION

    def __bool__(self):
        return not self.empty()

    def __str__(self):
        if not(self):
            return '' 
        return ', '.join(str(x) for x in self)

    def __repr__(self):
        return str(self)

    def __iter__(self):
        ### BEGIN SOLUTION
        i = 0
        while i < len(self.data):
            yield self.data[i]
            i += 1
        ### END SOLUTION

################################################################################
# QUEUE IMPLEMENTATION - TEST CASES
################################################################################

# points: 13
def test_queue_implementation_1():
    tc = TestCase()

    q = Queue(5)
    tc.assertEqual(q.data, [None] * 5)

    for i in range(5):
        q.enqueue(i)

    with tc.assertRaises(RuntimeError):
        q.enqueue(5)

    for i in range(5):
        tc.assertEqual(q.dequeue(), i)

    tc.assertTrue(q.empty())

# points: 13
def test_queue_implementation_2():
	tc = TestCase()

	q = Queue(10)

	for i in range(6):
	    q.enqueue(i)

	tc.assertEqual(q.data.count(None), 4)

	for i in range(5):
	    q.dequeue()

	tc.assertFalse(q.empty())
	tc.assertEqual(q.data.count(None), 9)
	tc.assertEqual(q.head, q.tail)
	tc.assertEqual(q.head, 5)

	for i in range(9):
	    q.enqueue(i)

	with tc.assertRaises(RuntimeError):
	    q.enqueue(10)

	for x, y in zip(q, [5] + list(range(9))):
	    tc.assertEqual(x, y)

	tc.assertEqual(q.dequeue(), 5)
	for i in range(9):
	    tc.assertEqual(q.dequeue(), i)

	tc.assertTrue(q.empty())

# points: 14
def test_queue_implementation_3():
	tc = TestCase()

	q = Queue(5)
	for i in range(5):
	    q.enqueue(i)
	for i in range(4):
	    q.dequeue()
	for i in range(5, 9):
	    q.enqueue(i)

	with tc.assertRaises(RuntimeError):
	    q.enqueue(10)

	q.resize(10)

	for x, y in zip(q, range(4, 9)):
	    tc.assertEqual(x, y)

	for i in range(9, 14):
	    q.enqueue(i)

	for i in range(4, 14):
	    tc.assertEqual(q.dequeue(), i)

	tc.assertTrue(q.empty())
	tc.assertEqual(q.head, -1)

################################################################################
# TEST HELPERS
################################################################################
def say_test(f):
    print(80 * "*" + "\n" + f.__name__)

def say_success():
    print("SUCCESS")

################################################################################
# MAIN
################################################################################
def main():
    for t in [test_check_delimiters_1,
              test_check_delimiters_2,
              test_check_delimiters_3,
              test_check_delimiters_4,
              test_check_delimiters_5,
              test_check_delimiters_6,
              test_infix_to_postfix_1,
              test_infix_to_postfix_2,
              test_infix_to_postfix_3,
              test_queue_implementation_1,
              test_queue_implementation_2,
              test_queue_implementation_3]:
        say_test(t)
        t()
        say_success()


if __name__ == '__main__':
    main()
