######################################################################
## Filename:      0th.py
##                
## Copyright (c) 2012,Yannis
## Version:       
## Author:        Yannis.Xu <excellentbright@gmail.com>
## Created at:    Fri Jan 13 01:18:21 2012
##                
## Description:   
##                
######################################################################
#��Ŀ˵����������Ŀ����ʾ����ÿ���ַ�����ƶ���λ���õ���Ϣ��
#i hope you didnt translate it by hand. thats what computers are for. doing it in by hand is inefficient and that's why this text is so long. using string.maketrans() is recommended. now apply on the url
#Ӧ���� map -> ocr    ����Ϊocr.html
def convert(str):
    newstr="";
    for char in str:
        if(char>='a'and char<='x'):             #���ַ�����a,x�м��һ����������ƶ���λ
            newstr+=chr(ord(char)+2);
        else:
            if(char>='y' and char<='z'):        #���ַ���y,z�е�һ�������ַ�ת��Ϊa,b
                newstr+=chr(ord(char)-24);
            else:                               #����������ַ��򲻱�
                newstr+=char;
    return newstr;

if __name__ == "__main__":
    #print "main function";
    str="g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj";
    newstr=convert(str);
    print newstr;
        
    
    
