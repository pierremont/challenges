'''Exes and Ohs (codewars.com, 7kyu)
Check to see if a string has the same amount of 'x's and 'o's. The method must return a boolean and be case insensitive. The string can contain any char.
Examples input/output:
XO("ooxx") => true
XO("xooxx") => false
XO("ooxXm") => true
XO("zpzpzpp") => true // when no 'x' and 'o' is present should return true
XO("zzoo") => false'''

import unittest

def count_xo(s):
    return s.lower().count('x') == s.lower().count('o')

#print(count_xo('xoxoo'))


class TestCountXo(unittest.TestCase):
    def test_countxo(self):
        self.assertEqual(count_xo('ooxx'), True)
        self.assertEqual(count_xo('xoxoo'), False)
        self.assertEqual(count_xo('zpzpzpp'), True)

if __name__ == '__main__':
    unittest.main()







