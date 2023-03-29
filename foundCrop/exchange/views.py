"""
views file for project
"""
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from .models import Card, Command, Detail, Product
from .forms import CLiForm, CardForm, DetailForm, ProForm, ProductCreateForm, UserForm
from exchange.constant import CATEGORY, COUNTRY, SEXE
from exchange.models import Product


# home page
def home(request):
    """
    method of index.htm file
    """
    products = Product.objects.all()

    if request.method == 'GET':
        search = request.GET.get('search')
        if search is not None:
            products = Product.objects.filter(name__icontains=search)
        
    context = {
        'food': CATEGORY,
        'products': products
    }
    return render(request, 'index.html', context)

# category for food
def category(request, name):
    """
    all product from same category
    """
    products = Product.objects.filter(category=name)

    if request.method == 'GET':
        search = request.GET.get('search')
        if search is not None:
            products = products.filter(name__icontains=search)

    context = {
        'products': products,
        'food': CATEGORY
    }
    return render(request, 'category.html', context)


# logout
@login_required
def output(request):
    """
    deconnexion
    """
    logout(request)
    return redirect('home')


# -----------------------------------------------------------------------------
# user fonction
#
# dashbord
@login_required
def dashboard(request):
    """
    dashboard statistiques
    """
    if request.user.status == 'client':
        card  = Card.objects.filter(user=request.user).first()
        item = Command.objects.filter(card=card)
        # nbre de command effectuer
        sale = item.count()
        # frais total de tous les command
        revenue = sum([obj.total() for obj in item])
        customers = 1
    else:
        products = Product.objects.filter(professional=request.user)
        details = Detail.objects.all()
        # nombre total de vente
        sale = 0
        # gains total
        revenue = 0
        # nbre total de client
        customers = 0
        for detail in details:
            if detail.product.professional in [prod.professional for prod in products]:
                revenue += detail.product.price
                sale += 1
        customers = len(set([cmd.card.user for cmd in Command.objects.all()]))

    context = {
        'sale' : sale,
        'revenue' : revenue,
        'customers': customers
    }
    return render(request, 'auth/dashboard.html', context)

# profile
@login_required
def profile(request):
    """
    update profile
    """
    form = UserForm(request.POST or None, request.FILES or None, instance=request.user)
    if form.is_valid():
        form.save()
        return redirect('signin')
    
    card = Card.objects.filter(user=request.user).first()
    
    if card:
        cardform = CardForm(request.POST or None, instance=card)
    else:
        cardform = CardForm(request.POST or None)

    if cardform.is_valid():
        obj = cardform.save(commit=False)
        obj.user = request.user
        obj.save()

    context = {
        'form': form,
        'cardform': cardform,
        'country': COUNTRY,
        'sexe': SEXE
    }
    return render(request, 'auth/profile.html', context)


# --------------------------------------------------------------------------------
## product

# view
@login_required
def productView(request):
    """
    product view
    """
    products = Product.objects.filter(professional=request.user)
    
    if request.method == "GET":
        search = request.GET.get('search')
        if search is not None:
            products = Product.objects.filter(name__icontains=search)

    context = {
        'products': products
    }
    return render(request, 'product/view.html', context)


#add
@login_required
def productAdd(request):
    """
    product create
    """
    form = ProductCreateForm(request.POST or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.professional = request.user
        obj.save()
        return redirect('productView')

    context = {
        'form': form,
    }
    return render(request, 'product/add.html', context)


# del
@login_required
def productDel(request, prd_id):
    """
    product delete
    """
    error = ""
    obj = get_object_or_404(Product, id=prd_id)

    if request.method == 'POST':
        if obj.professional == request.user:
            obj.delete()
            return redirect('productView')
        else:
            error = "you are not the owner of this product"

    context = {
        'product': obj,
        'error': error
    }
    return render(request, 'product/del.html', context)


# update
@login_required
def productUpdate(request, prd_id):
    """
    update product
    """
    error = ''
    obj = get_object_or_404(Product, id=prd_id)

    form = ProductCreateForm(request.POST or None, instance=obj)
    if form.is_valid():
        if obj.professional == request.user:
            form.save()
            return redirect('productView')
        else:
            error = "you are not the owner of this product"

    context = {
        'form': form,
        'error': error
    }
    return render(request, 'product/update.html', context)


# ---------------------------------------------------------------------------------

# command
# view
@login_required
def cmdView(request):
    card = Card.objects.filter(user=request.user).first()
    cmd = Command.objects.filter(card=card).filter(valid=True).filter(pay=False).first()
    details = Detail.objects.filter(cmd=cmd).filter(active=True)
    context = {
        'details': details,
        'cmd': cmd
    }
    return render(request, 'cmd/view.html', context)


#add
@login_required
def add_to_cart(request, prd_id):
    """
    add a product to cart
    """
    product = get_object_or_404(Product, id=prd_id)

    form = DetailForm()
    if request.method == 'POST':
        form = DetailForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.cmd = Command.objects.get(valid=True)
            obj.product = product
            obj.save()
            return redirect('home')

    context = {
        'form': form
    }
    return render(request, 'cmd/add_to_cart.html', context)


# del
@login_required
def cmdDel(request, cmd_id):
    cmd = get_object_or_404(Command, id=cmd_id)

    if request.method == 'POST':
        cmd.delete()
        return redirect('dashboard')
    context = {
        'cmd': cmd
    }
    return render(request, 'cmd/del.html', context)


# del to card
@login_required
def del_to_cart(request, detail_id):
    detail = get_object_or_404(Detail, id=detail_id)

    if request.method == 'POST':
        detail.delete()
        return redirect('cmdView')
    context = {
        'detail': detail
    }
    return render(request, 'cmd/del_to_cart.html', context)


# update
@login_required
def Update_to_cart(request, detail_id):
    detail = get_object_or_404(Detail, id=detail_id)

    form = DetailForm(request.POST or None, instance=detail)
    if form.is_valid():
        form.save()

    context = {
        'form': form
    }
    return render(request, 'cmd/update_to_cart.html', context)


# buy
@login_required
def buy(request):

    cmd = Command.objects.filter(valid=True, pay=False)
    details = Detail.objects.filter(cmd=cmd, active=True)

    # le virement
    context = {
        'cmd': cmd,
        'details': details
    }
    return render(request, 'cmd/buy.html', context)


# -----------------------------------------------------------------------

# login
def signin(request):
    """
    all user login from
    """
    error = ''
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            error = 'username or password invalid'
    
    context = {
        'error': error
    }
    return render(request, 'login.html', context)


# register
def signup(request):
    """
    all user register form
    """
    form = UserForm()
    if request.method == 'POST':
        form = UserForm(data=request.POST)
        if request.POST['status'] == 'client':
            form = CLiForm(request.POST)
        else:
            form = ProForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('signin')
    context = {
        'form': form
    }
    return render(request, 'signup.html', context)
