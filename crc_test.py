import crc
import sys
from bitarray import bitarray

def main():
    filename = sys.argv[1]
    divisor = bitarray(sys.argv[2])
    r = int(sys.argv[3])
    n = int(sys.argv[4])
    seed = int(sys.argv[5])
    iter_max = int(sys.argv[5])
    zero_rem = bitarray(r)
    zero_rem.setall(0)
    counter = 0
    msg, crc_code = crc.compute(filename, divisor, r)
    for i in range(0, iter_max):
        corrupted_msg = crc.burst_error(msg + crc_code, n, seed+i)
        rem = crc.mod2_div(corrupted_msg, divisor)
        success = 1 if rem[1:len(divisor)] != zero_rem else 0
        counter += success
    print('Probability = {}'.format(counter/iter_max))

if __name__ == '__main__':
    main()