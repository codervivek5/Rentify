from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from .forms import UserRegisterForm, PropertyForm
from .models import Property, Interest
from django.core.paginator import Paginator
from django.core.mail import send_mail
from django.conf import settings
from django.http import JsonResponse


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
    else:
        form = UserRegisterForm()
    return render(request, 'main/register.html', {'form': form})


@login_required
def home(request):
    properties_list = Property.objects.all()
    paginator = Paginator(properties_list, 5)  # Show 5 properties per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'main/home.html', {'page_obj': page_obj})


@login_required
def post_property(request):
    if request.method == 'POST':
        form = PropertyForm(request.POST)
        if form.is_valid():
            property = form.save(commit=False)
            property.seller = request.user
            property.save()
            return redirect('my_properties')
    else:
        form = PropertyForm()
    return render(request, 'main/post_property.html', {'form': form})

@login_required
def my_properties(request):
    properties = Property.objects.filter(seller=request.user)
    return render(request, 'main/my_properties.html', {'properties': properties})

@login_required
def update_property(request, property_id):
    property = get_object_or_404(Property, id=property_id)
    if request.method == 'POST':
        form = PropertyForm(request.POST, instance=property)
        if form.is_valid():
            form.save()
            return redirect('my_properties')
    else:
        form = PropertyForm(instance=property)
    return render(request, 'main/update_property.html', {'form': form})

@login_required
def delete_property(request, property_id):
    property = get_object_or_404(Property, id=property_id)
    if request.method == 'POST':
        property.delete()
        return redirect('my_properties')
    return render(request, 'main/delete_property.html', {'property': property})

@login_required
def property_detail(request, property_id):
    property = get_object_or_404(Property, id=property_id)
    if request.method == 'POST':
        # Assuming Interest model has buyer, property fields
        Interest.objects.create(property=property, buyer=request.user)

        # Sending email to the buyer
        send_mail(
            'Seller Contact Details',
            f'The seller contact details are: {property.seller.email}',
            settings.DEFAULT_FROM_EMAIL,
            [request.user.email],
            fail_silently=False,
        )
        # Sending email to the seller
        send_mail(
            'New Buyer Interested',
            f'A buyer is interested in your property: {request.user.email}',
            settings.DEFAULT_FROM_EMAIL,
            [property.seller.email],
            fail_silently=False,
        )
        return redirect('home')
    
    return render(request, 'main/property_detail.html', {'property': property})



def like_property(request, property_id):
    if request.method == 'POST':
        property = Property.objects.get(pk=property_id)
        property.likes += 1
        property.save()
        return JsonResponse({'likes': property.likes})
    else:
        # Handle other HTTP methods (e.g., GET) if necessary
        return JsonResponse({'error': 'Method not allowed'}, status=405)


# @login_required
# def like_property(request, property_id):
#     property = get_object_or_404(Property, id=property_id)
#     property.likes += 1
#     property.save()
#     return JsonResponse({'likes': property.likes})
