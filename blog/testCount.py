f = open('count.txt','r')
counting = int(f.readline())
f.close()
print counting

w = open('count.txt','w')
w.write(str(counting + 1))
w.close()

