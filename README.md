# Restaurant Management System

A comprehensive restaurant management system built with Python, Streamlit, and MySQL that allows customers to browse restaurants, view menus, place orders, and manage their cart.

## Features

- Customer registration and management
- Restaurant browsing with images
- Menu item display and selection
- Shopping cart functionality
- Bill generation
- Database triggers for price updates
- Stored procedures for common operations

## Prerequisites

- Python 3.x
- MySQL Server
- Required Python packages:
  - streamlit
  - mysql-connector-python
  - python-dotenv
  - MySQLdb

## Setup

1. Clone the repository
2. Create a `.env` file with the following variables:
   ```
   DB_HOST=your_host
   DB_USER=your_username
   DB_PASSWORD=your_password
   DB_NAME=your_database_name
   ```
3. Install required packages:
   ```bash
   pip install -r requirements.txt
   ```
4. Set up the database:
   ```bash
   mysql -u your_username -p your_database_name < data.sql
   mysql -u your_username -p your_database_name < procedures.sql
   mysql -u your_username -p your_database_name < trigger_update_price_in_cart_info.sql
   mysql -u your_username -p your_database_name < trigger_update_price_in_cart_items.sql
   ```

## Running the Application

1. Start the Streamlit application:
   ```bash
   streamlit run main.py
   ```
2. Open your web browser and navigate to the provided local URL (typically http://localhost:8501)

## Database Structure

The system uses a MySQL database with the following main tables:
- customer
- restaurants
- menu_items
- cart_info
- cart_items
- bill

## Features in Detail

### Customer Management
- Registration with name, contact number, address, and email
- Automatic cart creation for new customers

### Restaurant Selection
- Browse available restaurants with images
- Select a restaurant to view its menu

### Menu and Ordering
- View restaurant menu items
- Add items to cart
- Update quantities
- Remove items from cart

### Cart Management
- View cart contents
- Update item quantities
- Remove items
- Automatic price updates

### Billing
- Generate bills for orders
- View order history
- Remove items from bill

## Database Triggers and Procedures

The system includes several database triggers and stored procedures for:
- Automatic price updates in cart
- Cart total calculations
- Bill generation
- Data validation