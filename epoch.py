import statistics
 
x=[1,2,3,4,5,6]
y=[5,4,6,5,6,7]
xy = [x[i]*y[i] for i in range(len(x))]
xx = [x[i]*x[i] for i in range(len(x))]

m=(statistics.mean(x)*statistics.mean(y)-statistics.mean(xy))/(statistics.mean(x)*statistics.mean(x)-statistics.mean(xx))
print("m="+str(m))
b=statistics.mean(y)-m*statistics.mean(x)
print("b="+str(b))