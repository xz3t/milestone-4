#  APINI MD

[View the live project here.](https://apinimd.herokuapp.com/)

The project objective is to create a full stack site around an business with e-commerce feature using Python with Django Framwork/PostgreSQL/AWS/Stripe payment methond and deploy the project to Heroku.

![Preview](/docs/responsive.jpg)

## User Experience (UX)

### Project Goals

Project goal is to create an online presence with online shop functionality for a small family business producing natural honey and derivated products, as well as made from-zero handmade soaps, shampoos, and cosmetics. 
The couple makes part of a small ecovillage project, created in the center of the Republic of Moldova 15 years ago inspired by permacultural and sustainable living principles.


#### As a Shopper, I want to:

	* have access to the shop in one click
	* view a list of all products and have quick access to purchase them
	* view individual product details with description and stock information
	* have a view on my purchase list at any time not to overspend
	* sort products by Name/Categories/Price
	* search for a product by name or description
	* easily selected quantity and amount of selected product when purchasing it
	* view all the items in my shopping bag with name/qty/grand total
	* easily make changes and adjustments before my purchase/order
	* easily enter payment information to check out with no unwanted delays
	* feel my information is secured and be confident to provide required data to make an order/purchase
	* view confirmation after checkout and receive an email with a confirmation of the order

####  As a User, I want to :

    * have content in my native preffered language 
    (R.Moldova have 2 main spoken languages, Romanian and Russian)
    * have a clean interface with a familiar layout
    * create a personal account and be able to view and change my profile detail
    * access and change my personal account information
    * recover a forgotten password to my account
    * have meaningful messages and confirmation of my interaction with the site 
    as confirmation emails and messages
    * add/edit/delete a review to products


####  As an Admin/Store Owner, I want to :
    * receive a copy of order to email
	* have easy access to manage products
	* add new products
	* edit and update product description /images and availability
	* remove products that are no longer needed 
    * add/edit and update events and news section
    * add/edit and update About section with new articles and links
    * create and change promotional coupons

-   ### Design
    -   #### Color Scheme
        -   Simple is better, black/white/grey colors are used.
    -   #### Typography
        -   Roboto Slab is used throughout the site with fall back to Serif.
    -   #### Imagery
        -   All images are provided by recipient of the site.

*   ### Wireframes
    -   Wireframes - [View](/docs/wireframes.html)

## Features

### Main page
- 

## Technologies Used

    - [HTML5](https://en.wikipedia.org/wiki/HTML5)
    - [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
    - [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
    - [Python](https://en.wikipedia.org/wiki/Python_(programming_language))

### Frameworks, Libraries & Programs Used

1. [Git](https://git-scm.com/)
    - Git was used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub.
2. [GitHub:](https://github.com/)
    - GitHub is used to store the projects code after being pushed from Git.
3. [Font Awesome:](https://fontawesome.com/)
    - Font Awesome was used on all pages throughout the website to add icons for aesthetic and UX purposes.
4. [Bootstrap](https://getbootstrap.com/)
    - Bootstrap is a free and open-source CSS framework directed at responsive, mobile-first front-end web development.
5. [JQuery](https://en.wikipedia.org/wiki/JQuery)
    - JavaScript library designed to simplify HTML DOM tree traversal and manipulation, event handling, css animation.
6. [Heroku](https://en.wikipedia.org/wiki/Heroku)
    - Heroku is a cloud platform as a service (PaaS) supporting several programming languages, including Python used in this project.
7. [PostgreSQL](https://www.postgresql.org/)
    - PostgreSQL, also known as Postgres, is a free and open-source relational database management system.
8. [Django](https://www.djangoproject.com/)
    - The web framework for perfectionists with deadlines.
9. [Stripe API](https://stripe.com/)
    - Payment processing system.
10. [AWS S3](https://aws.amazon.com/s3/)
    - Amazon Simple Storage Service (Amazon S3) is an object storage service used to store static and media files for this project.

## Testing

[Testing](https://github.com/xz3t/milestone-4/blob/master/TESTING.md)


### Known Bugs

- Back to top link from products page doesnt work on some mobiles, might have a clash with hide delivery header script.
- after testing identified following issue that is not addressed: 
when amending order in django admin panel discount will not recalculate, solution to save discount as a % value and use it in calculations.

### Features to implement

- Implement Twillio API for SMS confirmation of orders

## Deployment

### Local Deployment

Requirements: 
1. Installed Python on your environment 
2. An AWS account with S3 bucket setup
3. As Stripe account

Environment variables:

    * SECRET_KEY = secret key for django app
    * DEVELOPMENT = "True" variable to set Debug to True, also will use console.EmailBackend
    * EMAIL_HOST_USER = User for live emails
    * EMAIL_HOST_PASS = Password for live emails
    * DATABASE_URL = with youre link to databse if not setup local sqlite3 will be used
    * STRIPE_PUBLIC_KEY = Public key from Stripe
    * STRIPE_SECRET_KEY = Secret key from Stripe
    * STRIPE_WH_SECRET  = Webhook secret key from Stripe
    * USE_AWS  = True to use static and media files from S3 account
    * AWS_ACCESS_KEY_ID = AWS Access Key Id
    * AWS_SECRET_ACCESS_KEY = AWS Secret Access Key

1. Open Console navigate to directory project will be created.
2. Get a local copy : "git clone https://github.com/xz3t/milestone-4.git"
3. Install the requirements: "pip3 install -r requirements.txt"
4. Create a superuser: python3 manage.py create superuser
5. Set up database: "python3 manage.py makemigrations" , "python3 manage.py migrate"
6. For a copy of products: "python3 manage.py loaddata products"
7. For a copy of events: "python3 manage.py loaddata events"
8. For a copy of about: "python3 manage.py loaddata about"
9. If using AWS set up all variables and copy media/ folder to your S3 bucket
10. Run localy: python3 manage.py runserver


### Heroku with Github integration

1. Create a Procfile with the terminal command echo web: python app.py > Procfile.
2. Create a requirements.txt: pip3 freeze --local > requirements.txt.
3. Push and commit requirements.txt and Procfile
3. On Heroku app page, go to Resources tab in Add-on section search and add Heroku Postgres Set up
4. On the Heroku app page, click on the Deploy, find Deployment method and select GitHub
5. In search for repository to connect to select desired repo-name and link it to Heroku.
6. On the Heroku app page, click on Settings -> Reveal Config Vars
7. Set the Config Vars in the Settings: 
    * SECRET_KEY = secret key for django app
    * EMAIL_HOST_USER = User for live emails
    * EMAIL_HOST_PASS = Password for live emails
    * DATABASE_URL = with youre link to Heroku Postgres databse
    * STRIPE_PUBLIC_KEY = Public key from Stripe
    * STRIPE_SECRET_KEY = Secret key from Stripe
    * STRIPE_WH_SECRET  = Webhook secret key from Stripe
    * USE_AWS  = True to use static and media files from S3 account
    * AWS_ACCESS_KEY_ID = AWS Access Key Id
    * AWS_SECRET_ACCESS_KEY = AWS Secret Access Key
8. Navigate back Deploy section, click on the Deploy Branch, you can enable Automatic Deploy, in automatic mode every push to GitHub wil automatically the latest version.
9. Now app is deployed on Heroku, you can open and view it by clicking on the Open app on top of the page.


    
### Media

-   All pictures are provided by recipent of the project and have copyright on them.


### Acknowledgements

-   My Mentor for continuous constructive feedback.


### Links

- review : [Link](https://www.youtube.com/watch?v=IVyc06bASSg&list=PLeyK9Dw9ShReHUdt5Nh2qlgF6keN6DI7z&index=31&ab_channel=Onthir)
- coupons : [Link](https://www.youtube.com/watch?v=_dSCGMJcoe4&ab_channel=PacktVideo)
- hide delivery/language selection header :[Link](https://stackoverflow.com/questions/17908542/how-to-hide-div-when-scrolling-down-and-then-show-it-as-you-scroll-up)
- close div on click outside : [Link](https://stackoverflow.com/questions/17965839/close-a-div-by-clicking-outside)