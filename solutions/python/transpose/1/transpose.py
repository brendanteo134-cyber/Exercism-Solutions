import itertools
def transpose(s):
    a = itertools.zip_longest(*s.splitlines(), fillvalue='$')
    return '\n'.join(''.join(w).rstrip('$').replace('$', ' ') for w in a)