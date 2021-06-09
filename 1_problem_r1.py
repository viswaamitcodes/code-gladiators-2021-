def result(sample,virus):
    sa=len(sample)
    vi=len(virus)
    s=v=0
    while s<sa and v<vi:
        if sample[s]==virus[v]:
            s+=1
        v+=1
    return s==sa
    virus=input()
    for i in range(int(input())):
        sample=input()
        if result(sample,virus):
            print("POSITIVE")
        else:
            print("NEGATIVE")
