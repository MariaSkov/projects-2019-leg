def hello_world():
    return "hello world"
    1. read the data
2. rename the variables as the VN are the same
1
2
3
4
	myDict = {}
for i in range(2008, 2017): # range goes from 2008 to but not including 2017
    myDict[str(i)] = f'e{i}' 
myDict
3. merge the data
4. drop if nan
5. summary statistics: df.describe() (groupby)
6. generate a variable called real_spending
7. plot the real_spending for certain country
8. group by GDP/capita;
9. aggregate for each group and plot the aggregated results
