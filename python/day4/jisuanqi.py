#! /usr/bin/env python
x = int(input("first:"))
o = input('operator:')
y = int(input("second:"))

operator = {
    '+':x+y,
    '-':x-y,
    'x':x*y,
    '/':x / y
}
result = operator.get(o,'please input +|-|*|')
print(result)