# -*- coding: utf-8 -*-
"""
Created on Sat Aug 22 10:14:19 2020

@author: MyPC
"""

def select_sort(num):
    for i in range(len(num)-1):
        min_index=i
        for j in range(i+1,len(num)):
            if num[j]<num[min_index]:
                min_index=j
        tmp=num[i]
        num[i]=num[min_index]
        num[min_index]=tmp
    return num

test=[5,3,6,3,4,1,2,5]
select_sort(test)


def insert_sort(num):
    for i in range(1,len(num)):
        preindex=i-1
        current=num[i]
        while preindex>=0 and num[preindex]>current:
            num[preindex+1]=num[preindex]
            preindex-=1
        num[preindex+1]=current
    return num
insert_sort(test)


def bubble_sort(num):
    for i in range(len(num)-1):
        for j in range(len(num)-i-1):
            if num[j]>num[j+1]:
                num[j],num[j+1]=num[j+1],num[j]
    return num
test=[5,3,6,3,4,1,2,5]
bubble_sort(test)

def quickSort(num,begin,end):
    if end<=begin:
        return 
    pivot=partition(num,begin,end)
    quickSort(num,begin,pivot-1)
    quickSort(num,pivot+1,end)
def partition(num,begin,end):
    pivot=end
    counter=begin
    for i in range(begin,end):
        if num[i]<num[pivot]:
            tmp=num[counter]
            num[counter]=num[i]
            num[i]=tmp
            counter+=1
    tmp=num[pivot]
    num[pivot]=num[counter]
    num[counter]=tmp
    return counter
test=[5,3,6,3,4,1,2,5]
quickSort(test,0,len(test)-1)
    

def mergeSort(num,left,right):
    if right<=left:
        return
    mid=(left+right)>>1
    mergeSort(num,left,mid)
    mergeSort(num,mid+1,right)
    merge(num,left,mid,right)

def merge(num,left,mid,right):
    tmp=[0]*(right-left+1)
    i,j,k=left,mid+1,0
    while i<=mid and j<=right:
        if num[i]<=num[j]:
            tmp[k]=num[i]
            i+=1
        else:
            tmp[k]=num[j]
            j+=1
        k+=1
    while i<=mid:
        tmp[k]=num[i]
        i+=1
        k+=1
    while j<=right:
        tmp[k]=num[j]
        j+=1
        k+=1
    for p in range(len(tmp)):
        num[left+p]=tmp[p]
test=[5,3,6,3,4,1,2,5]
mergeSort(test,0,len(test)-1)