## Full Stack Frameworks with Django Project - Code Institute
---
# Star Trek
Do you like Star Trek? Are you looking for a community of people who like Star Trek franchise as much as you? Then join our community! We have 
news from Star Trek franchise and Federation itself! You can find nice goodies for you or friends in our store. Yes, of course we have Raktajino mugs.
Or just join for discussion about everything Star Trek in our Forum where you can chat with other Trekkies. Live long and prosper!


#### Click on the image to see live project!
[![Star Trek Demo](https://raw.githubusercontent.com/romangrubic/Star-Trek-Django/master/static/images/readme/responsive.png "Star Trek Demo")](https://star-trek-by-romangrubic.herokuapp.com/)

---
## Summary
* [Project summary](#project-summary)
* [User Experience](#ux)
    * [User Stories](#user-stories)
    * [Five planes](#strategy)
* [Features](#features)
    * [Existing Features](#existing-features)
    * [Future Features](#future-features)
* [Database Architecture](#database-architecture)
* [Technologies used](#technologies-used)
* [Testing](#testing)
* [Deployment](#deployment)
    * [AWS S3](#aws-deployment)
    * [Heroku](#heroku-deployment)
    * [Local deployment](#local-deployment)
* [Credits](#credits)

---
## Project summary

Welcome to my Full Stack Frameworks with Django Project for Code Institute. 

The goal of this project was to allow the user to create an account and make a purchase of product/membership with Stripe. Database used is a SQL database PostgresSQL.

I am a big Star Trek fan so for my last project with Code Institute, I decided to make a Star Trek web-site, where beside creating account and purchasing a product via Stripe, 
user can also read news from Star Trek franchise, find games about Star Trek and join discussions about Star Trek in a discussion forum. Users can also chat via private
messaging system and edit their profiles so beside this project being a web-shop, it is also a social network for people who like Star Trek.

[Back to top](#summary)

---
## UX
### User Stories
Since this is a big project, I have decided to put user stories in separate file instead here because the README file would be too big.

#### You can access them [here](https://github.com/romangrubic/Star-Trek-Django/blob/master/user_stories.md).

[Back to top](#summary)


### Strategy
Star Trek web-site purpose it to be a social network for people who like STar Trek. Users can read news, discuss on discussion forum with other users about Star Trek,
 visit other users profile and send private messages to others. Also it is a web-shop that sells Star Trek merchandise so the owner can earn some money.

### Scope
In designing the page, I wanted for the user to have a positive experience and for the web-site to be simple to use. User can navigate through navigation bar that 
is always visible and by links in the footer. They can go from any part of the web-site to any other part. Simple to navigate and intuitive.

### Structure
When the user arrives on site, it will see the image and cards as a call to action. By clicking on image, if user is not authorized, it will redirect him to 
registration page. There are four cards for each section with a title that acts as a link to the section and a short description of what user can do/find in 
the section. Navigation is always on top of the screen and has a logo which acts as a link to Home page and a link for each section of the website. Also, I have placed
main links of the web-site in the footer section as I've seen it in almost all web-sites I have visited.

When user goes to news section, they can choose to see all all filter by news and FNN (Federation News Network - fictional news). They can see main image of the news,
title and short description. If they go to view more, news will open in new page where images will slide in a carousel and the whole news can be read. Also they can see 
who the author is, when was it published and how many views. I added an option if the specific news has a post on forum, user can click "Go to Forum" and they will 
be redirected to the relevant post. If user is not authorized, they will be redirected to registration page.

Shop section is similar to every other web-shop. When they arrive at Shop, they will see all products available. I have put option to filter merchandise by five main
 categories. Products are presented as cards with images, name, short description and price. When user hovers over a product card, it gets an overlay and user see 
"Click to view" button. If user decides to view product, they will see up to three pictures of product in a carousel, full name, full description, price and an option 
to add product to cart. If user adds to cart, they will see a message at the top of the page informing them that they have put that product with quantity X in their 
cart. Back to Shop button redirects them back to all products page.

Games section is presenting most popular games about Star Trek franchise. User is presented with an image, title and short description of the game. When they click 
to read more, they can see images from the game, full description of the game and features of it, button with a link to the games web-site where they can read 
more aboout it. There is also button which lead to Forum post about the game where user can comment and find friends to play with.

Forum section is big part where users can interact with each other. They can write posts, read other users posts and comment it, visit others profile by clicking on their
image or username. On other users profile, they have an option to send them a private message if they want to. User can also search Forum posts for a keyword in 
post title to narrow the search or they can filter by date, views and alphabeticaly by author or post title.

In a cart section, users can see all the items in their cart and when they change the quantity of it, it shows instantly. They can also view the product in their cart 
by clicking on name and/or image. Once user is ready for checkout, they will see a form which they have to fill in order for the checkout to be completed. Once completed,
the order will be stored in Account > Orders and user can see it anytime.

In account section, user can view their profile page and edit it. Profile page is a way for user to show their love for Star Trek. They can edit it how they want, they
 can put pictures if they want and change their details. Also send other user a message if they want. Messages part is divided between inbox (received messages) and 
 outbox (messages sent). Every new user when they register will receive a message from admin welcoming the user to the web-site and short description what they can 
 do on web-site. In the messages it is clearly shown who is sender and receiver. The images and username when clicked, will rediret to that users profile. User can write 
 reply from the bottom of the message instead of opening in another page. Orders page are showing past orders that user submitted. If no orders are in database,
 a message is shown and a button that redirects to Shop.

After every user input, submission, registration, login, comment, reply they are notified by a message from the web-site that briefly describes the action taken so that 
user knows their action was properly submitted.

### Wireframes
Since this is a big project, I have decided to put wireframes in separate file.

#### You can access them [here](https://github.com/romangrubic/Star-Trek-Django/blob/master/wireframes.md).

### Surface 
Throughout the project im switching between three colors. Im using shades of white and black for background and shade of yellow-orange for action button. 
By making all the elements stand out correctly and are simple to use, I'm creating environment where user can see what interests it and is intuitive for use. 

 + Main colors used throughout the web-site : 
    - Navigation and footer background - ![#000000](https://placehold.it/15/000000/000000?text=+) `#000000`
    - Background of news, products, posts, games, cart and profile - ![#ffffffe6](https://placehold.it/15/ffffffe6/000000?text=+) `#ffffffe6`
    - Action color - ![#fbce3c](https://placehold.it/15/fbce3c/000000?text=+) `#fbce3c`
    - Return color - ![#17a2b8](https://placehold.it/15/17a2b8/000000?text=+) `#17a2b8`

[Back to top](#summary)

---
## Features
### Existing Features
* Navigation bar
  - Navigation bar is visible on all pages and on all sizes (on a smaller width, it toggles into "hamburger"). It contains web-site logo and a set of links for 
  each section and subsection of web-site.

* Footer section
  - Footer section contains three columns with links to different section of web-site, my contact information with Github, LinkedIn and a contact modal 
  so users can contact me and last part are my projects to date. On a medium and smaller size screen, only section with my contact information is visible.

* News section
  - In news section, users can read about new things in Star Trek franchise. By clicking on a specific news, user can see the news in full size, with 
  pictures and all content. Content for this section was borrowed from the official [Star Trek](https://intl.startrek.com/) website.

* Shop section
  - In the Shop, user can see products available for sell. There are filters in place so user, can easily serch for any type of things (clothes, accessory, drinkware, 
home and collectible). By clicking on a product, user can see the full product info including pictures of product in a Bootstrap carousel, name, description, price and
an add button if they would like to add product. Content for this section was borrowed from the official [Star Trek](https://intl.startrek.com/) website.

* Games section
  - Users can see games about Star Trek franchise available to play. When they click to read more, they can see photos of the game in a carousel, description of the game
and links to the game main page as well as a link that will forward them to Forum post about that game.

* Forum section
  - I wanted for this website to be something more than just another web-shop so I created a discussion forum where users can post their opinion on things Star Trek.
  They can join discusion by commenting bellow post or creating their own. There is a search bar for a quick topic search and also user can filter by 
  author, title, views and date created. User has to register or log-in in order to visit this part of web-site!

* Cart/Checkout section
  - Here users can edit quantity of items or remove them from cart and see price total amount. In order to proceed with checkout, user will be required to register 
  on the site. When user decides to finish shopping, they will need to input their information and credit card details so that purchase can be completed.

* Account section
  - Account is needed if user wants to finish shopping or visit the discussion forum section. Also, when user creates account, it automatically creates a user 
  profile where user can edit information about self and gives opportunity to join the discussion forum and ability to privately chat with other users.

* Django messages
  - I am using a number of django messages to inform user. Whenever user adds, edit or remove a product, they are notified. Same when posting or commenting 
  in Forum section, editing their profile and when sending or replying to private messages. 
  - When user registers, they will see a message instructing 
  them to check their inbox messages and customize their profile

* Forum posts
  - Each forum post has author so users can click on the name or the picture and they will be redirected to that users profile. User can edit post if it is creator
 of the post, and any user can comment to any post in the Forum.

* Profile page
  - Since this is also a social network, users can modifiy their profiles and present themselves to the other users and check other people profiles 
  and send them messages.

* Private chat
  - User can start chatting by going to another user profile and seeing button `send message`. Once sent message will be stored in sender outbox and receivers inbox.
 I have put a check in place so that only these two users can see the message.
  - Whenever new user registers to the site, they will receive a welcoming message from admin where they will be introduced to what they can do on the web-site 
  and customize their profile and join the discussion Forum and become part of the community.

* Orders
  - Users can check their past orders on Orders page.

* Pagination 
  - I have added pagination to News, Shop and Forum sections. 

* "Go to top" button
  - Instead of user scrolling back to the top of the page when he reaches the bottom, I have put a button that will return to top once pressed.

* No results - page 404
  - If user search for an topic in Forum that is not in database, they will see a message that searched item is not in database.

[Back to top](#summary)

### Future Features
  - I would like to expand web-site with more content and more options for the user.

[Back to top](#summary)

---
## Database Architecture

### Database
This project employs SQL database available as add-on on Heroku known as [Heroku Postgres](https://www.heroku.com/postgres). 

#### Full database schema is located [here](https://github.com/romangrubic/Star-Trek-Django/blob/master/database.md)


### Database relations
Beneath is an image that represents relation of tables used in my project.
![Database relations Demo](https://raw.githubusercontent.com/romangrubic/Star-Trek-Django/master/static/images/readme/database/Django.png "Database relations")

[Back to top](#summary)

---
## Technologies Used 
The website is designed using following technologies:

### Programming languages
-	**HTML** - the project used HTML to define structure and layout of the web page;
-	**CSS** - the project used CSS stylesheets to specify style of the web document elements;
-	**JavaScript** - the project used JavaScript to implement Stripe, EmailJS and custom Javascript.
-	**Python** - the project back-end functions are written using Python.

### Libraries
-	**[Font Awesome](https://fontawesome.com/v4.7.0/)** - Font Awesome icons were used throughout the web-site.

-	**[jQuery](https://code.jquery.com/jquery-3.4.1.min.js)** - is a JavaScript library designed to simplify HTML DOM tree traversal and manipulation.

### Frameworks & Extensions
-	**[Django]( https://www.djangoproject.com/)** – Django is a high-level Python Web framework that encourages rapid development and clean, pragmatic design. 

-	**[Bootstrap](https://getbootstrap.com/)** – Bootstrap is a web framework that focuses on simplifying the development of informative web pages.

-	**[EmailJS](https://www.emailjs.com/)** – Service that helps sending emails using client side technologies only. It only requires to connect EmailJS to one of the supported email services, 
create an email template, and use their Javascript library to trigger an email.

-	**[Stripe](https://stripe.com/ie)** – Allows individuals and businesses to make and receive payments over the Internet.


### Database
-	**[Heroku Postgres](https://www.heroku.com/postgres/)** – PostgreSQL is one of the world's most popular relational database management systems.

### Others
-	**[GitHub](https://github.com/)** - GitHub is a global company that provides hosting for software development version control using Git.

-	**[Gitpod](www.gitpod.io)** - One-click ready-to-code development environments for GitHub.

-	**[Heroku](www.heroku.com)** - Heroku is a cloud platform that lets companies build, deliver, monitor and scale apps.

-	**[Travis-CI](https://travis-ci.org/)** – Travis CI is a hosted continuous integration service used to build and test software projects hosted at GitHub. 

-	**[AWS-S3](https://aws.amazon.com/s3/)** – Object storage service that offers industry-leading scalability, data availability, security, and performance.

[Back to top](#summary)

---
## Testing

#### Testing section is located [here](https://github.com/romangrubic/Star-Trek-Django/blob/master/testing.md)

### Travis CI
 - Travis CI is a hosted continuous integration service used to build and test software projects hosted at GitHub and Bitbucket. 

[![Build Status](https://travis-ci.org/romangrubic/Star-Trek-Django.svg?branch=master)](https://travis-ci.org/romangrubic/Star-Trek-Django)


### Validating code
- HTML
  - code is validated through [W3 validator](https://validator.w3.org/).

- CSS
  - code is validated through [W3 Jigsaw](https://jigsaw.w3.org/css-validator/).

- JavaScript
  - code is validated through [JS Hint](https://jshint.com/).

- Python
  - code is validated through [PEP8](http://pep8online.com/).

 [Back to top](#summary)

---
## Deployment

### AWS Deployment

Created a new Amazon account and connect to amazon service AWS3 account are cloud based serve where the project media and staicfiles will be stored unto.
 At first, we locate S3 on amazon service then we create a bucket. While creating the bucket on S3, the note that public access must be all switched off to allow 
 access for users.

Once we've created the bucket, we now can now click on it's properties and enable the Static Website Hosting option, so it can serve the purpose of hosting our 
static files, you will need to imput an `index.html` and `error.html` before saving. Then we go into the created bucket Permissions and click into CORS configuration, 
this part already have a prefilled default config, All that is needed is just to write the default code and save the config.

Then we go into the bucket policy to allows access to the contents across all web and inside this we will put in here some code including arn address displayed at 
the top of the heading. Then we go into amazon IAM to allow identity and access management of our stored files and folder. In the IAM service, we add a new group 
for our application and then we set the policies to ALL Then it generates a downlaodable zip file containing ID and KEY for us to use for the newly added group. 
This ID and KEY as to be stored in an environment variable.

This then allows us to into our terminal window and install some settings Boto3 Django Storages

The Django Storages is passed into the installed apps in settings and also a custom_storage file is created to store credentials in environment variable. And once 
everything looks fine we can run `python3 manage.py collectstatic`. This will collect all the static files in our app including any changes that is made. N.B this 
command has to be run in the development(local) environment each time a change is been made in the static files/folder And your folder and files should display in 
your AWS S3 BUCKETS


### Heroku deployment

The site is hosted through Heroku and is synced to the master branch of the Git repository. 
This means that the latest push to the heroku branch will update the live site automatically.       

The process for initial deployment is as follows -      
- Log into Heroku dashboard and select "Create new app" from teh dropdown menu located on the top right.     
- Enter a name for the app, select a region where you would like your app to be hosted & click the "Create app" button.        
- In the app dashboard, click on settings. Under "Config Vars", click "Reveal Config Vars" and set the variables in Heroku as they are in you env.py file:
- Type in your local terminal: `$ heroku login -i` and once you are logged in, create a requirements file `$ pip3 freeze -- local > requirements.txt`
and create a Procfile for Heroku by typing `echo web: gunicorn <YOUR_PROJECT_NAME>.wsgi:application > Procfile`
- Go back to Heroku, and at Django `Settings` copy `https://<app_name>.herokuapp.com/` 
- Go to Heroku and connect it to GitHub repository so that will automatically update itself after each push. You can also click to wait for CI to pass before pushing 
if you are using Travis CI or any CI
- Once the build is complete, go back to Heroku and click on `Open App`


### Local deployment

To run locally, you can clone this repository directly into the editor of your choice by pasting `git clone https://github.com/romangrubic/Star-Trek-Django.git` 
into your terminal. To cut ties with this GitHub repository, type `git remote rm origin` into the terminal.  

Further help with cloning can be found on this GitHub Help [page](https://help.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository).

[Back to top](#summary)

---
## Credits
### Content
+ Most of the content was used from the official [Star Trek](https://intl.startrek.com/)
website. Including images, products, news and games.

### Acknowledgement
* Inspiration was taken from the official [Star Trek](https://intl.startrek.com/) website.
* Videos on [CodeInstitute](https://codeinstitute.net/).
* Thanks to my mentor Aaron Sinnott for feedback and ideas.
* Big thanks to [Django Project](https://www.djangoproject.com/) and [W3 Schools](https://www.w3schools.com/) for all the content and clarification of different methods.

#### This is for educational use.
[Back to top](#summary)