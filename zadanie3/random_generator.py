import random
import math

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def main():
    iterations = 1000000
    coprime_count = 0

    for _ in range(iterations):
        x = random.randint(1, 2**31 - 1)
        y = random.randint(1, 2**31 - 1)

        if gcd(x, y) == 1:
            coprime_count += 1

    probability = coprime_count / iterations
    pi_approximation = math.sqrt(6.0 / probability)

    print(f"Ilośc iteracji: {iterations}")
    print(f"Liczba par wzajemnie pierwszych: {coprime_count}")
    print(f"Przybliżona wartość pi: {pi_approximation}")

if __name__ == "__main__":
    main()
