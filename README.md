# Django E-commerce Application

This is a simple Django e-commerce application that features categories and product listings.


## Models

### Category Model

The `Category` model defines a hierarchical structure where each category can have a parent category. This is useful for organizing products into nested categories, such as "Electronics" -> "Mobile Phones" -> "Smartphones".

#### Fields:
- `name`: A `CharField` that stores the category name with a maximum length of 255 characters.
- `parent`: A `ForeignKey` to the `Category` model itself, allowing for nested categories. It can be blank or null for root categories.

#### Methods:
- `__str__()`: Returns the category name as a string representation.


### Product Model

The `Product` model represents an individual product and links it to one or more categories. It also supports uploading product images.

#### Fields:
- `name`: A CharField that stores the product name with a maximum length of 255 characters.
- `category`: A ManyToManyField that allows a product to be associated with multiple categories.
- `image`: An image field for product images, with a default image (default.png) if none is provided.
- `price`: A float field to store the price of the product.
- `quantity`: An integer field representing the available stock quantity.

#### Methods:
- `__str__()`: Returns the product name as a string representation.


## Views


### `Category View`

The `category` view fetches all parent categories (those without a parent category) and passes them to the template, along with their related products.

- `parent_categories`: This query fetches categories where the parent_id is None, meaning they are top-level or parent categories.
- `prefetch_related('product_set')`: Optimizes the database query by preloading all products related to each category, which avoids separate database queries for each product later. This makes fetching related products more efficient.
- Template: The view renders the `category.html` template, passing the list of parent categories with their products to the template context.




### `Product Listing View`

Lists all products in a given category, along with pagination and statistics for the products.

#### Template: product_listing.html

- Lists products based on category.
- Annotates products with `total_price` (price multiplied by quantity).
- Aggregates statistics such as the most expensive, cheapest, average, and total price.
- Implements pagination for product listings.

### Pagination
 
- Products are paginated in the `product_listing` view with 1 product per page (can be modified in the `Paginator` object).


### `Product Detailed Page View`

Displays detailed information about a specific product.


#### Template: product_detailed_page.html

- Fetches and displays detailed information about a specific product by its ID.


##  Requirements

To get this project up and running, make sure you have the following installed:

- Python 3.x
- Django 4.x (or later)





