from django.shortcuts import render
from basic_app.forms import UserForms, UserProfileForms

# Create your views here.
def index(request):
    return render(request, 'basic_app/index.html')

def register(request):
    registered = False
    if request.method == 'POST':
        #getting the data from the user
        user_form = UserForms(data=request.POST)
        profile_form = UserProfileForms(request.POST)
        # checking if both forms are valid
        if user_form.is_valid() and profile_form.is_valid():
            #saving only the user_form but not the profile fomr
            user_form.save()
            # saving the profile form but not to the database with the use of commit=False
            profile = profile_form.save(commit=False)
            #matching up the user and the profile model
            profile.user = UserForms()
            #checking if the user provides image
            if 'profile-pic' in request.FILES:
                #getting the image from the user
                profile.profile_pic = request.FILES['profile_pic']
                #saving the profile
            profile.save()
            registered = True
            return render(request, 'register')
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form= UserForms()
        profile_form = UserProfileForms()
        return render(request, 'basic_app/registration.html', {'user_form':user_form, 'profile_form':profile_form, 'registered':registered})