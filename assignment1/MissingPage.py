def findMissingPages(list) :
    pages = []
    for i in range(1, 26) :
        if i not in list :
            pages.append(i)

    return pages

print("Missing pages : ", findMissingPages([1,2,3,4,5,6,7,8,11,12,16,17,18,25]))