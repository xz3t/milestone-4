#  Name of the app

[View the live project here.](https://xm/)

into 

![Preview](/docs/responsive.jpg)

## User Experience (UX)

### Project Goals

Project goal is to create an online presence with online shop functionality for a small family business producing natural honey and derivated products, as well as made from-zero handmade soaps, shampoos, and cosmetics. 
The couple makes part of a small ecovillage project, created in the center of the Republic of Moldova 15 years ago inspired by permacultural and sustainable living principles.


#### As a Shopper, I want to:

	* have access to the shop in one click
	* view a list of all products and have quick access to purchase them
	* view individual product details with description, available sizes, and stock information
	* have a view on my purchase list at any time not to overspend
	* sort products by available/out of stock
	* search for a product by name or description
	* easily selected quantity and amount of selected product when purchasing it
	* view all the items in my shopping bag with description/qty/size/grand total
	* easily make changes and adjustments before my purchase/order
	* easily enter payment information to check out with no unwanted delays
	* feel my information is secured and be confident to provide required data to make an order/purchase
	* view confirmation after checkout and receive an email with a confirmation of the order.

####  As a User, I want to :

    * have content in my native preffered language 
    (R.Moldova have 2 main spoken languages, Romanian and Russian)
    * have a clean interface with a familiar layout
    * Create a personal account and be able to view and change my profile detail
    * access and change my personal account information
    * recover a forgotten password to my account
    * have meaningful messages and confirmation of my interaction with the site 
    as confirmation emails and messages


####  As an Admin/Store Owner, I want to :
    * receive a copy of order to email
	* have easy access to manage products
	* add new products
	* edit and update product description /images and availability
	* remove products that are no longer needed 
    * add/edit and update events
    * add edit and update About section with new articles and links

-   ### Design
    -   #### Color Scheme
        -   
    -   #### Typography
        -   
    -   #### Imagery
        -  

*   ### Wireframes

    -   Wireframes - [View](/docs/wireframes.html)

## Features

### Main page
- 

## Technologies Used

-   [HTML5](https://en.wikipedia.org/wiki/HTML5)
-   [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
-   [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
-   [Python](https://en.wikipedia.org/wiki/Python_(programming_language))


### Frameworks, Libraries & Programs Used

1. [Git](https://git-scm.com/)
    - Git was used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub.
2. [GitHub:](https://github.com/)
    - GitHub is used to store the projects code after being pushed from Git.

5. [Font Awesome:](https://fontawesome.com/)
    - Font Awesome was used on all pages throughout the website to add icons for aesthetic and UX purposes.
6. [JQuery](https://en.wikipedia.org/wiki/JQuery)
    - JavaScript library designed to simplify HTML DOM tree traversal and manipulation, event handling, css animation.

9. [Heroku](https://en.wikipedia.org/wiki/Heroku)
    - Heroku is a cloud platform as a service (PaaS) supporting several programming languages, including Python used in this project.


## Testing

-

### Features Testing

#### Main page
- 


### Further Testing

-   


### Known Bugs


- 

### Features to implement

- 

## Deployment

### Heroku with Github integration

1. Create a Procfile with the terminal command echo web: python app.py > Procfile.
2. Create a requirements.txt: pip3 freeze --local > requirements.txt.
3. Push and commit requirements.txt and Procfile
4. On the Heroku app page, click on the Deploy, find Deployment method and select GitHub
5. In search for repository to connect to select desired repo-name and link it to Heroku.
6. On the Heroku app page, click on Settings -> Reveal Config Vars
7. Set the Config Vars in the Settings: 
    - Debug: False; 
    - IP: 0.0.0.0; 
    - PORT: 5000;
    - MONGO_URI: mongodb+srv://username:password@myfirstcluster.kmobf.mongodb.net/weeklyShopping?retryWrites=true&w=majority;
    - SECRET_KEY: <your_secret_key>.
8. Navigate back Deploy section, click on the Deploy Branch, you can enable Automatic Deploy, in automatic mode every push to GitHub wil automatically the latest version.
9. Now app is deployed on Heroku, you can open and view it by clicking on the Open app on top of the page.


    
### Media

-   


### Acknowledgements

-   My Mentor for continuous constructive feedback.


### Links

- review : https://www.youtube.com/watch?v=IVyc06bASSg&list=PLeyK9Dw9ShReHUdt5Nh2qlgF6keN6DI7z&index=31&ab_channel=Onthir
- event-timeline : https://bootsnipp.com/snippets/xrKXW