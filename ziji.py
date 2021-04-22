def getData():
    lists = [4, 5, 6, 7]
    results = []
    for i in range(0,3):
        for x in lists[i:]:
            if len(results)<len(lists):
                temp=[]
                temp.append(x)
                results.append(temp)
            else:
                # n -= len(lists) - i
                for y in results:
                    if x not in y and len(y)==i:
                        temp=[]
                        temp.extend(y)
                        temp.append(x)
                        results.append(temp)
    results.append([4,5,6,7])
    results.append([])
    return results

print(getData())