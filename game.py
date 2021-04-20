from random import seed
from random import randint

# Seed Random Number Generator
seed(1)

# Generate the Random Number
for _ in range(1):
	randomNumber = randint(1, 6)

print(randomNumber)