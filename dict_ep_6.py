colors={10:"red",35:"green",15:"blue",25:"white"}
print(sorted(colors.items(),key=lambda x: x[0]))
print(sorted(colors.items(),key=lambda x: x[0],reverse=True))
print(sorted(colors.items(),key=lambda x: x[1]))
print(sorted(colors.items(),key=lambda x: x[1],reverse=True))