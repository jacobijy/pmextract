kFnvPrime_64 = 0x00000100000001b3
kOffsetBasis_64 = 0xCBF29CE484222645


def hashFnv1_64(input: bytes, hash=kOffsetBasis_64):
    for c in input:
        hash *= kFnvPrime_64
        hash ^= c
    return hash

def hashFnv1_64str(input: str, hash=kOffsetBasis_64):
    for c in input:
        hash *= kFnvPrime_64
        hash ^= ord(c)
    return hash

def hashFnv1a_64(input: bytes, hash=kOffsetBasis_64):
    for c in input:
        hash ^= c
        hash *= kFnvPrime_64
    return hash

def hashFnv1a_64str(input: str, hash=kOffsetBasis_64):
    for c in input:
        hash ^= ord(c)
        hash *= kFnvPrime_64
    return hash


kFnvPrime_32 = 0x01000193;
kOffsetBasis_32 = 0x811C9DC5;

def hashFnv1_32(input: bytes, hash=kOffsetBasis_32):
    for c in input:
        hash *= kFnvPrime_32
        hash ^= c
    return hash


def HashFnv1a_32(input: bytes, hash=kOffsetBasis_64):
    for c in input:
        hash ^= c
        hash *= kFnvPrime_32
    return hash
