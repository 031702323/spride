import re
import json
while 1:

    a=input()
    if (a == "END"):
        break
    else:
        dirt={"姓名":"","手机":"","地址":[]}
        #a=("x2!小陈,广东省东莞市凤岗13965231525镇凤平路13号.")
        #a=input()
        flag=re.search(r'.'*1,a)
        mark=flag.group()      #提取难度标识
        a=a.replace(mark,'',1)
        a=a.replace('!','',2)
        s = re.search(r'\d{11}', a)
        phone_number = s.group()
        dirt["手机"]=phone_number

        c = a.replace(phone_number, '')  # 将字符串中的电话号码删除

        d = a.index(',')   # 找到逗号的下标

        e = re.search(r'.' * d, c)   # 找到名字
        name = e.group()
        dirt["姓名"]=name

        addr = c.replace(name, '',1)   # 将地址中的名字删除
        addr = addr.replace(",", '',1)
        addr = addr.replace('.', '',1)

        # 省
        if ('省' in addr) and addr.index("省")<=3:
            sheng1 = addr.index('省')
            sheng2 = re.search(r'.' * sheng1, addr)
            sheng3 = sheng2.group()
            sheng3 += '省'
            addr = addr.replace(sheng3, '',1)
        elif '自治区' in addr:
            sheng1 = addr.index('自')
            sheng2 = re.search(r'.' * sheng1, addr)
            sheng3 = sheng2.group()
            sheng3 += '自治区'
            addr = addr.replace(sheng3, '',1)
        # 直辖市
        elif '北京' in addr or '上海' in addr or '重庆' in addr or '天津' in addr:
            if '市' in addr:  # 存在 市
                sheng1 = addr.index('市')
                sheng2 = re.search(r'.' * sheng1, addr)
                sheng3 = sheng2.group()
                sheng4 = sheng3 + '市'
                addr = addr.replace(sheng4, '',1)
            else:  # 不存在市
                sheng2 = re.search(r'.' * 2, addr)
                sheng3 = sheng2.group()
                addr = addr.replace(sheng3, '',1)
        else:  # 缺少省
            sheng2 = re.search(r'.' * 2, addr)
            sheng3 = sheng2.group()
            addr = addr.replace(sheng3, '',1)
            sheng3 += '省'
        dirt["地址"].append(sheng3)

        # 市级
        shiji=['市','地区','自治州','盟']

        if ("市"in addr and addr.index("市")<=3)or ("地区"in addr and addr.index("地区")<=3) or ("自治州"in addr and addr.index("自治州")<=3) or ("盟"in addr and addr.index("盟")<=3) :
            for erji in shiji:
                if erji in addr:  # 存在市
                    shi1 = addr.index(erji)
                    shi2 = re.search(r'.'*shi1, addr)
                    shi3 = shi2.group()
                    shi3 += erji
                    addr = addr.replace(shi3,'',1)
                    break

        elif '北京' in sheng3 or '天津' in sheng3 or '重庆' in sheng3 or '上海' in sheng3:  # 不存在市
                shi3 = sheng3 + '市'
        else:
                shi2 = re.search(r'.' * 2, addr)
                shi3 = shi2.group()
                addr = addr.replace(shi3, '',1)
                shi3 += '市'
        dirt["地址"].append(shi3)
        #县级
        xianji=['县','区','市','自治县','旗','自治旗','林区','特区']
        if  ("县"in addr and addr.index("县")<=4) or ("区"in addr and addr.index("区")<=4) or("市"in addr and addr.index("市")<=4) or ("自治县"in addr and addr.index("自治县")<=4) or ("旗"in addr and addr.index("旗")<=4) or ("自治旗"in addr and addr.index("自治旗")<=4) or ("林区"in addr and addr.index("林区")<=4) or ("特区"in addr and addr.index("特区")<=4):# 存在关键字
            for sanji in xianji:
                if sanji in addr:
                    xian1 = addr.index(sanji)
                    xian2 = re.search(r'.' * xian1, addr)
                    xian3 = xian2.group()
                    xian3 += sanji
                    addr = addr.replace(xian3, '',1)
                    break

        else:
            xian3=''
        dirt["地址"].append(xian3)

        #镇级
        zhenji=['街道','镇','乡','民族乡','苏木','民族苏木','县','区',"开发区"]
        if ("街道"in addr and addr.index("街道")<=3) or ("镇"in addr and addr.index("镇")<=3) or ("乡"in addr and addr.index("乡")<=3) or ("民族乡"in addr and addr.index("民族乡")<=3) or ("苏木"in addr and addr.index("苏木")<=3) or ("民族苏木"in addr and addr.index("民族苏木")<=3) or ("县"in addr and addr.index("县")<=3) or ("区"in addr and addr.index("区")<=3) or ("开发区"in addr): # 存在关键字
            for siji in zhenji:
                if siji in addr:
                    zhen1 = addr.index(siji)
                    zhen2 = re.search(r'.' * zhen1, addr)
                    zhen3 = zhen2.group()
                    zhen3 += siji
                    addr = addr.replace(zhen3, '',1)
                    break
        else:
            zhen3=''

        dirt["地址"].append(zhen3)

        if mark==('2') :
         #路级
         luji=['路','街','巷','村','胡同','弄']
         if ("路"in addr and addr.index("路")<=3) or ("街"in addr and addr.index("街")<=5) or ("巷"in addr and addr.index("巷")<=3) or ("村"in addr and addr.index("村")<=3) or ("胡同"in addr and addr.index("胡同")<=3) or ("弄"in addr and addr.index("弄")<=3):    # 存在关键字
            for wuji in luji:
                if wuji in addr:
                    lu1 = addr.index(wuji)
                    lu2 = re.search(r'.' * lu1, addr)
                    lu3 = lu2.group()
                    lu3 += wuji
                    addr = addr.replace(lu3, '',1)
                    break
         else:
            lu3=''
         dirt["地址"].append(lu3)
         #号级
         if ("号"in addr and addr.index("号")<=3) : #存在关键字
            hao1 = addr.index("号")
            hao2 = re.search(r'.' * hao1, addr)
            hao3 = hao2.group()
            hao3 += "号"
            addr = addr.replace(hao3, '',1)
         else:
            hao3=' '
         dirt["地址"].append(hao3)
         #地点级
        dirt['地址'].append(addr)
        str=json.dumps(dirt,ensure_ascii=False)
        print(str)
