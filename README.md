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
     2. [Media](#Media)
     3. [Code](#Code)
9. [Acknowledgements](#Acknowledgements)
***

## Introduction

The Wagging Tailor is a company which designs and creates custom clothing for pets. This includes anything from harnesses to biker jackets. This site was devevoloped to facilitate the sale and commision of these products, as well as provide information about the business and it's products. This site includes a products list, including individual product pages, a payment feature, and a personal profile for the user to enter their and their pet's information for future use.

This site was developed to be intuitive and appealing to users. There are options also for the site owner to add, edit and delete products from the site for future changes and new stock.

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
- As a Site User I want to be able to view a list of products so that I can select some to purchase.
- As a Site User I want to be able to view individual product details so that I can identify the price, description, product rating, product image and sizes.
- As a Site User I want to be able to quickly identify deals and promotions so that I can take advantage of special savings on products I'd like to purchase.
- As a Site User I want to be able to easily view the total of my purchase at any time so that I can avoid spending too much.
- As a Site User I want to be able to easily log in or log out so that I can access my personal account information.
- As a Site User I want to be able to easily recover my password in case I forget it so that I can recover access to my account.
- As a Site User I want to be able to receive an email confirmation after registering so that I can verify my account registration was successful.
- As a Site User I want to be able to have a personalised user profile so that I can view my personal order history and order confirmations and save my payment information.
- As a Site User I want to be able to be able to save my pet's measurements to my user profile so that I can remind myself of the correct sizing when ordering a product.
- As a Site User I want to be able to sort the list of available products so that I can easily identify the best rated, best priced and categorically sorted products.
- As a Site User I want to be able to sort a specific category of product so that I can find the best-priced or best-rated product in a specific category, or sort the products in that category by name.
- As a Site User I want to be able to search for a product by name or description so that I can find a specific product I'd like to purchase.
- As a Site User I want to be able to easily see what I've searched for and the number of results so that I can quickly decide whether the product I want is available.
- As a Site User I want to be able to easily select the size and quantity of a product when purchasing it so that I can ensure I don't accidentally select the wrong product, quantity or size.
- As a Site User I want to be able to view a specific category of products so that I can quickly find products I'm interested in without having to search through all products.
- As a Site User I want to be able to view items in my bag to be purchased so that I can Identify the total cost of my purchase and all items I will receive.
- As a Site User I want to be able to adjust the quantity of individual items in my bag so that I can easily make changes to my purchase before checkout.
- As a Site User I want to be able to receive an email confirmation after checking out so that I can keep the confirmation of what I've purchased for my records.
- As a Site User I want to be able to easily enter my payment info so that I can check out quickly and with no hassles.
- As a Site User I want to be able to feel my personal and payment information is safe and secure so that I can confidently provide the needed information to make a purchase.
- As a Site User I want to be able to view an order confirmation after checkout so that I can verify that I haven't made any mistakes.

#### Store Owner
- As a Store Owner I want to be able to add a product so that I can add new items to my store.
- As a store/owner I want to be able to edit/update a product so that I can change product prices, descriptions, images, and other product criteria.
- As a Store Owner I want to be able to delete a product so that I can Remove items that are no longer for sale.

### **Development Planes**
To create a comprehensive and appealing website, the developer researched other pet related websites to discover what features and functionality would be required. This information created the above user stories and is developed further below.

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
        - Fun loving
        - Creative
        - Outgoing
        - Playful

    - Values:
        - Loves animals
        - Fashionable
        - Trend setter

    - Lifestyles:
        - Has or knows someone who does have Pets
        - Keeps up with latest trends
        - Goes to pet shows
        - Likes to dress up


The website needs to enable the **Site User** to:
- Select that plan that suits the type of animal, as well as the toys/flavours they prefer.
- Purchase a subscription which renews each month unless instructed otherwise.
- View a selection of products not included in the subscription service.
- Create a personalised profile relating to their pet type and preferences

The website needs to enable the **Site Owner** to:
- Add, edit and delete products on the site.
- View orders in the admin screen

With the user stories in mind, the developer created the below strategy table to determine the trade-off of importance and viability with the following results:

![Strategy Table](media/README/strategy-table.png)

#### Scope
A scope was defined to identify what needed to be done to align features with the strategy previously defined. This was broken into two categories:

- **Content Requirements**
    - The user will be looking for:
        - A variety of designs to choose from
        - Details of the products provided
        - A way to search the site according to their preferred category, ie. Shirts
        - A personalised Profile Page displaying the user's details and their pet's measurements
- **Functionality Requirements**
    - The user will be able to:
        - Select their desired size for each product, ie. Cat-M or Dog-XS
        - Update their profile with pet details and images
        - Easily navigate the site to find product information.

#### Structure
The information architecture was organized in a hierarchical tree structure to ensure that users could navigate through the site with ease and efficiency, with the following results:

![Site Map](media/README/site-map.png)

#### Skeleton 
Wireframe mockups were created using [Balsamiq](https://balsamiq.com/ "Link to Balsamiq's site"), providing a positive user experience with the following results:

<details>
<summary>Home Page:</summary>

![Home Page Wireframe](media/README/wireframes/wireframe-home.png)
</details>

<details>
<summary>Products List Page:</summary>

![Product List Page Wireframe](media/README/wireframes/wireframe-products.png)
</details>

<details>
<summary>Product Details Page:</summary>

![Products Page Wireframe](media/README/wireframes/wireframe-product-details.png)
</details>

<details>
<summary>Shopping Bag Page:</summary>

![Shopping Bag Page Wireframe](media/README/wireframes/wireframe-bag.png)
</details>

<details>
<summary>Checkout Page:</summary>

![Checkout Page Wireframe](media/README/wireframes/wireframe-checkout.png)
</details>

<details>
<summary>Order Confirmation Page:</summary>

![Order Confirmation Page Wireframe](media/README/wireframes/wireframe-order-confirmation.png)
</details>

<details>
<summary>Personal Profile Page:</summary>

![Personal Profile Page Wireframe](media/README/wireframes/wireframe-profile.png)
</details>

<details>
<summary>Edit/Delete Profile Page:</summary>

![Edit/Delete Profile Page Page Wireframe](media/README/wireframes/wireframe-user-edit.png)
</details>

<details>
<summary>Order History Page:</summary>

![Order History Page Wireframe](media/README/wireframes/wireframe-order-history.png)
</details>

<details>
<summary>FAQs Page:</summary>

![FAQs Page Wireframe](media/README/wireframes/wireframe-faqs.png)
</details>

<details>
<summary>Edit/Delete Product Page:</summary>

![Edit/Delete Product Page Wireframe](media/README/wireframes/wireframe-admin-edit.png)
</details>

### Design

#### Colour Scheme
Sample text relating to colour

#### Typography
Sample text relating to Typography

#### Imagery
Sample text relating to Imagery

[Back to top ⇧](#Project-Name)

## Features

### Design Features
Nav Feature Desciption:
- Details of feature


<dl>
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
- **Feature** - feature description.
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

1. 

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

### Media
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
