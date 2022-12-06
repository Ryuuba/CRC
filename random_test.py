from sys import argv
from numpy.random import Generator, MT19937

seed = int(argv[1])
rng = Generator(MT19937(seed))
print([rng.integers(0, 10) for i in range(0, 10)])

