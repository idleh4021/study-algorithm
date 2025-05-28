a = int(input())
arr = [str(i+1) if (i+1)%6!= 0 else str(i+1) +' Go!'  for i in range(a)]
print((' '.join(arr)+' Go!').replace(' Go! Go!',' Go!'))