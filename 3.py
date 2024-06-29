a = [int(x) for x in open("17.txt")]
m = max([x for x in a if x%100==68]) 
ans = []
for i in range(len(a)-3):
  if (a[i] +a[i+1] + a[i+2] +a[i+3]) > m\
  and ((10 <= a[i] <= 99) + (10 <= a[i+1] <= 99) + (10 <= a[i+2] <= 99) + (10 <= a[i+3] <= 99)) == 1 or ((10 <= a[i] <= 99) + (10 <= a[i+1] <= 99) + (10 <= a[i+2] <= 99) + (10 <= a[i+3] <= 99)) == 4:
    ans.append(a[i] + a[i+1] + a[i+2] + a[i+3]) 
print(len(ans)) 
