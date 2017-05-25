import time
L1="2649821731631836529481632803462831616487712734074314936141303241873417434716340124362304724324324324324323412121323164329751831"
L2="1045091731748365195814509145981509438583247509149821493213241431431319999999999999999999999999999999999999999999999999341344779"

startTime=time.time()
#长度强行扭转到一致 不够前面补0
max_len= len(L1) if len(L1)>len(L2) else len(L2)
l1=L1.zfill(max_len)
l2=L2.zfill(max_len)

a1=list(l1)
a2=list(l2)
#长度一致 每个对应的位置的相加的和 %10 前一位补1 如果>10 否则0  99+99最大3位所以多一位
a3=[0]*(max_len+1)

for index in range(max_len-1,-1,-1):
    index_sum=a3[index+1]+int(a1[index])+int(a2[index])
    less=index_sum-10
    a3[index+1]=index_sum%10
    a3[index]=1 if less>=0 else 0
if(a3[0]==0):
    a3.pop(0)
a33=[str(i) for i in a3]
print(''.join(a33))
print('耗时{0}ms'.format(time.time()-startTime))
