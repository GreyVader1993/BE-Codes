from xml.dom import minidom
import random, time, sys
from multiprocessing import Pool, Process, Pipe
from itertools import chain
def swap(a,i,j):
        temp = a[i]
        a[i] = a[j]
        a[j] = temp
    
def partition(a,lo,hi):
        rnd = random.randint(lo, hi)
        pivot = a[rnd]
        swap(a,hi,rnd)
        b = lo
        for i in range(lo, hi):
            if a[i] < pivot:
                swap(a, i, b)
                b += 1
        swap(a, hi, b)
        return b
    
def partitionWrap(i_list):
    ind, lyst = i_list
    if len(lyst) <= 1:
        return [lyst]
    b = partition(lyst, 0, len(lyst)-1)
    return (ind, [lyst[:b], [lyst[b]], lyst[b+1:]])

class QuickSort:
    dataList=[]
    def __init__(self):
        pass
        
    def getData(self):
        self.dataList=[]
        xmldoc = minidom.parse('data.xml')
        itemlist = xmldoc.getElementsByTagName('Item')
        for s in itemlist:
            self.dataList.append(s.getAttribute("index").encode("utf-8"))
        print self.dataList

   

    def QuickSortParallel(self,n):
        numproc = 2**n
        #Basically, we're going to partition the list until it's all
        #singletons. We'll store each singleton in the master list.
        ml = list(self.dataList)
        
	os.getpid()
	
        pool = Pool(processes = numproc)
        results = [(0, self.dataList)] 
        #the one initial argument to partitionWrap
        print results
        while len(results) > 0:
            #debug: print(str(results) + '\n\n\n')
            temp = pool.map(partitionWrap, results)
            print temp
            #Each element of temp is a list of up to three lists.
            results = []
            for i, plist in temp:
                for ll in plist: #for each little list in the partition output
                    if len(ll) == 1:
                        ml[i] = ll[0]
                        i += 1
                    elif len(ll) > 1:
                        results.append((i, ll))
                        i += len(ll)
            print results
    
        return ml
    
conSort=QuickSort()
conSort.getData()
n=3
sortedList=[]
sortedList=conSort.QuickSortParallel(n)
print sortedList

            
