#!/usr/bin/python -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

# Basic list exercises
# Fill in the code for the functions below. main() is already set up
# to call the functions with a few different inputs,
# printing 'OK' when each function is correct.
# The starter code for each function includes a 'return'
# which is just a placeholder for your code.
# It's ok if you do not complete all the functions, and there
# are some additional functions to try in list2.py.

# A. match_ends
# Given a list of strings, return the count of the number of
# strings where the string length is 2 or more and the first
# and last chars of the string are the same.
# Note: python does not have a ++ operator, but += works.
def match_ends(words):
  # +++your code here+++
	count = 0
	for i in range(0,len(words)):
		lenword = len(words[i])
		if lenword >= 2 and words[i][0] == words[i][-1] :
			count = count + 1
	return count

#range(1, 11), range function include the first one but not the last one
#[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# B. front_x
# Given a list of strings, return a list with the strings
# in sorted order, except group all the strings that begin with 'x' first.
# e.g. ['mix', 'xyz', 'apple', 'xanadu', 'aardvark'] yields
# ['xanadu', 'xyz', 'aardvark', 'apple', 'mix']
# Hint: this can be done by making 2 lists and sorting each of them
# before combining them.
def front_x(words):
  # +++your code here+++
	xwords = []
	others = []
	for i in range(len(words)):
		if words[i][0] == 'x' :
			xwords.append(words[i])
		else :
			others.append(words[i])
	xwords.sort()
	others.sort()
	return (xwords + others)



# C. sort_last
# Given a list of non-empty tuples, return a list sorted in increasing
# order by the last element in each tuple.
# e.g. [(1, 7), (1, 3), (3, 4, 5), (2, 2)] yields
# [(2, 2), (1, 3), (3, 4, 5), (1, 7)]
# Hint: use a custom key= function to extract the last element form each tuple.

# a tuple is a list of elements that may include different type, it is not allow to modify

#tup1 = ('physics', 'chemistry', 1997, 2000);
#tup1[0]
#tup2 = ('Hi!',) * 4	; deplicate Hi four times
#tup3 = tup1 + tup2;
#del	tup3
#3 in tup1; #check where 3 exist in tup1 or not	

def extract_last(tuple):
  # extract the last data of a tuple 		
	return tuple[-1]

def sort_last(tuples):
  # +++your code here+++
	tuplist = [];
	tups_sort = [];
	for i in range(len(tuples)):
		if len(tuples[i]):
			tuplist.append(extract_last(tuples[i]))
	tuplist.sort()
	for i in range(len(tuplist)):
		for j in range(len(tuples)):
			if extract_last(tuples[j]) == tuplist[i]:
				tups_sort.append(tuples[j])
	return tups_sort


# Simple provided test() function used in main() to print
# what each function returns vs. what it's supposed to return.
def test(got, expected):
  if got == expected:
    prefix = ' OK '
  else:
    prefix = '  X '
  print ('%s got: %s expected: %s' % (prefix, repr(got), repr(expected)))


# Calls the above functions with interesting inputs.
def main():
  print (match_ends)
  test(match_ends(['aba', 'xyz', 'aa', 'x', 'bbb']), 3)
  test(match_ends(['', 'x', 'xy', 'xyx', 'xx']), 2)
  test(match_ends(['aaa', 'be', 'abc', 'hello']), 1)

  print
  print (front_x)
  test(front_x(['bbb', 'ccc', 'axx', 'xzz', 'xaa']),
       ['xaa', 'xzz', 'axx', 'bbb', 'ccc'])
  test(front_x(['ccc', 'bbb', 'aaa', 'xcc', 'xaa']),
       ['xaa', 'xcc', 'aaa', 'bbb', 'ccc'])
  test(front_x(['mix', 'xyz', 'apple', 'xanadu', 'aardvark']),
       ['xanadu', 'xyz', 'aardvark', 'apple', 'mix'])

       
  print
  print (sort_last)
  test(sort_last([(1, 3), (3, 2), (2, 1)]),
       [(2, 1), (3, 2), (1, 3)])
  test(sort_last([(2, 3), (1, 2), (3, 1)]),
       [(3, 1), (1, 2), (2, 3)])
  test(sort_last([(1, 7), (1, 3), (3, 4, 5), (2, 2)]),
       [(2, 2), (1, 3), (3, 4, 5), (1, 7)])


if __name__ == '__main__':
  main()
