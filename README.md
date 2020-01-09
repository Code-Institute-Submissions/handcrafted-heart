# Handcrafted heart 
This is my Milestone Project 4: Full Stack Frameworks with Django - Code Institute.

This is a page for.. 
The idea of this web page is that.. My aim is that..
In this app I have used the programming language Python along with the framework .. and the database...
[Check it out here!]()

![Handcrafted heart img](the link to the am i responsive webpage imageg "The handcrafted heart image")

## UX

### Design process
After doing research looking at websites with knitted products I found that there where no pages dedicated only to.. which is a gap I wanted to fill. I wanted to narrow this search down to..  My goals with the design was set to:

* To make the design suitable for people who wants to find .. in an easy way. I wanted to do this with a stylistic and easily understandable design with.. colors and buttons with clear directions.
* To make a web application with several pages, each with it´s clear purpose, and this with a user friendly and easy layout to quick be able to understand what you can do and how.
* The fonts that I chose to use for this website are.. because it presents the content in a stylistic and easy-to-read way.
* I chose to use..
* 
*

This handles the CRUD functionality (Create, Read, Update and Delete) and I planned for this web page to give a sense of.. 

### Wireframes
The wireframes are created with Balsamiq. They where made as a part of the design process and are saved as a pdf document and kept in the separate folder; wireframes. All of the pages are showed as I planned them and one example of mobile view can be found on the last page in the document. [Check them out here!](add link to the wireframes)

### User stories
* 
*
*

## Features
#### Existing Features
* The navbar contains the name of the web application and the pages you can click on to visit. The pages are named clearly.
* The select menu with the products and the search button is placed .. as a natural next step of action to follow.
* The products and the details about them are shown in ...panel bodies?, in a responsive way. The user can click on the product to view the details about the product and to be able to add it to the cart.
* The fields in the forms are required (except for the insert image field), so the user won´t be able to submit the forms until all of these fields are filled in. This will show nicely in the panel bodies?.., with all rows complete inside of them.
* The name of the webpage is placed in the navbar in the left corner as good common pratcice, and are clickable and leads to the landing page. The navbar collapse to a burger icon on smaller devices.
* If a user clicks on the add product button...
* The page has authentication in the sign in and the registration forms, so the user can add products and buy them only when they are logged in.
* pagination..

#### Features Left to Implement
* In the future I want to add 
* If I have had more time with the project I would have added..
* If I have had more time I would also have wanted to add..
* In the future I would want users to be able to..
* I also want to add..
* I want to add icons to the ..
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
* 
*

#### Databases
* [PostgreSQL](https://www.postgresql.org/) was used for production database, which is provided by heroku.
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
For local deployment you must have an IDE, like [Visual Studio Code](https://code.visualstudio.com/) and the following to be installed locally on your machine: [git](https://git-scm.com/), [PIP](https://pip.pypa.io/en/stable/installing/), [Python 3](https://www.python.org/downloads/), [Flask](https://flask.palletsprojects.com/en/1.1.x/installation/) and a [MongoDB Atlas account](https://docs.atlas.mongodb.com/).
* After creating your own folder and are in it, type this in to the terminal `git clone https://github.com/LivHed/coworking-spaces.git`
* Then run this command `pip install --upgrade pip`
* To be followed by this command `pip install -r requirements.txt` to install the required modules. 
* You can run the app with the command `python3 app.py`

### Heroku Deployment
This website is deployed on Heroku, following these steps:

* First, create a `requirements.txt` file using the `pip freeze > requirements.txt` command in the terminal. 
* Then,create a Procfile with the command `echo web: python app.py > Procfile` in the terminal. 
* Then type the `git add` and `git commit` commands for these new files and then `git push` to GitHub.
* Then go to the Heroku website and go to Dashboard and click on the New button, and then click on Create new app. Name it and set the region to Europe.
* In the new Heroku app, Click on Deploy. In the section Deployment method, click on Github.
* Choose the correct GitHub repository to link it to the Heroku app.
* In the section Automatic Deploys, click on Enable automatic deploys, from master branch.
* Now go to Settings and click on Reveal config vars, and set them to: 
```
IP : 0.0.0.0
PORT: 5000
SECRET_KEY: <your_secret_key>
```
* 
* Click on the button Open app in the top right corner in the Heroku page and you can now view your deployed app.

## Credits

### Content
* The content on the website was written by me and Sarah, the owner of the page is an imaginary person, after doing research with searching for and looking at other pages containing knitted products.
*  

### Media
* The images of the products are gathered from this page (e.g Unspalsh) following their guidelines.
* 

### Acknowledgements
* For the.. 
