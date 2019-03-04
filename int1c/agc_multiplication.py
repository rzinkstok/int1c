def complement(i):
    return int(not bool(i))


def copy_bit(source, dest, source_index, dest_index):
    dest[dest_index] = source[source_index]


def copy_bit_range(source, dest, source_range, dest_range=None):
    if dest_range is None:
        dest_range = source_range

    source_range = range(source_range[0], source_range[1]+1)
    dest_range = range(dest_range[0], dest_range[1]+1)
    for source_index, dest_index in zip(source_range, dest_range):
        copy_bit(source, dest, source_index, dest_index)


def int1c_sum(x, y, u, ci):
    pass



class Register(list):
    def __init__(self, size):
        list.__init__(self)
        self.size = size
        self.append(None)
        for i in range(self.size):
            self.append(0)
        self.dependant = None

    def clear(self):
        for i in range(self.size):
            self[i+1] = 0

    def __setitem__(self, key, value):
        list.__setitem__(self, key, value)
        if self.dependant:
            self.dependant._update()

    def __str__(self):
        return str(list(reversed(self[1:])))

    @property
    def sign(self):
        if self[15]:
            return -1
        return 1

    @property
    def value(self):
        s = 0
        for i in range(14):
            b = self[i+1]
            if self[15]:
                b = complement(b)
            s += b * pow(2, i)
        return self.sign * s


class ComplementRegister(Register):
    def __init__(self, source):
        Register.__init__(self, source.size)
        self.source = source
        self.source.dependant = self
        self._update()

    def _update(self):
        for i in range(self.size):
            self[i] = complement(self.source[i])


class SumRegister(Register):
    def __init__(self, size, x, y, ci):
        Register.__init__(self, size)
        self.x = x
        self.y = y
        self.ci = ci

    def _update(self):
        int1c_sum(self.x, self.y, self, self.ci)



EAC = True
A = Register(16)
B = Register(16)
C = ComplementRegister(B)
G = Register(16) # LEM System Manual 4-79: G has six bits
L = Register(16)
S = Register(12)
SQ = Register(7)
U = Register(16)
WL = Register(16)
X = Register(16)
Y = Register(16)
Z = Register(16)

CIFF = Register(1)
SCFF = Register(2)
BR = Register(2)


ADDRESS_MAP = {

}

def A2X():
    copy_bit_range(A, X, (1, 16))


def CI():
    pass


def G2LS():
    # Is this right? See G register comment
    copy_bit_range(G, X, (15, 16), (15, 16))
    copy_bit_range(G, X, (4, 14), (2, 12))
    copy_bit(G, X, 1, 1)


def L16():
    L[16] = 1


def L2GD():
    copy_bit(L, G, 16, 16)
    copy_bit_range(L, G, (1, 14), (2, 15))
    G[1] = 1


def NEACOF():
    EAC = False


def NEACON():
    EAC = True


def NISQ():
    # Bit complicated...
    pass


def R1C():
    # Put octal 177776 in WL's
    # That is 1111111111111110 in binary
    WL[0] = 0
    for i in range(2, 17):
        WL[i] = 1


def RA():
    copy_bit_range(A, WL, (1, 16))


def RB():
    copy_bit_range(B, WL, (1, 16))


def RB1():
    WL[0] = 1
    for i in range(2, 17):
        WL[i] = 0


def RC():
    copy_bit_range(C, WL, (1, 16))


def RG():
    copy_bit_range(G, WL, (1, 16))


def RL():
    WL[16] = L[16]
    WL[15] = L[16]
    copy_bit_range(L, WL, (1, 14))


def RSC():
    reg = ADDRESS_MAP[S.value]
    copy_bit_range(reg, WL, (1, 16))


def RU():
    pass


for i in range(1, 17):
    G.clear()
    X.clear()
    G[i] = 1
    G2LS()
    print(f"{i:02}", X)

R1C()
print(WL)