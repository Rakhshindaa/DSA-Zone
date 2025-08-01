nums=list(map(int,input().split()))
zer=0
one=0
zer=0
one=0
two=0
for i in range(len(nums)):
            if nums[i]==0:
                zer+=1
            elif nums[i]==1:
                one+=1
            else:
                two+=1
for i in range(len(nums)):
            if zer>0:
                nums[i]=0
                zer-=1
            elif one>0:
                nums[i]=1
                one-=1
            elif two>0:
                nums[i]=2
                two-=1