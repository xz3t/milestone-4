## Testing 

Automated testing forms and views for Contact Page https://xz3t.github.io/milestone-4/htmlcov/index.html

All links and functionality manually tested by myself/friends and work colleagues.

## Code testing

* HTML5 - https://validator.w3.org/
 [Index](https://validator.w3.org/nu/?doc=https%3A%2F%2Fapinimd.herokuapp.com%2F)
 [Products](https://validator.w3.org/nu/?doc=https%3A%2F%2Fapinimd.herokuapp.com%2Fproducts%2F)
 [Bag](https://validator.w3.org/nu/?doc=https%3A%2F%2Fapinimd.herokuapp.com%2Fbag%2F)
 [Checkout](https://validator.w3.org/nu/?doc=https%3A%2F%2Fapinimd.herokuapp.com%2Fcheckout%2F)

* CSS3 -  https://jigsaw.w3.org/css-validator/ 
 [checkout.css](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fxz3t.github.io%2Fmilestone-4%2Fcheckout%2Fstatic%2Fcheckout%2Fcss%2Fcheckout.css&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en)
 [profile.css](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fxz3t.github.io%2Fmilestone-4%2Fprofiles%2Fstatic%2Fprofiles%2Fcss%2Fprofile.css&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en)
 [base.css](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fxz3t.github.io%2Fmilestone-4%2Fstatic%2Fcss%2Fbase.css&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en)

* JS - all scripts validated with:  https://jshint.com/

* Python - http://pep8online.com/

## User stories testing

As a Shopper, I want to:

> As a Shopper, I want to have access to the shop in one click.

* "Shop now" button is located on main page and give 1 click access to list of all products in the store.

> As a Shopper, I want to view a list of all products and have quick access to purchase them.

* Shoppers have access to all product and sub categories through navigation bar located on top of the page.

> As a Shopper, I want to view individual product details with description and stock information.

* Shopper are able to click on product cards to access details for each product, description, stock information
as well as back to stock info. 

> As a Shopper, I want to have a view on my purchase list at any time not to overspend.

* Navigation bar always display a total of added items to shopping bag,
shopper can click and get to shopping bag page with full information about added items.

> As a Shopper, I want to sort products by Name/Categories/Price.

* Products page contains a dropdown menu that facilitate sorting the products Price/Name and Category.

> As a Shopper, I want to search for a product by name or description.

* Products page contains a search bar where user can search in name and description,
in 3 languages supported by the app.

> As a Shopper, I want to easily selected quantity and amount of selected product when purchasing it.

* Details page for each product is presented with a quantity selector and "Add to bag" button 
that makes easy for the shopper to add desired quantity to the bag.

> As a Shopper, I want to view all the items in my shopping bag with name/qty/total.

* Shopping bag contains name, quantity and subtotal as well as a picture of product
and breakdown of the grand total including delivery and discount information.

> As a Shopper, I want to easily make changes and adjustments before my purchase/order.

* Shopping bag facilitate removing or updating quantity for each item before continuing to checkout.

> As a Shopper, I want to easily enter payment information to check out with no unwanted delays.
> As a Shopper, I want to fill my information is secured and be confident to provide required data to make an order/purchase.

* On checkout page shopper is presented with a form with minimum of required information with name/phone number and address for delivery.
With option to save delivery and checkout information on first order when user is logged in or will create an account. 

> As a Shopper,  I want to view confirmation after checkout and receive an email with a confirmation of the order.

* After successfully checkout shopper will receive a confirmation message and will be redirected to confirmation page
with a summary of the order and an email will be sent to provided email address

> As a User, I want to have content in my native preferred language 
(R.Moldova have 2 main spoken languages, Romanian and Russian)

* On access user will be redirected to default language set-up by his/hers browser, 
User can change language in the menu on the top right corner of the page.
If default language is different then available Romanian, Russian or English, English version will be loaded. 

> As a User, I want to have a clean interface with a familiar layout.

* Users are presented with a clean black/white and grey page with a familiar page layout, navigation menu on top, main body and footer.

> As a User, I want to create a personal account and be able to view and change my profile detail.
> As a User, I want to access and change my personal account information.
> As a User, I want to recover a forgotten password to my account.

* With implemented Django allauth application that is addressing authentication, registration, account management,
Users can create personal a account and view and edit profile details as well as reset password.

> As a User, I want to have meaningful messages and confirmation of my interaction with the site 
as confirmation emails and messages

* All user actions are followed by a success or error messages that are displayed on the right of the page with Bootsrap Toast,
Confirmation email is sent on registration and each order.

> As a User, I want to add/edit/delete a review to products.

* On details page for each product users can leave comment as well as edit and delete comments created by them.

> As an Admin/Store Owner, I want to receive a copy of order to email.

* Owner is set up to receive a copy of all orders

> As an Admin/Store Owner, I want to have easy access to manage products.

* All superusers have a quick to edit or remove product from the list of the product and individual details page.

> As an Admin/Store Owner, I want to add new products.

* All superusers have a quick access to add a product in navigation bar under My Account-> Product Management. 

> As an Admin/Store Owner, I want to edit and update product description /images and availability.

* Edit page contains all required fields to fully update product information/description/picture/price/avalability  

> As an Admin/Store Owner, I want to remove products that are no longer needed.

* Superusers have quick access to remove an item from product page and details page of the product.

> As an Admin/Store Owner, I want to add/edit and update events and news section.
> As an Admin/Store Owner, I want to add /edit and update About section with new articles and links.

* Admin and store owner have access to events and about section control through Django Admin panel

> As an Admin/Store Owner, I want to create and change promotional coupons

* Django Admin facilitate adding and editing discount coupons and their availability.


## Browser Testing and responsive design

- Windows 10: Firefox/Edge/Chrome/Opera
- Pop!_OS: Firefox/Chrome

Devices:

- Iphone 5s (Safari)
- Iphone 6s (Safari)
- Pixel 3a (Chrome)
- Nokia 5 (Chrome)
- Pixel 3XL (Chrome)

Responsive design adjusted to fit screens down to 320px.
All identified issues in English version were fixed.


## Bugs (fixed)

In final user testing stage next bugs identified:

> Mobile view in other 2 languages can suffer because of longer words in translation.
- addressed a few reported bugs and renamed for a shorter button name as scaling down with result in extra small buttons.
In further development before deploying page to use might change buttons position for full name on the buttons.

> Discount does not appear on success page and in confirmation email.
- identified issue: discount was not saved in order
- solution:
 1. created discount field in orders models,
 2. modified update total function to extract discount,
 3. added discount field to admin OrderAdmin,
 4. in bag context added a session key with discount calculated from the bag
 5. save discount from session_discount to order.discount

> Order email confirmation sent from example.com
- Missed out to add an Domain Name and Display name in Django Admin -> Home › Sites › Sites

