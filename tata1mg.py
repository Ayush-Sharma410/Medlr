## Here I have used another python library and webscraped the data from tata1mg using HTMLSession ##
import pyppdf.patch_pyppeteer
from requests_html import HTMLSession
from csv import writer
header = {'Origin': 'https://www.1mg.com',
'Referer': 'https://www.1mg.com/categories/diabetes/diabetic-medicines-583?filter=true&pageNumber=1',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'
}
x=0
while (True):
    url = 'https://www.1mg.com/categories/diabetes/diabetic-medicines-583?filter=true&pageNumber='+str(x)
    x=x+1
    s=HTMLSession()
    r = s.get(url=url,headers=header)
    r.html.render(timeout=30)
    products=r.html.xpath('//*[@id="category-container"]',first=True)
    print(products)
    with open('medicines.csv', 'w', encoding='utf8', newline='') as f:
        thewriter = writer(f)
        information = ['Name','Price']
        thewriter.writerow(information)
        for name in products.absolute_links:
            try:    
                r=s.get(name)
                target=r.html.find('div.style__pro-title___2QwJy',first=True)
                price=r.html.find('div.style__price-tag___cOxYc',first=True)
                info=[target.text,price.text.replace('₹',' ').replace('MRP',' ').strip()]
                print(info)
                thewriter.writerow(info)
            except:
                pass 
