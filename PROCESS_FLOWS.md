# Database Schema
- Database (SQLite) is implemented as an in-built version for Django
- Django Models are defined using the framework (`models.py`) for each of the apps defined (`users`, `photostore`)  to emulate tables similar to SQL
- After defining the required models the changes are updated through 'Migrations', which translate the instructions in `models.py` to the database to create/update tables
- Database schema (below) defines the logical flow of data through the application backend

![Database Schema](/design/DATABASE-SCHEMA.png)


<br>
<hr>

# Workflow
```mermaid
flowchart TD

subgraph USERS
    subgraph EXTERNAL
        Z(Unregistered User)
    end
    subgraph INTERNAL
        Z1(SIGNUP)
        A(Registered User)
        B(Authentication)
        C(Authorization)
        J(Verified User)
        K(Customer Profile)
    end
end


subgraph CHECKOUT
    L(Payment Gateway)
end

subgraph ORDERS
    M(Order History)
end


subgraph PLATFORM
    subgraph HOME
        D(Home)
    end
    subgraph SEARCH
        E(Search)
        F(Search Results)
    end
    subgraph PRODUCT
      G(Cart)
      H(Inventory)
    end    
    USERS -->|All Users can search by keywords, filters| SEARCH
    EXTERNAL<-->|Non-User redirected to SIGNUP| PRODUCT
    EXTERNAL ---> Z1

    Z1-->|User registers| A
    A -->|User Logs In| B
    B -->|Authenticated User verified| C
    C -->|System grants access to Authorized User| J
    J -->|Verified User has full access - Home, all sub-modules| HOME

    E --> F
    F -->|Customer adds items to Cart| PRODUCT
    G <-->|Backend Adds/Removes items| H
    J -->|Customer can edit profile| K
    HOME -->|Customer adds items to Cart or Checkout| PRODUCT
    PRODUCT -->|Customer pays with image| CHECKOUT
    CHECKOUT -->|Image payment added to Inventory| PRODUCT
    CHECKOUT -->|Successful payment saves Customer Order & exchanged image| ORDERS

end

```
<br>
<hr>

> [Back To README](/README.md) | [Back To ADD-ONS](/ADD-ONS.md)