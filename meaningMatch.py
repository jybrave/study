# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 22:18:43 2019

@author: juyng
"""
if __name__ == "__main__":
    rule = []
    rule.append("<[播]放|来>[一|几]<首|曲|个>@{singer}的<歌[曲]|[流行]音乐>")
    print(rule[0])
    sen = list(input())
    #print(sen[0:2])
    if(sen[0:2] == ['播','放']):
        if(sen[2] == '一' or sen[2] == '几'):
            if(sen[3] == '首' or sen[3] == '曲' or sen[3] == '个'):
                i=4
                while(sen[i] != '的'):#如果输入没有‘的’无法识别
                    i += 1
                if(sen[i+1] == '歌' or sen[i+1:i+3] == ['歌','曲'] or sen[i+1:i+3] == ['音','乐'] or sen[i+1:i+5] == ['流','行','音','乐']):
                    print(1)
                else:
                    print(0)
            else:
                print(0)
        elif(sen[2] == '首' or sen[2] == '曲' or sen[2] == '个'):
            i=3
            while(sen[i] != '的'):#如果输入没有‘的’无法识别
                i += 1
            if(sen[i+1] == '歌' or sen[i+1:i+3] == ['歌','曲'] or sen[i+1:i+3] == ['音','乐'] or sen[i+1:i+5] == ['流','行','音','乐']):
                print(1)
            else:
                print(0)
        else:
            print(0)
    elif(sen[0] == '放' or sen[0] == '来'):
        if(sen[1] == '一' or sen[1] == '几'):
            if(sen[2] == '首' or sen[2] == '曲' or sen[2] == '个'):
                i = 3
                while(sen[i] != '的'):#如果输入没有‘的’无法识别
                    i += 1
                if(sen[i+1] == '歌' or sen[i+1:i+3] == ['歌','曲'] or sen[i+1:i+3] == ['音','乐'] or sen[i+1:i+5] == ['流','行','音','乐']):
                    print(1)
                else:
                    print(0)
            else:
                print(0)
        elif(sen[1] == '首' or sen[1] == '曲' or sen[1] == '个'):
            i=2
            while(sen[i] != '的'):#如果输入没有‘的’无法识别
                i += 1
            if(sen[i+1] == '歌' or sen[i+1:i+3] == ['歌','曲'] or sen[i+1:i+3] == ['音','乐'] or sen[i+1:i+5] == ['流','行','音','乐']):
                print(1)
            else:
                print(0)
        else:
            print(0)