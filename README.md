<h1 align="center"> Ecommerce Photo Store - 🎨 <i>PG's Picsies</i> 📸 </h1>

<hr>

# Contents
- [Setup](#setup)
- [Overview](#overview)
- [Walk-through](#walk-through)
- [Tools](#tools)
- [Resources](#resources)
- [Credits](#credits)

</br>
<hr>

# Setup
- Please refer to the [Guidebook](GUIDE.md) for steps to setup the development environment and execute the project.


# Overview
The aim of the project is to build a functional E-commerce platform with a built-in payment gateway. For tech stack check [Tools](#tools). The platform being a skills demonstration for Full-Stack Development will have browsing functionality and a barter-exchange checkout.

**PG's Picsies** is a Photo store similar to ShutterStock, Pexels, FreePik, etc. Images advertised on the platform will be loaned (check [Credits](#credits)). The website consists of :
- Images themed on the platform is *Nature*
- Art from *Bing Copilot Designer*
- Photos from *Pexels*
- Users or Customers can be Photographers, Artists or Enthusiasts.

<br>

In brief, currently the application is capable of performing the following functions:
- Authorize and authenticate Users(Customers) based on their credentials
- Users/Customers can :
  - Register and create their own profiles
  - Browse *Products* and add items to the *Cart*
  - Search *Products* through filters - *Type, Theme & Author*
  - Edit their *Cart* - increase/decrease product quantity, remove product
  - Upload photographs and/or art to the *Product Inventory* as Payment

<br>

The application is fully-functional on a fundamental level (check [Walk-through](#walk-through))
<br>
The application will be updated at every chance available, for advanced functionality (check [ADD-ONS](/ADD-ONS.md))
</br>
<hr>

- Jump to either of the sections below for a glimpse

> [Workflow](/PROCESS_FLOWS.md) | [Walkthrough](#walkthrough) | [Database Schema](#database-schema) | [Features Implemented](#features-implemented)

<br>
<hr>

# Walk-through

## User Login/Sign Up
  - Login/Signup includes User Authentication & Authorization
  - System(database and Backend) authenticates and authorizes User based on their credentials
  - Upon successful authentication, Users/Customers can 
    - View or edit their profiles, 
    - Browse or search for products and
    - Proceed to [**Checkout**](#checkout) to barter an image in exchange for the images they would like to own
- **User *login* page**
![Login page](/screenshots/login.png)

- **User *registration* page** ( logo and text remain the same for sign up page as well )
![Sign Up page](/screenshots/signup.png)

<br>
<hr>

## Home Page
  - Customers once authenticated will be welcomed with their name
  - Home page consists of :
    - 'Photo' & 'Art of the Day' images,
    - Images related to 'Theme of the Day'
  - If unauthenticated Users access the **Home** page they will be redirected to *Login* upon doing either of the following actions :
    - add image to Cart, Or
    - access [**Checkout**](#checkout)
  - Unauthenticated Users can still :
    - search for images using the Search bar,
    - browse images in 'Products'
<!--
![Text](path/to/image)
-->
- **Non-User *Home* page**
![Non-User Home page](/screenshots/home-nonUser.png)
- **User *Home* page** 
![User Home page](/screenshots/home-user.png)

<br>
<hr>

## Products
  - *Images*
    - 'Photo' & 'Art of the Day' images,
    - Authenticated and Unauthenticated Users can access all images using *Search Filters*
    - Only verified Users/Customers can add items to *Cart* and *Checkout* for payment
  - *Search Filters*
    - Authenticated and Unauthenticated Users can filter images by - *Image Theme, Image Type & Artist*
  - *Cart*
    - After authentication, Customer can :
      - add/remove items 
      - access *Checkout* to purchase added products
  - *Inventory*
    - Only Admin has access
    - All Users/Customers information is accessible
    - All images information is accessible
    - All Carted items & Orders are accessible

- **Filter images by Type, Theme and Artist**
![Products page](/screenshots/products.png)


### Checkout
  - Displays all items added to *Cart*
  - Provides options to 'Change Quantity' or 'Remove', default quantity is 1
  - Provides options to 'Continue Shopping' or 'Proceed to Payment'
- **Checkout view of verified Customer**
![Checkout](/screenshots/checkout.png)

### Payment Gateway
  - Final display of all items added to Cart with quantity
  - Provides options to 'Remove'
  - Explains payment procedure
  - Information about payment is to be filled in the form
  - Upon successful payment, redirects to *Home* page with success message
- **Payment view - payment procedure & items summary**
![Payment summary](/screenshots/payment1.png)
- **Payment view - payment information**
![Payment details](/screenshots/payment2.png)
- **Successful Payment view - order & payment confirmation message**
![Payment success message](/screenshots/payment-success.png)

<br>
<hr>

> _Demo video_

*...production in progress...*

[Back To Contents](#contents)

<br>
<hr>

# Tools
- **Frontend**
  - Figma (for design)
  - HTML
  - CSS 

- **Database**
  - SQLite

- **Backend**
  - Django (Python)


</br>

[Back To Contents](#contents)

<br>
<hr>

# Features Implemented
## Project Design
- [X] Define project directories and files
- [X] Use Figma to build ecommerce store design
- Resources: Figma

## Project Setup and HTML/CSS
- [X] Project Setup: Create a Django project.
- [X] HTML/CSS: Review and strengthen HTML and CSS skills.
- Resources: Online HTML/CSS tutorials, Django documentation.

## Django Fundamentals
- [X] Django Basics: Learn about Django's project structure, settings, and apps.
- [X] Models: Create Django models for products and categories.
- Resources: Official Django documentation.

## Django Views and Templates
- [X] Views: Create views to render product listings and detail pages.
- [X] Templates: Build HTML templates for product pages.
- Resources: Django documentation on views and templates.

## User Authentication
- [X] User Authentication: Implement user registration and login functionality.
- [X] Custom User Model: Create a custom user model with additional fields.
- Resources: Django documentation on User authentication.

<br>

[Back To Contents](#contents)

<br>
<hr>


# Resources
- Django
  - [Official Django Documentation](https://docs.djangoproject.com/)
  - [CS50 Web Programming](https://cs50.harvard.edu/web/2020/weeks/3/)
  - [Mozilla Developer Network (MDN) - Django tutorial](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django)

- SQLite
  - [Official SQLite Documentation](https://www.sqlite.org/docs.html)


<br>
<hr>

# Credits
- **Planning assistance** 
  - ChatGPT (GPT 3.5)
- **Development assistance** 
  - [![built with Codeium](https://codeium.com/badges/main)](https://codeium.com/badges/main)
  - **GitHub CoPilot**
- **Photos** 
  - *[Pexels](https://www.pexels.com)*
- **Art** 
  - *Bing Copilot Designer*

<br>

[Back To Contents](#contents)

<hr>
