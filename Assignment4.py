#print the letters in decreasing frequency

def most_frequent(s):
    d = {}
    import operator
    for i in s:
        count=s.count(i)
        d.update({i:count})
    sort=sorted(d.items(),reverse=True,key=operator.itemgetter(1))
    for i in sort:
        print(i)
        
s=input("Enter a string:")
(most_frequent(s))
       
