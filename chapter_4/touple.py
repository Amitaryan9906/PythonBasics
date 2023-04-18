a=(10,2,3,3,4)
b=(2,5,8,86)
print(a)

print(len(a))
print('10' in a)
print(a.count(10))
print(a+b)
print(a.index(4))
print('-------------------------------------')
for x in a:
    if x%2 != 0:
     print(x)
print('<--------------------------------------------------------->')
# Function to check if a number is prime
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5)+1):
        if n % i == 0:
            return False
    return True

# Generate the first 10 prime numbers
count = 0
num = 2
while count < 10:
    if is_prime(num):
        print(num)
        count += 1
    num += 1


