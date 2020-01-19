[![Build Status](https://travis-ci.org/LivHed/handcrafted-heart.svg?branch=master)](https://travis-ci.org/LivHed/handcrafted-heart)
# Handcrafted heart 
This is my Milestone Project 4: Full Stack Frameworks with Django - Code Institute.

The idea of this web page is that.. My aim is that..

This page is made for an imaginary person from Sweden, Sarah, a small business owner who makes knitted handcrafted products and sell them. The purpose of the products are for warming during winter time up north.

[Check it out here!]()

![Handcrafted heart img](the link to the am i responsive webpage imageg "The handcrafted heart image")

## UX

### Design process
After doing research looking at websites with knitted products I found that there where no pages dedicated only to.. which is a gap I wanted to fill. I wanted to narrow this search down to..  My goals with the design was set to:

* To make the design suitable for people who wants to find knitted products in an easy way. I wanted to do this with a stylistic and easily understandable design with warm colors and buttons with clear directions.
* To make a web application with several pages, each with it´s clear purpose, and this with a user friendly and easy layout for the user to quick be able to understand what you can do and how.
* The fonts that I chose to use for this website provides an artistic feeling, but are at the same time easy to read, which I think suits the purpose of the page, and it´s audience.
* I chose to use..
* 
* I chose the name of the page to be Handcrafted heart, which are supposed to give the customers a personal and warm experience when visiting the page, also some of the products descriptions are a bit more warm and personal to enrich this experience.

This handles the CRUD functionality (Create, Read, Update and Delete) and I planned for this web page to give a sense of.. 

### Wireframes
The wireframes are created with Balsamiq. They where made as a part of the design process and are saved as a pdf document and kept in the separate folder; wireframes. All of the pages are showed as I planned them and one example of mobile view can be found on the last page in the document. [Check them out here!](add link to the wireframes)

### User stories
* As a person living up north, for example in Sweden, I would like to find knitted products to keep me warm during the winter season. 
* As a person interested in knitting I would like to have a look at someone elses creations, and buy something from this person to get inspiration of my own.
* As a creative, mindful, environmental friendly person living up north I would rather buy handmade knitted products to support small local business owners instead of buying products from big companies. 
*

## Features
#### Existing Features
* The navbar contains the name of the web application and the pages you can click on to visit. The pages are named clearly.
* When a user is logged in the Profile and Logout link is showing in the navbar, but if a user is Logged out the Login and Register links are showing instead. All of the other links are showing all the time.
* The search box to search for specific products by keayword is placed underneath the heading. Underneath the search box there is a button to view all the products, this is placed here to direct the user as a natural step to see all of the products at once again after the search for a specific product, if wished.
* The products and the details about them are shown in with cards, in a responsive way. The user can click on the quantity field to choose between the amount from 1 to 5, and are then able to add it to the cart with the Add button.
* The fields in the forms are required so the user won´t be able to submit the forms until all of the fields are filled in.
* The name of the webpage is placed in the top left corner of the navbar as good common pratcice, and are clickable and leads to the landing page. The navbar collapse to a burger icon on smaller devices and are placed in the top right corner.
* The page has authentication functionality in the sign in and the registration forms.
* The requirement to log in is activated and the user are redirected to the Login page when the user clicks on the Checkout button in the Cart page. A user can buy products only when he/she are logged in.
* The user is also required to Login in and are redirected to the Login page when he/she clicks on the button Add Inspiration on the Inspire page.
* On the Cart page the user can view the order, and also use the Amend button to change the quantity of the order. If the cart is empty the user can click on a button to redirect them to the Shop page. 
* Checkout form to add customer details and credit card details
* Purchase the products with Stripe test functionality. 
* Blog entries page, where the admin adds blogposts to inspire the users with knitting related topics.
* 


#### Features left I would like to Implement
* In the future I want the users to be able to add comments to the shop owners blogposts, and possibly also stars to vote for the most inspirational posts.
* If I have had more time with the project I would have added the functionality to click on a product to view it in a new tab, and add more information about the product to read there. 
* If I have had more time I would also have wanted to add a commenting system for the users Inspiration posts to give eachother feedback and start discussions. 
* 
*


## Technologies Used
#### Languages
* [HTML](https://www.w3schools.com/html/html5_intro.asp), [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS), [Javascript](https://developer.mozilla.org/en-US/docs/Web/JavaScript) 
* [Python](https://www.python.org/download/releases/3.0/) and [Django](https://www.djangoproject.com/) as the framework.

#### Libraries
* [Google Fonts](https://fonts.google.com/) is used to style the fonts of the website.
* [Bootstrap](https://www.bootstrapcdn.com/) for the content to be responsive and a simple structure of the web page.
* [JQuery](https://jquery.com/) to simplify DOM manipulation, and for the Bootsrap components that requires the use of JavaScript to function.
* [Popper.js](https://popper.js.org/) also for the Bootsrap components that requires the use of JavaScript to function.
* [Font Awesome](https://fontawesome.com/) for the icons. 
*

#### Tools
* [AWS Cloud9 IDE](https://aws.amazon.com/cloud9/) for the development of this site: writing, debugging and running my code. GIT was then used to push files to Github.
* [GitHub](https://github.com/) to store and share the project remotely.
* the database
* [Balsamiq](https://balsamiq.com/) to create my wireframes as a part of the design process, with a simple yet goodlooking result.
* [Responsinator](http://www.responsinator.com/) was used to check the responsiveness of the page, and also [Responsivedesign](http://ami.responsivedesign.is/) for this.
* [Stripe](https://stripe.com/en-se) was used as the payment platform to validate and accept credit card payments in a secure way.
* [AWS S3 Bucket](https://aws.amazon.com/s3/) to store images that was entered into the database.
* [GMAIL SMTP](https://docs.djangoproject.com/en/3.0/ref/settings/#email-backend) was installed and set with specific settings to be used for the function to send emails within this app to users. You can read more [here](https://docs.djangoproject.com/en/3.0/topics/email/).
* I used [Compressed JPEG](https://compressjpeg.com/) to compress images to take up less space in the S3 Bucket. 

#### Databases
* The relational database [PostgreSQL](https://www.postgresql.org/) was used for production database, which is provided by heroku.
* [SQlite3](https://www.sqlite.org/index.html) was used for development database, which is provided by django.

## Information Architecture
* The database structure..



## Testing
Here I present how my website meet the needs of the users that will visit the site, which I presented in the section UX: User stories:

* 
*
*

### Validation of code
- I used [this website](https://validator.w3.org/#validate_by_input) to validate my HTML by direct input.
- I used [this website](https://jigsaw.w3.org/css-validator/validator.html.en#validate_by_input) to validate my CSS by direct input.
- how I validated django and python..

### The responsiveness of the website
I used Responsinator to check the responsiveness of the page.

- The webpage is responsive since I´m using Bootstrap 4 and it works good on smaller devices too. Yhe navbar collapse on smaller views with a standard navbar icon for smaller devices.
- The title of the page inside of the navbar in the top left corner works in a responsive way with the navbar and takes the user back to the landing page when it´s clicked on. 

### Testing process scenarios

#### Manual testing

Example
-Search for products Select menu and -Search- button
1. Click on the dropdown menu.
2. Choose a category.
3. Click on the search button.
4. Try this with all of the categories one by one, and verify that results with products are showing if the chosen ccategory matches the products shown.
5. Verify that the text "No products found" is showing, if no products exist in the database from the chosen product.


Add a product to the cart
1. 
2. 
3. 
4.  


Sign in form


Register form

Contact form
1. Click on the Contact page in the navbar.
2. Fill in the fields, verify that they are required by leaving one out, and see that a text shows that says that you have to fill in that field.
3. Click on the Submit button and verify that the form is not submitted, you are still on the page. (This is because this project did not require authentication, and is therefore something I´ll add later when there is time.)

### Bugs I came across while creating the site and while testing it
* 
*

#### A small example of one of the debugging processes
* 

## Deployment

### Local Deployment
For local deployment you must have an IDE, like for example [Visual Studio Code](https://code.visualstudio.com/) and the following to be installed locally on your machine: [Git](https://git-scm.com/), [PIP](https://pip.pypa.io/en/stable/installing/) and [Python 3](https://www.python.org/downloads/). 
* After creating your own folder and you are in it, type this in to the terminal `git clone https://github.com/LivHed/handcrafted-heart.git`
* Then run this command `pip install --upgrade pip`
* To be followed by this command `pip install -r requirements.txt` to install the required modules. 
* Run the commands to create a superuser, makemigrations and migrate. Read more about this further down in the section Heroku deployment.
* You can now run the app locally with the command `python manage.py runserver`

### Heroku Deployment
This website is deployed on Heroku, following these steps:

* First, create a `requirements.txt` file using the `pip freeze > requirements.txt` command in the terminal to make all of the installed packages and libraries to go in to the file. 
* Then, create a Procfile with the command `echo web: python app.py > Procfile` in the terminal. 
* Then type the `git add` and `git commit` commands for these new files and then `git push` to GitHub.
* Then go to the Heroku website and go to Dashboard and click on the New button, and then click on Create new app. Name it and set the region to Europe.
* In the new Heroku app, Click on Deploy. In the section Deployment method, click on Github.
* Choose the correct GitHub repository to link it to the Heroku app.
* In the section Automatic Deploys, click on Enable automatic deploys, from master branch.
* To add the Postgres database url go to the page Resources in your Heroku app page, and search for Heroku Postgres in Addons, and attach the database to your app.
* Now go to Settings and click on Reveal config vars, and set them to: 
```
SECRET_KEY: <your secret key>
AWS_ACCESS_KEY_ID: <your aws access key>
AWS_SECRET_ACCESS_KEY: <your secret aws access key>
DATABASE_URL: <the database url>
DISABLE_COLLECTSTATIC: <1> 
EMAIL_PASS: <your email password>
EMAIL_USER: <your email> 
STRIPE_PUBLISHABLE: <your stripe publishable key>
STRIPE_SECRET: <your stripe secret key> 
```

* To get the AWS secret keys for the AWS S3 Storage you have to have an AWS account to get access for the S3 Storage. Follow the instructions on [these pages](https://docs.aws.amazon.com/s3/index.html).
* Disable collectstatic is set to 1 because it means that since I´m using static on S3, Heroku will not try and upload the static files.
* To use the email functionality called Gmail SMTP, follow the instructions from [these pages](https://docs.djangoproject.com/en/3.0/ref/settings/#email-backend) and even more detailed [here](https://medium.com/@_christopher/how-to-send-emails-with-python-django-through-google-smtp-server-for-free-22ea6ea0fb8e).
* To get the Stripe keys follow the instructions from the [Stripe](https://stripe.com/docs/payments) documents, and use Stripe´s test functionality.

* With all these steps gone through you can run this command in your terminal: `python manage.py makemigrations` and then run `python3 manage.py migrate` to migrate the database models, which will allow you access to the data models from the backend.
* After the migrations you can create your superuser account in your new database by running the command `python manage.py createsuperuser` which creates an adminstrator for the application. 

* Now in your Heroku page for the application click on the button Open app in the top right corner and you can now view your deployed app.

## Credits

### Content
* The content on the website was written by me for the imaginary shop owner Sarah, after doing research with searching for and looking at other pages containing knitted products for smaller businesses.
* For the Featured Products carousel I´m using a Carousel code snippet example, the third example With Indicators, copied from [this page](https://mdbootstrap.com/docs/jquery/javascript/carousel/)
and then modified for my own needs.
* The footer code snippet is copied from [this page](https://mdbootstrap.com/docs/jquery/navigation/footer/) and then modified for my needs.

### Media
* On this webpage I´m using photos from [Unsplash](https://unsplash.com/), according to their [Unsplash licence](https://unsplash.com/license).
* 

### Acknowledgements
* For the.. 
