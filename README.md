README.md

# The Wagging Tailor

![The Wagging Tailor  Logo](file path)

[View the live project here](depolyed link)

## Table of contents
1. [Introduction](#Introduction)
2. [UX](#UX)
    1. [Ideal User Demographic](#Ideal-User-Demographic)
    2. [User Stories](#User-Stories)
    3. [Development Planes](#Development-Planes)
    4. [Design](#Design)
3. [Features](#Features)
    1. [Design Features](#Design-Features) 
    2. [Existing Features](#Existing-Features)
    3. [Features to Implement in the future](#Features-to-Implement-in-the-future)
4. [Issues and Bugs](#Issues-and-Bugs)
5. [Technologies Used](#Technologies-Used)
     1. [Main Languages Used](#Main-Languages-Used)
     2. [Additional Languages Used](#Additional-Languages-Used)
     3. [Frameworks, Libraries & Programs Used](#Frameworks,-Libraries-&-Programs-Used)
6. [Testing](#Testing)
     1. [Testing.md](TESTING.md)
7. [Deployment](#Deployment)
     1. [Deploying on Heroku](#Deploying-on-Heroku)
     2. [Forking the Repository](#Forking-the-Repository)
     3. [Creating a Clone](#Creating-a-Clone)
8. [Credits](#Credits)
     1. [Content](#Content)
     2. [static/Media](#static/Media)
     3. [Code](#Code)
9. [Acknowledgements](#Acknowledgements)
***

## Introduction

The Wagging Tailor is a company which designs and creates custom clothing for pets. This includes anything from harnesses to biker jackets. This site was devoloped to facilitate the sale and commission of these products, as well as provide information about the business and its products. This site includes a products list, including individual product pages, a payment feature, and a personal profile for the user to enter their and their pet's information for future use.

This site was developed to be intuitive and appealing to users, with a clean, attractive appearance and easy to use features. There are options also for the site owner to add, edit and delete products from the site for future changes and new stock.

[Back to top ⇧](#)

## UX 

### Ideal User Demographic
#### The ideal user of this website is:
- Pet Owners
- Animal Lovers
- Gift Givers
- Trendy Individuals
- Fashionable Individuals


### User Stories
#### Site User:
- As a Site User, I want to be able to view a list of products so that I can select some to purchase.
- As a Site User, I want to be able to view individual product details so that I can identify the price, description, product rating, product image and sizes.
- As a Site User, I want to be able to quickly identify deals and promotions so that I can take advantage of special savings on products I'd like to purchase.
- As a Site User, I want to be able to easily view the total of my purchase at any time so that I can avoid spending too much.
- As a Site User, I want to be able to easily log in or log out so that I can access my personal account information.
- As a Site User, I want to be able to easily recover my password in case I forget it so that I can recover access to my account.
- As a Site User, I want to be able to receive an email confirmation after registering so that I can verify my account registration was successful.
- As a Site User, I want to be able to have a personalised user profile so that I can view my order history and order confirmations and save my payment information.
- As a Site User, I want to be able to save my pet's measurements to my user profile so that I can remind myself of the correct sizing when ordering a product.
- As a Site User, I want to be able to sort the list of available products so that I can easily identify the best rated, best priced and categorically sorted products.
- As a Site User, I want to be able to sort a specific category of product so that I can find the best-priced or best-rated product in a specific category, or sort the products in that category by name.
- As a Site User, I want to be able to search for a product by name or description so that I can find a specific product I'd like to purchase.
- As a Site User, I want to be able to easily see what I've searched for and the number of results so that I can quickly decide whether the product I want is available.
- As a Site User, I want to be able to easily select the size and quantity of a product when purchasing it so that I can ensure I don't accidentally select the wrong product, quantity or size.
- As a Site User, I want to be able to view a specific category of products so that I can quickly find products I'm interested in without having to search through all products.
- As a Site User, I want to be able to view items in my bag to be purchased so that I can Identify the total cost of my purchase and all items I will receive.
- As a Site User, I want to be able to adjust the number of individual items in my bag so that I can easily make changes to my purchase before checkout.
- As a Site User, I want to be able to receive an email confirmation after checking out so that I can keep the confirmation of what I've purchased for my records.
- As a Site User, I want to be able to easily enter my payment info so that I can check out quickly and with no hassles.
- As a Site User, I want to be able to feel my personal and payment information is safe and secure so that I can confidently provide the needed information to make a purchase.
- As a Site User, I want to be able to view an order confirmation after checkout so that I can verify that I haven't made any mistakes.

#### Store Owner
- As a Store Owner, I want to be able to add a product so that I can add new items to my store.
- As a store Owner, I want to be able to edit/update a product so that I can change product prices, descriptions, images, and other product criteria.
- As a Store Owner, I want to be able to delete a product so that I can remove items that are no longer for sale.

### **Development Planes**
To create a comprehensive and appealing website, the developer researched other pet-related websites to discover what features and functionality would be required. This information created the above user stories and is developed further below.

#### Main Inspirations
- [BarkBox](https://www.barkbox.com/ "Link to BarkBox")
- [Great Pet](https://home.greatpetcare.com/ "Link to Great Pet")
- [Chewy](https://www.chewy.com/ "Link to Great Pet")

#### **Strategy**
Broken into three categories, the website will attempt to focus on the following target audiences:
- **Roles:**
     - Site User
     - Site Owner

- **Demographic:**
     - Young to mature adults
     - Pet owners
     - Gift givers

- **Psychographics:**
    - Personality & Attitudes:
        - Fun-loving
        - Creative
        - Outgoing
        - Playful

    - Values:
        - Loves animals
        - Fashionable
        - Trendsetter

    - Lifestyles:
        - Has or knows someone who does have Pets
        - Keeps up with the latest trends
        - Goes to pet shows
        - Likes to dress up


The website needs to enable the **Site User** to:
- Find attractive products designed for pets, including various sizes specific to pet types.
- Add their desired products to the shopping bag for purchasing.
- Filter products according to name, categories, rating and prices.
- Search products by name or description.
- Create a personalised profile relating to their pet type and measurements.

The website needs to enable the **Site Owner** to:
- Add, edit and delete products on the site.
- View orders on the admin screen

With the user stories in mind, the developer created the below strategy table to determine the trade-off of importance and viability with the following results:

![Strategy Table](static/media/README/strategy-table.png)

#### **Scope**
A scope was defined to identify what needed to be done to align features with the strategy previously defined. This was broken into two categories:

- **Content Requirements**
    - The user will be looking for:
        - A variety of designs to choose from
        - Details of the products provided
        - A way to search the site using the name or description fields.
        - A filtering function by rating, name, price and category
        - A personalised Profile Page displaying the user's details and their pet's measurements
- **Functionality Requirements**
    - The user will be able to:
        - Select their desired size for each product, ie. Cat-M or Dog-XS
        - Update their profile with pet details and images
        - Easily navigate the site to find product information.

#### **Structure**
The information architecture was organized in a hierarchical tree structure to ensure that users could navigate through the site with ease and efficiency, with the following results:

![Site Map](static/media/README/site-map.png)

#### **Skeleton**

Wireframe mockups were created using [Balsamiq](https://balsamiq.com/ "Link to Balsamiq's site"), providing a positive user experience with the following results:

<details>
<summary>Home Page:</summary>

![Home Page Wireframe](static/media/README/wireframes/wireframe-home.png)
</details>

<details>
<summary>Products List Page:</summary>

![Product List Page Wireframe](static/media/README/wireframes/wireframe-products.png)
</details>

<details>
<summary>Product Details Page:</summary>

![Products Page Wireframe](static/media/README/wireframes/wireframe-product-details.png)
</details>

<details>
<summary>Shopping Bag Page:</summary>

![Shopping Bag Page Wireframe](static/media/README/wireframes/wireframe-bag.png)
</details>

<details>
<summary>Checkout Page:</summary>

![Checkout Page Wireframe](static/media/README/wireframes/wireframe-checkout.png)
</details>

<details>
<summary>Order Confirmation Page:</summary>

![Order Confirmation Page Wireframe](static/media/README/wireframes/wireframe-order-confirmation.png)
</details>

<details>
<summary>Personal Profile Page:</summary>

![Personal Profile Page Wireframe](static/media/README/wireframes/wireframe-profile.png)
</details>

<details>
<summary>Edit/Delete Profile Page:</summary>

![Edit/Delete Profile Page Page Wireframe](static/media/README/wireframes/wireframe-user-edit.png)
</details>

<details>
<summary>Order History Page:</summary>

![Order History Page Wireframe](static/media/README/wireframes/wireframe-order-history.png)
</details>

<details>
<summary>FAQs Page:</summary>

![FAQs Page Wireframe](static/media/README/wireframes/wireframe-faqs.png)
</details>

<details>
<summary>Edit/Delete Product Page:</summary>

![Edit/Delete Product Page Wireframe](static/media/README/wireframes/wireframe-admin-edit.png)
</details>


#### **Database Structure**
In addition to wireframes, a Database ER Disgram was mocked up to show the relationship between the various database structures.

![Database ER Diagram](static/media/README/database-diagram.png)


### Design

#### **Colour Scheme**
The colour scheme was influenced by the home page photo. The yellow colour of the dog's sweater was chosen for the message bar to tie the photo in and make an attractive appearance. The navy coloured font, logo and nav background was influenced by the writing on the dog's ascot.

A clean white background was chosen for the top header to help give a pleasant, uncluttered appearance. The main background chosen was a white background with a very faint blue/grey pawprint pattern to give a subtle but playful design.

#### **Typography**
The font chosen for the headings and important text was Libre Baskerville for its simple, easy-to-read format. To complement this font, Open Sans was chosen for the standard text in text blocks and buttons, as well as the message bar.

#### **Imagery**
The imagery used in this site is entirely related to the products being sold, namely animals in clothing. A logo was also chosen to represent the company, showing an old-style sewing machine on top and a pawprint underneath.

[Back to top ⇧](#)

## Features

### Design Features
**Navigation & Header**

Each page of the website features a consistent responsive navigational system:

- **Logo** - The Logo image is linked to the home page, clicking it will bring the user back to the home page.

- **Search Bar** - The search bar is coded to display the results of the user's search request, using the product name and description as parameters.

- **User & Shopping Bag Icons** - There is an icon for both the user options dropdown and a link to the shopping bag showing the current bag total. The user icon's dropdown selection is updated depending on whether the user is logged in, logged out, or if they a logged in as a superuser. Each has varying options to choose from.

- **Links to Category Pages** - On the second row there are links to several categories of product pages. These pages show products in a number of categories linked to a specific type, eg. All Warm Wear would have Coats & Jackets, Hoodies And Sweaters categories displayed on the products screen.

- **Custom Orders Message** - Underneath the main navigation links, there is a section asking the user to click a link to be brought to a form submission page to request a custom order from the store owner.

**Footer**

Each page of the website features a consistent responsive footer design:

- **'Thank You' Text** - The footer displays a small piece of text thanking the user for using this site. It also asks the user to get in touch regarding custom orders by clicking on a link.

- **Social Media Links** - These links connect the site user to the store's business profiles on Instagram and Facebook, and also the developer's LinkedIn and GitHub profiles.


<dl>
    <dt><a href="#" target="_blank" alt="Home Page">Home Page</a></dt>
    <dd>The home page is the main entry page to the site, it introduces the people involved in the store and gives a sneak peek into some of the products:
        <ul>
            <li><strong>Main Image</strong> - This feature is an image underneath the navigation bar and Custom Orders message bar. The image displayed is of a dog wearing an outfit sold in the store, with the company name and logo also displayed.
            </li>
            <li><strong>Introduction Cards</strong> - Directly underneath the Main Image is a welcome message and a set of three cards that display the person/pet's name, image and a short text piece about each one.
            </li>
            <li><strong>Product Carousel</strong> - Next is the Product Carousel which displays some of the products sold in the store. Clicking on the button will bring you to that specific product's info page.
            </li>
            <li><strong>Category Cards</strong> - These cards invite the user to view products related to the categories 'Warm Wear' and 'Accessories'. There is a short description of the category and a link for the user to go to the category's product page.
            </li>
        </ul>
    </dd>
    <dt><a href="#" target="_blank" alt="Products Page">Products Page</a></dt>
    <dd>This page displays a list of all products. The user can use filters and search queries to filter the list to their desired results:
        <ul>
            <li><strong>Product Category Links</strong> - Directly below the 'Products' heading are a set of button links that filter the list of products to the selected category.
            </li>
            <li><strong>Products Home Link</strong> - There is a link to bring the user back to the 'Products Home', this will display all products rather than filtering by category or search queries.
            </li>
            <li><strong>Search Results/Product Counter</strong> - Right next to the link to the 'Products Home' is a counter that tells the user how many products are displayed on the page. If the user has entered a search query, the counter will advise how many products were found for that specific search query.
            </li>
            <li><strong>Sort By Selector</strong> - This selector allows the user to order the products displayed by name, rating, price and category in both ascending and descending orders.
            </li>
            <li><strong>Product Cards</strong> - The product cards display the products listed on the site. The information shown on each card is the product's image, name, price, category and rating. There is a single card for each product.
            </li>
        </ul>
    </dd>
    <dt><a href="#" target="_blank" alt="Product Info Page">Product Info Page</a></dt>
    <dd>This page will render the information for the chosen product and allow the user to select a size and add the item to the shopping bag:
        <ul>
            <li><strong>Product Details</strong> - The product details change for each product. This would include the product image, name, description, price, rating and category.
            </li>
            <li><strong>Size Selector</strong> - The size selector can be used to select the specific size the user wishes to purchase, eg. Dog XS (Teacup Chihuahua) or Cat XL (Maine Coon)
            </li>
            <li><strong>Add to Bag Button</strong> - When the user has selected their chosen size, they would click the Add to Bag button to add the desired product and size to their shopping bag for purchasing.
            </li>
            <li><strong>Comments Section</strong> - Underneath the product information is a commenting feature where users can leave comments about the product. These comments can only be added by users who have an account.
            </li>
        </ul>
    </dd>
    <dt><a href="#" target="_blank" alt="Page">Page</a></dt>
    <dd>description of page:
        <ul>
            <li><strong>feature</strong> - description.
            </li>
            <li><strong>feature</strong> - description.
            </li>
        </ul>
    </dd>
    <dt><a href="#" target="_blank" alt="Page">Page</a></dt>
    <dd>description of page:
        <ul>
            <li><strong>feature</strong> - description.
            </li>
            <li><strong>feature</strong> - description.
            </li>
        </ul>
    </dd>
    <dt><a href="#" target="_blank" alt="Page">Page</a></dt>
    <dd>description of page:
        <ul>
            <li><strong>feature</strong> - description.
            </li>
            <li><strong>feature</strong> - description.
            </li>
        </ul>
    </dd>
</dl>
 
### Existing Features
- **Search bar** - This feature is user to find items on the site, matching the queries keywords to the items name or description. These results are shown in the products page with an indicator of how many items were found using the keyword(s).
- **Shopping Bag Icon** - This feature shows the user the current total cost of the items in the shopping bag, including shipping.
- **Back-to-Top Button** - This feature is only available on certain pages and will bring the user back to the top of the page when clicked.
- **Query Form** - This feature allows the user to contact the store owner to ask a question, as well as request a quote. It includes a picture upload feature to help with queries and quotes.
- **Category Buttons** - This feature is a selections of buttons which filters the selection of products by the user's desired categories.
- **Sort-By Selector** - This feature is a selector box whose selections sort the product list by name, category, rating and price in both ascending and descending order.
- **Size Selector And Guide** - This feature only appears when the item has size options available. If the item has sizes, a selector box appears with a list of sizes. Underneath the product information, a sizing guide and measurement instruction image also appears for the users convenience.
- **Increment/Decrement Quantity Buttons** - This feature is visible in the product info and shopping bag pages. It allows the user to cick a button to update the item quantity instead of typing it in manually.
- **Success Message - Add A Product** - This feature appears each time the user adds an item to the shopping bag. It details the current shopping bag items, including quantity, sizes, names and images, as well as how much the user still  needs to spend to qualify for free shipping.
- **Checkout Form** - This feature allows the user to enter payment details, allowing them to purchase the items in their shopping bag. The form has required fields ensuring the user has all relevant fields filled in correctly before purchasing.
- **Order Confirmation** - This feature is shown after a purchase is made. It details the items purchased, their sizes, prices and quantity. It also lists the details provided in the checkout page as the shipping address. A similar page is shown throught the profile page showing each previous order's confirmation details.
- **Pet Profile** - feature description.
- **Feature** - feature description.
- **Feature** - feature description.

### Features to Implement in the future
- **Feature Name**
     - **Feature** - description.
     - **Reason for not featuring in this release** - reason.
 
[Back to top ⇧](#Project-Name)

## Issues and Bugs 
Sample text about bugs

**Bug** - bug description.
	- ***Solution***: description

**Bug** - bug description.
	- ***Solution***: description

[Back to top ⇧](#Project-Name)

## Technologies Used
### Main Languages Used
- [Technology](Wiki Link "description of link")
- [Technology](Wiki Link "description of link")

### Additional Languages Used
- [Technology](Wiki Link "description of link")
     - Used to .

### Frameworks, Libraries & Programs Used
- [Technology](Wiki Link "description of link")
     - Used to .

[Back to top ⇧](#Project-Name)

## Testing

Testing information can be found in a separate testing [file](TESTING.md "Link to testing file")

## Deployment

This project was developed using .

### Deploying on Heroku
To deploy this page to Heroku from its GitHub repository, the following steps were taken:

### Deploying on Heroku
To deploy this page to Heroku from its GitHub repository, the following steps were taken:

1. Create the Heroku App:
    - Select "Create new app" in Heroku.
    - Choose a name for your app and select the location.

2. Attach the Postgres database:
    - In the Resources tab, under add-ons, type in Postgres and select the Heroku Postgres option.

3. Prepare the environment and settings.py file:
    - In the Settings tab, click on Reveal Config Vars and copy the url next to DATABASE_URL.
    - In your GitPod workspace, create an env.py file in the main directory. 
    - Add the DATABASE_URL value and your chosen SECRET_KEY value to the env.py file.
    - Add the SECRET_KEY value to the Config Vars in Heroku.
    - Update the settings.py file to import the env file and add the SECRETKEY and DATABASE_URL file paths.
    - Update the Config Vars with the Cloudinary url, adding into the settings.py file also.
    - In settings.py add the following sections:
        - STATIC_URL
        - STATICFILES_DIRS
        - MEDIA_URL
        - MEDIA_ROOT
        - TEMPLATES_DIR
        - Update DIRS in TEMPLATES with TEMPLATES_DIR
        - Update ALLOWED_HOSTS with ['app_name.herokuapp.com', 'localhost']

4. Set DISABLE_COLLECTSTATIC and Deploy to Heroku:
    - Create three directories in the main directory; media, storage and templates.
    - Create a file named "Procfile" in the main directory and add the following:
        - web: gunicorn project-name.wsgi
    - in the terminal, log in to Heroku and then enter the following:
        - heroku config:set DISABLE_COLLECTSTATIC=1 --app (Heroku App Name)
    - Go to Deploy tab on Heroku and connect to the GitHub, then to the required recpository.
    Click on Delpoy Branch and wait for the build to load. When the build is complete, the app can be opened through Heroku. 

### Forking the Repository
By forking the GitHub Repository we make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original repository by using the following steps...

1. Log into [GitHub](https://github.com/login "Link to GitHub login page") or [create an account](https://github.com/join "Link to GitHub create account page").
2. Locate the [GitHub Repository](https://github.com/rebeccatraceyt/KryanLive "Link to GitHub Repo").
3. At the top of the repository, on the right side of the page, select "Fork"
4. You should now have a copy of the original repository in your GitHub account.

### Creating a Clone
How to run this project locally:
1. Install the [GitPod Browser](https://www.gitpod.io/docs/browser-extension/ "Link to Gitpod Browser extension download") Extension for Chrome.
2. After installation, restart the browser.
3. Log into [GitHub](https://github.com/login "Link to GitHub login page") or [create an account](https://github.com/join "Link to GitHub create account page").
2. Locate the [GitHub Repository](https://github.com/rebeccatraceyt/KryanLive "Link to GitHub Repo").
5. Click the green "GitPod" button in the top right corner of the repository.
This will trigger a new gitPod workspace to be created from the code in github where you can work locally.

How to run this project within a local IDE, such as VSCode:

1. Log into [GitHub](https://github.com/login "Link to GitHub login page") or [create an account](https://github.com/join "Link to GitHub create account page").
2. Locate the [GitHub Repository](repo url "Link to GitHub Repo").
3. Under the repository name, click "Clone or download".
4. In the Clone with HTTPs section, copy the clone URL for the repository.
5. In your local IDE open the terminal.
6. Change the current working directory to the location where you want the cloned directory to be made.
7. Type 'git clone', and then paste the URL you copied in Step 3.
```
git clone https://github.com/USERNAME/REPOSITORY
```
8. Press Enter. Your local clone will be created.

Further reading and troubleshooting on cloning a repository from GitHub [here](https://docs.github.com/en/free-pro-team@latest/github/creating-cloning-and-archiving-repositories/cloning-a-repository "Link to GitHub troubleshooting")

[Back to top ⇧](#Project-Name)

## Credits 

### Content
- sample text.

### static/Media
- images sourced from .
- Text sourced from .

### Code 
Did the developer use outside references when building code?
- [Stack Overflow](https://stackoverflow.com/ "Link to Stack Overflow page")
- [W3Schools](https://www.w3schools.com/ "Link to W3Schools page")
- [Bootstrap](https://getbootstrap.com/ "Link to BootStrap page")
- etc.


[Back to top ⇧](#Project-Name)

## Acknowledgements

- I would like to thank my friends and family for their valued opinions and critic during the process of design and development.
- I would also like to thank my mentor, Name, for his/her invaluable help and guidance throughout the process.

[Back to top ⇧](#Project-Name)

***
