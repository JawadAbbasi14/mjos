from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Product

def read_products(request):
    products = Product.objects.all()
    return render(request, 'db_lab/db_product_table.html', {"products": products})

def create_product(request): 
    if request.method == "POST":
        p_name = request.POST.get('pname')
        p_price = request.POST.get('pprice')
        p_quantity = request.POST.get('pquantity')
        p_description = request.POST.get('pdescription')
        
        if p_name and p_price and p_quantity:
            Product.objects.create(
                name=p_name, 
                price=p_price, 
                quantity=p_quantity, 
                description=p_description
            )
            return redirect('db_home')  # ✅ Create ke baad redirect karo
            
    return render(request, 'db_lab/create_product.html')

def update_product(request, product_id):
    product = Product.objects.get(id=product_id)

    if request.method == "POST":
        product.name = request.POST.get('pname')
        product.price = request.POST.get('pprice')
        product.quantity = request.POST.get('pquantity')
        product.description = request.POST.get('pdescription')
        product.save()
        return redirect('db_home')

    return render(request, 'db_lab/update_product.html', {'product': product})

def delete_product(request, product_id):
    product = Product.objects.get(id=product_id)  # ✅ URL se mila hua ID use karo
    product.delete()
    return redirect('db_home')  # ✅ Redirect karo, render nahi