kFnvPrime_64 = 0x00000100000001b3
kOffsetBasis_64 = 0xCBF29CE484222645


def hashFnv1_64(input: bytes, hash=kOffsetBasis_64):
    for c in input:
        hash *= kFnvPrime_64
        hash ^= c
    return hash


def HashFnv1_64(input: bytes, hash=kOffsetBasis_64):
    for c in input:
        hash *= kFnvPrime_64
        hash ^= c
    return hash
