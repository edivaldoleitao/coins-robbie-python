def mdc(a, b):
  while True:
    r = a % b
    if r == 0:
      break
    else:
      a = b
      b = r
  return b


def is_prime(num):
  primo = True
  cont = 0
  for c in range(1, num + 1):
    verifica = mdc(num, c)
    if verifica > 1:
      cont += 1
    if cont >= 2:
      primo = False
      break
  return primo

# Main



M = int(input())

coins = list()

for c in range(0, M):
  coin = int(input())
  coins.append(coin)

N  = int(input())

soma = 0

for s in range(0, len(coins), N):
  soma += coins[s]

primo = is_prime(soma)


if primo:
  print('You’re a coastal aircraft, Robbie, a large silver aircraft.')
else:
  print("Bad boy! I’ll hit you.")
print(soma)


