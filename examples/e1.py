from autoqubo import Binarization, SamplingCompiler, SearchSpace, Utils
import dynex
import dimod


s = SearchSpace()
s.add('a', Binarization.uint, 3)
s.add('b', Binarization.uint, 3)


def ff(a, b):
    return 2 * a + 3 * b


q, offset = SamplingCompiler.generate_qubo_matrix(ff, s.size, s)

print(q)

x = s.encode({'a': 3, 'b': 6})

print(s.decode(x))
print(s.decode_dict(x))

sampleset = dynex.sample_qubo(q, offset, num_reads=1024, annealing_time=200)
print(sampleset)
