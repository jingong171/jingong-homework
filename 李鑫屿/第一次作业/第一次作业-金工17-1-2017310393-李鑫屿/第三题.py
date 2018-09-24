shuixianhua=[]
for a in range(1,10):
  for b in range(10):
    for c in range(10):
      if a*a*a + b*b*b + c*c*c == 100*a + 10*b + c:
        shuixianhua.append(100*a + 10*b + c)
for a in shuixianhua:
  if a == shuixianhua[-1]:
    print(a)
  else:
    print(a, end = ',')
