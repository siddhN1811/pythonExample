# Escape Sequences Represent Special Characters
s1='raju\nmane'
print('Newline:',s1,len(s1))
s2='raju\\mane'
print('Backslash:',s2)
s3='raju\'mane'
print('Single quote:',s3)
s4='raju\"mane'
print('double quote:',s4)
s5='raju\amane'
print('bell :',s5)
s6='raju\bmane'
print('Backspace:',s6)
s7='raju\fmane'
print('Formfeed:',s7)
s8='raju\rmane' 
print('Carriage return:',s8)
s9='raju\tmane' 
print('Horizontal tab:',s9)
s10='raju\vmane' 
print('Vertical tab:',s10)
