from django.shortcuts import render
from django.shortcuts import render,redirect
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
# from django.contrib.auth.mixins import LoginRequiredMixinfrom 
from django.contrib.auth import login

from django.contrib.auth.models import User
from .forms import WorkerRegistrationForm, EmployerRegistrationForm
from django.contrib.auth.decorators import login_required
from .models import CustomUser,Job
from django.contrib import messages
from .forms import UserUpdateForm,JobForm

# Create your views here.

def home(request):
    return render(request,'index.html')

def worker_login(request):
    return render(request,'worker_login.html')

def employer_login(request):
    return render(request,'employer_login.html')

def worker_registration(request):
    return render(request,'worker_register.html')

def employer_registration(request):
    return render(request,'employer_register.html')

def employer_dashboard(request):
    return render(request,'employer_dasboard.html')

@login_required
def employer_dashboard(request):
    return render(request,'employer_dashboard.html',{'user': request.user})

@login_required
def worker_dashboard(request):
    job = Job.objects.all()
    return render(request,'worker_dashboard.html',{'user': request.user,
                                                   'jobs' : job
                                                   })


class CustomLoginView(LoginView):
    template_name = 'worker_login.html'
    next_page = 'home'  

    def form_valid(self, form):
        user = form.get_user()
        login(self.request, user)  # Log in the user

        # Redirect based on user type
        if user.user_type == 'worker':
            return redirect('/worker_dashboard')
        elif user.user_type == 'employer':
            messages.error(self.request, "Oops that's an Employer Account!")
            return self.form_invalid(form)  
        return super().form_valid(form)  

class CustomLoginView2(LoginView):
    template_name = 'employer_login.html'
    next_page = 'home' 
    def form_valid(self, form):
        user = form.get_user()
        login(self.request, user)  # Log in the user

        # Redirect based on user type
        if user.user_type == 'worker':
            messages.error(self.request, "Oops that's a Worker's Account!")
            return self.form_invalid(form)  
        elif user.user_type == 'employer':
            return redirect('/employer_dashboard')
        return super().form_valid(form)  

def register_worker(request):
    if request.method == "POST":
        form = WorkerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registration successful! 🎉")
            return redirect("worker_login") 
        else:
            messages.error(request, "Please correct the errors below.")  
    else:
        form = WorkerRegistrationForm()

    return render(request, "worker_register.html", {"form": form})




def register_employer(request):
    if request.method == "POST":
        form = EmployerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registration successful! 🎉")
            return redirect("employer_login")
        else:
            messages.error(request, "Please correct the errors below.") 
    else:
        form = EmployerRegistrationForm()

    return render(request, "employer_register.html", {"form": form})

@login_required  
def post_job(request):
    if request.method == "POST":  
        form = JobForm(request.POST)  # Create a form instance with submitted data
        if form.is_valid(): 
            job = form.save(commit=False)  # Create a Job object but don't save yet
            job.employer = request.user.employer_profile 
            job.save()  
            messages.success(request, "Job posted successfully!")  
    else:
        form = JobForm() 

    return render(request, 'employer_dashboard.html', {'form': form})  

@login_required
def update_user_profile(request):
    if request.method == "POST":
        form = UserUpdateForm(request.POST, instance=request.user)  # Update the logged-in user
        if form.is_valid():
            form.save()
            return redirect('worker_dasboard')  # Redirect to profile page (change as needed)
        else:
            print(form.errors)
    else:
        form = UserUpdateForm(instance=request.user)  # Prefill form with current user data

    return render(request, 'worker_dashboard.html', {'form': form})





