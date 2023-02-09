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

listCarLinks = []
baseUrl = 'https://oto.com.vn/'

current = 0
result = []

def processingData(link: str):
    try:
        link = baseUrl + link
        response = requests.get(link)
        soup = BeautifulSoup(response.content, "html.parser")

        TenXe = soup.select_one('.group-title-detail > .title-detail').get_text().replace('\r\n', '')
        Gia = soup.select_one('.price-big > .price').get_text().replace('\r\n', '')
        print(TenXe)
        if TenXe == '':
            print(link)

        carInfos = soup.select('.box-info-detail > .list-info > li')
      
        price = convertPrice(Gia.strip())
        
        print(price)
        result.append({
            "Tên" : TenXe.strip(),
            "Giá" :price,
            "Năm sản xuất" : carInfos[0].text.replace("Năm SX",'').strip(),
            "Kiểu dáng" :  carInfos[1].text.replace("Kiểu dáng",''),
            "Tình trạng" : carInfos[2].text.replace("Tình trạng",''),
            "Xuất xứ": carInfos[3].text.replace("Xuất xứ",''),
            "Số km đã đi": carInfos[4].text.replace("Km đã đi",'').strip().replace(" km","").replace(".",""),
            "Tỉnh thành": carInfos[5].text.replace("Tỉnh thành",'').strip(),
            "Quận huyện": carInfos[6].text.replace("Quận huyện",'').strip(),
            "Hộp số": carInfos[7].text.replace("Hộp số",''),
            "Nhiên liệu": carInfos[8].text.replace("Nhiên liệu",''),

        })
       
    except:
        pass


for i in range(1, 200):
    try:
        response = requests.get('https://oto.com.vn/mua-ban-xe-cu-da-qua-su-dung/p' +str(i) )
        soup = BeautifulSoup(response.content, "html.parser")

        links = soup.select('.item-car > .photo > a')
        for link in links:
            if link['href']:
                listCarLinks.append(link['href'])

        print('done: ' + str(i), response.status_code)
    except:
        pass

for link in listCarLinks:
    processingData(link)
df = pd.DataFrame(result)
df.to_csv('data.csv', encoding='utf-8-sig')
