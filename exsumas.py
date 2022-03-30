#Suma de dos numeros enteros:
a = int(input('Ingresa el primer numero entero: '))
b = int(input('ingresa el segundo numero entero: '))


def suma(a,b):
    return a + b
print ('El resultado es:', a + b)



#Suma de numeros de un arreglo:

nums= [1,2,3,4,5,6,10]
sum = 0

for i in range(0,len(nums)):
    sum = sum + nums[i]

print('El resultado es:', sum )






