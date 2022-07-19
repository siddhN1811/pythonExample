#Advanced Formatting Expression Examples
s1=+1234
s2='integer %d, %+10d, %+010d'  %(s1,s1,s1)
print('s2',s2)
s3=1.12e-1
s4='%e | %f | %g' % (s3,s3,s3)
print('s4',s4)
s5=1.23456789
s6='%-6.2e | %05.2f | %+06.1g' % (s3,s3,s3)
print('s6',s6)
s7='%f, %.2f, %*.*f' % (1/3.0, 1/3.0,10, 4, 1/3.0)
print('s7',s7)
