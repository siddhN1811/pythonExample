#String Method Examples: Changing Strings II
s1='pyon'
print("s1='python'",s1)
print("s1='python'",s1[:2])
print("s1='python'",s1[2:])
print("s1='python'",s1[:2]+'th'+s1[2:])
print()
s2='python prograxxing'
print("s2='python prograxxing'",s2.replace('xx','mm'))
s3='aa$bb$cc$dd'
print("s3='aa$bb$cc$dd'",s3.replace('$',' ',2))
s4='xxxxSPAMxxxxSPAMxxxx'
s5='EGGS'
where=s4.find('SPAM')
print("s4='xxxxSPAMxxxxSPAMxxxx'",where)
print("s4='xxxxSPAMxxxxSPAMxxxx'",s4[:4]+s5+s4[(where+len(s5)):])
s6='prograxxing'
print("s6='prograxxing'",s6)
l1=list(s6)
print("s6='prograxxing' list",l1)
print("s6='prograxxing' list",l1[6:8])
l1[6:8]=['m','m']
print("s6='prograxxing' list",l1[6:8])
print("s6='prograxxing' list",l1)
print("s6='prograxxing'",s6)

