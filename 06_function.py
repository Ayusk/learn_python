def fact_iter(n):
    prod = 1
    for i in range(n):
        prod = prod * (i+1)
    return prod

def fact_rec(n):
    if n==0 or n==1:
        return 1
    else: return n*fact_rec(n-1)

print(fact_rec(5))
print(fact_iter(5))

def recu_sum(n):
    if n==0: return 0;
    else: return n+recu_sum(n-1)

print(recu_sum(5))

n=3
for i in range(n):
    print("*"*(n-i))

def remove_word(string,word):
    newstr = string.replace(word,"")
    return newstr.strip()

new_str = remove_word("    hello ayush ji   ","ji")
print(new_str)