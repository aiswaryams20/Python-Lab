def circulate(c,n):
  for i in range (1,n+1):
    d=c[i:]+c[:i]
    print("Circulate","=",d)
  return
c=[0,1,2,3,4,5]
n=int(input("Enter n :"))
circulate (c,n)
