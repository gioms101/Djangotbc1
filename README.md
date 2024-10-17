# # Django Project with Custom User, UserCard, and Admin Panel Customizations

This project extends Django's default `AbstractUser` model to include additional fields and custom admin interfaces. It includes models for managing users and user-related information, as well as a custom admin interface for managing products and categories.



## Features

1. **Custom User Model**:
   - The default Django user model is extended with additional fields such as:
     - `phone`: A phone number field with a maximum length of 15 characters.
     - `address`: An address field with a maximum length of 255 characters.

2. **UserCard Model**:
   - A `UserCard` model is defined with a one-to-one relationship with the `CustomUser`.
   - A signal (`post_save`) is used to automatically create a `UserCard` when a new `CustomUser` is created.

3. **Custom Admin for Products and Categories**:
   - Admin interfaces are defined for the `Product` and `Category` models with the following customizations:
     - `Product` Admin:
       - `list_display`: Displays `name`, `price`, `quantity`, and `image` in the admin list.
       - `list_filter`: Filters products based on `price` and `quantity`.
       - `search_fields`: Allows searching by `name`.
       - `list_editable`: Allows editing the `quantity` field directly from the list view.
     - `Category` Admin:
       - `list_display`: Displays `name` and `parent`.
       - `list_filter`: Filters categories based on the `parent` category.
       - `list_select_related`: Optimizes queries by using `select_related` for the `parent` field.
       - `search_fields`: Allows searching by `name`.

## Models

### `CustomUser`
- Extends Django's `AbstractUser`.
- Additional fields:
  - `phone`: `CharField`, optional.
  - `address`: `CharField`, optional.

### `UserCard`
- One-to-one relationship with the `CustomUser` model.

## Signals

- `create_user_card`: Automatically creates a `UserCard` instance when a new `CustomUser` is created.

## Admin Customizations

### Product Admin
- Manages products with enhanced filtering and editable fields.

### Category Admin
- Manages categories with `select_related` for optimizing database queries.





