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
     - [Browser Validation](#Browser-Validation)
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
    - .

- As a Site User, I want to be able to feel my personal and payment information is safe and secure so that I can confidently provide the needed information to make a purchase.
    - .

- As a Site User, I want to be able to view an order confirmation after checkout so that I can verify that I haven't made any mistakes.
    - .

#### Store Owner
- As a Store Owner, I want to be able to add a product so that I can add new items to my store.
    - .

- As a Store Owner, I want to be able to edit/update a product so that I can change product prices, descriptions, images, and other product criteria.
    - .

- As a Store Owner, I want to be able to delete a product so that I can remove items that are no longer for sale.
    - .


[Back to top](#Student-Rations---Testing)

## Manual Testing

### Common Elements Testing
Manual testing was conducted on the following elements that appear on every page:

- Test that Logo redirects to home screen.

    ![Test that Logo redirects to home screen](static/media/TESTING/logo-redirects.gif)

- Test that Nav Links work.

    ![Test that Nav Links work.](static/media/TESTING/nav-links-work.gif)

- Test that Footer Links work.

    ![Test that Footer Links work.](static/media/TESTING/footer-links-work.gif)

- Test that Social Links work.

    ![Test that Social Links work.](static/media/TESTING/social-links-work.gif)


### Home Page
Manual testing was conducted on the following elements of the [Home Page](https://student-rations.herokuapp.com/):
     
- Test that user welcome message displays username.

    ![Test that user welcome message displays username](static/media/TESTING/welcome-message-username.gif)

- Test that recipe cards redirect user to recipe pages.

    ![Test that recipe cards redirect user to recipe pages](static/media/TESTING/cards-redirect-to-recipe.gif)

### Recipe Page/Edit Recipe Page
Manual testing was conducted on the following elements of the [Recipe Page](https://student-rations.herokuapp.com/best-ever-chocolate-brownies-recipe/) and [Edit Recipe Page](https://student-rations.herokuapp.com/edit-a-recipe/best-ever-chocolate-brownies-recipe):

- Test that recipes can be edited by author only.

    ![Test that recipes can be edited by author only](static/media/TESTING/can-edit-recipe.gif)

- Test that recipes can only be deleted by author.

    ![Test that recipes can only be deleted by author](static/media/TESTING/can-delete-recipe.gif)
     
- Test that recipes can be liked and unliked when logged in.

    ![Test that recipes can be liked and unliked when logged in](static/media/TESTING/like-unlike-recipe.gif)
     
- Test that comments can be submitted and approved.

    ![Test that comments can be submitted and approved](static/media/TESTING/comment-on-recipe.gif)

### Share Recipe Page
Manual testing was conducted on the following elements of the [Share recipe Page](https://student-rations.herokuapp.com/share-a-recipe/):

- Test that recipes create unique slugs

    ![Test that recipes create unique slugs](static/media/TESTING/unique-slug-url.gif)
     
- Test that recipes are saved.

    ![Test that recipes are saved](static/media/TESTING/recipe-saves.gif)
     
### Sign in/Sign Out/Sign Up Pages
Manual testing was conducted on the following elements of the [Sign In Page](Link), [Sign Out Page](Link) and [Sign Up Page](Link):

- Users can register, log in and logout.

    ![Users can register, log in and logout](static/media/TESTING/signup-signout-signin.gif)

### Pages are Responsive
- Manual testing was conducted on the following pages for responsiveness on large, medium and small screens

    ![Responsive Home](static/media/TESTING/responsive-home.gif)

    ![Responsive About](static/media/TESTING/responsive-about.gif)

    ![Responsive Recipe](static/media/TESTING/responsive-recipe.gif)

    ![Responsive Form](static/media/TESTING/responsive-form.gif)

    ![Responsive Sign In, Sign Out and Sign Up](static/media/TESTING/responsive-signin-signout-signup.gif)

[Back to top](#Student-Rations---Testing)

## Automated Testing

### Code Validation
The [W3C Markup Validator](https://validator.w3.org/ "Link to M£C Markup Validator Site") service was used to validate the `HTML` and `CSS` code used. The [PEP8 Python Validator](http://pep8online.com/ "Link to the PEP8 Python Validator Site") was used to validate the `Python`code used.

**Results:**

- HTML Pages
<details>
<summary>HTML Pages - Code Validation</summary>

![Home Page HTML Validation Results](static/media/TESTING/html-valitadtion-home.png)

![About Page HTML Validation Results](static/media/TESTING/html-validation-about.png)

![Recipe Page HTML Validation Results](static/media/TESTING/html-validation-recipe.png)

![Share Recipe Page HTML Validation Results](static/media/TESTING/validate-html-recipe-form.gif)

![Edit Recipe Page HTML Validation Results](static/media/TESTING/validate-html-edit-recipe-form.gif)

![Sign In Page HTML Validation Results](static/media/TESTING/html-validation-sign-in.png)

![Sign Up Page HTML Validation Results](static/media/TESTING/html-validation-sign-up.png)

![Sign Out Page HTML Validation Results](static/media/TESTING/html-validation-sign-out.png)

</details>

- CSS stylesheet
<details>
<summary>CSS Stylesheet - Code Validation</summary>

![Style sheet validation results](static/media/TESTING/css-validation.png)

</details>

- Python Files
<details>
<summary>Python Files - Code Validation</summary>

![Python Validation - student_rations - urls.py](static/media/TESTING/python-validation-urls-sr.png)

![Python Validation - settings.py](static/media/TESTING/python-validation-settings.png)

![Python Validation - admin.py](static/media/TESTING/python-validation-admin.png)

![Python Validation - forms.py](static/media/TESTING/python-validation-forms.png)

![Python Validation - models.py](static/media/TESTING/python-validation-models.png)

![Python Validation - recipes - urls.py](static/media/TESTING/python-validation-urls-recipes.png)

![Python Validation - views.py](static/media/TESTING/python-validation-views.png)

</details>

### Browser Validation
- **Chrome** - ![Validate Chrome](static/media/TESTING/validate-browser-chrome.png)
- **Edge** - ![Validate Edge](static/media/TESTING/validate-browser-edge.png)
- **Opera** - ![Validate Opera](static/media/TESTING/validate-browser-opera.png)
- **Firefox** - ![Validate Firefox](static/media/TESTING/validate-browser-firefox.png)

## User testing 
My husband and the lovely people of Slack were asked to review the site and documentation to point out any bugs and/or user experience issues. Their helpful advice throughout the process led to a few small UX changes in order to create a better experience. 

[Back to top ⇧](#Student-Rations---Testing)

***
