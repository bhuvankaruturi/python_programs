# statistics module consists of various aggregate functions

import statistics as st

xlist = [1,5,3,8,5,2,9,10,3,8,2,1,9,8,7,5,4,3,2,2]

x = st.mean(xlist)
print('mean',x)

x = st.median(xlist)
print('median',x)

x = st.mode(xlist)
print('mode',x)

x = st.stdev(xlist)
print('standard deviation',x)

x = st.variance(xlist)
print('variance',x)


