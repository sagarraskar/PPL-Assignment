
def getGeometricSeries(a, r) :
    series = []
    for n in range(0, 10) :
        series.append(a * (r ** n))

    return series


a = int(input("Enter the first element : "))
r = int(input("Enter the common ratio: "))

series = getGeometricSeries(a, r)
print(series)