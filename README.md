# DADS6005_Final 

# Predicted from USDTHB for Gold price 
![gold](https://user-images.githubusercontent.com/122340391/211766981-2873446b-6aff-4885-9f53-026bbf11c106.jpg)


# Introduction
ในปัจจุบันปัจจัยที่มีผลต่อการขึ้น-ลงของราคาทองคำจะขึ้นอยู่กับเศรษฐกิจของโลก ทำให้ราคาทองคำมีการขึ้น-ลงและมีการปรับเปลี่ยนตัวเลขอยู่ตลอดเวลา โดยที่ตัวเลขจะขึ้นกับราคาตลาดโลกว่า ณ เวลานั้นตัวเลขว่ามีการปรับเปลี่ยนไปจากเดิมมากน้อยเพียงใด โดยปัจจัยเศรษฐกิจของโลกที่มีผลต่อราคาทองคำนั้นจะขึ้นอยู่กับอัตราดอกเบี้ย, ราคาน้ำมัน, Demand เเละ Supply ของความต้องการของทองคำเเละค่าเงินดอลล่า (USD)  <br />


เนื่องจากค่าเงินดอลล่า (USD) เป็นสกุลเงินที่ใช้เป็นสื่อกลางกว้างขวางทั่วโลก เเละยังเป็นสื่อกลางที่ใช้ซื้อ-ขาย เพราะเหตึนี้จึงส่งผลให้ค่าเงินดอลล่า (USD) มีความผันผวนกับราคาทองคำ เมื่อค่าเงินดอลล่า (USD) มีแนวโน้มอ่อนค่าลง และเมื่อราคาทองที่เป็นสินทรัพย์ที่สามารถเก็บมูลค่า จะส่งผลให้กระเเสเงินของเเต่ละประเทศไหล่สู่ทองคำ เพราะคนจะมองว่าทองคำจะกลายเป็นสินทรัพย์ที่เหมาะกับการสะสมมูลค่ามากกว่า ไม่ด้อยค่าลงอย่างสกุลเงินดอลลา (USD) ในขณะนั้นนั่นเอง จึงทำให้ราคาทองคำมีมูลค่าเพิ่มสูงขึ้น เเต่หากค่าเงินดอลล่า (USD) มีแนวโน้มสูงค่าขึ้นจะส่งผลให้ราคาทองคำปรับตัวลง  <br /> 

งานวิจัยนี้จึงได้ทำการสร้างโมเดลเพื่อทำนายราคาทองคำโดยอ้างอิงจากสกุลเงินดอลล่า (USD)



# Data source
### Fixer Currency
```
import requests

url_currency = "https://fixer-fixer-currency-v1.p.rapidapi.com/latest"

querystring = {"base":"USD","symbols":"THB"}

headers_currency = {
	"X-RapidAPI-Key": "SIGN UP FOR KEY",
	"X-RapidAPI-Host": "fixer-fixer-currency-v1.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)
```

### Gold Price
```
import requests

url_gold = "https://gold-price1.p.rapidapi.com/get_price/USD"

headers_gold = {
	"X-RapidAPI-Key": "SIGN UP FOR KEY",
	"X-RapidAPI-Host": "gold-price1.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers)

print(response.text)
```


# Coding



# Result


![messageImage_1673437212416](https://user-images.githubusercontent.com/122340391/211798189-2c5afab9-b990-4a79-9ee5-2b7f7c802b68.jpg)
Exchange rate: จากภาพจะเห็นได้ว่า ค่าเงินมีการเปลี่ยนแปลงตลอดเวลา

![messageImage_1673437227149](https://user-images.githubusercontent.com/122340391/211798212-47504fb0-8012-45a6-a3be-6d885a0b3ae9.jpg)
Gold price:
จากภาพจะเห็นได้ว่า เมื่อค่าเงินดอลล่า (USD) มีเเนวโน้มสูงค่าขึ้นราคาทองคำจะลดลง มีค่าผกผันและเมื่อค่าเงินดอลล่า (USD) มีแนวโน้มอ่อนค่าลงจะส่งผลให้ราคาทองคำสูงขึ้น

![IMG_1021](https://user-images.githubusercontent.com/122516738/212100452-147f8e5e-fbd9-4153-a73d-8eb9cf6b88f7.jpg)


# Future Works
จากการศึกษาปัจจัยที่ส่งผลต่อราคาทองคำที่กล่าวมานั้น จะเห็นได้ว่าปัจจัยที่มีผลต่อราคาทองคำ เช่น อัตราดอกเบี้ย ราคาน้ำมัน Demand เเละ Supply ของความต้องการของทองคำ และอาจรวมถึงสถานการณ์ทางการเมืองเชื่อมโยงถึงสภาวะเศรษฐกิจ เเละแนวโน้มค่าเงินดอลล่า (USD) ทำให้เกิดความผันผวนที่ส่งอิทธิพลต่อตลาดหุ้น <br />

ในการศึกษาครั้งนี้ ได้เลือกปัจจัยของค่าเงินดอลลา (USD) เพียงปัจจัยเดียวมาพยากรณ์ราคาทองคำ อาจไม่เพียงพอต่อความเเม่นยำ ให้อนาคตอาจนำปัจจัยส่วนต่าง ๆ ที่กล่าวมาข้างต้นมาร่วมพยากรณ์เพื่อให้การพยากรณ์ราคาทองคำให้มีประสิทธิภาพและมีความแม่นยำมากขึ้น

# Member
Advisor ผศ.ดร. เอกรัฐ รัฐกาญจน์ (ekaratnida)  
Director in Data Analytics and Data Science (DADS) MSc Program, Nida, Bkk, Thailand https://orcid.org/0000-0003-2191-3856  

- กมลวรรณ ตาวงศ์ 6410412001  
- พิชญภัส ผลสุขการ 6410412008  
- ศิริวลัย มณีสินธุ์ 6410412011  
- ภคนันท์ เนาว์รุ่งโรจน์ 6410412017
