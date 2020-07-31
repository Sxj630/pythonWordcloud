import requests
import re
import wordcloud
import jieba
def getTaobao(num):
    kv = {
        'cookie': 'cna=qMU/EQh0JGoCAW5QEUJ1/zZm; enc=DUb9Egln3%2Fi4NrDfzfMsGHcMim6HWdN%2Bb4ljtnJs6MOO3H3xZsVcAs0nFao0I2uau%2FbmB031ZJRvrul7DmICSw%3D%3D; lid=%E5%90%91%E6%97%A5%E8%91%B5%E7%9B%9B%E5%BC%80%E7%9A%84%E5%A4%8F%E5%A4%A9941020; otherx=e%3D1%26p%3D*%26s%3D0%26c%3D0%26f%3D0%26g%3D0%26t%3D0; hng=CN%7Czh-CN%7CCNY%7C156; x=__ll%3D-1%26_ato%3D0; t=2c579f9538646ca269e2128bced5672a; _m_h5_tk=86d64a702eea3035e5d5a6024012bd40_1551170172203; _m_h5_tk_enc=c10fd504aded0dc94f111b0e77781314; uc1=cookie16=V32FPkk%2FxXMk5UvIbNtImtMfJQ%3D%3D&cookie21=U%2BGCWk%2F7p4mBoUyS4E9C&cookie15=UtASsssmOIJ0bQ%3D%3D&existShop=false&pas=0&cookie14=UoTZ5bI3949Xhg%3D%3D&tag=8&lng=zh_CN; uc3=vt3=F8dByEzZ1MVSremcx%2BQ%3D&id2=UNcPuUTqrGd03w%3D%3D&nk2=F5RAQ19thpZO8A%3D%3D&lg2=U%2BGCWk%2F75gdr5Q%3D%3D; tracknick=tb51552614; _l_g_=Ug%3D%3D; ck1=""; unb=3778730506; lgc=tb51552614; cookie1=UUBZRT7oNe6%2BVDtyYKPVM4xfPcfYgF87KLfWMNP70Sc%3D; login=true; cookie17=UNcPuUTqrGd03w%3D%3D; cookie2=1843a4afaaa91d93ab0ab37c3b769be9; _nk_=tb51552614; uss=""; csg=b1ecc171; skt=503cb41f4134d19c; _tb_token_=e13935353f76e; x5sec=7b22726174656d616e616765723b32223a22393031623565643538663331616465613937336130636238633935313935363043493362302b4d46454e76646c7243692b34364c54426f4d4d7a63334f44637a4d4455774e6a7378227d; l=bBIHrB-nvFBuM0pFBOCNVQhjb_QOSIRYjuSJco3Wi_5Bp1T1Zv7OlzBs4e96Vj5R_xYB4KzBhYe9-etui; isg=BDY2WCV-dvURoAZdBw3uwj0Oh2yUQwE5YzQQ9qAfIpm149Z9COfKoZwV-_8q0HKp',
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
        'referer': 'https://detail.tmall.com/item.htm?spm=a230r.1.14.19.59c17172WOwft2&id=611224893062&ns=1&abbucket=7&sku_properties=10004:7169121965;5919063:6536025',
        'accept': '*/*',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'zh-CN,zh;q=0.9'
    }
    for i in range(num):
        url = "https://rate.tmall.com/list_detail_rate.htm?itemId=611224893062&spuId=1526565904&sellerId=1714128138&order=3&currentPage=" + str(
            i + 1) + \
              '&append=0&content=1&tagId=&posi=&picture=&groupId=&ua=098%23E1hvQ9vRvpWvUvCkvvvvvjiPn2ch0jn2PsSUAj1VPmPyzj3CP2ch0jlUP25ZljDURphvCvvvvvmCvpvWz%2Fw65h34zYMNZR' \
              'fwdphvmpvh4UWOVvv6euwCvvpvvUmm2QhvCvvvMM%2FEvpvVmvvC9j3Euphvmvvv92DCk5J1Kphv8vvvvvCvpvvQvvmChZCvmb%2BvvvWvphvW9pvvvQCvpvQEvvmmfyCv2ChEvpCWCH%2BQvvwD%2BExr1EAKNB3' \
              'r1n1lHqyQc8cBIU9BDVQEfwLwaXTAVAdyafFE%2BF%2BDxG0xI8p7%2B3%2Butjc6D40OaAuguf0Dn1Bkp8oQD76fd9hCvvOvCvvvphvtvpvhvvvvvUwCvvpvCvvvdphvhovhMgbT%2F9vWJkeSI2BvAxZ1dphvmpvh4InZ' \
              'xvvgSv%3D%3D&needFold=0&_ksTS=1589168041522_777&callback=jsonp778'
        r = requests.get(url, headers=kv)
        # r.encoding = r.apparent_encoding
        print(r.status_code)
        #name = re.findall('"displayUserNick":"(.*?)"', r.text)
        display = re.findall('"rateContent":"(.*?)"', r.text)
        display=" ".join(display)
        with open('D:\\Python37\\pyhon-crawler\\xiaomi.txt','w+',encoding='utf-8') as f:
            f.write(display)
    f=open('D:\\Python37\\pyhon-crawler\\xiaomi.txt','r',encoding='utf-8')
    ls=jieba.lcut(f.read())
    txt = " ".join(ls)
    w = wordcloud.WordCloud( \
    width = 1000, height = 700,\
    background_color = "white",
    font_path = "msyh.ttc",
    max_words=20
   
    )
    w.generate(txt)
    w.to_file("grwordcloud.png")
def main():
    num = eval(input('输入需要爬取页面的数量\n'))
    getTaobao(num)


main()

