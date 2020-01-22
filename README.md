[![Build Status](https://travis-ci.org/LivHed/handcrafted-heart.svg?branch=master)](https://travis-ci.org/LivHed/handcrafted-heart)
# Handcrafted heart 
This is my Milestone Project 4: Full Stack Frameworks with Django - Code Institute.

The idea of this web page is that.. My aim is that..

This page is made for an imaginary shop owner from Sweden, Sarah, a small business owner who makes knitted handcrafted products and sell them. The purpose of the products are for warming during winter time up north.
To buy warm products knitted by hand and to get inspiration through the blog and to share inspiration of yout own is all combined in this web application.
[Check it out here!]()

![Handcrafted heart img](the link to the am i responsive webpage image "The handcrafted heart image")

## UX

### Design process
After doing research looking at websites with knitted products I found that there where no pages dedicated only to.. which is a gap I wanted to fill. I wanted to narrow this search down to..  My goals with the design was set to:

* To make the design suitable for people who wants to find knitted products in an easy way. I wanted to do this with a stylistic and easily understandable design with discrete and warm colors, and buttons with clear directions.
* To make a web application with several pages, each with it´s clear purpose, and this with a user friendly and easy layout for the user to quick be able to understand what you can do and how.
* The fonts from Google Fonts that I chose to use for this website `Alegreya', serif` provides an artistic feeling, but are at the same time easy to read, which I think suits the purpose of the page and it´s audience.
* I chose to use..
* 
* I chose the name of the page to be Handcrafted heart, which are supposed to give the customers a personal and warm experience when visiting the page, also some of the products descriptions are a bit more warm and personal to enrich this experience.

My discrete & warm color design choices goes well together with the background image, and are listed here:

Color for the navbar | Color for the footer | Color for the Featured items carousel
--- | --- | ---
#f9d5bb | #cccccc | #f6f4e6

### Wireframes
The wireframes are created with Balsamiq. They where made as a part of the design process and are saved as a pdf document and kept in the separate folder; wireframes. All of the pages are showed as I planned them and one example of mobile view can be found on the last page in the document. [Check them out here!](add link to the wireframes)

### User stories
1. As a person living up north, for example in Sweden, I would like to find knitted products to keep me warm during the winter season. 
2. As a person interested in knitting I would like to have a look at someone elses creations and buy a product to wear something inspiring. I also want to get inspiration from a blog, and share my own knowledge of this craft.
3. As a creative, mindful person living up north I would rather buy handmade knitted products to support small local business owners with a personal touch, instead of buying products from big companies. 


## Features
#### Existing Features
* The navbar contains the name of the web application and the pages you can click on to visit. The pages are named clearly.
* When a user is logged in the Profile and Logout link is showing in the navbar, but if a user is Logged out the Login and Register links are showing instead. All of the other links are showing all the time.
* The search box to search for specific products by keayword is placed underneath the heading. Underneath the search box there is a button to view all the products, this is placed here to direct the user as a natural step to see all of the products at once again after the search for a specific product, if wished.
* The products and the details about them are shown in with cards, in a responsive way. The user can click on the quantity field to choose between the amount from 1 to 5, and are then able to add it to the cart with the Add button. The amount is set to 5 as max since this is a small store with one person that makes the products by hand.
* The fields in the forms are required so the user won´t be able to submit the forms until all of the fields are filled in.
* The name of the webpage is placed in the top left corner of the navbar as good common pratcice, and are clickable and leads to the landing page. The navbar collapse to a burger icon on smaller devices and are placed in the top right corner.
* The page has authentication functionality in the sign in and the registration forms.
* The requirement to log in is activated and the user are redirected to the Login page when the user clicks on the Checkout button in the Cart page. A user can buy products only when he/she are logged in.
* The user is also required to Login and are redirected to the Login page when he/she clicks on the button Add Inspiration on the Inspire page.
* On the Cart page the user can view the order, and also use the Amend button to change the quantity of the order. If the cart is empty the user can click on a button to redirect them to the Shop page. 
* Checkout page displaying the products the user have put in the cart, and a Checkout form to add customer details and credit card details. For the test functionality with Stripe used in this project you can use these digits for the credit card number ´4242 4242 4242 4242´ and these for the CVV number	´111´ and any other expiration credit card date and year.
* On the Inspire page the user can add own posts called Inspiration. The user can Add new inspiration, Edit an already existing Inspiration post and View Inspiration to see the post in an own page.
* Blog entries page, where the admin adds blogposts to inspire the users with knitting related topics.
* Blogposts are on the Blog page truncated in the cards, and when you click Read more you are redirected to a page where you can read the full blogpost.
* Green alert messages are showing underneath the navbar when a user have been logged in, logged out, have registered, have payed, have sent an email. 
* When a user add a product to the cart with the Add button in the Shop page the number of items are showing in the cart in the navbar. Every time the quantity is changed the number in the cart are directly corrected.
* A carousel with 3 images showing Featured products on the landing page. Just to get a small glimpse of what the shop offers.
* 
* 

#### Features left I would like to Implement
* In the future I want the users to be able to add comments to the shop owners blogposts, and possibly also stars to vote for the most inspirational posts.
* If I have had more time with the project I would have added the functionality to click on a product to view it in a new tab, and add more information about the product to read more about it there.
* If I have had more time I would also have wanted to add a commenting system for the users Inspiration posts on the Inspire page to give eachother feedback and start discussions. 
* Add a message on the Shop page "No products found that matched the word you searched for" when a user have searched for a word, such as hockey, that does not match any products.
* Add a message if a user tries to register with an email that another user already uses for an account. When trying this now, nothing happends, the page just remains the same. I want to add an error message here that tells the user that the email already exists for another user account. 


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
* [This](https://favicon.io/favicon-generator/) is the page where I generated the favicon from. 
* I have used [Cripsy forms](https://django-crispy-forms.readthedocs.io/en/latest/install.html) for the contact form, and django-forms for the other forms.




#### Databases
* The relational database [PostgreSQL](https://www.postgresql.org/) was used for production database, which is provided by Heroku.
* [SQlite3](https://www.sqlite.org/index.html) was used for development database, which is provided by django.

## Information Architecture
* The database structure..

#### Data Models
* In the `products` app I have this model: 
1. Product 
* In the `checkout` app I have these models:
1. Order
2. OrderItem
* In the `posts` app I have this model:
1. BlogPost
* In the `inspiration` app I have this model:
1. Inspiration

Example of the structure of one of the models:
---
BlogPost model
---

| Key in db      | FieldType     | Validation                                  |
| -------------- |:-------------:| -------------------------------------------:|
| title          | CharField     | max_length=200                              |
| content        | TextField     |                                             |
| created_date   | DateTimeField | auto_now_add=True                           |
| published_date | DateTimeField | blank=True, null=True, default=timezone.now |
| image          | ImageField    | upload_to="images", blank=True, null=True   |



## Testing
Here I present how my website meet the needs of the users that will visit the site, which I presented in the section UX: User stories:
1. As a person living up north, for example in Sweden, I would like to find knitted products to keep me warm during the winter season. 
2. As a person interested in knitting I would like to have a look at someone elses creations and buy a product to wear something inspiring. I also want to get inspiration from a blog, and share my own knowledge of this craft.
3. As a creative, mindful person living up north I would rather buy handmade knitted products to support small local business owners with a personal touch, instead of buying products from big companies. 

How I meet these needs:
1. This need can be met with visiting the shop page, where you can search for specific products with the search function, and also see all products at once. How to add products to the cart, and to see how many items are added in the cart are made clear to the user. It´s easy to see the order in the cart page and how to proceed to the checkout page, and fill in the payment form. 
2. This need can be met going to the Shop page to look at the shop owners creations and buy something that inspires the user, and on the Blog page the user can get inspiration. The user can also share his/hers own knowledge in the Inspire page where it´s possible to add posts to inspire others. 
3. This need can be met with this kind of small shop that provides a personal, warm feeling that does not have a large amount of products that a large company would have. The shop owner also share some of her stories and feelings in the blog and in the product descriptions, which adds to the personal touch of the page.

### Validation of code
- I used [this website](https://validator.w3.org/#validate_by_input) to validate my HTML by direct input.
- I used [this website](https://jigsaw.w3.org/css-validator/validator.html.en#validate_by_input) to validate my CSS by direct input.
- how I validated python..

### The responsiveness of the website
I used Responsinator to check the responsiveness of the page.

- The webpage is responsive since I´m using Bootstrap 4 and it works good on smaller devices too. Yhe navbar collapse on smaller views with a standard navbar icon for smaller devices.
- The title of the page inside of the navbar in the top left corner works in a responsive way with the navbar and takes the user back to the landing page when it´s clicked on.
- 

### Testing process scenarios

#### Manual testing

-Search for products by keyword in the product page, and View all button
1. Click on the searchfield that says Search for products.
2. Write for example the word hat.
3. Click on the search button.
4. Verify that one or several products are being displayed that matches the keyword searched for.
5. Try to search for a word you know won´t match the products, for example the word hockey, and verify that no products are showing up.
6. Click on the View all button to verify that all products are showing again. 

Add a product to the cart and amend the quantity
1. Click on a products Quantity field and choose a number from 1 to 5. 
2. Verify that the numebr appears in the cart icon in the navbar. 
3. Add another product and verify that the amount in the cart icon is added and is showing the exact number of added products.
4. Click on the cart in the navbar and verify that the amount is correct when viewing the products in the cart summary order table.
5. Click on the Quantity field in the table and verify that the amount is changing in the table after clicking the amend button.
6. Try and amend the products to 0, and verify that a text appears that says that the cart is empty, and a button that suggests to go back to the shop page.

Checkout page functionality
1. Verify that you can see an overview of your products you added to the cart.
2. Fill in the textfields in the form, and verify that the Required textmessage appears when leaving a field out and try to submit, try one by one.
3. When you will fill in the fields for the numbers, the credit card nr, the CVV nr, **please note** that there is a bug here, described in the Bugs section.
4. If you fill in all the fields, you get the message that the payment was successful. If you leave one of those two fields out, you Also get a message that the payment was successful, and the test payment went through and registered on the Stripe website in the Test data.

Inspire page functionality. Add, Edit and View.
1. Click on the Inspire page in the navbar.
2. Verify that you land on the Inspire page where you get three main options.
3. Firstly, click on the button View inspiration to see the content in an own page. There you get two options; To click on the Back to Inspire page button and to click on the Edit inspiration button.
4. Click on Back to Inspiration button and verify that you are redirected back to the main Inspire page.
5. Click again on the View inspiration button in a post to try out the other button Edit Inspiration.
6. Verify that you are redirected to the Add some inspiration page with the prefilled editable fields in the form.
7. Change Title and Content, and verify that you are redirected back to the main Inspire page and that the Inspiration post has been updated.
8. While back on the main Inspire page, click on the Add inspiration button and get redirected to a page with an empty form.
9. Fill out the fields and click on Add inspiration button. Verify that you are redirected to the View Inspiration page, where you can read the post you just created and again are presented with the two button options to Go back to Inspire page and Edit Inspiration.
10. At last, click on Go back to Inspire page and verify that the new post has been added. 

Blog page. View posts.
1. Click on Blog in the Navbar.
2. Confirm that you see the blogposts displayed in a sort of liststyle with cards that stick together.
3. Click on the button Read more and verify that you are redirected to a page where you can reag the full blogpost.
4. Click on the button Go back to Blog and verify that you are now on the main Blog page again.

Log in form
1. Click on Login in the navbar
2. On the Login page fill in the username and password fields.
3. Click on the Login button and verify that you are getting a success message that tells you that you are logged in. 
4. Go to the Profile page that now shows in the navbar and confirm that your user name and email is displayed along with the information about what you can do as logged in.

Register form
1. Click on Register in the navbar. 
2. Fill in the fields, and try and leave one out, one by one at a time, to verify that a text shows that says that you have to fill in that empty field.
3. Click on the Register button and verify that you get a message that tells you that you are now registered and logged in, and that you are redirected to the index page.
4. Go to the Profile page that now shows in the navbar and confirm that your user name and email is displayed along with the information about what you can do as logged in.

Contact form
1. Click on the Contact page in the navbar.
2. Fill in the fields, verify that they are required by leaving one out at a time, and see that a text shows that says that you have to fill in that empty field.
3. Click on the Send button and verify that you are getting a message that says that your message has been sent.

### Bugs I came across while creating the site and while testing it
* Example of an error message I got from the console when adding blogposts from the backend logged in as admin. The error message from the running link from the development environment: """Failed to load resource: the server responded with a status of 404 ()  blogpostimg3-min.jpg'):1""" and the error message showed in the console when running the app from Heroku: "GET https://handcrafted-heart.herokuapp.com/url('https://handcrafted-heart.s3.amazonaws.com/media/images/blogpostimg1-min.jpg') 404 (Not Found)" The images is stored in the images file in the AWS S3 Bucket and was not showing at first. 
* The register form to register a new user was at first not functioning. After filled out all of the required fields, and clicked the submit button nothing happend, only that the two password fields cleaned up empty, but no successmessage was shown.

* One bug discovered not yet solved is that when you leave one field out in the payment form, leaving one of the number fields out, for example the CVV field, the form is submitted anyway, and you get a success message that the payment was successful. 
1. This is not yet solved. As the fields in the form in the forms.py file in the checkout app was set to required=False, I tried to change these to True. This though, gave an error message that the payment was not successful. 
2. I tried to add `required` to the html code, but as the forms are loaded with `payment_form | as_bootstrap` with no input fields, adding the required did not make any difference.
3. Which result in that it´s currently possible to pay with Stripe´s test functionality with all fields filled in, but also with one of the number fields Not filled in. 


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
* On this webpage I´m using jpg images from [Unsplash](https://unsplash.com/), according to their [Unsplash licence](https://unsplash.com/license).
* 

### Acknowledgements
* For the.. 
