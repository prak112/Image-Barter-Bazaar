# Overview
- [Design](#design)
- [Frontend & Backend](#frontend--backend)
- [Functionality](#functionality)

<br>
<hr>

# DESIGN
- [X] User interface must be practical and arranged appropriately for the entire screen 
- [X] Look for inspiration online from various existing online stores. 
- [X] The target screen size is 1920 × 1080, but the page must also look good on larger screens. No need to make less than 1920x1080 or mobile view.
- [X] Customise Django Admin functionality through Backend
- [ ] Customise Django Admin layout and styles


<br>
<hr>

# FRONTEND & BACKEND

1. [X] Header and footer on each page
Header:
   - [X] Logo/image
   - [X] Search field for products
   - [X] Navigation (links in the navigation, which allows you to navigate the page)
   - [X] Log in/log out button (not the correct login)
   - [X] Link to the shopping cart
Footer
   - [X] Generate footer content

2. [X] Front page
   - [X]Show 5 pages random product

3. [X] Search page
   - [X] List the products based on the user's search

4. [X] Product page (the page can be accessed either through the product on the front page or the product on the search page)
   - [X] Details of a certain product
   - [X] Can add the product to the shopping cart

5. [X] Shopping cart
   - [X] Shows the products added to the shopping cart
   - [X] The user fills in their own information (name, email, address) / User logs in before adding items to cart
   - [X] Sends the order (not yet a real order, the information is only sent to the server)

6. [X] Order confirmation page
   -[X] After the order, the user will be notified of the order's success.

<br>
<hr>

# FUNCTIONALITY

Technical implementation requirements of the Web service (Ready around week 3) :

1. [X] Adding a customer registration page where the user can create an account on the site.

2. [X] Logging in on the site is done in real and data secure manner.

3. [X] Customer:
   - [ ] When the customer is logged in to the site, he has a page where he can edit his own information (link in the Header section.)
   - [X] If the user is logged in, his information is filled in directly in the shopping cart.

4. [X] Admin pages: (the styling of the pages can be simpler, but still practical)
   - [X] Only admin users can access the pages
   - [X] Admin front page with links to listings of products, users and orders
   - [X] Added CRUD operations (Create, Read, Update and Delete) for products, for users and orders.


<br>
<hr>