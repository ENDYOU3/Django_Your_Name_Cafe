# Django_Your_Name_Cafe
This is a web-app created using Python and Django. This allows the user to login, add items to their cart, delete items from their cart, view their shopping history, and so on. 

## Function :
   -  Save product into the database (admin-page)
   -  Show all products
   -  Show products for each type
   -  Show details of the product
   -  Add products to your cart.
   -  Delete products form the cart
   -  Add customer addresses
   -  Save customer addresses into the database.
   -  Show all orders and total price
   -  Save orders into the database
   -  History shopping
   -  Contact
   -  Login
   -  Logout  
   -  Register

## Implementation :
**Programming Language :** `python`,  `html`

**Libraries :** `Django`,  `mysql-connector-python`,  `python-dotenv`, `pillow`

## Installation : 
### Run with Integrated development environment (IDE)
**Create environment and install package :** 
   -  Open file location on `terminal` or `cmd`
```bash
   cd "location path"
```
   -  install `pipenv`
```bash
   pip install pipenv
```
   -  Activate a virtual environment
```bash
   pipenv shell
```
   -  Install all packages in pipfile
```bash
   pipenv install
```

**Create super user**
```bash
   python manage.py createsuperuser
```

**Change setting in .env**
   -  Change settings according to your device.

**Run Server**
```bash
   python manage.py runserver
```

**In your web browser enter the address : http://localhost:8000 or http://127.0.0.1:8000/**

**If you do something in models.py (database)**
   -  applying and unapplying migrations
```bash
   python manage.py makemigrations
```
   -  creating new migrations based on the changes you have made to your models
```bash
   python manage.py migrate
```

## Screenshots :
![login](https://user-images.githubusercontent.com/103243756/225934878-2770a9b2-6120-421b-a860-6b5f617dcb9b.JPG)
![register](https://user-images.githubusercontent.com/103243756/225934892-813d050f-a9c2-4ee2-94e4-d12de42b880b.JPG)
![all_product](https://user-images.githubusercontent.com/103243756/225934936-88e354ab-0ac0-4112-aff3-45db5630ac7c.JPG)
![product_detail](https://user-images.githubusercontent.com/103243756/225937096-2a384f31-0b63-43b1-adc5-025ae8caa14b.JPG)
![shopping_cart](https://user-images.githubusercontent.com/103243756/225935046-8f80d9aa-6fc1-41a6-bd9f-7123e45801b7.JPG)
![order_list](https://user-images.githubusercontent.com/103243756/225935080-15617587-89f9-4533-9a32-ee58c5915bd3.JPG)
![add_address](https://user-images.githubusercontent.com/103243756/225935126-c65beb6e-2b88-4eb1-a8a3-360fef996b36.JPG)
![order_list2](https://user-images.githubusercontent.com/103243756/225935086-a91318e1-083f-4925-befe-5dccda0327b7.JPG)
![order_history](https://user-images.githubusercontent.com/103243756/225935142-64e606fa-b0dc-4f0c-97b4-43bbe8c29758.JPG)
![contact](https://user-images.githubusercontent.com/103243756/225935159-b348a37e-637a-4e64-8217-fc7a5140724d.JPG)

## Credit :
   - Picture of coffee
   https://www.olivemagazine.com/recipes/collection/best-ever-coffee-recipes/
   - Picture of tea
   https://guide.michelin.com/us/en/article/features/7-varieties-of-green-tea-explained
   https://freshtea.com/black-tea/
   https://www.freepik.com/premium-photo/thai-milk-tea-with-bubble-brown-sugar_18514947.htm
   - Picture of cake
   https://www.cookwithprincess.com/recipe/red-velvet-cake/
   - Picture of home-page
   https://www.freepik.com/premium-photo/scatteing-coffee-beand-coffee-cup-with-coffee-beans-bamboo-tray_5810228.htm#query=coffee&position=26&from_view=search&track=sph
   https://www.freepik.com/free-photo/porcelain-gaiwan-three-cups-chinese-tea-golden-frog-tea-desk_2584175.htm#query=tea&position=45&from_view=search&track=sph
   https://www.freepik.com/free-photo/arrangement-with-delicious-traditional-thai-tea_15035746.htm#query=milk%20tea&position=7&from_view=search&track=sph
