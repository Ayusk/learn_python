dic = {"ayush":"kumar",
        "gaurav":"nager",
        "anurag":"parothia",
        "marks":[23,34,45],
        "new_dic": {'ak':"ha"},
        1:2}
print(dic['ayush'])
print(dic['marks'])
print(dic['new_dic']['ak'])

print(list(dic.keys()))
print(dic.values())
print(dic.items())
print(dic)

upd_dic = {"akash":"mishra"}
dic.update(upd_dic)
print(dic)

s=set()   #empty set
s1={1,2,3,4}

print(type(s1))

s2={}
print(type(s2))         #empty dictionary
