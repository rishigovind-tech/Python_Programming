import fractions

f1=fractions.Fraction(1,2)
print(f1)

f2=fractions.Fraction(0.3)
print(f2)

f3=fractions.Fraction('0.2')
print(f3)

f2=f2.limit_denominator(10)
print(f2)

print(f1+f2)
print(f2-f1)
print(f2*f1)
print(f2/f1)


