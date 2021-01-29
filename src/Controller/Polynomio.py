import random
import functools
from numpy.polynomial.polynomial import Polynomial as Poly
from .Field import Field
import numpy.polynomial.polynomial as polynomial

class Lagrange_Polynomial():
    """
    A class used to apply Lagrange Interpolation method to find out secret

    Args:
        object ([type]): [description]
    """
    def __init__(self, prime_number, k, n,key):
        """
        Constructs Lagrange Polymial given a prime to use finite field arithmetic
        
        Args:
            prime_number (int): prime number to use finite field arithmetic
            k (int) : minimun number of shares to reconstruct the polynomial
            n (int) : number of shares to generate
            key (int) : secret to save
        """
        self.field_p = Field(prime_number)
        """ (Field) : Object Field"""
        self.key = key
        """ key as the secret given"""
        self.partial_randomNumber = functools.partial(random.SystemRandom().randint, 0)
        """ Random Number"""
        self.k = k
        """ Polynomial Degree"""
        self.n = n
        """ Maximum of shares to be generated"""
        self.polynomial = Poly(self.generate_random_poly())
        """ Polinomio generated"""
        
        
    def generate_random_poly(self):
        """
        Generate a random polynomial

        Returns:
            list: List of coeficcients of a polynomial
        """
        poly = [self.partial_randomNumber(self.field_p.get_prime() - 1) for i in range(self.k)]
        
        poly[0] = self.key # Key
        
        return poly
        
    def generate_random_shares(self):
        """
        Generates random shares from our random polynomial

        Returns:
            list: A list of tuples (x,y), where x is the point, and y = P(x)
        """
        x_points = []
        for _ in range(1, self.n + 1):
            x_points.append(self.partial_randomNumber(self.field_p.get_prime() - 1))
        return [
            # We use % self.p below to take advantage of finite field arithmetic
            (x_points[i], polynomial.polyval(x_points[i], self.polynomial.coef) % self.field_p.get_prime())
            for i in range(len(x_points))
        ]
        
    def get_poly(self):
        """
        Return the random polynomial

        Returns:
            Polynomial: Random Polynomial
        """
        return self.polynomial
            
    def lagrange_polynomial(self, i, x_points, x):
        """
        Reconstructs a Lagrange basis polynomial

        Args:
            i (int): [x_i]
            x_points (list): vector of x points
            x (int): value to find

        Returns:
            int: A Lagrange basis polynomial
        """
        num, dem = 1, 1 # We calculate each separately to avoid inexcat division
        for j in range(len(x_points)):
            if x_points[j] != i:
                num *= x - x_points[j] # X - x_j
                dem *= (i-x_points[j]) # x_i - x_j
                
        return self.field_p.division(num, dem) # (X - x_j) (x_i - x_j)^-1 -> where (x_i - x_j)^-1 is the inverse multiplicative
    
    def reconstruct_secret(self, shares, x):
        """
        Reconstructs the secret from a given list of shares

        Args:
            shares (list): share to use to reconstruct the secret
            x (int): term to find

        Raises:
            ValueError: in case that the number of shares is not enough to reconstruct the secret

        Returns:
            int: the secret
        """
        res = 0
        
            
        x_points, y_points = zip(*shares)
        for i in range(len(x_points)):
            poly = self.lagrange_polynomial(x_points[i], x_points, x)
            
            product = (poly * y_points[i]) % self.field_p.get_prime()
            
            res += product
            
        return res % self.field_p.get_prime()
            
                
        



        