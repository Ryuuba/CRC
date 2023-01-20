import crc_custom as crc
import sys
from bitarray import bitarray
import matplotlib.pyplot as plt

def main():
    # Program parameters
    filename = sys.argv[1]
    divisor = bitarray(sys.argv[2])
    burst_size = int(sys.argv[3])
    seed = int(sys.argv[4])
    iter_max = int(sys.argv[5])
    # Redundancy
    crc_len = len(divisor)-1
    zero_rem = bitarray(crc_len)
    zero_rem.setall(0)
    counter = 0 # actual number of repetitions
    # Computes CRC
    msg, crc_code = crc.compute(filename, divisor, crc_len)
    print(f'crc of text {filename} equals {crc_code}')
    # Evaluation of the CRC robustness
    probability = []
    for i in range(0, iter_max):
        # Burst error generation
        corrupted_msg = crc.burst_error(msg + crc_code, burst_size, seed + i)
        # Computes remainder
        rem = crc.mod2_div(corrupted_msg, divisor)
        # Determines whether rem equals zero or not
        success = 1 if rem[1:len(divisor)] != zero_rem else 0
        # Compute the number of times the CRC detects the error
        counter += success
        probability.append(counter/(i + 1))
    print(f'Probability = {probability[-1]}, {counter/iter_max}')
    plt.plot([i for i in range(1, iter_max+1)], probability, '-')
    plt.xscale('log')
    plt.show()

if __name__ == '__main__':
    main()
