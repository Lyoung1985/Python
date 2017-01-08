#coding:gbk
'''
Created on 2017��1��8��

@author: coldjune
'''

import uuid,string

def createActivationCode(num,length=16):
    result=[]
    
    while num>0:
        uuid_id=uuid.uuid1()
        #ɾ��-
        temp=str(uuid_id).replace('-', '')[:length]+'\n'
        #û��λ���һ��'-'
        l=len(temp)
        tem=[]
        for n in range(l):
            if n%4==0:
                tem.append(temp[n:n+4])
        temp='-'.join(tem)
        #��ȡ�����ڶ��ַ�
        if temp[-2]=='-':
            #��ȡ�������ڶ����ַ�ǰ�������ϻ��з�
            temp=temp[:-2]+'\n'
                
        if temp not in result:
            result.append(temp)
        num-=1
    
    activationCode=open('./../../activation/activationCode.txt','w')
    activationCode.writelines(result)
    activationCode.close()

createActivationCode(5,21)