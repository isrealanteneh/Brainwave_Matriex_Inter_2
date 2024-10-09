from django.shortcuts import render, redirect ,get_object_or_404,HttpResponse
from django.contrib.auth import authenticate , login ,logout
from .forms import UserCreationForm ,ProductForm ,LoginForm,MangegerForm,OrderForm,MangegerOrderForm
from django.contrib import messages
from .models import Product, StoreUser , User, Order, Sale, StoreReport
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import re
import random


# Create your views here.

# this is home page or landing page 
def home_link_view(request):
    return render(request,'home.html')


# this function copy all users from user table to StoreUser table
def copy_user_record(model1,model2): #called when a new user added to auth_user table
    admin_users_length = len(model1.objects.all())
    store_users_length = len(model2.objects.all())
    untracked_users =  admin_users_length - store_users_length
    if untracked_users > 0:
        last_records = User.objects.order_by('-id')[:untracked_users] # order users by reverse then and get last recorde. getting users added lastly and add to storeuser table
        for user in last_records:
            user_id = user.id
            role = "staff"
            store_user = StoreUser(user_id=user_id, user=user,role=role)
            try:
                store_user.save()
                print("new record saved successfully")
            except Exception as e:
                print("Error saving new record" )
    else:
        print("No user to Copy from User model to StoreUser model")

# generate a unique color for each users
def generate_random_color():
    r = lambda: random.randint(0,255)
    color = f'#{r():02x}{r():02x}{r():02x}'
    return color

account_color = generate_random_color() # this is applied to account avator in users side bar


################################ functions focus on processing ORDERS  ##################################

# used to view products to make orders 
def make_order_view(request):
    items = Product.objects.all()
    context = {
        "items":items,
        "color":account_color,
    }
    return render(request,"orders/createorder.html", context)

# render a from template to make orders
def make_order(request, pk):
    if request.user.is_authenticated:
            order_item = get_object_or_404(Product, id=pk)
            form = OrderForm(instance=order_item) #prepopulate the form with the selected product
            context = {
            "form": form,
            "pk": pk,
            "color":account_color,

            }
            return render(request, 'orders/orderform.html', context)
    return render(request, 'home.html')
    
def saved_orders(request,pk):
    if request.user.is_authenticated:
        product = get_object_or_404(Product,id=pk)
        item_amount = product.amount # amount in the store
        if request.method == 'POST':
            form = OrderForm(request.POST, instance=product)
            if form.is_valid():
                new_amount = request.POST.get('amount')
                shipping_address = request.POST.get("shipping_address")
                # order amount alwayes must be less than the amount in the store
                if int(new_amount) < item_amount and int(new_amount) > 0:
                    total_price = product.unit_price * int(new_amount)   # calculate the total price for the new order  
                    current_item_amount = item_amount - int(new_amount) # each time new order created the amount in the store decrease
                    new_order = Order(product=product, name=product.name, total_price=total_price, amount=new_amount, shipping_address=shipping_address)
                    product.amount = current_item_amount                    
                    product.save(update_fields=['amount']) # update only amount field in Product model with update_fields attribute
                    new_order.save()  # save the newly created order 
                    return redirect("view_saved_order")
                else:
                    messages.error(request, "Order qunatity must be less than the quantity in the store! .")
                    return redirect("make_order_view")
    return render(request, 'home.html')

# viewing orders
def view_saved_order(request):   
    is_stuff = check_user_role(request) # check for users helps to give permission to access  
    orders =Order.objects.all()
    has_order = False # to know if their is order in the list
    if len(orders) > 0:
        has_order = True     
    context = {
        "orders": orders,
        "color":account_color,
        "has_order": has_order,
        "is_stuff": is_stuff
        
    }
    return render(request,"orders/savedorder.html",context)

canceled_order = 0 # used to count canceled order 

def manage_order(request):
    is_stuff = check_user_role(request) # this function return bool value.  This can check user is stuff or not
    form = MangegerOrderForm()
    orders = Order.objects.all()
    if request.method == "POST":
        form = MangegerOrderForm(request.POST)
        new_status = request.POST.getlist('status') # get the list of order status weather it fulfiled or canceled
        if form.is_valid():
            for i in range(len(orders)):
                if new_status[i] == "fulfilled":  #move this order to sales table and delete the order from order table
                    sold_order = Sale(name=orders[i].name, price=orders[i].total_price,customer_address=orders[i].shipping_address) # adding fulfiled order to sales table with those fields
                    sold_order.save()
                    orders[i].delete()                    
                    messages.success(request,"Order was successfully fulfiled")
                    return redirect("view_sales")                   
                elif new_status[i] == "canceled":
                    canceled_order += 1
                    revert_amount = orders[i].amount # canceled amount
                    current_amount = orders[i].product.amount # current amount in the store 
                    total_revert_amount = current_amount + revert_amount # total amount in the store
                    product_id = orders[i].product.id
                    product = get_object_or_404(Product, id=product_id)
                    product.amount = total_revert_amount # update the current amount in the store
                    product.save(update_fields=['amount']) # get back the order amount into product amount and remove this order
                    orders[i].delete() # remove it from the order model
                    messages.success(request,"Order was successfully canceled")
                    return redirect("view_saved_order")                   
                if orders[i].status != new_status[i]: #check if the current status is different
                    orders[i].status = new_status[i] # and apply the new status accordingly
                    orders[i].save()
                    messages.success(request,"Order was successfully created")
                    return redirect("view_saved_order")  
    has_order = False
    if len(orders) > 0:
        has_order = True                 
    context = {
        "form": form,
        "orders":orders,
        "color":account_color, # giving random color for each users in their avator
        "is_stuff":is_stuff, # to know the user role weather stuff , manager or admin
        "has_order":has_order, # to know if their is order or no order

    }    
    return render(request,"orders/orderstatus.html", context)



################################ functions focus on processing USERS  ##################################
# create new user 

def signup_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST) # find all data the user send to validate
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        user_name = request.POST.get("username")
        password = request.POST.get("password")
        is_correct = True # assuming user data is correct and give True value
        if not re.match(r"^[A-Za-z' -]+$", first_name): # validate all data before creating a new user
            messages.error(request, "First name can only contain letters, hyphens, and apostrophes.")
            is_correct = False # if the user data doesnt pass the validation flag will be false
        if not re.match(r"^[A-Za-z' -]+$", last_name):
            messages.error(request, "Last name can only contain letters, hyphens, and apostrophes.")
            is_correct = False

        if not re.match(r"^[A-Za-z0-9][A-Za-z0-9._]{1,29}[A-Za-z0-9]$", user_name):
            messages.error(request, "Username must be 3-30 characters long and can include letters, numbers, underscores, and dots.")
            is_correct = False
        if len(password) < 8:
            messages.error(request, "Password must be at least 8 characters long.")
            is_correct = False
        if not re.search(r'[A-Z]', password) or not re.search(r'[a-z]', password) or not re.search(r'\d', password) or not re.search(r'[@$!%*?&]', password):
            messages.error(request, "Password must include at least one uppercase letter, one lowercase letter, one number, and one special character.")
            is_correct = False
        if is_correct: # if all validation passes  then the user can create new account
            if form.is_valid():
                form.save()
                copy_user_record(User,StoreUser)
                return redirect('login_user') # then redirect the new user to login page
    form = UserCreationForm()
    return render(request, 'signup.html', {'form':form})


# logout the user
def logout_view(request):
    logout(request)
    return redirect("home_link_view")

# used to check and authenticate user
def login_user(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST) # get login form data
        if form.is_valid():    
                username = form.cleaned_data.get('username') # find username from form data
                password = form.cleaned_data.get('password') # find password from from data
                user = authenticate(username=username,password=password) # authenticate user using django built in authentication functionality
                if user is not None: #check if user is exist
                    storeuser = get_object_or_404(StoreUser,user_id=user.id) # get the user from store users model
                    if storeuser.user_status == 'active': # and check if user is active or not only actvie users can logged in
                        login(request,user)
                        return redirect('view_inventory') #if logging in is successfull redirect to a page that has all products list 
                    else:
                        messages.error(request, 'Sorry you can not Login ')                                    
        else:
            messages.error(request, 'Invalid username or password')
    form = LoginForm()
    return render(request, 'login.html',{'form':form}) #if thire is error in logging in rerender the page again


# view all store users this function give only viewing access 
def view_user(request):
    store_users = StoreUser.objects.all()
    is_stuff = check_user_role(request)
    context = {
        "storeusers":store_users,
        "color":account_color,
        "is_stuff":is_stuff
    }    
    return render(request,"viewuser.html", context)

# check if the user is weather stuff or not and return a boolean. this function is reuseable
def check_user_role(request):
    user_id = request.user.id
    user = StoreUser.objects.get(user_id=user_id) # users role are stored in storeUsers model
    is_stuff = True
    if user.role == "admin" or user.role =="manager":
        is_stuff = False   
    return is_stuff
 
def manage_user(request): 
    form = MangegerForm()
    store_users = StoreUser.objects.all()
    if request.method == "POST":
        form = MangegerForm(request.POST)
        new_roles = request.POST.getlist('role') # get the list of role form all users as a list to compare with the new roles
        new_status = request.POST.getlist('user_status') # get the list of user status as a list to compare with the new status
        if form.is_valid():
            for i in range(len(store_users)):
                if store_users[i].role != new_roles[i]: # if there is a change track and save it # track the changes in edit role field and save the new role
                    store_users[i].role = new_roles[i] # get the changes and update the existing role
                    store_users[i].save()
                    return redirect("view_user")                   
                if store_users[i].user_status != new_status[i]: # track the changes in edit status field and save the new status
                    store_users[i].user_status = new_status[i] # get the changes and update the existing role
                    store_users[i].save()
                    return redirect("view_user")                   
    context = {
        "form": form,
        "storeusers":store_users,
        "color":account_color,
        "is_stuff":check_user_role(request),
    }    
    return render(request,"manager.html", context)



################################ functions focus on processing SALES ##################################

def view_sales(request):
    sold_items = Sale.objects.all()
    context = {
                "sales":sold_items,
                "color":account_color,
        }
    return render(request,"sales/solditems.html",context)



################################ functions focus on processing CRUDS ##################################

# view all items in inventory
def view_inventory(request):    
    if request.user.is_authenticated:
        product =  []
        items = Product.objects.all() # data called from db once to increase performance
        for item in items:
            product.append({ #appending models fields to product list
                "id":item.id,
                "name":item.name,
                "amount":item.amount,
                "unit_price":item.unit_price,
                "unit_of_measure":item.unit_of_measure,
                "catagoires":item.catagoires,
                })         
        if request.method == "POST":
            selected_categorie = request.POST['selected_option'] # getting the selected option from request
            if selected_categorie: 
                new_product_list = [item for item in product if item['catagoires'] == selected_categorie] #getting the selected category item form product list and add to new list
                product =  []
                product = new_product_list.copy()  # copy the new list filterd by category to product list
        has_items = False
        if len(product) > 0:
            has_items = True
        context = {
                "items":product,
                "user":request.user,
                "color":account_color,
                "has_items":has_items,
                "is_stuff":check_user_role(request),
        }
        return render(request,'view.html', context)
    return render(request, 'home.html')

# add new product
def create_inventory(request):
    if request.user.is_authenticated:
        form = ProductForm()
        if request.method == 'POST':
            form = ProductForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request,"Product was successfully created")
                return redirect("view_inventory")
        return render(request,'additem.html',{"form":form,"color":account_color})
    return render(request, 'home.html')

# update or edit the existing product
def update_inventory(request, pk):
    if request.user.is_authenticated:
        update = get_object_or_404(Product, id=pk)
        form = ProductForm(instance=update)
        context = {
        "form":form,
        "pk":pk,
        "color":account_color,
        }
        return render(request, 'update.html', context)
    return render(request, 'home.html')

# save the changes made in update form
def save_changes(request ,pk):
    if request.user.is_authenticated:
        data = get_object_or_404(Product,id=pk)
        if request.method == 'POST':
            form = ProductForm(request.POST, instance=data)
            if form.is_valid():
                form.save()
                return redirect("view_inventory")
    return render(request, 'home.html')

#  delete selected product  
def delete_inventory(request, pk):
    if request.user.is_authenticated:
        data = get_object_or_404(Product, id=pk)
        data.delete()
        return redirect("view_inventory")
    return render(request, 'home.html')



################################ functions focus on generating REPORT ##################################
 
def generate_report(request):
    low_level_items = Product.objects.filter(amount__lt=10).count()  # getting low_stock_level_items
    sold_items = Sale.objects.all()  # getting sold items amount
    total_sold_price = sum(item.price for item in sold_items)
    sold_items_amount = sold_items.count()
    order_amount = Order.objects.all().count()
    canceled_orders = canceled_order
    report_data = StoreReport(low_stock_level_items=low_level_items,sold_items_amount=sold_items_amount,sold_items_price=total_sold_price,order_amount=order_amount,canceled_orders=canceled_orders)
    report_data.save()  
    # Save report data into StoreReport model
    report_data = StoreReport(
        low_stock_level_items=low_level_items,
        sold_items_amount=sold_items_amount,
        sold_items_price=total_sold_price,
        order_amount=order_amount,
        canceled_orders=canceled_orders
    )
    report_data.save()
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="Store report.pdf"'

    p = canvas.Canvas(response, pagesize=letter)
    width, height = letter
    y = height - 50 

    # Add Title
    p.setFont("Helvetica-Bold", 16)
    p.drawString(100, y, "Sales and Store Report")
    y -= 30  # Space after title

    # Add report details to the PDF
    p.setFont("Helvetica", 12)
    p.drawString(100, y, f"Low Stock Level Items: {low_level_items}")
    y -= 20
    p.drawString(100, y, f"Sold Items Amount: {sold_items_amount}")
    y -= 20
    p.drawString(100, y, f"Total Sold Price: {total_sold_price:.2f}")
    y -= 20
    p.drawString(100, y, f"Order Amount: {order_amount}")
    y -= 20
    p.drawString(100, y, f"Canceled Orders: {canceled_orders}")
    y -= 40

    # List all products
    products = Product.objects.all()
    for product in products:
        p.drawString(100, y, f"Product Name: {product.name}")
        p.drawString(100, y - 20, f"Amount: {product.amount}")
        y -= 40 
        if y < 50:  
            p.showPage()
            y = height - 50  
    # Add Summary at the bottom
    p.showPage()  # Start a new page for the summary
    p.setFont("Helvetica-Bold", 14)
    p.drawString(100, height - 50, "Summary")
    y = height - 80  
    
    p.setFont("Helvetica", 12)
    p.drawString(100, y, f"{low_level_items} products  are Low level items. ")
    y -= 20
    p.drawString(100, y, f"{sold_items_amount} products are sold in this week.")
    y -= 20
    p.drawString(100, y, f"Total Sales Revenue $:{total_sold_price:.2f}")
    y -= 20
    p.drawString(100, y, f"Total Orders: {order_amount}")
    y -= 20
    p.drawString(100, y, f"{canceled_orders} orders are canceled")

    p.showPage()
    p.save()

    return response