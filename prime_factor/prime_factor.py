
class PrimeFactors():
    @staticmethod
    def generate(n):
        results = []
        for i in range(2, n+1):
            if n > 1:
                while n % i == 0:
                    results.append(i)
                    n /= i
                i += 1
        return results
