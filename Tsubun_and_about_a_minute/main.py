#!D:\Python\Python34
# -*- coding: utf-8 -*-

# CodeIQ:https://codeiq.jp/q/1385
# 通分と約分を実装しよう

import fractions


def main():
	numerator = [[1, 2], [2, 3], [3, 1], [3, 5], [2, 2]]
	denominator = [[3, 7], [8, 5], [10, 6], [4, 8], [5, 3]]

	for i in range(len(denominator)):
		n1 = fractions.Fraction(numerator[i][0], denominator[i][0])
		n2 = fractions.Fraction(numerator[i][1], denominator[i][1])
		print(n1, " + ", n2, " = ", n1 + n2)

if __name__ == '__main__':
	main()
