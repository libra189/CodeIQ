# coding: utf-8

# arctan(1/n)をTaylor展開で求める
def arctan(p, n):
    x = p/n
    nn = n*n
    c = 1
    s = x
    k = 1
    while x > 0:
        x /= nn
        k += 2
        c = -c
        s += c*(x/k)
    return s

# 円周率を求める
# 整数部分「3」も含む仮数表現の長整数で返します
def pi_mantissa(digit, redund=10):
    p = 10**digit
    q = 10**redund
    p *= q
    pi = 4*(12*arctan(p,18)+8*arctan(p,57)-5*arctan(p,239))
    pi /= q
    return pi

# アルファベット・インデックス表作成
def indexmap():
	indexmap = {}

	for i in range(ord('a'), ord('z')+1):
		num = str(i - ord('a'))
		if(int(num) < 10):
			num = '0' + num

		indexmap[num] = chr(i)
	return indexmap

if __name__ == '__main__':

	word = [i for i in "raspberry"]
	alpha_index = indexmap()

	digit = 1000
	pi = str(pi_mantissa(digit))[1:]

	i = 0
	count = 0
	while i <= len(pi):
		num = pi[i:i+2]
		count = count + 1 if((alpha_index.has_key(num)) and (alpha_index[num] in word)) else count + 0
		i += 2

	print(count)