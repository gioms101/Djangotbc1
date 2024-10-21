# E-commerce Django Application

This is a Django-based e-commerce application with basic functionality, including product listing, category filtering, cart management, and checkout.

## Features

- **Main Page**: Displays a list of all products, prefetching related categories for performance optimization.
- **Category Page**: Displays products filtered by category, with a list of all categories preloaded.
- **Shop Detail Page**: Displays detailed information about a specific product, with the option to load the product by a slug or the first product if no slug is provided.
- **Cart Page**: Displays the user's shopping cart.
- **Checkout Page**: Provides the checkout functionality.
- **Contact Page**: A simple contact form.

## URL Patterns

- `/` : Main page showing all products.
- `/category/` : Category page showing all the product.
- `/category/<slug:slug>` : Category page with products filtered by category.
- `/product/` : Shop detail page with the first product.
- `/product/<slug:slug>` : Shop detail page with the product specified by the slug.
- `/order/cart` : Cart page displaying the user's cart.
- `/order/checkout` : Checkout page for order completion.
- `/contact/` : Contact page for reaching out to support.

## Models

- **Product**: Represents a product in the store.
- **Category**: Represents a product category.
- **CartItem**: Represents an item in the user's cart. Linked to a `UserCard` model.

### `UserCard`
- One-to-one relationship with the `CustomUser` model.

# Templates
The views render the following templates:

- index.html: The main page.
- shop.html: The category page showing all the products.
- shop-detail.html: The detail page for an individual product.
- cart.html: Displays the user's shopping cart.
- checkout.html: Provides the checkout interface.
- contact.html: A contact form for user inquiries.

# HTML Fragments

- category_fragment.html: Displays a list of categories with the number of products in each category.
- featured_products_fragment.html: Displays up to three featured products with their image, name, and price.
- scroll_products_fragment.html: Displays products with a similar structure to products-fragment.html, optimized for a scrollable layout.
- products-fragment.html: Displays all products with their image, name, price, and category.



