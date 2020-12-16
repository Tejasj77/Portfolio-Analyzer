import pandas as pd

main_frame = pd.read_csv('VP6938_tradebook_2019-03-01_to_2020-03-01.csv')
company = list(main_frame["tradingsymbol"])
attribute = list(main_frame["trade_type"])
quant = list(main_frame["quantity"])
price = list(main_frame["price"])

class make_me_a_dict(dict):
    def __init__(self):
        self = dict

    def add_key(self,key):
        self[key] = {}

main_dict = make_me_a_dict()
for iter in company:
    if iter not in main_dict.keys():
        main_dict.add_key(iter)

for a,b,c,d in zip(company,attribute,quant,price):
    if a in main_dict.keys():
        for k,v in main_dict.items():
            if a == k:
                if b in v.keys():
                    for k1,v1 in v.items():
                        if k1 == b:
                            temp = (int(c)*int(d)) + v1
                            v[k1] = temp
                else:
                    v[b] = int(c) * int(d)

print(main_dict)
for k,v in main_dict.items():
    temp_list = []
    for v1 in v.values():
        temp_list.append(v1)
    if len(temp_list)>1 :
        if temp_list[1]>temp_list[0]:
            print(f"Profit for {k} = " +str(temp_list[1] - temp_list[0]))
        elif temp_list[0]>temp_list[1]:
            print(f"Loss for {k} = " + str(temp_list[0] - temp_list[1]))
    else:
        print(f"Still holding stock {k} at {temp_list[0]}")
