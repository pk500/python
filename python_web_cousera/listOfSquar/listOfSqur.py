no=[i**2 for i in range(1,100)]
f=open("output.txt","w")
for n in no:
    f.write(str(n)+"\n")
f.close