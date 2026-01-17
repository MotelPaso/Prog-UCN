"""
Created on Mon Apr 28 16:44:37 2025
"""

def factorial(a):
    multi = 1 # balatro
    for i in range(1,a+1):
        multi = multi * i
    return multi
    
num = int(input('Ingrese su numero!: '))
multi = factorial(num)
print(f'tu multi es {multi}')

