n=[0,0,0,0,0]
d=0
a=[]
for i in n:
  c=0
  for j in n:
    if i==j:
      c+=1
  
  if c>1 and i not in a:
    a.append(i)
    print(a)
    d+=1

print(int(d))
