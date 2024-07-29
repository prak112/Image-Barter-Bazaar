# GOAL
 To evolve/advance the current application to a Single-Page Application (SPA) using Javascript and React.

# REASON
- Key features of an SPA include :
    - No page refresh on page change
    - Fast, as most resources (HTML/CSS/Scripts) are only loaded once
    - Great user experience as there are no page reloads
    - More responsive, with a desktop-app-like behavior.

  - Current application works successfully at a fundamental level. However, refactoring the codebase to translate into an SPA using `ReactJS` the application will include :
    - Single-page UI (no multiple tabs redirecting)
    - Faster response rate
    - On-screen notifications for User actions (ex. "Item added!", "Order placed.")
    - Items availability update in "Products" section (ex. "Out of Stock" cannot be ordered but redirected to possible matches)

<br>
<hr>

# Features In Progress
- The following features are updated not neccessarily in sequence.
- Currently learning Javascript, hence would start updating from [Client-side interaction](#client-side-interaction)



## Real-time Updates (WebSockets)
- [ ] WebSocket Basics: Understand WebSocket communication using Django Channels .
- [ ] Implement Real-Time: Add real-time features like instant cart updates.
- Resources: [WebSocket Tutorials](https://www.geeksforgeeks.org/django-channels-introduction-and-basic-setup/), Django Channels documentation.

## User Authorization and Permissions
- [X] Authorization: Implement user roles (e.g., admin, customer).
- [ ] Permission Control: Set up authorization for views and API endpoints.
- Resources: Django authorization documentation.

## Database Optimization and Transactions
- [X] SQL Skills: Deepen your SQL knowledge for database queries.
- [ ] Transactions: Learn about database transactions and ACID properties.
- [ ] Database Optimization: Optimize database queries for performance.
- Resources: SQL tutorials, SQL optimization guides.

## Client-side interaction 
### Fundamental Javascript
- [X] JavaScript Fundamentals: Start learning JavaScript from scratch (Vanilla JS).
- [X] Interactive Features: Enhance your product pages with basic interactivity.
- Resources: MDN JavaScript guide, JavaScript.info, freeCodeCamp's JavaScript curriculum.

### Advanced JavaScript
- [X] Dynamic Content: Use JavaScript to load products dynamically.
- [X] Event Handling: Implement user interactions like adding products to the cart.
- [X] Implement Complex Features: Enhance user experience with advanced JS features.
- Resources: freeCodeCamp JavaScript tutorials, MDN web APIs.

## Django REST Framework
- [ ] API Development: Learn to build RESTful APIs with Django REST Framework.
- [ ] API Endpoints: Create API endpoints for product data.
- Resources: Django REST Framework documentation, DRF tutorials.

## Testing and Deployment
- [ ] Testing: Write unit and integration tests for your application.
- [ ] Deployment: Deploy your Django application to a hosting platform (e.g., pythonanywhere).
- Resources: Django testing documentation, deployment guides.


<br>
<hr>

> [Back To README](/README.md) | [Back To PROCESS_FLOWS](/docs/PROCESS_FLOWS.md)