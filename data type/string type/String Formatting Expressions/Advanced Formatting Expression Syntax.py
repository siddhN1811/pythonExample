#Advanced Formatting Expression Syntax
s1='my name is %s' %('ganesh')
print('String (or any object’s str(X) string): ',s1)
s2='charcter %c' %(97)
print('Character (int or str): ',s2)
s3='decimal %d' %(87)
print('Decimal (base-10 integer): ',s3)
s4='Integer %i' %(87)
print('Integer: ',s4)
s5='Octal %o' %(0o21)
print('Octal integer (base 8): ',s5)
s6='Hex %d' %(0xf)
print('Hex integer (base 16): ',s6)
s7='exponent %e' %(1.2e-2)
print('Floating point with exponent, lowercase: ',s7)
s8='exponent %E' %(1.2e-2)
print('Floating point with exponent, uppercase: ',s8)
s9='Floating-point %f,lowercase' %(12.34567890123456789)
print('Floating-point decimal: ',s9)
s10='Floating-point %F,uppercase' %(12.34567890123456789)
print('Floating-point decimal: ',s10)
s11='Floating-point e or f %g' %(1.2e-2)
print('Floating-point e or f: ',s11)
