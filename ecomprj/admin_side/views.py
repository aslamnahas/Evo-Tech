from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from core.models import Customer
from core.models import Main_Category , Product
from django.shortcuts import get_object_or_404



def admin_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to dashboard upon successful login
            return redirect('dashboard')  # Assuming 'admin_dashboard' is the name of the URL pattern for the dashboard
        else:
            # Handle invalid login credentials
            messages.error(request, 'Invalid username or password.')
    # Render the login form
    return render(request,'adminside/adminlogin.html')


# def users(request):

#     return render(request,'adminside/users.html')

# @login_required
def dashboard(request):
    # Set session data
    request.session['user_id'] = request.user.id
    request.session['username'] = request.user.username
    return render(request,'adminside/dashboard.html')


def users(request):
     users = Customer.objects.all()
     context = {
            'users':users,
        }
     return render(request,'adminside/users.html',context)


def user_block(request, user_id):
    user = get_object_or_404(Customer, id=user_id)
    user.is_blocked = not user.is_blocked  # Toggle the block status
    user.save()
    return redirect('adminside:users')


def main_category(request):
    data = Main_Category.objects.all().order_by('id')
    return render(request, "adminside/categories.html", {"data": data})

def add_main_category(request):
    if request.method == 'POST':
        # print("rewussssssssssssssssss post")
        main_category_name = request.POST.get('main_category_name')
        description = request.POST.get('description')
        offer = request.POST.get('offer')
        image = request.FILES.get('image')
        delete = request.POST.get('delete', False) == 'True'
        
        # Check if the category name already exists
        if Main_Category.objects.filter(name=main_category_name).exists():
            messages.error(request, "Category already exists.")
            return redirect('adminside:add_categories')  # Redirect to the add category page
            
        # Save data to the database
        main_category = Main_Category(
            name=main_category_name,
            descriptions=description,
            offer=offer,
            img=image,
            deleted=delete
        )
        main_category.save()
        messages.success(request, "Category added successfully.")
        return redirect('adminside:categories')  # Redirect to the main category page
    return render(request, 'adminside/add_categories.html')






#update_categories

def update_main_category(request, id):
    data = Main_Category.objects.get(id=id)

    if request.method      == 'POST':
        main_category_name = request.POST['main_category_name']
        description        = request.POST['description']
        offer              = request.POST['offer']

        # Retrieve existing data
        edit = Main_Category.objects.get(id=id)

        # Update fields
        if Main_Category.objects.filter(name = main_category_name).exclude(id=id).exists():
            messages.error(request, "Category is already exists.")
            return render(request,'adminside/update_main_categories.html',{"data": data})

            
        edit.name = main_category_name
        edit.descriptions = description 
        edit.offer = offer

        if 'image' in request.FILES:
            image = request.FILES['image']
            edit.img = image
        
        # Save updated data
        edit.save()

        return redirect('adminside:categories')

    return render(request,'adminside/update_main_categories.html',{"data": data})







def soft_delete_category(request, id):
    data = Main_Category.objects.get(id=id)

    data.deleted = not data.deleted
    data.save()

    return redirect('adminside:categories')



#delete categories



def delete_main_category(request,id):
    data = Main_Category.objects.get(id=id) 
    data.delete()  
    return redirect('adminside:categories')






# product============================================================================================================
                                # add --- update ---- delete ---soft delete--


def products(request):
    items = Product.objects.all().order_by('-id')
    return render(request, 'adminside/products.html', {"items": items})




def add_product(request):
    data = Main_Category.objects.all()  

    if request.method == 'POST':
        # Extract data from the POST request
        model = request.POST['model']
        description = request.POST['description']
        color = request.POST['color']
        display_size = request.POST['display_size']
        camera = request.POST.get('camera', '')  # Get camera data or empty string if not provided
        battery = request.POST.get('battery', '')  # Get battery data or empty string if not provided
        network = request.POST.get('network', False) == 'true'
        smart = request.POST.get('smart', False) == 'true'
        image = request.FILES.get('image')
        main_category_id = request.POST.get('main_category_id')  

        # Retrieve the main category object
        main_cat = Main_Category.objects.get(id=main_category_id)

        # Create a new Product object
        new_product = Product(
            main_category=main_cat,
            model=model,
            description=description,
            color=color,
            display_size=display_size,
            camera=camera,
            battery=battery,
            network=network,
            smart=smart,
            image=image
        )

        # Save the new product to the database
        new_product.save()

        # Handle multiple images (processing not shown in this example)

        # Redirect to the products view
        return redirect('adminside:products')

    return render(request, 'adminside/add_product.html', {'data': data})




#update product