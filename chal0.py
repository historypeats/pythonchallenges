#!/usr/bin/env python

# Challenge URL: http://www.pythonchallenge.com/pc/def/0.html

NEXT_URL = 'http://www.pythonchallenge.com/pc/def/PLACEHOLDER.html'


def main():
	''' main '''
	solution = NEXT_URL.replace('PLACEHOLDER', str(2**38))
	print 'Solution: {0}'.format(solution)

if __name__ == '__main__':
	main()
