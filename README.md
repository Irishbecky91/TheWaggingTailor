README.md

# The Wagging Tailor

![The Wagging Tailor  Logo](file path)

[View the live project here](https://the-wagging-tailor.herokuapp.com/ 'Link to the deployed Heroku site for The Wagging Tailor')

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

The Wagging Tailor is a company which designs and creates custom clothing for pets. This includes anything from harnesses to biker jackets. This site was developed to facilitate the sale and commission of these products, as well as provide information about the business and its products. This site includes a products list, including individual product pages, a payment feature, and a personal profile for the user to enter their and their pet's information for future use.

This site was developed to be intuitive and appealing to users, with a clean, attractive appearance and easy-to-use features. There are options also for the site owner to add, edit and delete products from the site for future changes and new stock.

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
- As a Store Owner, I want to be able to edit/update a product so that I can change product prices, descriptions, images, and other product criteria.
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
In addition to wireframes, a Database ER Diagram was mocked up to show the relationship between the various database structures.

![Database ER Diagram](static/media/README/database-diagram.png)


### Design

#### **Colour Scheme**
The colour scheme was influenced by the home page photo. The yellow colour of the dog's sweater was chosen for the message bar to tie the photo in and make an attractive appearance. The navy-coloured font, logo and nav background was influenced by the writing on the dog's ascot.

A clean white background was chosen for the top header to help give a pleasant, uncluttered appearance. The main background chosen was a white background with a very faint blue/grey pawprint pattern to give a subtle but playful design.

#### **Typography**
The font chosen for the headings and important text was Libre Baskerville for its simple, easy-to-read format. To complement this font, Open Sans was chosen for the standard text in text blocks and buttons, as well as the message bar.

#### **Imagery**
The imagery used in this site is entirely related to the products being sold, namely animals in clothing. A logo was also chosen to represent the company, showing an old-style sewing machine on top and a pawprint underneath.

[Back to top ⇧](#)

## Features

## Design Features
**Navigation & Header**

Each page of the website features a consistent responsive navigational system:

- **Logo** - The Logo image is linked to the home page, clicking it will bring the user back to the home page.

- **Search Bar** - The search bar is coded to display the results of the user's search request, using the product name and description as parameters.

- **User & Shopping Bag Icons** - There is an icon for both the user options dropdown and a link to the shopping bag showing the current bag total. The user icon's dropdown selection is updated depending on whether the user is logged in, logged out, or if they a logged in as a superuser. Each has varying options to choose from.

- **Links to Category Pages** - On the second row there are links to several categories of product pages. These pages show products of certain categories grouped by the type of clothing or category, eg. All Warm Wear would have Coats & Jackets, Hoodies And Sweaters categories displayed on the products screen.

- **Custom Orders Message** - Underneath the main navigation links, there is a section asking the user to click a link to be brought to a form submission page to request a custom order from the store owner.

**Footer**

Each page of the website features a consistent responsive footer design:

- **A 'Thank You' Piece Of Text** - The footer displays a small piece of text thanking the user for using this site. It also asks the user to get in touch regarding custom orders by clicking on a link.

- **Social Media Links** - These links connect the site user to the store's business profiles on Instagram and Facebook, and also the developer's LinkedIn and GitHub profiles.


<dl>
    <dt><a href="https://the-wagging-tailor.herokuapp.com/" target="_blank" alt="Home Page">Home Page</a></dt>
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
    <dt><a href="https://the-wagging-tailor.herokuapp.com/products/" target="_blank" alt="Products Page">Products Page</a></dt>
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
    <dt><a href="https://the-wagging-tailor.herokuapp.com/products/1/" target="_blank" alt="Product Info Page">Product Info Page</a></dt>
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
    <dt><a href="https://the-wagging-tailor.herokuapp.com/shopping_bag/" target="_blank" alt="Shopping Bag Page">Shopping Bag Page</a></dt>
    <dd>This page allows the user to view, edit and delete items in their shopping bag before going to the checkout screen:
        <ul>
            <li><strong>Product Information</strong> - This feature displays the information of each item added to the shopping bag. This includes the name, price, image, size and quantity of the product. If more than one size of a single product is selected, separate entries are shown on the page, showing the quantity of each size of the item.
            </li>
            <li><strong>Update/Remove Buttons</strong> - These features allow the user to update the quantity of an item in their shopping bag, or remove it entirely. Updating the quantity to '0' remove the item from the shopping bag.
            </li>
            <li><strong>Updated Total, Shipping and Grand Total</strong> - The total cost of the shopping bag updates each time an item is added, updated or removed from the shopping bag. If the user spends more than €100.00 on items, they qualify for free shipping. Otherwise, shipping is calculated to be 10% of the user's total cost, which is then added to create the grand total.
            </li>
        </ul>
    </dd>
    <dt><a href="https://the-wagging-tailor.herokuapp.com/checkout/" target="_blank" alt="Checkout Page">Checkout Page</a></dt>
    <dd>This page allows the user to securely enter their payment information before they :
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
- **Search bar** - This feature is used to find items on the site, matching the query's keywords to the item's name or description. These results are shown on the products page with an indicator of how many items were found using the keyword(s).
- **Shopping Bag Icon** - This feature shows the user the current total cost of the items in the shopping bag, including shipping.
- **Back-to-Top Button** - This feature is only available on certain pages and will bring the user back to the top of the page when clicked.
- **Query Form** - This feature allows the user to contact the store owner to ask a question, as well as request a quote. It includes a picture upload feature to help with queries and quotes.
- **Category Buttons** - This feature is a selection of buttons which filters the selection of products by the user's desired categories.
- **Sort-By Selector** - This feature is a selector box whose selections sort the product list by name, category, rating and price in both ascending and descending order.
- **Size Selector And Guide** - This feature only appears when the item has size options available. If the item has sizes, a selector box appears with a list of sizes. Underneath the product information, a sizing guide and measurement instruction image also appears for the user's convenience.
- **Increment/Decrement Quantity Buttons** - This feature is visible in the product info and shopping bag pages. It allows the user to click a button to update the item quantity instead of typing it in manually.
- **Success Message - Add A Product** - This feature appears each time the user adds an item to the shopping bag. It details the current shopping bag items, including quantity, sizes, names and images, as well as how much the user still  needs to spend to qualify for free shipping.
- **Update/Delete Buttons** - This feature is shown across the site. Examples are on the items in the shopping bag, on the pet profiles in the user's profile, and the products page when logged in as a superuser.
- **Checkout Form** - This feature allows the user to enter payment details, allowing them to purchase the items in their shopping bag. The form has required fields ensuring the user has all relevant fields filled in correctly before purchasing.
- **Order Confirmation** - This feature is shown after a purchase is made. It details the items purchased, their sizes, prices and quantity. It also lists the details provided on the checkout page as the shipping address. A similar page is shown through the profile page showing each previous order's confirmation details.
- **Pet Profile** - This feature displays a profile for each of the user's pets, including their measurements to assist with purchases. The profiles display the pet name, gender, breed, measurements and an image. A placeholder image is available if none is provided.
- **Add a pet form** - This feature allows the user to add profiles for each of their pets, including their name, gender, breed, measurements and an image. Each form filled adds a new 'pet profile' to the user's profile page.
- **Add/Edit Product Form** - This feature allows the site admin to add or edit a product on the site. If editing, all fields are populated for the admin to edit. If adding a product, a blank form is provided. The admin can add if sizes are available, a price, a title, a description, and an image. If no image is provided, a placeholder will be used instead.
- **** - feature description.
- **Feature** - feature description.
- **Feature** - feature description.

### Features to Implement in the future
- **Feature Name**
     - **Comments/Reviews section** - A comment or review section will be implemented in the future to allow users to add their thoughts on the products.
     - **Reason for not featuring in this release** - Time constraints in the development prevented this feature from being implemented before deployment. Further development of this site will see the implementation of this feature.
 
[Back to top ⇧](#)

## Issues and Bugs 
The developer ran into several issues during the development of the website, with the noteworthy ones listed below, along with solutions or ideas to implement in the future.

**Increment/Decrement Product Buttons** - In production, it was found that the increment/decrement buttons on the product page and shopping bag page were increasing/decreasing by 2 instead of 1. The developer investigated and found this was caused by two activations of the same code on each button press instead of one.
- ***Solution***: The developer discovered the code was being activated twice as the code was referenced in both the templates and the base.html. By removing the code from the base.html, the issue was resolved.

**Updating Quantity When Sizes Are Involved** - If there was more than one size of a specific item in the shopping bag and the user attempted to adjust the amount of a specific size, all other sizes were removed. In addition, the size indicator for the remaining item was removed so it was unclear which size the user is purchasing.
- ***Solution***: This issue was caused by a small section of code being mistyped. In line 33 of shopping_bag views.py, the developer had missed out **[size]** in the following line of code. Adding this piece of code rectified the issue:

```
shopping_bag[item_id]['items_by_size'][size] = quantity
```

**Toast Messages Not Appearing** - When a user added an item to their shopping bag, a success message was to appear in the top right corner of the screen. This did not happen and so the user was not able to see what the current shopping bag displayed.
- ***Solution***: The developer found the issue was caused by the version of Bootstrap they were using. The developer was using the JS control from Bootstrap4 but was using Bootstrap5 in the HTML. The developer decided to convert all Bootstrap5 code to Boostrap4 to keep with the deadline for the project. Changing to Bootstrap4 across the site corrected the issues.

**Remove Item Button In Shopping Bag** - The button used to remove a product from the shopping bag was not activating when clicked. This meant users were unable to remove items from the shopping bag.
- ***Solution***: This issue was resolved by adding the minified JQuery link in the HTML head, which was not added when the developer was reverting to Bootstrap4 from Bootstrap5 which did not require the link. When added, the user was able to remove any item from the shopping bag.

**Pet Profile Form Not Saving Pet Info** - There was an issue with the pet profiles where the form, when submitted, did not save the pet information to the profile user. This meant the information was not visible on the profile.
- ***Solution***: The issue was rectified by correcting the 'add_pet' view in the 'my_profile' app. In lines 41-43, the code was changed to not commit the save initially, register the 'userprofile' as the 'pet_owner', and then commit the save. below is the corrected code:

```
if pet_form.is_valid():
    pet = pet_form.save(commit=False)
    pet.pet_owner = request.user.userprofile
    pet.save()
```

**Sorting Selector Not Filter Products** - The Sort-by selector did not work on the products page, meaning the user was unable to filter the products by name, category, price or rating.
- ***Solution***: This issue was also resolved by adding the jQuery link to the base.html head. Adding this link allowed the code to work as it should allowing the user to filter in both ascending and descending order on the named filtering options.

**User Database not updating on Heroku** - When a user attempted to log in to the site or register on the deployed site only, they were met with a 500 error. This was due to the database not correctly updating and saving the user information from the development site.
- ***Solution***: To start, the developer corrected a line of code in the settings.py file following this, the developer assigned the DATABASE_URL ket to the GitPod variables and restarted the workspace. Next, the current database was dropped and the user migrated all changes again. Following this, the developer was able to test on both the local and deployed sites and found the functionality had returned.

**All User' Pet Info Showing Instead Of Only Current User** - On the profile page, when more than one user created a pet profile, all users' pet info was displayed on all users' profiles.
- ***Solution***: The developer had accidentally added '.all()' in the profile view, causing all available pet profiles to be called. This was rectified by correcting this to '.filter(pet_owner=profile)'. Now only the current user's pet info is displayed.

[Back to top ⇧](#)

## Technologies Used
### Main Languages Used
[Python](https://en.wikipedia.org/wiki/Python_(programming_language) "Wiki Page for Python")
[JavaScript](https://en.wikipedia.org/wiki/JavaScript "Wiki Page for JavaScript")
[CSS](https://en.wikipedia.org/wiki/CSS "Wiki Page for CSS")
[HTML](https://en.wikipedia.org/wiki/HTML "WikiPage for HTML")

### Frameworks, Libraries, Programs and Additional Languages Used
[Django](https://en.wikipedia.org/wiki/Django_(web_framework) "WikiPage for Django")
- Used to build the pages used in the site, from the models and forms to the views and page templates used.

[Bootstrap](https://en.wikipedia.org/wiki/Bootstrap_(front-end_framework) "Wiki Page for Bootstrap")
- Used to add uniform styling to the site without the use of large amounts of CSS.

[GitPod](https://gitpod.io/ "GitPod Site")
- Used for writing code, committing, and then pushing to GitHub.

[GitHub](https://github.com/ "GitHub Site")
- Used to store the project after pushing.

[Heroku](https://heroku.com/ "Heroku Site")
- Used to store the project after pushing.

[django-allauth](https://django-allauth.readthedocs.io/en/latest/ "django-allauth Docs")
- Used to store the project after pushing.

[Lucid](https://lucid.app/ "Lucid Site")
- Used to create a flowchart of information, making the logic of the game easily understood.

[AmIResponsive](https://ui.dev/amiresponsive "AmIResponsive Site")
- Used to generate mockup imagery of the terminal showing the game in use on Heroku.

[Back to top ⇧](#)

## Testing

Testing information can be found in a separate testing [file](TESTING.md "Link to testing file")

## Deployment

This project was developed using a [GitPod](https://gitpod.io/ "GitPod Site") workspace. The code was committed to Git and pushed to [GitHub](https://github.com/ "GitHub Site") using the terminal. The code was then remotely deployed to [Heroku](https://heroku.com/ "Heroku Site").

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
    - In the Settings tab, click on Reveal Config Vars and copy the URL next to DATABASE_URL.
    - In your GitPod workspace, create an env.py file in the main directory. 
    - Add the DATABASE_URL value and your chosen SECRET_KEY value to the env.py file.
    - Add the SECRET_KEY value to the Config Vars in Heroku.
    - Update the settings.py file to import the env file and add the SECRETKEY and DATABASE_URL file paths.
    - Update the Config Vars with the Cloudinary URL, adding into the settings.py file also.
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
    - Go to the 'Deploy' tab on Heroku and connect to GitHub, then to the required repository.
    Click on 'Deploy Branch' and wait for the build to load. When the build is complete, the app can be opened through Heroku. 

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
This will trigger a new GitPod workspace to be created from the code in GitHub where you can work locally.

How to run this project within a local IDE, such as VSCode:

1. Log into [GitHub](https://github.com/login "Link to GitHub login page") or [create an account](https://github.com/join "Link to GitHub create account page").
2. Locate the [GitHub Repository](repo URL "Link to GitHub Repo").
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

[Back to top ⇧](#)

## Credits 

### Content
- The webpage [GitHub Docs - Fork a Repo](https://docs.github.com/en/github-ae@latest/get-started/quickstart/fork-a-repo 'Link to GithHub Docs - Fork a Repo') was used to get instructions on forking and cloning a repository. This information was used in the Deployment section of the README file.

### Static/Media
- Most images on the site were sourced from [Unsplash](https://unsplash.com/ 'Link to Unsplash'), [Pexels](https://www.pexels.com/ 'Link to Unsplash') and [PXHere](https://pxhere.com/ 'Link to Unsplash'). Below is the list of artists whose images were used in this project.

**UNSPLASH ARTISTS**

- Mocna Fotografia
- Karsten Winegeart
- FLOUFFY
- charlesdeluvio
- Matt Walsh
- Jay Wennington
- Alexandra Novitskaya
- Martin Castro
- Max Simonov
- Pearl Lynn
- Kerwin Elias
- Aneta Voborilova
- Sophia Kunkel
- Delaney Dawson
- Reba Spike
- Đồng Phục Hải Triều
- Amber Kipp
- The3dragons
- Paul Hanaoka

**PEXELS ARTISTS**

- Alice Castro
- Kat Smith
- Peng Louis
- Pırıl Şahin
- Mister Mister
- Breno Cardoso
- Skyler Ewing
- Eric Mclean
- Enzo Muñoz
- Maria Lindsey Content Creator
- Juan Vargas
- Kelly L
- Eun Suk
- Koi San

**PXHERE ARTISTS**
- typertitor

### Code 
Did the developer use outside references when building code?
- [Stack Overflow](https://stackoverflow.com/ "Link to Stack Overflow page")
- [W3Schools](https://www.w3schools.com/ "Link to W3Schools page")
- [Bootstrap](https://getbootstrap.com/ "Link to BootStrap page")
- [Django Docs](https://docs.djangoproject.com/en/4.0/ 'Link to Django Docs')
- etc.


[Back to top ⇧](#)

## Acknowledgements

- I would like to thank my friends and family for their valued opinions and criticism during the process of design and development.
- I would like to give a massive thank you to the Tutor support network who guided me through fixing many of the bugs on this site.
- I would also like to thank my mentor, Chris, for his invaluable help and guidance throughout the process.

[Back to top ⇧](#)

***
