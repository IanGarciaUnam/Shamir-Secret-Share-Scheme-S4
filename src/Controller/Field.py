class Field():
    """
    A class to use some methods for finite fields arithmetic
    """
    def __init__(self, prime):
        """
        Constructs a finite field given a prime number

        Args:
            prime (int)-- a prime number
           
        """
        self.p = prime
        """  p(int) = prime assigned """
        
    def extended_euclides(self, a, b):
        """
        Extended Euclide algorith to find the gcd from a and b

        Args:
            a (int): number to find gcd with b
            b (int): number to find gcd with a

        Returns:
            int : gcd(a,b)
        """
        x = 0
        last_x = 1
        y = 1
        last_y = 0
        while b != 0:
            quot = a // b
            a, b = b, a % b
            x, last_x = last_x - quot * x, x
            y, last_y = last_y - quot * y, y
        return last_x, last_y
    
    def division(self, num, denom):
        """
        Modular divison using finite fields arithmetic

        Args:
            num (int): numerator
            denom (int): denominator

        Returns:
            int: modular division between num and denom
        """
        inverse, _ = self.extended_euclides(denom, self.p)
        return num * inverse
    
    def get_prime(self):
        """
        Return the prime number used

        Returns:
            int: prime number used
        """
        return self.p