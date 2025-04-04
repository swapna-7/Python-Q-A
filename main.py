
# n = input()
# arr = n.split(" ")

# lowest = 0
# f = 0 # flag

# while lowest < 9 and f == 0:
#     for i in range(len(arr)):
#     # print("i: ", i)
#     # print("arr[i]: ", arr[i])

#         if str(lowest) not in arr[i]:
#             break
#         else:
#             if i == len(arr) - 1:
#                 print(lowest)
#                 f = 1
#                 break


#     lowest += 1


# n = "123456789"
# # print(n)       

# def sum_digits(n):
#     s = 0
#     for i in str(n):
#         s += int(i)
#     # print(s)
#     return s

# sum = sum_digits(n)

# while sum > 9:
#     sum = sum_digits(sum)
    

# print(sum)



# s="abbabacccfefefeghghghjkjkjkopopop"

# def freqofchars(s):

#     d={}

#     for i in s:
#         print(d)
#         if i not in d:
#             d[i] = 1
#         else:
#             d[i] = d[i] + 1

    
    
#     l= list(d.values())
#     print(l)

#     print(sum(l)/len(l)==l[0])

#     # return d

# freqofchars(s)

# # check if all frequencies are same




# s="444112233"
# # eo="212223"

# d={}
# for i in s:
#     if i in d:
#         d[i]+=1
#     else:
#         d[i]=1

# print(d)

# eo=""

# for i in d:
#     eo+=str(d[i])+i
# print(eo)


# keys=list(d.keys())
# values=list(d.values())


# for i in range(len(keys)):
#     print(str(values[i])+keys[i] ,end="")



# strinput="-2,2,3,4,-2,21,0"
# arr=list(map(int,input.split(',')))

# h=sum(arr)
# for i in range(len(arr)):
#     for j in range(i+1,len(arr)+1):
#         if sum(arr[i:j])>h:
#             h=sum(arr[i:j])

# print("Highest sum: ",h)


# arr = [[3,4],[2,3],[5,7]]
# q=[[1,3],[3,3]]


# print(arr)

# freq={}
    
# for i in arr:
#     start=i[0]
#     end=i[1]
#     for j in range(start,end+1):
#         if j in freq:
#             freq[j]+=1
#         else:
#             freq[j]=1

# print(freq)

# def P(x):
#     count = 0
#     li = list(freq.values())
#     for i in li:
#         if i == x:
#             count+=1
#     return count
    

# # print(P(4))
# ans = []
# for i in q:
#     ans.append(max(P(i[0]),P(i[1])))
# print(ans)

# a=input().split()


# a.sort()
# print(a[-1])

# n=5
# c=1
# a=[]
# for i in range(n):
#     d=[]
#     for j in range(n):
#         d.append(0)
#     a.append(d)

# for i in a:
#     print(i)

# for i in range(n):
#     for j in range(n):
#         print(str(i)+","+str(j),end=" ")
#         if i<=j:
#             a[j][i]=c
#             c=c+1

#     print()
# print("\n")
# for i in a:
#     print(i)

# for i in range(n):
#     for j in range(n):
#         if a[i][j]!=0:
#             print(a[i][j],end=" ")
#     print()







