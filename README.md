# Inventory Management System (Django)

This project is a robust web application built with Django for managing inventory items, tracking stock levels, and facilitating efficient order processing.

## Table of Contents
- [Installation](#installation)
- [Database Setup](#database-setup)
- [Key Features](#key-features)
- [Contributing](#contributing)
- [Contact](#contact)

## Installation

1. **Prerequisites**
   - **Python:** Ensure you have Python 3.x installed. [Download here](https://www.python.org/downloads/).

2. **Set Up Virtual Environment**
   ```bash
   python -m venv myvenv
   myvenv\Scripts\activate  # On Windows
   source myvenv/bin/activate  # On macOS/Linux
   ```

3. **Clone the Repository**
   ```bash
   git clone https://github.com/isrealanteneh/Brainwave_Matriex_Inter_2.git
   cd Brainwave_Matriex_Inter_2/
   ```

4. **Install Django**
   ```bash
   pip install django
   ```

5. **Install Required Libraries**
   ```bash
   pip install -r requirements.txt
   ```

## Database Setup

### Database Configuration
Django uses SQLite by default, so no additional setup is required for local development. Your database file will be `db.sqlite3`.

### Run Migrations
This will create the initial database tables based on the project's database models.
```bash
python manage.py migrate
```

### Start the Development Server
```bash
python manage.py runserver
```
The development server will start at [http://127.0.0.1:8000/](http://127.0.0.1:8000/). Visit this URL to access the home page, which includes login and signup options.

### Login Credentials
A superuser is automatically created when the program runs:
- **Admin Username:** admin
- **Admin Password:** @20Admins

You can also create a new user by signing up.

## Key Features
- **Product Management:** Add, edit, and delete product information (name, amount, price, etc.).
- **Order Processing:** Create, manage, and track orders, including order status updates.
- **Sales Processing:** View sold items.
- **Reporting:** Generate reports on inventory levels, sales trends, and other key metrics.
- **User Management:** Provide limited access to users based on their roles.
- **User Authentication:** Secure user accounts for managing inventory data.
- **Data Validation:** Validate user inputs during signup.

## Contributing
Contributions are welcome! Please follow these steps:
1. Fork this repository.
2. Create a new branch for your feature or bug fix.
3. Commit your changes.
4. Push to your branch.
5. Open a pull request against the main branch.

## Contact
- **Email:** [Israel Anteneh](mailto:israleanteneh@gmail.com)
- **LinkedIn:** [Israel Anteneh](https://www.linkedin.com/mwlite/profile/in/israelanteneh)