from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Product

def read_products(request):
    product = Product.objects.all()
    return render(request, 'db_lab/db_product_table.html', {"products": product})

#create products
def create_product(request): 
    if request.method == "POST":
        p_name = request.POST.get('pname')
        p_price = request.POST.get('pprice')
        p_quantity = request.POST.get('pquantity')
        p_description = request.POST.get('pdescription')
    
        print("Saari values aa gy. Product banio!",{p_name})
                                    
        if p_name and p_price and p_quantity:
        # .create() khud hi database mein save kar deta hai
            new_product = Product.objects.create(name=p_name, price=p_price, quantity=p_quantity,description=p_description)
            print("Product successfully saved!")
        
    return render(request,'db_lab/create_product.html')

                   

        

#update Product
def update_product(request):
    return render(request,'db_lab/update_product.html')


#Delete Products
def delete_product(request):
    return render(request,'db_lab/delete_product.html')

