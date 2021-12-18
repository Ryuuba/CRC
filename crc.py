from bitarray import bitarray
import random

def burst_error(msg: bitarray, n: int, seed: int) -> bitarray:
    """
    This function generates a error burst of length n
    Arguments:
    msg: A bitarray holding the message to be corrupted
    n: The length of the error burst
    seed: An integer to set the RNG (MT19937)
    Returns:
    A corrupted message 
    """
    random.seed(seed)
    start = random.randint(0, len(msg)-n)
    msg[start] ^= 1
    msg[start+n-1] ^= 1
    for i in range (start + 1, start + n - 1):
        if random.random() > 0.5:
            msg[i] ^= 1
    return msg

def mod2_div(dividend: bitarray, divisor: bitarray) -> bitarray:
    """
    This function performs mod-2 divison (without carry)
    Arguments:
    dividend: a bitarray holding the dividend
    divisor: a bitarray holding the divisor
    returns:
    remainder: a bitarray holding the divider
    """
    divisor_len = len(divisor)
    end = len(dividend)
    rem = dividend[0 : divisor_len]
    for i in range(divisor_len, end + 1):
        if rem[0]:
            rem ^= divisor
        if i < end:
            rem <<= 1 
            rem[-1] = dividend[i]    
    return rem

def compute(filename: str, divisor: bitarray, len_crc: int) -> tuple[bitarray, bitarray]:
    """
    This function computes the CRC of a plain-text file 
    arguments:
    filename: the file containing the plain-text
    divisor: the generator polynomium
    len_crc: The number of redundant bits (r)
    """
    redundancy = len_crc * bitarray('0')
    bin_file = bitarray()
    len_p = len(divisor)
    with open(filename, 'rb') as file:
        bin_file.fromfile(file)
    cw = bin_file + redundancy
    rem = mod2_div(cw, divisor)
    return bin_file, rem[len_p-len_crc : len_p]
        
"""
Prueba del funcionamiento de la función cyclic_redundacy_check
http://www.sunshine2k.de/coding/javascript/crc/crc_js.html
"""

