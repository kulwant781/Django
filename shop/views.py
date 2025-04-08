from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from .models import Product, Form, Coupon, Orders
from django.core.mail import send_mail
from math import ceil
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
# from django.db import connection

# Create your views here.

# def home(request):
#     # products = Product.objects.all()
#     # print(products)
#     # n = len(products)
#     # nSlides = n//4 + ceil((n/4)-(n//4))

#     allProds = []
#     catprods = Product.objects.values('category', 'id')
#     cats = {item['category'] for item in catprods}
#     for cat in cats:
#         prod = Product.objects.filter(category=cat)
#         n = len(prod)
#         nSlides = n // 4 + ceil((n / 4) - (n // 4))
#         allProds.append([prod, range(1, nSlides), nSlides])

#     # params = {'no_of_slides':nSlides, 'range': range(1,nSlides),'product': products}
#     # allProds = [[products, range(1, nSlides), nSlides],
#     #             [products, range(1, nSlides), nSlides]]
#     params = {'allProds':allProds}
#     return render(request, 'shop/index.html', params)

def home(request):
    allProds = []
    
    # Fetch unique categories
    categories = Product.objects.values_list('category', flat=True).distinct()
    
    for cat in categories:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        nSlides = ceil(n / 4)  # Ensuring correct slider calculation
        
        # Create a list of dictionaries with discount price calculation
        products_with_discount = []
        for product in prod:
            price = float(product.price) if product.price else 0
            discount = float(product.discount) if product.discount else 0
            discount_price = price - (price * discount / 100)
            
            # Append the product details as a dictionary
            products_with_discount.append({
                'id': product.id,
                'product_name': product.product_name,
                'category': product.category,
                'price': price,
                'discount': discount,
                'discount_price': discount_price,
                'desc': product.desc,
                'image': product.image,
                'rating': product.rating,
            })

        # Only add to allProds if products exist
        if products_with_discount:
            allProds.append([products_with_discount, range(nSlides), nSlides])

    params = {'allProds': allProds}
    return render(request, 'shop/index.html', params)


def about(request):
    return render(request, 'shop/about.html')

def contact(request):
    if request.method == 'POST':
        email = request.POST.get('email', '')
        fname = request.POST.get('f_name', '')
        lname = request.POST.get('l_name', '')
        subjectC = request.POST.get('subject', '')
        msg = request.POST.get('message', '')

        # Sending email
        subject = "Thank You for Contacting Us"
        message = f"Hi {fname},\n\nThank you for reaching out to us. We will get back to you soon."
        from_email = settings.DEFAULT_FROM_EMAIL  # Ensure this is set in settings.py
        recipient_list = [email]
        # contact_data = Form(Email=email, F_name=fname, L_name=lname, SubjectC=subjectC, Message=msg)           
        # contact_data.save()
        try:
            send_mail(subject, message, from_email, recipient_list)
            contact_data = Form(Email=email, F_name=fname, L_name=lname, SubjectC=subjectC, Message=msg)           
            contact_data.save()
            return redirect('thank_you')  # Redirect to a thank-you page
        except Exception as e:
            print(f"Email sending failed: {e}")  # Log error for debugging

    return render(request, 'shop/contact.html')

def thank_you(request):
    return render(request, 'shop/thank_you.html')

# def productView(request, Pid):
    
#     product = Product.objects.filter(id=Pid).values('id', 'product_name', 'price', 'desc')  # Adjust fields as needed
#     price = float(product.price) if product.price else 0
#     discount = float(product.discount) if product.discount else 0
#     discount_price = price - (price * discount / 100)
#     if not product:
#         return HttpResponse("Product not found", status=404)  # Handle missing products properly

#     proParma = {'product': product[0]}  # Extract first item
#     return render(request, 'shop/productView.html', proParma)

def productView(request, Pid):
    # Retrieve product or return 404 if not found
    product = get_object_or_404(Product, id=Pid)

    # Get price and discount (handle missing values)
    price = float(product.price) if product.price else 0
    discount = float(product.discount) if hasattr(product, 'discount') else 0

    # Calculate discounted price
    discount_price = price - (price * discount / 100)

    # Pass data to template
    context = {
        'product': {
            'id': product.id,
            'product_name': product.product_name,
            'price': price,
            'desc': product.desc,
            'discount': discount,
            'discount_price': discount_price,
            'image': product.image,
            'rating': product.rating
        }
    }
    return render(request, 'shop/productView.html', context)

def checkout(request):
    if request.method == 'POST':
        email_r = request.POST.get('email', '')
        itemjson_r = request.POST.get('itemsJson', '')
        amount_r = request.POST.get('amount', '')
        product_id_r = request.POST.get('pro_id', '')
        name_r = request.POST.get('name', '')
        address_r = request.POST.get('address1', '') + request.POST.get('address2', '')
        city_r = request.POST.get('city', '')
        state_r = request.POST.get('state', '')
        zipcode_r = request.POST.get('zipcode', '')
        phone_r = request.POST.get('phone', '')
        coupon_r = request.POST.get('couponcode', '')

        # Example for sending email (optional)
        # subject = "Order Received"
        # message = f"Hi {name},\n\nYour order has been received. We'll contact you shortly."
        # from_email = settings.DEFAULT_FROM_EMAIL
        # recipient_list = [email]

        try:
            # send_mail(subject, message, from_email, recipient_list)

            # Save to database
            order = Orders(
                email=email_r,
                itemsjson=itemjson_r,
                amount=amount_r,
                product_id=product_id_r,
                name=name_r,
                address=address_r,
                city=city_r,
                state=state_r,
                Zipcode=zipcode_r,
                phone=phone_r,
                coupon=coupon_r,
            )
            order.save()
            # return redirect('thank_you')
            thank = True
            return render(request, 'shop/checkout.html', {'thank':thank})
        except Exception as e:
            print(f"Order saving failed: {e}")
    return render(request, 'shop/checkout.html')



@csrf_exempt  # Disable CSRF for testing; use CSRF token in production

def checkout_ajax(request):
    if request.method == "POST":
        product_id = request.POST.get("id")

        if not product_id:
            return JsonResponse({"success": False, "message": "Product ID is required"})

        # Fetch products with the given ID
        products = Product.objects.filter(id=product_id)
        
        allProds = []
        products_with_discount = []

        for product in products:
            price = float(product.price) if product.price else 0
            discount = float(product.discount) if product.discount else 0
            discount_price = price - (price * discount / 100)

            products_with_discount.append({
                'id': product.id,
                'product_name': product.product_name,
                'category': product.category,
                'price': price,
                'discount': discount,
                'discount_price': discount_price,
                'desc': product.desc,
                'image': str(product.image.url) if product.image else None,  # Ensure correct image URL
                'rating': product.rating,
            })

        if products_with_discount:
            allProds.append(products_with_discount)

        return JsonResponse({"success": True, "allProds": allProds})

    return JsonResponse({"success": False, "message": "Invalid request method"})

@csrf_exempt
def apply_coupon(request):
    if request.method == "POST":
        coupon_code = request.POST.get("coupon", "").strip().upper()
        total_price = float(request.POST.get("total_price", 0))
        # Fetch the coupon
        coupon = Coupon.objects.filter(coupon_name=coupon_code).values('coupon_name', 'discount_per').first()

        if coupon:
            discount_value = coupon['discount_per']
            
            # Percentage discount
            if discount_value <= 100:
                discount_amount = (total_price * discount_value) / 100
            else:
                discount_amount = discount_value  # Flat discount

            final_price = max(total_price - discount_amount, 0)  # Ensure final price is not negative

            return JsonResponse({
                "success": True,
                "discount_amount": discount_amount,
                "final_price": final_price
            })
        else:
            return JsonResponse({"success": False, "message": "Invalid Coupon Code"})

    return JsonResponse({"success": False, "message": "Invalid Request Method"})

def tracking(request):

    return HttpResponse("Tracking View")

def pro_search(request):
    query = request.GET.get('query', '').strip()
    if query:
        products = Product.objects.filter(product_name__icontains=query)
        n = len(products)
        nSlides = ceil(n / 4)  # Ensuring correct slider calculation
        if not products.exists():
            return HttpResponse("No products found matching your query.", status=404)
        # Calculate number of slides
        allProds = []
        allProds.append([products , range(nSlides), nSlides])
        #allProds.append([products])
        params = {'allProds': allProds}
        return render(request, 'shop/search.html', params)
