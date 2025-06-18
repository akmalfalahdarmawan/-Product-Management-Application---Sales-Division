!["Sales Division Product Management System Banner"](banner.jpeg)



# 📦 Product Management System - Sales Division


## 🧾 Project Definition
The Product Management System for the Sales Division is a text-based application designed to facilitate efficient product data management. This application helps the sales team easily monitor product information such as stock levels, expiration status, and the process of product inflow and outflow.

## 👥 Stakeholders
This application is intended for sales division personnel, particularly those responsible for inventory tracking, product coordination, and stock reporting. It is suitable for individuals or teams managing product availability and movement in retail or distribution settings.

## 🏢 Target Industry
This system is primarily designed for companies operating in the retail, wholesale, or distribution sectors, especially those requiring detailed tracking of product stock, expiry dates, and supply flow within a sales-focused environment.

## 🔍 Application Overview
The application is built with a text-based interface and allows users to:

- View product data in a structured table format.
- Search products by ID PRODUCT.
- Track and filter low stock items.
- Monitor upcoming or expired products.
- Add or remove products from inventory.
- Manage product inflow and outflow logs.

The program includes various submenus for each function and integrates validation checks to prevent incorrect user inputs.

🔄 Typical User Flow
This section describes how users typically interact with the system through its menu-based CLI:

1. Main Menu Access
Users are presented with a main menu to choose from:
- View Product List
- Search Product by ID
- Check Expired Product Status
- Filter Low Stock Products
- Delete Product from Inventory
- Exit the Application
2. Viewing Products
From the Product List submenu, users can:
- Display all products in a table
- Add incoming stock (with input validation and date checks)
- Record outgoing products with destination and description
3. Product Entry 
- If the entered product ID already exists, the system updates the stock.
- If the ID is new, it allows full product entry including expiry date, storage category, etc.
4. Product Output 
- Users input product ID and quantity to reduce stock.
- The destination and a note can be added, and the system logs the transaction.
5. Product Lookup 
- Users can search for a product by entering a 4-digit ID.
- If found, product details are displayed in a formatted view.
6. Expired Product Filter
- System checks which products are expired or will expire in the next 30 days.
- Users may add notes for each product status.
7. Low Stock Filter (Read)
- Products with stock below 10 units are listed for review.
8. Delete Product (Delete)
- Allows product removal from the inventory by confirming a 4-digit ID input.
9. Exit
- The program terminates gracefully with a closing animation.

## 🛠️ Technologies Used

ython 3.x
tabulate (for formatted tables)
datetime, os, sys (standard libraries)


## 📂 Project Structure

├── product_management.py      # Main application file
├── README.md                  # Project documentation
└── requirements.txt           # Dependencies

## 📦 Installation

To install required dependencies, run the following command:

```bash
pip install -r requirements.txt





