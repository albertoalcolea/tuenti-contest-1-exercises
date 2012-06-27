#! /usr/bin/python

import sys
import re


def calcular_primos(num):
    uno_len = 1
    nueve_len = 9
    
    for i in range (1, len(str(num))):
        uno_len = (uno_len * 10)
        nueve_len = (nueve_len * 10) + 9
        
    if uno_len == num:
        primos = eratostenes(nueve_len / 10)
    else:
        primos = eratostenes(nueve_len)

    return primos
    


# Criba de eratostenes
def eratostenes(num):
    nums=[]
    primes = []

    for i in range(2, num+1):
        nums.append(i)
            
    while nums != []:
        n = nums[0]
        primes.append(n)
        for j in nums:
            if ((j % n ) == 0):
                nums.remove(j)
    
    return primes


def num_espejo(num):
    origin = num
    result = 0
    
    while origin > 0:
        result = result * 10
        result = result + (origin % 10)
        origin = origin / 10
        
    return result


def emirps(primos, tabla_primos):
    list_emirps = []
    
    for num in primos:
        reverse_num = num_espejo(num)
        if reverse_num != num:
            if reverse_num in tabla_primos:
                list_emirps.append(num)
    return list_emirps


def primos_hasta_num(num, tabla_primos):
    primos = []
    
    encontrado = False
    aux = num
    
    while not encontrado and aux > 0:
        if aux in tabla_primos: 
            encontrado = True
        else:
            aux = aux - 1
    
    if encontrado:
        primos = tabla_primos[:tabla_primos.index(aux) + 1]
        
    return primos       


def parse_line(line):
    return re.findall('\d+', line)


def parse_input():
    data = []
    
    for line in sys.stdin:
		data.append(line.split("\n")[0])
        
    return data


# main()
def main():
    data = parse_input()
    for line in data:
        line_parsed = parse_line(line)
        num = int(line_parsed[0])
        tabla_primos = calcular_primos(num)
        primos = primos_hasta_num(num, tabla_primos)
        list_emirps = emirps(primos, tabla_primos)
        print sum(list_emirps)


if __name__ == '__main__':
    main()
