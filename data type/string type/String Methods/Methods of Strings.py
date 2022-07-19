#Methods of Strings

s1='python is programming. python is beginner friendly code. python has simpler friendly code python'
s2='###sss00...python***'
s3='raju16111990'
s4='raju'
s5='RAJU'
s6=s1.count('python')
s7='programming \n python'
s8='ß'
s9='python#programming#book'
s10='0123456789'
s11='0xff'
s12=' '
s13='Raju mAnE'
s14='raju'
print('S.capitalize()',s1.capitalize())
print('S.casefold()',s8.casefold())

'''---------------------------------------------------------------------
It is similar to the lower() method, but the casefold()
method converts more characters into lower case.
For example, the German lowercase letter 'ß' is equivalent to 'ss' .
Since it is already lowercase, the lower() method would not convert it;
whereas the casefold() converts it to 'ss' .
---------------------------------------------------------------------------'''

print('S.center(width [, fill])',s2.center(40,'+'))
print('S.count(sub [, start [, end]])',s1.count('python',10,40))
print('S.endswith(suffix [, start [, end]])',s1.endswith('b',19,31))
print('S.find(sub [, start [, end]])',s1.find('python',10,40))
print('S.index(sub [, start [, end]])',s1.index('python',10,40))
print('S.isalnum()',s3.isalnum())
print('S.isalpha()',s4.isalpha())
print('S.ljust(width [, fill])',s2.ljust(20,'#'),'programming')
print('S.rjust(width [, fill])',s2.rjust(20,'#'))
print('S.lower()',s8.lower())
print('S.lstrip([chars])',s2.lstrip('#s0.'))
print('S.rstrip([chars])',s2.rstrip('*'))
print('S.rstrip([chars])',s2.rstrip('*'))
print('S.partition(sep)',s9.partition('#'))
print('S.rpartition(sep)',s1.rpartition('python'))

'''
-------------------------------------------------------------------------
Difference between partition() and rpartition()
The string module has various operative functions.
These being Python’s partition() and rpartition(). Now what’s the main difference between
these two? They both function in a similar manner. The only difference is that the partition()
method splits the string from the first occurrence of the separator,
while the rpartition() separates the string from the last occurrence of the separator.
-----------------------------------------------------------------------------'''

print('S.replace(old, new [, count])',s1.replace('python','PYTHON',s6))
print('S.rfind(sub [,start [,end]])',s7.rfind('python'))
print('S.rindex(sub [, start [, end]])',s7.rindex('python'))
print('S.rindex(sub [, start [, end]])',s7.rindex('python'))
print('S.split([sep [,maxsplit]])',s9.split('#',1))
print('S.rsplit([sep [,maxsplit]])',s9.rsplit('#',1))
print('S.isdecimal()',s10.isdecimal())#checks if all characters are decimal
print('S.isdigit()',s11.isdigit())
print('S.isidentifier()',s5.isidentifier())

print('S.isnumeric()',s10.isnumeric())

'''------------------------------------------------------------------------------
Definition and Usage
The isnumeric() method returns True if all the characters are numeric (0-9), otherwise False.

Exponents, like ² and ¾ are also considered to be numeric values.

"-1" and "1.5" are NOT considered numeric values, because all the characters in the string
must be numeric,and the - and the . are not.
-------------------------------------------------------------------------------------'''

'''a = "\u0030" #unicode for 0
b = "\u00B2" #unicode for ²
c = "10km2"
d = "-1"
e = "1.5"

print('\n\n',a.isnumeric())
print(b.isnumeric())
print(c.isnumeric())
print(d.isnumeric())
print(e.isnumeric())'''

print('\n\nS.isprintable()',s7.isprintable())
print('S.isspace()',s12.isspace())
print('S.title()',s7.title())
print('S.istitle()',s7.istitle())
print('S.splitlines([keepends])',s7.splitlines())
print('S.strip([chars])',s2.strip('#s0.*'))
print('S.swapcase()',s13.swapcase())
print('S.zfill(width)',s14.zfill(20))
