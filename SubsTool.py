# coding: utf-8

import os
import sys
import getopt
import codecs
import io

python_ver=sys.version_info.major

if python_ver is 2:
    print '''
Please install python3 or use `python3` instead `python`
'''
    
try:
    from PIL import Image, ImageFont, ImageDraw, ImageColor
except e:
    print('''
Please Check Python Library PIL

Install Command : pip3 install PIL
''')
    
    else:
        print()
## Command Line: SubsTool -s <sourceTXT> [ -f <font file> ]
_usage="""
   Usage: python SubsTool.py -s <sourceTXT> [ -f <fontfile> ]

        sourceTXT (necessary) : SubTitles in txt file, use Enter to split
        fontfile  (optional)  : Font Family file 
                    default   : MFShangYa_Noncommercial-Regular.otf

    If you are MacOS or Linux,Please install Python3 in www.python.org.
    And You Command Line Will be:
    
        python3 SubsTool.py -s <sourceTXT> [ -f <fontfile> ]
        
"""

def usage():
    print(_usage)

def  del_file(path):
    for i in os.listdir(path):
        path_file = os.path.join(path,i)
        if os.path.isfile(path_file):
            os.remove(path_file)
        else:
             del_file(path_file)

filename_length=4

def filename_fix(now):
    
    if len(str(now)) < filename_length :
        return filename_fix('0'+str(now))
    else:
        return now

source=''
fontname = "MFShangYa_Noncommercial-Regular.otf"

## parse Args
try:
    options,args = getopt.getopt(sys.argv[1:],"hs:f:",["help","source=","font="])
except getopt.GetoptError:
    usage()
    sys.exit()

for name,value in options:
    if name in ("-h","--help"):
        usage()
    if name in ("-s","--source"):
        source=value
        if(os.path.exists(source) is False):
            print("source file doesn't exist")
            exit(0)
    else:
        usage()
        exit(0)
    if name in ("-f","--font"):
        fontname=value
        print("Custom Font Family: "+fontname)

if(os.path.exists(fontname) is False):
    print("Font Family file "+fontname+" doesn't exist")
    exit(0)

# fontsize为字体大小
# subcoord 为字幕左上角坐标
# save_directory 字幕图片保存目录
fontsize = 50
subcoord1 = (90,850)
subcoord2 = (90,920)
save_directory=os.path.splitext(os.path.split(source)[1])[0]
if(os.path.exists(save_directory) is False):
    os.mkdir(save_directory)
print("\nThe directory and file under '"+save_directory+"/' will be deleted.\npress y to continue, other input will stop this script")
if(str.lower(input()) != 'y'):
    exit(0)
del_file(save_directory)


## 打开文件并读取字幕数据
subText = open(source,'r',encoding='utf-8')
subList = subText.readlines()

print("File Successfully Read, " + str(len(subList)) +" Lines Found.")

## 读取并设置字幕字体
font = ImageFont.truetype(fontname, fontsize, 0, "gbk")

for i in range(0,int(len(subList))):
    ## 创建新图片
    # subString1 = subList[2*i]
    # subString2 = subList[2*i-1]
    im = Image.new("RGBA", (1920,1080))
    ## 创建绘图句柄
    draw = ImageDraw.Draw(im)
    # draw.text(subcoord1, subString1, font=font)
    # draw.text(subcoord2, subString2, font=font)
    draw.text(subcoord2, subList[i], font=font)
    dic=save_directory + "/" + save_directory.replace(" ","") + "-" + filename_fix(str(i)) + ".png"
    print(dic)
    im.save(dic,"PNG")
