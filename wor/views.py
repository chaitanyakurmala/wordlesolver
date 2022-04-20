from django.http import HttpResponse
from django.shortcuts import render

def solution(good,bad,pos):
    
    def stol(s):
        l=[]
        for i in s:
            l.append(i)
        return l

    def gd(good,bad):
        for i in good:
            if i in bad:
                return False
                break

    def bp(bad,pos):
        bad=stol(bad)
        for i in bad:
            if i in pos:
                return False
                break
            
            
    def chec1(pos):
        if pos[0]==0 and pos[1]==0 and pos[2]==0 and pos[3]==0 and pos[4]==0:
            return True
        else:
            return False


    def wcheck(bad,word):
        op=0
        for i in word:
            if i in bad:
                op=1
                break
        if op==1:
            return 1
        else:
            return 0
    
    def rwcheck(good,word):
        op=0
        for i in word:
            if i in good:
                op=1
                break
            else:
                pass
        if op==1:
            return 1
        else:
            return 0
            
    def sor(good,word):
        word=list(word)
        op=0
        for i in good:
            if i not in word:
                op=1
                break
        if op==1:
            return 1
        else:
            return 0
            



    #good=stol("ab")
    #bad=stol("")
    
    #pos=['a','b',0,0,0]
    
    stopword=open(r"C:\Users\chait_ffbio80\exp2\wor\words.csv")
    words = stopword.read().split('\n')
    words.pop()
    
    
    if(gd(good,bad)==False):
        s=["No"]
        return s
        
    if(bp(good,bad)==False):
        s=["No"]
        return s
        


    if len(good)==0:
        sol=[]
        if (chec1(pos)):
            for word in words:
                if (wcheck(bad,word) == 0):
                    sol.append(word)
        return sol
        
    
    else:
        sol=[]
        sol1=[]
        sol2=[]
        for i in words:
            if wcheck(bad,i)==0:
                sol2.append(i)
        



        for i in sol2:
            if sor(good,i)==0:
                sol1.append(i)

    a,b,c,d,e=pos
    
    d={1:a,2:b,3:c,4:d,5:e}
    shh=list(d.values())


    
    
    nic=[]
    for i in shh:
        if i!='0':
            if i!=0:
                nic.append(i)
    
    lgth=len(nic)
    
    for word in sol1:
        c=0
        k=list(word)
        u,v,x,y,z=k   
        d1={1:u,2:v,3:x,4:y,5:z}
        for i in d.keys():  
            if d[i]==0:
                pass
            else:
                if d[i]==d1[i]:
                    c=c+1
        if c==lgth:
            sol.append(word)
    return sol
      
      
# Create your views here.
def index(request):
    return render(request,'home.html')

def add(request):
    pos=[]

    good=request.GET['good'].lower()
    bad=request.GET['bad'].lower()
    p1=request.GET['p1']
    p2=request.GET['p2']
    p3=request.GET['p3']
    p4=request.GET['p4']
    p5=request.GET['p5']

    pos.append(p1.lower())
    pos.append(p2.lower())
    pos.append(p3.lower())
    pos.append(p4.lower())
    pos.append(p5.lower())

    listt=solution(good,bad,pos)

    return render(request,'res.html',{'d':listt})