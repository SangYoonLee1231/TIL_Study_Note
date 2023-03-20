
from functools import reduce

def gen_record(data_str):
    for line in data_str.split('\n'):
        if line.strip():
            yield line.strip().split(',')

def gen_frequent_1_itemset(datas, min_count):
    item_list = {}
    for data in datas:
        for item in data:
            if item not in item_list:
                item_list[item] = 1
            else:
                item_list[item] += 1

    nums_of_data = len(datas)
    for item, count in item_list.items():
        if count / nums_of_data >= min_count:
            yield (item, )


data_str = 'apple,beer,rice,chicken\n'
data_str += 'apple,beer,rice\n'
data_str += 'apple,beer\n'
data_str += 'apple,mango\n'
data_str += 'milk,beer,rice,chicken\n'
data_str += 'milk,beer,rice\n'
data_str += 'milk,beer\n'
data_str += 'milk,mango'

# dataset = list(gen_record(data_str))
# frequent_1_itemsets_1 = list(gen_frequent_1_itemset(dataset, 0.5))
# frequent_1_itemsets_2 = list(gen_frequent_1_itemset(dataset, 0.7))

# print(sorted([itemset[0] for itemset in frequent_1_itemsets_1]))
# # Output: ['apple', 'beer', 'milk', 'rice']

# print(sorted([itemset[0] for itemset in frequent_1_itemsets_2]))
# # Output: ['beer']


# YOUR CODE MUST BE HERE
# from itertools import combinations
# from functools import reduce

# def gen_frequent_2_itemset(dataset, min_sup):
#     """
#     Apriori Algorithm을 사용하여 주어진 데이터에서 빈번하게 등장하는 '2개의 아이템 묶음'들을 찾습니다.
#     이 때 '빈번하게 등장한다'고 판단하는 기준은 역시 min_sup 변수의 값이 됩니다.
#     """
#     # Candidate 1-itemset
#     item_list = {}
#     for data in dataset:
#         for item in data:
#             if item in item_list:
#                 item_list[item] += 1
#             else:
#                 item_list[item] = 1
    
#     # Frequent 1-itemset
#     frequent_items = set(
#         item
#         for item, count in item_list.items()
#         if count/len(dataset) >= min_sup
#     )
    
#     # Candidate 2-itemset
#     for itemset in combinations(frequent_items, 2):
#         count = reduce(
#             lambda count, dataset: count + (set(itemset).issubset(dataset)),
#             dataset, 0
#         )
#         if count/len(dataset) >= min_sup:
#             yield tuple(sorted(itemset))


# dataset = list(gen_record(data_str))
# print(sorted(list(gen_frequent_2_itemset(dataset, 0.5))))


# # YOUR CODE MUST BE HERE
# from itertools import combinations
# from collections import defaultdict

# def gen_frequent_3_itemset(datas, min_count):
#     item_counts = defaultdict(int)
#     for data in datas:
#         for item in data:
#             item_counts[item] += 1

#     frequent_items = set(item for item in item_counts if item_counts[item] / len(datas) >= min_count)
#     frequent_2_itemsets = set(combinations(frequent_items, 2))

#     for data in datas:
#         for itemset in combinations(data, 3):
#             if set(itemset).issubset(frequent_items):
#                 yield tuple(sorted(itemset))

#     for itemset in combinations(frequent_items, 3):
#         support = 0
#         for data in datas:
#             if set(itemset).issubset(data):
#                 support += 1
#         if support / len(datas) >= min_count:
#             yield tuple(sorted(itemset))

# dataset = list(gen_record(data_str))
# print(sorted(list(gen_frequent_3_itemset(dataset, 0.1))))



from collections import Counter
from itertools import combinations
def gen_frequent_2_itemset(n2,min_sup):
    print("원문은", n2)
    result1=list(gen_frequent_1_itemset(n2,min_sup))#이전에서 걸러진 1개짜리 리스트
    print(result1)
    newlist=list(combinations(result1,2))#걸러진거에서 2개씩 짝지어 만들어진 2개짜리 새로운 리스트
        #print("result1 1개", result1)
        #print("newlist 2개", newlist) #각 단어가 몇번씩 등장했는지 계산함
        
    seplist=Counter()
    for i in range(len(n2)):#하나씩 분리시켜 카운터 딕셔너리로 만듦
        seplist+=Counter(n2[i])
        #print("분리된 거", seplist)
        
    good=Counter()
    for i in range(len(result1)):#1개짜리의 포함갯수
        good.setdefault(result1[i],seplist.get(result1[i]))
    print("1개짜리가 포함된 갯수 good ",good)
        
    result1v=Counter()
    for i in range(len(newlist)):#2개짜리의 포함갯수
        for u in range(len(n2)):
            #print("각각",newlist[i]," ", n2[u])
            if newlist[i][0]in n2[u] :
                if newlist[i][1] in n2[u]:
                    result1v[newlist[i]]+=1
    print("2개짜리가 포함된 갯수 result1v ", result1v)    

    real=()
    rreal=[]
    for i in range(len(newlist)):
        perab=result1v[newlist[i]]/len(n2)
        #print(newlist[i]," ", perab)
        if perab >= min_sup:
            #print("넘는 리스트는 ", newlist[i]," ",perab)
            real+=newlist[i]
    for i in range(0,len(real),2):
        rreal.append(real[i:i+2])

    return sorted(rreal)



dataset = list(gen_record(data_str))
print(sorted(list(gen_frequent_2_itemset(dataset, 0.5))))