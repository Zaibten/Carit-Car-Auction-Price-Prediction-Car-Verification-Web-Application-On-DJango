from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import auth
from .forms import *
from app.models import *
from .models import *
from django.utils import timezone
import datetime


def signup(request):
    form = UserSignup(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return JsonResponse({"message": "success"}, safe=True)
        else:
            error = form.errors
            return JsonResponse({"message": error}, safe=True)
    context = {
        "title": "Sign Up"
    }
    return render(request, 'user/signup.html', context)


def signin(request):
    form = UserSignin(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save(request)
            print(request.user.id)
            return JsonResponse({"message": "success", "userID": request.user.id}, safe=True)
        else:
            error = form.errors
            return JsonResponse({"message": error}, safe=True)
    context = {
        'title': 'Sign in'
    }
    return render(request, 'user/signin.html', context)


@login_required
def logout(request):
    auth.logout(request)
    return redirect('home')


@login_required
def profile(request, userID=-1):
    user = User.objects.get(id=userID)
    cars = Car.objects.filter(seller=request.user).order_by('-end_at')
    customer = Customer.objects.get(user=user)

    on_auction, auction_ended = 0, 0
    for car in cars:
        if car.on_auction: 
            on_auction += 1
        else: 
            auction_ended += 1

    if request.method == 'POST':
        copy = request.POST.copy()
        image = request.FILES.copy()

        # Use .get() to avoid KeyError
        phone = copy.get('phone', customer.phone)
        location = copy.get('location', customer.location)

        # Handle the image field with a try-except block
        if 'image' in image:
            image_file = image['image']
        else:
            image_file = customer.image

        # Prepare data for the form
        copy['phone'] = phone
        copy['location'] = location

        end_at_str = copy.get('end_at')
        if end_at_str:
            naive_end_at = timezone.datetime.strptime(end_at_str, "%Y-%m-%dT%H:%M")
            end_at = timezone.make_aware(naive_end_at)
            copy['end_at'] = end_at  # Add it to the copied data for the form

        form = CustomerForm(copy, {'image': image_file}, instance=customer)
        if form.is_valid():
            form.save()

    context = {
        'title': 'Profile',
        'user': user,
        'cars': cars,
        'customer': customer,
        'on_auction': on_auction,
        'auction_ended': auction_ended
    }
    return render(request, 'user/profile.html', context)


@login_required
def add_car(request):
    if request.method == 'POST':
        # Extract the price from the form data
        price = request.POST.get('price')
        
        # Extract and convert end_at to a timezone-aware datetime
        end_at_str = request.POST.get('end_at')  # Assuming the format is '2024-10-22T05:09'
        try:
            # Parse end_at string and make it timezone-aware
            naive_end_at = datetime.datetime.fromisoformat(end_at_str)
            end_at = timezone.make_aware(naive_end_at)
        except (ValueError, TypeError):
            return JsonResponse({'error': 'Invalid date format'}, safe=True)

        # Create the car object and set bid = price
        car = Car.objects.create(
            make=request.POST.get('make'),
            model=request.POST.get('model'),
            seller=request.user,
            location=request.POST.get('location'),
            vin=request.POST.get('vin'),
            mileage=request.POST.get('mileage'),
            body_style=request.POST.get('body_style'),
            engine=request.POST.get('engine'),
            drivetrain=request.POST.get('drivetrain'),
            transmission=request.POST.get('transmission'),
            transmission_speed=int(request.POST.get('transmission_speed')),
            exterior_color=request.POST.get('exterior_color'),
            interior_color=request.POST.get('interior_color'),
            title_status=request.POST.get('title_status'),
            seller_type=request.POST.get('seller_type'),
            highlight=request.POST.get('highlight'),
            equipment=request.POST.get('equipment'),
            modification=request.POST.get('modification'),
            known_flaw=request.POST.get('known_flaw'),
            recent_service_history=request.POST.get('recent_service_history'),
            ownership_history=request.POST.get('ownership_history'),
            seller_note=request.POST.get('seller_note'),
            end_at=end_at,  # Use the timezone-aware datetime
            price=price,  # Set the price from the form data
            bid=price,    # Set bid equal to the price
        )

        # Handle image uploads for exterior and interior
        exterior_images = request.FILES.getlist('exterior_images')
        for image in exterior_images:
            Photo.objects.create(car=car, image=image, type="Exterior")
        interior_images = request.FILES.getlist('interior_images')
        for image in interior_images:
            Photo.objects.create(car=car, image=image, type="Interior")
        
        # Update the customer's auction_posted count
        customer = Customer.objects.get(user=request.user)
        customer.auction_posted += 1
        customer.save()
        
        return JsonResponse({'POST': 'success'}, safe=True)
    else:
        return JsonResponse({'error': 'invalid request'}, safe=True)
      
    
@login_required
def place_bid(request, car_id):
    car = get_object_or_404(Car, id=car_id)

    if request.method == 'POST':
        bid_value = int(request.POST.get('bid_value'))

        if bid_value > car.bid:
            # Update the car's bid
            car.bid = bid_value
            car.highest_bid_user = request.user.username
            car.highest_bid_user_email = request.user.email
            car.save()
            
            # Return a success response
            return JsonResponse({'success': 'Your bid has been placed successfully!'})

    # Render the bidding page with the car details
    return render(request, 'place_bid.html', {'car': car})



@login_required
def delete_auction(request, car_id):
    car = get_object_or_404(Car, id=car_id)

    if request.method == 'POST':
        car.delete()
        return HttpResponse(status=204)  # No content response

    return HttpResponse(status=204)

