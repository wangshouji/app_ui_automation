
"""
:author: shouji.wang
:Date: Created on 2018/1/19
:Description:
"""

import sys
import io

class COMMON_ARITHMERIC(object):
    #去除一个字符串的所有空格并转为小写字母
    @staticmethod
    def remove_all_blank(s):
        if not isinstance(s,str) :
            return '请检查传入的是否为字符串'
        s=s.strip().rstrip().lower()
        if len(s.split(' ')) == 1:
            return s
        else:
            lis=s.split(' ')
            s=''
            if len(lis) > 2:
                for i in range(len(lis)):
                    if i==len(lis)-1:
                        s+=lis[i]
                        return s
                    s += lis[i] + '_'
            elif len(lis) == 2:
                for i in range(len(lis)-1):
                    s += lis[i] + '_' + lis[i + 1]
            return s
        return s


    #递归断言两个json文件是否一致
    @staticmethod
    def assert_json_equels_json(json1, json2):
        if not isinstance(json1,dict) or not isinstance(json2,dict):
            return '请检查断言的两个文件是否都是json格式'
        for i in json1.keys():
            if not isinstance(json1[i] , dict):
                if json1[i]!= json2[i]:
                    return False
            elif isinstance(json1[i] , dict):
                COMMON_ARITHMERIC.assert_json_equels_json(json1[i],json2[i])
        return True


    #输入字符串进行模糊查询，利用递归二分查找法查询在列表中的位置并返回值
    @staticmethod
    def find_str_index(s , arr , start , end):
        if not isinstance(s , str) or not isinstance(arr , list) or not isinstance(start , int) \
                or not isinstance(end , int):
            return '传入的字符或列表类型错误，请检查'
        if start > end:
            return '请确认开始位置是否小于列表的长度'
        mid = int((end - start)/2 +start)
        if arr[mid].find(s) >= 0:
            return mid
        else:
            COMMON_ARITHMERIC.find_str_index(s , arr , mid+1 , end )
            COMMON_ARITHMERIC.find_str_index(s , arr , start, mid-1)
        return -1

    #遍历模糊查询某段字符串是否在列表中并返回列中对应的全部字符串
    @staticmethod
    def find_str_return(s , arr):
        if not isinstance(s , str) or not isinstance(arr , list):
            return '传入的字符或列表类型错误，请检查'
        for i in arr:
            if i.find(s) >= 0:
                return i



    #遍历查询字典中的key的values列表中是否有匹配的字符串并返回key和全部的字符串
    @staticmethod
    def find_str_return_tuple(s , dicts):
        if not isinstance(s , str) or not isinstance(dicts , dict):
            return '传入的字符或字典类型错误，请检查'
        for key in dicts.keys():
            if not isinstance(dicts[key] , list):
                return '传入的字典key的值必须为列表类型'
            for i in dicts[key]:
                if i.find(s) >= 0:
                    return key,i


    #遍历字典的key是否在某一字符串中，如果在并返回key对应的values的值
    @staticmethod
    def find_dict_key_return_value(dicts , s):
        for key in dicts.keys():
            lis=key.split('_')
            boo=False
            for i in lis:
                if s.find(i) >= 0:
                    boo=True
                else:
                    boo=False
                    break
            if boo:
                return dicts[key]