# Student Rations - Testing 

[Main README.md file](/README.md)

[View live project](https://the-wagging-tailor.herokuapp.com/)

[View GitHub repository](https://github.com/Irishbecky91/TheWaggingTailor)

***
## Table of contents
1. [Testing User Stories](#Testing-User-Stories)
2. [Manual Testing](#Manual-Testing)
3. [Automated Testing](#Automated-Testing) 
     - [Code Validation](#Code-Validation)
4. [User Testing](#User-Testing)


***

## Testing User Stories

### User Stories:
#### Site User
##### **Activities**
- As a Site User, I want to be able to save my pet's measurements to my user profile so that I can remind myself of the correct sizing when ordering a product.
    - There is a form available for the user to add a profile entry for each pet, detailing their name, breed, gender, mesaurements and an image.

- As a Site User, I want to be able to leave a comment on a product so that others can see my thoughts regarding the product.    
    - There is a form on the product info page which allows the user to add a title and the body of a comment to the product page. The comment will detail the user's username, date of entry, and the title and body of the comment.

##### **Steps**
- As a Site User, I want to be able to search for a product by name or description so that I can find a specific product I'd like to purchase.
    - There is a search bar in the header which allows users to search for products based on keywords in the description or name fields.

- As a Site User, I want to be able to sort the list of available products so that I can easily identify the best rated, best priced and categorically sorted products.
    - There is a 'sort-by' selector box on the products page which allows the user to sort the products by rating, name, price and category in ascending or decending order.

- As a Site User, I want to be able to sort a specific category of product so that I can find the best-priced or best-rated product in a specific category, or sort the products in that category by name.
    - There are navigation links and filter buttons that allow the user to view all products of a certin category or group of categories.

- As a Site User, I want to be able to easily select the size and quantity of a product when purchasing it so that I can ensure I don't accidentally select the wrong product, quantity or size.
    - On the product info page, there is a selection box for sizes, with a helpful sizing guide and diagram underneath, and a quantity selector with increment and decrement buttons beside it.

- As a Site User, I want to be able to adjust the number of individual items in my bag so that I can easily make changes to my purchase before checkout.
    - There is a quantity increment and decrement button with an update button that allows the user to increase or decrease the number of the specific item they wish to purchase.

- As a Site User, I want to be able to easily log in or log out so that I can access my personal account information.
    - There is a link in the header which allows the user to log in, log out and register for an account.

- As a Site User, I want to be able to easily recover my password in case I forget it so that I can recover access to my account.
    - There is an option on the log in page to request a resst password link be sent to the user's email address. Clicking the link and entering an email address sends an email to the person's email address to reset their password.

- As a Site User, I want to be able to receive an email confirmation after registering so that I can verify my account registration was successful.
    - On registering for an account, a verification email is sent to the user's registered email so they can verify their account and log in.

- As a Site User, I want to be able to easily enter my payment info so that I can check out quickly and with no hassles.
    - The checkout screen uses the Stripe payment system for safe and secure payment of purchases.

- As a Site User, I want to be able to have a personalised user profile so that I can view my order history and order confirmations and save my payment information.
    - On registration of a new account, a personal profile is automatically rendered. Here the user can view their order history and pet profiles.

##### **Details**
- As a Site User, I want to be able to view a list of products so that I can select some to purchase.
    - On the porducts page, a list of product cards are visible, showing the product name, rating, price, category and an image.

- As a Site User, I want to be able to easily see what I've searched for and the number of results so that I can quickly decide whether the product I want is available.
    - When a search query has been entered, the user is brought to a filtered products page. Here they can see the products which align with their search, as well as an indicator of how many items where found relating to the search query.

- As a Site User, I want to be able to view a specific category of products so that I can quickly find products I'm interested in without having to search through all products.
    - In the nav menu are links to each category class for ease of access. In addition, on the products page, there are category buttons that filter with the products currently visible.

- As a Site User, I want to be able to view individual product details so that I can identify the price, description, product rating, product image and sizes.
    - Each product in the products list has it's own info page which details the price, description, product rating, product image and sizes, including a sizing guide where sizes are available.

- As a Site User, I want to be able to easily view the total of my purchase at any time so that I can avoid spending too much.
    - The shopping bag icon in the header gives an up-to-date counter of the current shopping bag total. In addition, each item added to the shopping bag activates a pop-up which details your current bag summary, prices, total cost and shipping. It also advises the user how much more they need to spend to qualify for free shipping.

- As a Site User, I want to be able to view items in my bag to be purchased so that I can identify the total cost of my purchase and all items I will receive.
    - There is a shopping bag page which allows the user to view all products currently sleected, their sizes and quantities, and the total cost with and without shipping if applicable. Here the user can also update and delete items from the shopping bag if required.

- As a Site User, I want to be able to feel my personal and payment information is safe and secure so that I can confidently provide the needed information to make a purchase.
    - The link to the shopping bag page advises the checkout is secure, and the payment information input is set to ensure the user's information is correct and valid before purchasing.

- As a Site User, I want to be able to view an order confirmation after checkout so that I can verify that I haven't made any mistakes.
    - On submitting a purchase, the user is shown the order confirmation page which briefly details the order information, the shipping details, product information and the total cost. This information can also be viewed on the user profile in the order history section

#### Store Owner
- As a Store Owner, I want to be able to add a product so that I can add new items to my store.
    - There is a page accessible only by superusers where store owners add products to the store. The link for this page is in the user acconut dropdown in the header. This link takes the user to the add product page where they can fill the product details in the form. Each product added generates a new product id and individual product info page.

- As a Store Owner, I want to be able to edit/update a product so that I can change product prices, descriptions, images, and other product criteria.
    - On the individual products' pages, superusers can can see a link to update the product information. Clicking the link brings the store owner to a prepopulated form where adjustments can be made to the specific product.

- As a Store Owner, I want to be able to delete a product so that I can remove items that are no longer for sale.
    - On the individual products' pages, superusers can can see a link to delete the product information. Clicking the link immediately deletes the product page and information.


[Back to top](#)

## Manual Testing

### Common Elements Testing
Manual testing was conducted on the following elements that appear on every page:

<details>
<summary>Across Site - Manual Testing</summary>

- Test that Logo redirects to home screen.

    ![Test that Logo redirects to home screen](static/media/TESTING/manual_testing/logo-works.gif)

- Test that Nav Links work.

    ![Test that Nav Links work.](static/media/TESTING/manual_testing/nav-links-work.gif)

- Test that Query Links work.

    ![Test that Query Links work.](static/media/TESTING/manual_testing/query-links-work.gif)

- Test that Search Bar works.

    ![Test that Search Bar works.](static/media/TESTING/manual_testing/search-bar-works.gif)

- Test that Social Links work.

    ![Test that Social Links work.](static/media/TESTING/manual_testing/social-links-work.gif)

- Test that My Profile links show differently for users, super users and those not logged in.

    ![Test that My Profile links show differently for users, super users and those not logged in.](static/media/TESTING/manual_testing/profile-links-change-for-user-type.gif)

</details>


### Home Page
Manual testing was conducted on the following elements of the [Home Page](https://the-wagging-tailor.herokuapp.com/):
     
<details>
<summary>Home Page - Manual Testing</summary>

- Test that the three product buttons go to the correct pages.

    ![Test that the three product buttons go to the correct pages](static/media/TESTING/manual_testing/home-product-buttons-work.gif)

- Test that the carousel images slide when clicked.

    ![Test that the carousel images slide when clicked](static/media/TESTING/manual_testing/home-carousel.gif)

- Test that the Mail Chimp subscription form works.

    ![Test that the Mail Chimp subscription form works](static/media/TESTING/manual_testing/home-mail-chimp.gif)

</details>

### Products List
Manual testing was conducted on the following elements of the [Products List Page](https://the-wagging-tailor.herokuapp.com/products/):

<details>
<summary>Products List Page - Manual Testing</summary>

- Test that products can be sorted by price, category name and rating.

    ![Test that products can be sorted by price, category name and rating](static/media/TESTING/manual_testing/products-sort-by-selector.gif)

- Test that product category buttons work.

    ![Test that product category buttons work](static/media/TESTING/manual_testing/products-category-buttons.gif)
     
- Test that clicking on a product opens that products info page.

    ![Test that clicking on a product opens that products info page](static/media/TESTING/manual_testing/products-open-product-info.gif)

</details>

### Product Info Page
Manual testing was conducted on the following elements of the [Product Info Page](https://the-wagging-tailor.herokuapp.com/products/4/):

<details>
<summary>Product Info Page - Manual Testing</summary>

- Test that users can increase and decrease quantity of product.

    ![Test that users can increase and decrease quantity of product](static/media/TESTING/manual_testing/product-info-quantity.gif)
     
- Test that size selector and quide appear only for products with sizes.

    ![Test that size selector and guide appear only for products with sizes](static/media/TESTING/manual_testing/product-info-sizes-available.gif)
     
- Test that users can add a product to their shopping bag.

    ![Test that users can add a product to their shopping bag](static/media/TESTING/manual_testing/product-info-add-to-bag.gif)

- Test that the comments form is only available if logged in and the comments section displays comments submitted in the form.

    ![Test that the comments form is only available if logged in and the comments section displays comments submitted in the form](static/media/TESTING/manual_testing/product-info-comments.gif)

- Test that the Update and Delete Product buttons are only visible to super users.

    ![Test that the Update and Delete Product buttons are only visible to super users](static/media/TESTING/manual_testing/product-info-update-delete-product.gif)

- Test that a super user can add, edit and delete a product.

    ![Test that a super user can add, edit and delete a product](static/media/TESTING/manual_testing/product-info-add-product.gif)

</details>

### Shopping Bag Page
Manual testing was conducted on the following elements of the [Product Info Page](https://the-wagging-tailor.herokuapp.com/shopping_bag/):

<details>
<summary>Shopping Bag Page - Manual Testing</summary>

- Test that users can update quantity of product.

    ![Test that users can update quantity of product](static/media/TESTING)

- Test that users can remove product from shopping bag.

    ![Test that users can remove product from shopping bag](static/media/TESTING)

- Test that users can view the same products of different sizes.

    ![Test that users can view the same products of different sizes](static/media/TESTING)

- Test that total cost, shipping cost and grand total update when updating products in bag.

    ![Test that total cost, shipping cost and grand total update when updating products in bag](static/media/TESTING)

- Test that users can access the checkout page.

    ![Test that users can access the checkout page](static/media/TESTING)

</details>
     
### Sign in/Sign Out/Sign Up Pages
Manual testing was conducted on the following elements of the [Sign In Page](https://the-wagging-tailor.herokuapp.com/accounts/login/), [Verify Email Page](https://the-wagging-tailor.herokuapp.com/accounts/confirm-email/), [Sign Out Page](https://the-wagging-tailor.herokuapp.com/accounts/logout/) and [Sign Up Page](https://the-wagging-tailor.herokuapp.com/accounts/signup/):

<details>
<summary>User Account Pages - Manual Testing</summary>

- Test that users can register, verify their email, log in and logout.

    ![Test that users can register, verify their email, log in and logout](static/media/TESTING/manual_testing/account-signup-verify-signin-signout.gif)

</details>

### Pages are Responsive
- Manual testing was conducted on the following pages for responsiveness on large, medium and small screens

<details>
<summary>Home Page - Manual Testing</summary>

![Responsive Home](static/media/TESTING)

![Responsive About](static/media/TESTING)

![Responsive Recipe](static/media/TESTING)

![Responsive Form](static/media/TESTING)

![Responsive Sign In, Sign Out and Sign Up](static/media/TESTING)

</details>

[Back to top](#)

## Automated Testing

### Code Validation
The [W3C Markup Validator](https://validator.w3.org/ "Link to M£C Markup Validator Site") service was used to validate the `HTML` and `CSS` code used. The [PEP8 Python Validator](http://pep8online.com/ "Link to the PEP8 Python Validator Site") was used to validate the `Python`code used. The [JSHint JavaScript Validator](https://jshint.com/ "Link to the JSHint JavaScript Validator Site") was used to validate the `JavaScript` code used.

#### **Results:**

##### **HTML Pages**
<details>
<summary>HTML Pages - HTML Validation</summary>

![Home Page HTML Validation Results](static/media/TESTING/validation/valid-html-home.png)

![Products Page HTML Validation Results](static/media/TESTING/validation/valid-html-products.png)

![Product Info Page HTML Validation Results](static/media/TESTING/validation/valid-html-product-info.png)

![Add Product Page HTML Validation Results](static/media/TESTING/validation/valid-html-add-a-product.png)

![Edit Product Page HTML Validation Results](static/media/TESTING/validation/valid-html-edit-a-product.png)

![Shopping Bag Page HTML Validation Results](static/media/TESTING/validation/valid-html-shopping-bag.png)

![Checkout Page HTML Validation Results](static/media/TESTING/validation/valid-html-checkout.png)

![Order Confirmation Page HTML Validation Results](static/media/TESTING/validation/valid-html-checkout-successful.png)

![Order History Page HTML Validation Results](static/media/TESTING/validation/valid-html-my-order-history.png)

![Profile Page HTML Validation Results](static/media/TESTING/validation/valid-html-profile.png)

![Add Pet Page HTML Validation Results](static/media/TESTING/validation/valid-html-add-a-pet.png)

![Edit Pet Page HTML Validation Results](static/media/TESTING/validation/valid-html-edit-a-pet.png)

![Queries Page HTML Validation Results](static/media/TESTING/validation/valid-html-queries.png)

</details>

##### **CSS stylesheets**
<details>
<summary>CSS Stylesheets - CSS Validation</summary>

![Style sheet validation results - base.css](static/media/TESTING/validation/w3c-valid-base-css.png)

![Style sheet validation results - checkout.css](static/media/TESTING/validation/w3c-valid-checkout-css.png)

![Style sheet validation results - my_profile.css](static/media/TESTING/validation/w3c-valid-profile-css.png)

</details>

##### **JavaScript Files**
<details>
<summary>JavaScript Files - JS Validation</summary>

![JS validation results - base.html - postloadjs](static/media/TESTING/validation/jshint-valid-base-postloadjs.png)

![JS validation results - checkout_stripe_elements.js](static/media/TESTING/validation/jshint-valid-checkout-stripe-elements.png)

![JS validation results - index - postloadjs](static/media/TESTING/validation/jshint-valid-index-postloadjs.png)

![JS validation results - product_quantity_input_script](static/media/TESTING/validation/jshint-valid-product-quantity-input-script.png)

![JS validation results - products - postloadjs](static/media/TESTING/validation/jshint-valid-products-postloadjs.png)

![JS validation results - shooping_bag - postloadjs](static/media/TESTING/validation/jshint-valid-shopping-bag-postloadjs.png)

</details>

##### **Python Files**
- Checkout
    <details>
    <summary>Checkout Files - Python Validation</summary>

    ![Python Validation - student_rations - urls.py](static/media/TESTING/validation/pep8-valid-checkout-admin.png)

    ![Python Validation - settings.py](static/media/TESTING/validation/pep8-valid-checkout-apps.png)

    ![Python Validation - admin.py](static/media/TESTING/validation/pep8-valid-checkout-forms.png)

    ![Python Validation - forms.py](static/media/TESTING/validation/pep8-valid-checkout-models.png)

    ![Python Validation - models.py](static/media/TESTING/validation/pep8-valid-checkout-signals.png)

    ![Python Validation - recipes - urls.py](static/media/TESTING/validation/pep8-valid-checkout-urls.png)

    ![Python Validation - views.py](static/media/TESTING/validation/pep8-valid-checkout-views.png)

    </details>


- Home
    <details>
    <summary>Home Files - Python Validation</summary>

    ![Python Validation - student_rations - urls.py](static/media/TESTING/validation/pep8-valid-home-urls.png)

    ![Python Validation - settings.py](static/media/TESTING/validation/pep8-valid-home-views.png)

    </details>


- Products
    <details>
    <summary>Product Files - Python Validation</summary>

    ![Python Validation - student_rations - urls.py](static/media/TESTING/validation/pep8-valid-product-admin.png)

    ![Python Validation - settings.py](static/media/TESTING/validation/pep8-valid-product-forms.png)

    ![Python Validation - admin.py](static/media/TESTING/validation/pep8-valid-product-models.png)

    ![Python Validation - forms.py](static/media/TESTING/validation/pep8-valid-product-urls.png)

    ![Python Validation - models.py](static/media/TESTING/validation/pep8-valid-product-views.png)

    </details>


- Profile
    <details>
    <summary>Profile Files - Python Validation</summary>

    ![Python Validation - student_rations - urls.py](static/media/TESTING/validation/pep8-valid-profile-admin.png)

    ![Python Validation - settings.py](static/media/TESTING/validation/pep8-valid-profile-forms.png)

    ![Python Validation - admin.py](static/media/TESTING/validation/pep8-valid-profile-models.png)

    ![Python Validation - forms.py](static/media/TESTING/validation/pep8-valid-profile-urls.png)

    ![Python Validation - models.py](static/media/TESTING/validation/pep8-valid-profile-views.png)

    </details>


- Queries
    <details>
    <summary>Queries Files - Python Validation</summary>

    ![Python Validation - student_rations - urls.py](static/media/TESTING/validation/pep8-valid-queries-admin.png)

    ![Python Validation - settings.py](static/media/TESTING/validation/pep8-valid-queries-forms.png)

    ![Python Validation - admin.py](static/media/TESTING/validation/pep8-valid-queries-models.png)

    ![Python Validation - forms.py](static/media/TESTING/validation/pep8-valid-queries-urls.png)

    ![Python Validation - models.py](static/media/TESTING/validation/pep8-valid-queries-views.png)

    </details>


- Shopping Bag
    <details>
    <summary>Shopping Bag Files - Python Validation</summary>

    ![Python Validation - student_rations - urls.py](static/media/TESTING/validation/pep8-valid-shopping-bag-contexts.png)

    ![Python Validation - settings.py](static/media/TESTING/validation/pep8-valid-shopping-bag-urls.png)

    ![Python Validation - admin.py](static/media/TESTING/validation/pep8-valid-shopping-bag-views.png)

    </details>


- The Wagging Tailor

    <details>
    <summary>The Wagging Tailor Files - Python Validation</summary>

    ![Python Validation - student_rations - urls.py](static/media/TESTING/validation/pep8-valid-wagging-tailor-settings.png)

    ![Python Validation - settings.py](static/media/TESTING/validation/pep8-valid-wagging-tailor-urls.png)

    ![Python Validation - admin.py](static/media/TESTING/validation/pep8-valid-wagging-tailor-views.png)

    ![Python Validation - forms.py](static/media/TESTING/validation/pep8-valid-wagging-tailor-wsgi.png)

    </details>

## User testing 
My husband and the lovely people of Slack were asked to review the site and documentation to point out any bugs and/or user experience issues. Their helpful advice throughout the process led to a few small UX changes in order to create a better experience. 

[Back to top ⇧](#)

***
