   # Inventory Management System (Django) 
   
   This project is a robust web application built with Django for managing inventory items, tracking stock levels, and facilitating efficient order processing.
   
   ## Installation 
       
•  **Python:** Ensure you have Python 3.x installed. 
      [Download](https://www.python.org/downloads/) if needed.
      
  
   **Create a virtual environment:**
    ``` python -m venv myvenv ```
    ``` myvenv/Scripts/activate```
  
  ** clone the repository: ** 
  ``` git clone https://github.com/isrealanteneh/Brainwave_Matriex_Inter_2.git ```
  ** go to project directory: **
  ``` cd Brainwave_Matriex_Inter_2/ ```
  
•  **Django:** Install Django using pip:
    ```pip install django ```
   
   ** Install all required modules libraries :**
   ``` pip install -r requirements.txt ```
   
   ### Database Setup
   **Database Setup**
        SQLite: Django uses SQLite by default, so no additional setup is required for local development. Your    database file will be  **db.sqlite3**.
    
    **Run migrations**
      This will create the initial database tables based on the projects database models.
      ```python manage.py migrate ```
      
    **Start the Development Server:**
    ``` python manage.py runserver   ```
    
    This will start the development server on http://127.0.0.1:8000/.
    * head over to this url and get the home page that has login and sign up.
    - [home page](http://127.0.0.1.8000/store)
    
    **Login credientials:**
    
    super user are automatically created as the program run
    
    1. this user have admin roles 
    - Admin username = admin
    - Admin password = @20Admins
  
   or you can create new user by signing up

   #### Key Features
    -  Product Management: Add, edit, and delete product information (name, amount, price, etc.).
    -  Order Processing: Create, manage, and track orders, including order status updates. 
    -  Sales Processing: view sold items. 
    -  Reporting: Generate reports on inventory levels, sales trends, and other key metrics.
    -  Manage users : give limited access to users based on their role.
    -  User Authentication: Secure user accounts for managing inventory data
    -  Data validations : Validate data in signing up check for user inputs and validate
    
    
   ###### Contributing 
   Contributions are welcome! Please follow these steps:

    1. Fork this repository.
    2. Create a new branch for your feature or bug fix.
    3. Commit your changes.
    4. Push to your branch.
    5. Open a pull request against the main branch.

   ## Contact
    - Email - [Israel Anteneh](israleanteneh@gmail.com)
    - Linkedin  - [Israel Anteneh](https://www.linkedin.com/mwlite/profile/in/israelanteneh)

