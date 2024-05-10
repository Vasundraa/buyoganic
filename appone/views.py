from django.shortcuts import render
from .models import Product,Productshop
from django.core.paginator import EmptyPage, Paginator

PRODUCTS_PER_PAGE = 2
# Create your views here.
def cg(request):
    return render(request,'about.html')

def cg1(request):
    return render(request,'cart.html')

def cg2(request):
    return render(request,'checkout.html')

def cg3(request):
    return render(request,'contact-us.html')

def cg4(request):
    return render(request,'gallery.html')

def cg5(request):
    products=Product.objects.all()
    return render(request,'index.html',{'products':products})

def cg6(request):
    return render(request,'my-account.html')

def cg7(request):
    return render(request,'shop-detail.html')

def cg8(request):
    productshop = Productshop.objects.all()
    #pagination
    page= request.GET.get('page',1)
    product_paginator = Paginator(productshop, PRODUCTS_PER_PAGE)
    try:
        productshop = product_paginator.page(page)
    except EmptyPage:
        productshop = product_paginator.page(product_paginator.num_pages)
    except:
        productshop = product_paginator.page(PRODUCTS_PER_PAGE)

    return render(request,'shop.html',{'productshop':productshop, 'page_obj':productshop, 'is_paginated':True, 'paginator':product_paginator})

def cg9(request):
    return render(request,'wishlist.html')

def cg10(request):
    return render(request,'login.html')

def cg11(request):
    return render(request,'s1.html')

def cg12(request):
    return render(request,'s2.html')

def cg13(request):
    return render(request,'s3.html')