import math


class Int1C(object):
    def __init__(self, value, width=16):
        self.width = width
        if isinstance(value, str):
            self.value = self.to_dec(value)
            self.bits = value
        else:
            self.value = int(value)
            self.bits = self.to_bin(value)

        if not self.in_range:
            raise ValueError(f"Value {value} out of range for {width}-bit ones' complement")

    @property
    def range(self):
        r = pow(2, self.width-1) - 1
        return -r, r

    @property
    def in_range(self):
        minval, maxval = self.range
        return minval <= self.value <= maxval

    def to_bin(self, value):
        sign = math.copysign(1.0, value)
        value = int(value)

        if not self.in_range:
            raise ValueError(f"Value {value} out of range for {self.width}-bit ones' complement")

        a = abs(value)
        bs = "{:0" + str(self.width) + "b}"
        b = bs.format(a)
        if sign < 0:
            return self.complement(b)
        return b

    def to_dec(self, bvalue):
        if len(bvalue) != self.width:
            raise ValueError(f"Bit count of value is incorrect for {self.width}-bit ones' complement")
        if bvalue.startswith("1"):
            return -int(self.complement(bvalue), 2)
        return int(bvalue, 2)

    @staticmethod
    def complement(bvalue):
        return "".join([str(int(not bool(int(b)))) for b in bvalue])

    @property
    def negative(self):
        return self.bits.startswith("1")

    @property
    def sign(self):
        if self.negative:
            return "-"
        return ""

    @property
    def shift_char(self):
        if self.negative:
            return "1"
        return "0"

    def lshift(self, n):
        return Int1C(self.bits[n:] + self.shift_char * n, self.width)

    def rshift(self, n):
        return Int1C(self.shift_char * n + self.bits[:-n], self.width)

    def __str__(self):
        return f"Int1C {self.bits} [{self.sign}{abs(self.value)}]"

    def __invert__(self):
        return Int1C(self.complement(self.bits), self.width)

    def __neg__(self):
        return ~self

    def __abs__(self):
        if self.negative:
            return ~self
        return self

    def add_without_end_around_carry(self, bvalue1, bvalue2):
        result = ""
        carry = 0
        # print()
        for b1, b2 in reversed(list(zip(bvalue1, bvalue2))):
            b1, b2 = int(b1), int(b2)

            full_sum = b1 + b2 + carry
            s = full_sum % 2
            carry = full_sum // 2
            # print(f"{b1} + {b2} = {s} with carry {carry}")
            result = f"{s}{result}"
        return result, carry

    def __add__(self, other):
        neg1 = self.negative
        neg2 = other.negative

        result, carry = self.add_without_end_around_carry(self.bits, other.bits)

        if carry:
            result, carry = self.add_without_end_around_carry(result, Int1C(carry, width=self.width).bits)

        neg = result.startswith("1")
        if (neg1 == neg2) and (neg != neg1):
            raise OverflowError(f"Overflow in {self.width}-bit ones' complement addition of {self.value} and {other.value}")

        return Int1C(result, self.width)

    def __sub__(self, other):
        return self + -other

    def __mul__(self, other):
        n = max(self.width, other.width)
        multiplier = Int1C(other.value, 2*n)
        multiplicand = Int1C(self.value, 2*n)
        result = Int1C(0, 2*n)
        for b in reversed(list(multiplier.bits)):
            if b == "1":
                print(multiplicand)
                result = result + multiplicand
                pass
            multiplicand = multiplicand.lshift(1)
        print("      " + "-"*(2*n) + " +")
        return result


if __name__ == "__main__":
    x = Int1C(-7, 4)
    y = Int1C(7, 4)
    print(x)
    print(y)
    z = x * y
    print(z)
