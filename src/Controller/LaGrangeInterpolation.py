import sys
from .Field import Field
field = Field(208351617316091241234326746312124448251235562226470491514186331217050270460481)
class LagrangeInterpolation:
    """
    Class that brings statics methods for works that should be done without 
    taking creating the same objects as Encryption needs
    """
    
    @staticmethod  
    def lagrange_polynomial(i, x_points, x):
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
                
        return field.division(num, dem) # (X - x_j) (x_i - x_j)^-1 -> where (x_i - x_j)^-1 is the inverse multiplicative
    
    @staticmethod
    def reconstruct_secret(shares, x):
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
            poly = LagrangeInterpolation.lagrange_polynomial(x_points[i], x_points, x)
            
            product = (poly * y_points[i]) % field.get_prime()
            
            res += product
            
        return res % field.get_prime()