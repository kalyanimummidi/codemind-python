p,r,t=map(int,input().split())
compoundintrest=(p*(1+r/100)**t)
print("%0.2f"%compoundintrest)