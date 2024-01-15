from bs4 import BeautifulSoup
import requests

"Created By: Manan Agrawal"
"Roll no: 23bcs10206"
"Email-id: manan.23bcs10206@ms.sst.scaler.com"

#Step 1: Get the product name from the user.
print("Welcome to the Price Comparison Software")
search_item = input("Enter the product name: ")

#Step 2: Create a header for the request.
header = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/119.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,/;q=0.8"
}

#Step 3: Create a request to fetch the data from the website.
amazon = "https://www.amazon.in/s?k=" + search_item
flipkart = "https://www.flipkart.com/search?q=" + search_item

responseOnAmazon = requests.get(url=amazon, headers=header)
responseOnFlipkart = requests.get(url=flipkart, headers=header)


#Step-4: Store the data in a variable.
"---->for amazon"
if responseOnAmazon.status_code == 200:
    soup = BeautifulSoup(responseOnAmazon.text, 'lxml')
    productOnAmazon = soup.find_all('div', attrs={"data-component-type":"s-search-result"})
    AmazonProductList = []
    for product in productOnAmazon[:3]:
        productNameEl = product.find('span', class_='a-size-medium a-color-base a-text-normal') 
        if not productNameEl:
            productNameEl = product.find('span', class_='a-size-base-plus a-color-base a-text-normal')
        if productNameEl:
            productName = productNameEl.text.strip()
            productPrice = product.find('span', class_='a-price-whole').text.strip()
            AmazonProductList.append({'name': productName, 'price': productPrice})
        else:
            print("Product name not found on Amazon for this item.")
else:
    print("Failed to fetch data from Amazon")

"---->for flipkart"
if responseOnFlipkart.status_code == 200:
    soup = BeautifulSoup(responseOnFlipkart.text, 'lxml')
    productOnFlipkart = soup.find_all('div', class_='_2kHMtA')
    FlipkartProductList = []
    for product in productOnFlipkart[:3]:
        productNameEl = product.find('div', class_='_4rR01T')
        if not productNameEl:
            productNameEl = product.find('a', class_='s1q9rs')
        if productNameEl:
            productName = productNameEl.text.strip()
            productPrice = product.find('div', class_='_30jeq3').text.strip()
            FlipkartProductList.append({'name': productName, 'price': productPrice})
        else:
            print("Product name not found on Flipkart for this item.")
else:
    print("Failed to fetch data from Flipkart")

# Displaying results
print("\n")
print("Amazon Product List:")
for i, product in enumerate(AmazonProductList):
    print(f"{i+1}. {product['name']} : ₹{product['price']}")

print("\n")
print("Flipkart Product List:")
for i, product in enumerate(FlipkartProductList):
    print(f"{i+1}. {product['name']} : {product['price']}")

print("\n")
print("Thank you for using this software!")
