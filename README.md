![Image of logo](static/images/plant-swap-readme.png)
# *Plant Swap* - Third Milestone Project for Code Institute 
*Plant Swap* was created for plant enthusiasts around the world who are looking to adopt new plants while making sure their unwanted plants go to a good home. 

At *Plant Swap* we truly believe in "One Man's Trash Is Another Man's Treasure". Why spend money on a new plant when you can simply swap instead? 

A live preview of the site can be found here: [Plant Swap](https://plant-swap-ci.herokuapp.com/)
## Table of Contents
1. [UX Design](#ux-design)
    * [User Stories](#user-stories)
    * [Strategy](#strategy)
    * [Scope](#scope)
    * [Structure](#structure)
    * [Skeleton](#skeleton)
1. [Features](#features)
1. [Technologies Used](#technologies-used)
1. [Testing](#testing)
1. [Deployment](#deployment)
1. [Credits](#credits)

## UX Design
### User Stories
#### New Users:
* I want the ability to quickly learn about what the website offers.
* I want the ability to create an account so I can view posts and create my own posts.
#### Existing Users:
* I want the ability to log in to my account.
* I want the ability to see all available posts.
* I want the ability to contact someone about their post.
* I want the ability to filter all posts on location.
* I want the ability to create posts.
* I want the ability to edit my own posts.
* I want the ability to delete my own posts.
* I want the ability to log out of my account.
* I want the ability to delete my account and posts.

### Strategy
The primary goal of this website is to offer users an easy way to get in touch with others so they can swap plants. In order to accomplish this, the website is as minimalistic as possible and has simple navigation on every page. As a wide variety of users will visit *Plant Swap* the layout of the website will respect this and be straightforward and easily accessible to all. 
### Scope
The users need the following from the website: 
* A Landing Page that is easy to navigate. 
* A footer and navigation bar that change depending on whether the user is logged in or not. 
* A register and login form for users to either create a new account or to log in.
* A My Account Page for users to view/edit/delete their posts, and an option to delete their account. 
* A Sign Out button that is easy to find on every page (preferably in the navigation bar).
* An About page for both users and new visitors to see what the website does and how to use the website. 
* A Posts page where users can see all the posts on the website.
* A way to filter posts so users can see the plants available in their area. 
### Structure
Flask was used for this project in order to make an interactive website that sends users to different links/pages depending on their input.

A traditional navigation bar was implemented at the top of each page with the common "Tree Structure". This bar changes depending on whether a user is current logged in. If so, it includes links to the Posts, My Account, Add Post, and How To Swap pages. If not, it includes links to the Home, Log In, Register, and How To Swap pages.

**Color Scheme**: The background of the website, footer and navigation bar are all white. This allowed the focus to be on the content of the pages. Dark gray was used for all of the font on the website. Buttons and links were done in two different shades of green, as green is usually the color associated with plants. The only other color used was red for errors and delete buttons. Red was chosen because it stands out from the rests and alerts users about the error or that they are about to delete something important.  
![Image of Colors](static/images/color-scheme.png)

**Typography**: [Questrial](https://fonts.google.com/specimen/Questrial?sidebar.open=true&selection.family=Questrial) was used for the entire website. 

**Icons**: Icons from [FontAwesome](https://fontawesome.com/) were used in the footer for Social Media links in order to minimize text used. 

### Skeleton 
[Click here](wireframes) to see all wireframes for this project. 

*Please note that the wireframes show the initial design ideas for the website and therefore may not match the current version.*
## Features

### Existing Features
#### Navigation Bar
The navigation bar is the same on all pages, making navigating the website simple. It collapses to the popular hamburger icon on smaller devices in order to save screen space. 

Depending on whether the user is logged in or not, the navbar shows a different, menu. When logged in it has links to the Posts, Account, Add Post, and About pages. When not logged in, it links to the Home, Log In, Register, and About pages. When logged in there is also an option to Sign Out.

The *Plant Swap* logo is on the left side, which links to the home page if users are not logged in and the posts page if they are. 

To give feedback to the user, when hovering over the links their color changes to a dark green.

#### Footer
The footer is currently very basic. It displays a Site Map with the same links as the navbar, social media links, and a short about section. 

On mobile the footer is reduced to show only the social media links.

The links in the footer give the same feedback as in the header when hovered over.
#### Landing Page
A clean and minimal landing page that the users see when they visit the website. This allows users to either log in, register, or find out more about *Plant Swap*.

Both the Sign In and Lear More buttons change from a transparent background to a dark green background when being hovered over.

On mobile, the Learn More button disappears, in order to save screen space.

#### Registration Form
This allows new visitors to create an account. If an account with the username or email already exists, the user will get an error message asking to try again. 

In case users already have an account and want to sign in instead, there is a link at the bottom of the form that will take them to the Sign In page. 

#### Sign In Form
This form allows existing users to log in using their username and password. An error message will appear if an invalid username/password is entered. 

There is an option at the bottom of the form to go to the registration form if they don't have an account yet.

#### Account Page
Users are taken to this page as soon as they sign in/register. If they have posted in the past this page will show all of their posts and give them the option to edit/delete posts. There is also an option to delete the account, which will delete all the posts made by the user as well. 

If the user doesn't have any posts yet, a message will appear giving them the option to view posts made by other people, or to add a post.

#### Add Post Form
A simple form in the same style as all other forms on the website. when a user is logged in they can use this form to post a new plant. The following details need to be filled in on this form: 

* Plant Name
* Image url of plant
* The plant the user is looking for
* Country 
* Email (readonly which is filled automatically with the session email)
* Date Posted (readonly which is filled automatically with today's date)

When the Submit button is pressed the post is sent to the Mongo database and will show up on both the Account page and the Posts page.

#### Edit Post Form
Very similar to the Add Post Form. The only difference is that the existing values for the selected post are populated when the page loads, and users can simply change the values that they want to adjust.

When the submit button is pressed the updated information gets sent to the database for that post.

There is also a delete button at the bottom of the form. When this is selected the user should see a pop-up confirming that they want to delete the post. If they confirm the post is removed from the database.

#### Posts Page
This page shows all the posts made on the website.

There is an option under each post to contact the person who created the post. This will forward the user to their email client and allow them to get in touch with each other and organize the plant swap. 

There is also a filter at the top of the page. This makes it possible to filter posts based on the country selected, making it easier to find relevant swaps in the area.

#### How To Swap Page
This is a static page which gives instructions on how to use *Plant Swap*. It is available to both new visitors and registered users. The images for each step only appear on medium screens and larger, giving mobile a simple and clean look.

### Hopeful Future Features

## Technologies Used

### Languages
* [HTML5](https://developer.mozilla.org/en-US/docs/Web/HTML)
* [CSS3](https://developer.mozilla.org/en-US/docs/Web/CSS)
* [Javascript](https://www.javascript.com/)
* [Python](https://www.python.org/) 
* [Jinja2](https://jinja.palletsprojects.com/en/2.10.x/)

### Libraries/Frameworks 
* [Bootstrap](https://www.getbootstrap.com/) : Used for initial styling and in order to create a uniform website that renders well on all screen sizes. Also used for some basic Javascript additions.
* [Google Fonts](https://fonts.google.com/) : Used for the font on the website.
* [Font Awesome](https://fontawesome.com/) : Social Media icons on the website come from Font Awesome.
* [Flask](https://palletsprojects.com/p/flask/) : Used as the main framework for the project.
* [Bcrypt](https://pythonise.com/categories/python/python-password-hashing-bcrypt) : Used to hash entered passwords. 

### Tools
* [Visual Studio Code](https://code.visualstudio.com/) : The code editor used for this project.
* [Git](https://git-scm.com/) : Installed on VS Code to allow version control.
* [Balsamiq Mockups](https://balsamiq.com/) : Used to create the wireframes during the UX Design process.
* Chrome Developer Tools: Used to test the website while developing.
* [W3C Markup Validation Jigsaw](https://jigsaw.w3.org/css-validator/) : To validate the CSS code.
* [W3C Markup Validation](https://validator.w3.org/) : To validate the HTML code.
* [Pixabay](https://www.pixabay.com/) : Free online images. Used for some images on website.
* [Unsplash](https://unsplash.com/) : Free online images. Used for some images on website.
* Github: Used to host the repositories for this project.
* [Canva](https://www.canva.com/) : Used to resize images and create logo.
* [Heroku](https://heroku.com/) : Used to host the website.
* [PyMongo](https://pymongo.readthedocs.io/en/stable/) : Used in order to allow the website to communicate with the MongoDB database. 

### Databases:
* [MongoDB](https://www.mongodb.com/cloud/atlas) : Used to store users and posts

## Testing

## Deployment

## Credits
