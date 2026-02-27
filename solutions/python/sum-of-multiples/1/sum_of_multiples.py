def sum_of_multiples(bound, mults):
    ns = (x for x in range(bound) if divisible_by(x, mults))
    return sum(ns)
def divisible_by(n, mults):
    return any(n % mult == 0 for mult in mults if mult)