# E-commerce Django Application

This project is a simple e-commerce application built with Django. It allows users to browse products, filter them by categories and tags, and add them to their cart or delete an order. The project also includes pagination and sorting features for products.

## Features

- **Main Page**: Displays a paginated list of products.
- **Category Page**: Allows filtering products by categories, price, and tags.
- **Search Functionality**: Enables searching for products by name.
- **Sorting**: Products can be sorted by `Price` and `Quantity` field.
- **Cart**: Users can add products to their shopping cart.
- **Contact Page**: Simple contact page.


## URL Patterns

- `/` : Main page showing all products.
- `/category/` : Category page showing all the product.
- `/category/<slug:slug>` : Category page with products filtered by category.
- `/order/cart` : Showing selected items of cart.

## Models

- **Product**: Represents a product in the store.
- **ProductTag**: Represents tags that can be assigned to products.
- **Category**: Represents a product category.
- **CartItem**: Represents an item in the user's cart. Linked to a `UserCard` model.

### `UserCard`
- One-to-one relationship with the `CustomUser` model.

## Custom Template Tags
Custom template tags are used to modify data in templates. In this project, we have a `cut` filter to replace parts of a string.

## Context Processors
Context processors make specific variables available in all templates without explicitly passing them in views. In this project, we have two context processors:

- Product Count: Returns the count of products in the current user's cart.
- Parent Categories: Retrieves all top-level categories.

## Custom Model Manager
We have a custom `ProductManager` that overrides Django's default `Manager` to include a method for prefetching related fields (category and tags) in product queries to optimize database queries.

## Views

### Main Page:
Displays the main page with a paginated list of products. Products are fetched using a custom `join_related_tables` method in the `ProductManager`.

### Category Page:
Handles the category view, including filtering by categories, price range, tags, search functionality, and sorting.

### Contact Page:
A simple contact page view.

## Pagination
Pagination is implemented on both the main page and the category page to display products in batches.

## Filtering & Sorting
Products can be filtered by category, price range, and tags, and sorted based on user selection.

# Templates
The views render the following templates:

- index.html: The main page.
- shop.html: The category page showing all the products.
- contact.html: A contact form for user inquiries.
- cart.html: Added items to the cart.
# HTML Fragments

- category_fragment.html: Displays a list of categories with the number of products in each category.
- scroll_products_fragment.html: Displays products with a similar structure to products-fragment.html, optimized for a scrollable layout.
- products-fragment.html: Displays all products with their image, name, price, and category.



