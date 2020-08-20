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

A traditional navigation bar was implemented at the top of each page with the common "Tree Structure". This bar changes depending on whether a user is currently logged in. If so, it includes links to the Posts, My Account, Add Post, Log Out and How To Swap pages. If not, it includes links to the Home, Log In, Register, and How To Swap pages.

**Color Scheme**: The background of the website, footer and navigation bar are all white. This allowed the focus to be on the content of the pages. Dark gray was used for all of the font on the website. Buttons and links were done in two different shades of green, as green is usually the color associated with plants. The only other color used was red for errors and delete buttons. Red was chosen because it stands out from the rests and alerts users about the error or that they are about to delete something important.  
![Image of Colors](static/images/color-scheme.png)

**Typography**: [Questrial](https://fonts.google.com/specimen/Questrial?sidebar.open=true&selection.family=Questrial) was used for the entire website. 

**Icons**: Icons from [FontAwesome](https://fontawesome.com/) were used in the footer for Social Media links in order to minimize text used. 

### Skeleton 
[Click here](wireframes) to see all wireframes for this project. 

*Please note that the wireframes show the initial design ideas for the website and therefore may not match the current version.*

[Back to Top](#table-of-contents)
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

Both the Sign In and Learn More buttons change from a transparent background to a dark green background when being hovered over.

On mobile, the Learn More button disappears, in order to save screen space.

#### Registration Form
This allows new visitors to create an account. If an account with the username or email already exists, the user will get an error message asking to try again. 

In case users already have an account and want to sign in instead, there is a link at the bottom of the form that will take them to the Sign In page. 

#### Sign In Form
This form allows existing users to log in using their username and password. An error message will appear if an invalid username/password is entered. 

There is an option at the bottom of the form to go to the registration form if they don't have an account yet.

#### My Account Page
Users are taken to this page as soon as they sign in/register. If they have posted in the past this page will show all of their posts and give them the option to edit/delete posts. There is also an option to delete the account, which will delete all the posts made by the user as well. 

If the user doesn't have any posts yet, a message will appear giving them the option to view posts made by other people, or to add a post.

#### Add Post Form
CRUD - *Add* a New Post

A simple form in the same style as all other forms on the website. when a user is logged in they can use this form to post a new plant. The following details need to be filled in on this form: 

* Plant name
* Image url of plant
* The plant the user is looking for
* Country 
* Email (readonly which is filled automatically with the session email)
* Date Posted (readonly which is filled automatically with today's date)

When the Submit button is pressed the post is sent to the Mongo database and will show up on both the My Account page and the Posts page.

#### Edit Post Form
CRUD - *Update* and *Delete* a Post

Very similar to the Add Post Form. The only difference is that the existing values for the selected post are populated when the page loads, and users can simply change the values that they want to adjust.

When the submit button is pressed the updated information gets sent to the database for that post.

There is also a delete button at the bottom of the form. When this is selected the user should see a pop-up confirming that they want to delete the post. If they confirm the post is removed from the database.

#### Posts Page
CRUD - *Read* (view) all posts

This page shows all the posts made on the website.

There is an option under each post to contact the person who created the post. This will forward the user to their email client and allow them to get in touch with each other and organize the plant swap. 

There is also a filter at the top of the page. This makes it possible to filter posts based on the country selected, making it easier to find relevant swaps in the area.

#### How To Swap Page
This is a static page which gives instructions on how to use *Plant Swap*. It is available to both new visitors and registered users. The images for each step only appear on medium screens and larger, giving mobile a simple and clean look.

### Hopeful Future Features

* To allow users to message each other within the website, instead of needing to be forwarded to an external email client.
* A feature to allow users to simply upload images from their personal device, instead of needing to copy and paste a URL from the web.
* A section on the My Account page which would allow users to edit their details (username, email, password, etc.)
* Back-end form validation. At the moment the forms are only validated on the front-end which isn't secure.  
* A "Confirm Password" field when registering a new account, at the moment new visitors only need to fill their password in once. 

[Back to Top](#table-of-contents)

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
* [Font Awesome](https://fontawesome.com/) : Used for social media icons.
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
* [MongoDB](https://www.mongodb.com/cloud/atlas) : Used to store users and posts.

[Back to Top](#table-of-contents)

## Testing
Chrome Developer Tools was used the entirety of my project to test out how the website rendered on different viewports/devices. By using the device selector I went through each screen size to confirm that everything looked correct each time I changed anything. 

The website has been tested on Google Chrome, and Safari for mobile and web and on Microsoft Edge and Internet Explorer for web. Depending on the screen size the Jumbotron on the Landing Page can be a little too far down the page or too far up. I tried changing the margins, and adding the my-auto Bootstrap class, but neither of these resolved the issue. Internet Explorer currently also has some styling issues, but seeing as Microsoft Edge is officially replacing IE I decided this wasn't an urgent issue. 

[Am I Responsive](http://ami.responsivedesign.is/) was used throughout the process to ensure that the website rendered well on different screen sizes.

![Image of Am I Responsive](static/images/am-i-responsive.png)

### Validation Testing
* HTML: [W3C Markup Validation Service](https://validator.w3.org/) was used to validate. There were many errors due the program not accepting Jinja.
* CSS: [ W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/) was used to validate. No errors were found.
* Python: [PEP8 Online](http://pep8online.com/) was used to validate. There were some errors about the lines with comments being too long. Another error appeared regarding a line break but I was unable to resolve that as VS Code reformatted every time I tried to remove the line break. 

### Testing User Stories

* I want the ability to quickly learn about what the website offers.
    1. Head to the Homepage of the website.
    1. Press the "Learn More" button or the "How to Swap" navbar link.
    1. Read the steps that need to be taken in order to swap. 
* I want the ability to create an account so I can view posts and create my own posts.
    1. Head to the Homepage of the website.
    1. Select either the "Sign up here" link or the "Register" navbar link.
    1. Fill in the form on the "Create An Account" page.
    1. Press the "Register" button.
* I want the ability to log in to my account.
    1. Head to the Homepage of the website.
    1. Press either the "Sign In" button or the "Sign In" link on the navbar.
    1. Fill in the username and password on the "Sign In" form.
    1. Press the "Sign In" button.
    1. If password and username are correct the user will be taken to their "My Account" page. 
* I want the ability to see all available posts.
    1. Sign in or register using the above steps.
    1. On your "My Account" page, select the "Posts" link on the navbar or footer. 
    1. View all posts.
* I want the ability to contact someone about their post.
    1. Head to the "Posts" page using the steps above. 
    1. Press the "Get in Touch" button under the post you are interested in. 
    1. Your mail client will open up with the "To:" field filled in.
    1. Send your email as you usually would. 
* I want the ability to filter all posts on location.
    1. Head to the "Posts" page using the steps above.
    1. At the top of the page, use the dropdown menu to find your country. 
    1. Select "Filter".
    1. If there are posts available in your country they will appear.
    1. If not, you will have the option to either go back to all posts or to add a new post.
* I want the ability to create posts.
    1. Log in/register using the steps above.
    1. Once on your "My Account" page, select "Add Post" in the navbar. 
    1. Fill in all the fields on the "Create Post" form. Your email and today's date will be filled in for you. 
    1. Press the "Submit" button. 
    1. If you missed a field, an error message will appear asking you to fill in the field.
    1. If everything was filled in you will be taken back to your "My Account" page and should be able to see your new post. 
* I want the ability to edit my own posts.
    1. Log in/register using the steps above.
    1. Head to your "My Account" page.
    1. Select the "Edit" button under the post you would like to change.
    1. Change whichever fields you want on the "Edit Post".
    1. Press "Submit". 
* I want the ability to delete my own posts.
    1. Head to the "Edit Post" section using the steps above.
    1. Press the "Delete" button at the bottom of the page.
    1. A modal will pop up asking you to confirm.
    1. Press the "Delete" button to confirm.  
* I want the ability to log out of my account.
    1. When logged in, select the "Sign Out" link on either the navbar or the footer.
* I want the ability to delete my account and posts.
    1. Head to the "My Account" page using the steps above. 
    1. At the bottom of the page, below any posts you may have created, select the "Delete Account" button. 
    1. A modal will pop up asking you to confirm.
    1. Press the "Delete" button to confirm.

### Manual Testing

✔️ Navigation links: All redirect to the correct pages.

✔️ Footer links: All redirect to the correct pages.

✔️ Social links: All open a new tab with the correct social media website.

✔️ Misc. links on website: All other links are working correctly.

✔️ Try loading My Account page when not logged in: Get redirected to index.html.

✔️ Try loading Posts page when not logged in: An error message appears asking user to log in/register.

✔️ Try loading Add Post page when not logged in: An error message appears asking user to log in/register.

✔️ Submit registration form with a user/email that already exists in database: An error message appears.

✔️ Submit registration form with one of the fields not filled in: An error message appears asking user to fill in the field.

✔️ Submit registration form with a new user/email that doesn't exist in database: Successfully sends user data to MongoDB and redirects user to their My Account page. 

✔️ Submit Log In form if no username exists in database that matches entered username: Error message appears and asks user to try again.

✔️ Submit Log In form if username is correct but password doesn't match: Error message appears and asks user to try again.

✔️ Submit Log In form with one of the fields not filled in: An error message appears asking user to fill in the field.

✔️ Submit log in form with correct username and password: Starts session and takes user to their My Account page. 

✔️ Press the Sign Out button when logged in: Ends the session and sends user back to index.html. 

✔️ Try adding a post when logged in: Successfully creates a post and redirects user to their My Account page only if all the fields are filled in correctly. If not, an error message appears.

✔️ Try editing a post on the My Account page: Successfully updates post and redirects user to their Account page only if all the fields are filled in correctly. If not, an error message appears.

✔️ Try deleting a post while on the Edit Post form: A modal pops up asking for confirmation. When confirmed, it successfully removes the post from the website and redirects to the My Account page. 

✔️ Filter posts on posts.html by country that has no posts: Get a message that no posts are available in the area with the option to go back to all posts or to add a new post. 

✔️ Filter posts on posts.html by a country that has at least one available post: The matching posts appear and all posts from other countries disappear. 

✔️ Press the delete account button on the My Account Page: Get a pop up message asking to confirm. When confirmed both the account and the posts made by the account get deleted from the database.

✔️ Try logging in with the credentials from the deleted account: Get an error message. 

[Back to Top](#table-of-contents)

## Deployment
*Plant Swap* has been built with the help of Visual Studio Code, a desktop code editor. It has been committed to Git and Pushed to GitHub using the terminal in Visual Studio Code. the website is hosted on Heroku.

### Cloning
#### 1. Clone the repository and run locally:

1. Navigate to the repository from the Github Dashboard
1. Select the green button in the top right of the screen that says "Clone or download"
1. Click on the clipboard icon to the right of the URL to copy it
1. Open an Integrated Development Environment (IDE) and head over to the terminal
1. Change the directory to where you want to clone the repository to
1. Execute the following command by pasting in the URL you copied in step 3: git clone https://github.com/debrawolford/treat-your-pup.git
1. Press Enter
1. The site will then be cloned
1. Install all the project dependencies by typing `pip install -r requirements.txt`

#### Set Up Environment Variables:

1. Create an env.py file in your root directory.
1. Add env.py file to the.gitignore file.
1. Add the following to your env.py file with the applicable variables: 
```
import os
os.environ["MONGO_URI"] = "mongodb+srv://username:password@myfirstcluster-strtg.mongodb.net/plant_swap?retryWrites=true&w=majority"
os.environ["IP"] = "0.0.0.0"
os.environ["PORT"] = "5000"
os.environ["SECRET_KEY"] = "Your Secret Key"
```

### Deploying on Heroku
1. Go to your Dashboard in [Heroku](https://heroku.com/) and select New -> Create New App.
1. Add the following Config Vars in the settings tab: 
    * IP : 5000
    * PORT : 0.0.0.0
    * MONGO_URI : "mongodb+srv://username:password@myfirstcluster-strtg.mongodb.net/plant_swap?retryWrites=true&w=majority"
    * SECRET_KEY : "Your Secret Key"
1. Go to the Deploy tab and select GitHub as your Deployment method. 
1. Follow the instructions to connect to the correct Github repository.
1. Enable Automatic Deploys. This will deploy the website each time the master branch is updated.
1. If you prefer to deploy manually, head to the Manual Deployment section, choose the master branch, and select Deploy. 
1. Your website should now be live.

[Back to Top](#table-of-contents)

## Credits
### Content
I initially followed the tutorial by [Pretty Printed](https://www.youtube.com/watch?v=vVx1737auSE&t=6s) to create the Log In/Registration system. It was later adapted to suit my project.

In order to import a list of countries into MongoDB I followed the steps created by Albert-Gao on [Github](https://github.com/Albert-Gao/world-cities-mongodb).

### Media
All the images (other than the logo) on this website were taken from [Pixabay](https://www.pixabay.com/) and [Unsplash](https://unsplash.com/), websites that offers free stock images.

[Back to Top](#table-of-contents)

## Acknowledgements

Thanks to my mentor, Dick Vlaanderen for all of the guidance and for challenging me to improve my project with additional features.

[Back to Top](#table-of-contents)
