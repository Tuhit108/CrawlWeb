import requests
from bs4 import BeautifulSoup
import pandas as pd


def convertPrice(price: str):
    result = 0
    if 'tỉ' in price:
        temp1 = price.split(' tỉ ')
        result = result + int(temp1[0]) * 10 ** 9

        temp2 = temp1[1].split(' ')
        result = result + int(temp2[0]) * 10 ** 6
    else:
        temp3 = price.split(' ')
        result = result + int(temp3[0]) * 10 ** 6

    return result


carName = []
price = []
year = []
style = []
stat = []
xx = []
km = []
tt = []
hs = []
nl = []

dict = {'Tên xe': carName, 'Giá': price, 'Năm sản xuất': year, 'Kiểu dáng': style, 'Tình trạng': stat, 'Xuất xứ': xx,
        'Số km đã đi': km, 'Tỉnh thành': tt, 'Hộp số': hs, 'Nhiên liệu': nl}

listCarLinks = []
baseUrl = 'https://oto.com.vn/'

current = 0
result = []

def processingData(link: str):
    try:
        link = baseUrl + link
        response = requests.get(link)
        soup = BeautifulSoup(response.content, "html.parser")

        carTitle = soup.select_one('.group-title-detail > .title-detail').get_text().split(' - ')
        TenXe = carTitle[0]
        Gia = convertPrice(carTitle[1])
        if TenXe == '':
            print(link)

        carInfos = soup.select('.box-info-detail > .list-info > li')
        carInforTitles = ['Năm sản xuất', 'Kiểu dáng', 'Tình trạng', 'Xuất xứ', 'Số km đã đi', 'Tỉnh thành', 'Hộp số',
                          'Nhiên liệu']

        result.append({
            "Tên" : carTitle[0],
            "Giá" :convertPrice(carTitle[1]),
            "Năm sản xuất" : carInfos[0].text.replace("Năm sản xuất",''),
            "Kiểu dáng" :  carInfos[1].text.replace("Kiểu dáng",''),
            "Tình trạng" : carInfos[2].text.replace("Tình trạng",''),
            "Xuất xứ": carInfos[3].text.replace("Xuất xứ",''),
            "Số km đã đi": carInfos[4].text.replace("Số km đã đi",''),
            "Tỉnh thành": carInfos[5].text.replace("Tỉnh thành",''),
            "Hộp số": carInfos[6].text.replace("Hộp số",''),
            "Nhiên liệu": carInfos[7].text.replace("Nhiên liệu",''),

        })
        carName.append(TenXe)
        price.append(Gia)
        year.append('')
        style.append('')
        stat.append('')
        xx.append('')
        km.append('')
        tt.append('')
        hs.append('')
        nl.append('')
        for carInfo in carInfos:
            for carInforTitle in carInforTitles:
                if carInforTitle in carInfo.get_text():
                    dict.get(carInforTitle)[-1] = carInfo.get_text().replace(carInforTitle, '').replace(' ', '')

        current = current + 1
        print(current)
    except:
        pass


for i in range(0, 1):
    try:
        response = requests.get('https://oto.com.vn/mua-ban-xe-cu-da-qua-su-dung/p' + str(i))
        soup = BeautifulSoup(response.content, "html.parser")

        links = soup.select('.item-car > .photo > a')
        for link in links:
            if link['href']:
                listCarLinks.append(link['href'])

        print('done: ' + str(i), response.status_code)
    except:
        pass

for link in listCarLinks:
    print(link)
    processingData(link)
print(result)
df = pd.DataFrame(dict)
df.to_csv('data-1.csv', encoding='utf-8-sig')
