from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout
from django.contrib import messages
from .models import *
from .forms import *


def index(request):
    categories = Category.objects.all()
    articles = Article.objects.all()

    context = {
        "title": "Shop",
        "categories": categories,
        "articles": articles
    }

    return render(request, "shop/index.html", context)


def category_page_view(request, category_id):
    articles = Article.objects.filter(category=category_id)
    trends = Article.objects.all().order_by('views')
    category = Category.objects.get(id=category_id)

    context = {
        "title": f"Category:  {category.title} ",
        "articles": articles,
        "trends": trends,
        "category_name": category.title
    }

    return render(request, "shop/category_page.html", context)


def article_detail_view(request, article_id):
    article = Article.objects.get(id=article_id)
    last = Article.objects.all().order_by('-created_at')
    if request.user != article.author.id:
        article.views += 1
        article.save()
    comments = Comment.objects.filter(article=article.id)

    context = {
        "title": f"Статья: {article.title}",
        "article": article,
        "last_articles": last,
        "comments": comments
    }
    if request.user.is_authenticated:
        context.update({
            "comment_form": CommentForm()
        })

    return render(request, "shop/article_detail.html", context)


@login_required(login_url="login")
def add_article(request):
    if request.method == "POST":
        form = ArticleForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.save()
            messages.success(request, "Article added successfully !")
            return redirect("article_detail", article.id)
        else:
            for field in form.errors:
                messages.error(request, form.errors[field].as_text())
            return redirect("add_article")
    else:
        form = ArticleForm()

    context = {
        "title": "Add Article",
        "form": form
    }

    return render(request, "shop/add_article.html", context)


def register_user_view(request):
    if request.method == "POST":
        form = RegistrationUserForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            profile = Profile.objects.create(user=user)
            profile.save()
            messages.success(request, "User registration")
            return redirect('login')
        else:
            for field in form.errors:
                messages.error(request, form.errors[field].as_text())
            return redirect("register")
    else:
        form = RegistrationUserForm()

    context = {
        "title": "User Registration",
        "form": form
    }

    return render(request, 'shop/register.html', context)


def login_user_view(request):
    if request.method == "POST":
        form = LoginUserForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            if user:
                login(request, user)
                messages.success(request, "Successfully logged into your account !")
                return redirect('index')
            else:
                messages.error(request, "Login or Password incorrect")
        else:
            messages.error(request, "Login or Password incorrect")
    else:
        form = LoginUserForm()

    context = {
        "title": "Login",
        "form": form
    }

    return render(request, "shop/login.html", context)


@login_required(login_url="login")
def logout_user_view(request):
    logout(request)
    messages.info(request, "Successfully logged out !")
    return redirect('index')


@login_required(login_url="login")
def update_article_view(request, article_id):
    article = Article.objects.get(id=article_id)

    if request.method == "POST":
        form = ArticleForm(instance=article,
                           data=request.POST,
                           files=request.FILES)
        if form.is_valid():
            article = form.save()
            messages.info(request, "Article saved successfully")
            return redirect("article_detail", article.pk)
        else:
            for field in form.fields:
                messages.error(request, form.errors[field].as_text())
            return redirect("update_article", article.pk)
    else:
        form = ArticleForm(instance=article)

    context = {
        "title": "Update Article",
        "form": form
    }

    return render(request, "shop/add_article.html", context)


@login_required(login_url="login")
def article_delete(request, article_id):
    article = Article.objects.get(pk=article_id)

    if request.method == "POST":
        article.delete()
        messages.info(request, "Article deleted successfully")
        return redirect("index")

    context = {
        "title": "Удаление статьи",
        "article": article
    }

    return render(request, "shop/delete_article.html", context)


def profile_view(request, user_id):
    user = User.objects.get(id=user_id)
    profile = Profile.objects.get(user=user)

    context = {
        "user": user,
        "profile": profile,
        "title": "Профиль пользователя"
    }

    return render(request, "shop/profile.html", context)


@login_required(login_url="login")
def update_profile_view(request, user_id):
    user = User.objects.get(id=user_id)
    profile = Profile.objects.get(user=user)

    if request.method == "POST":
        user_form = UserForm(instance=user, data=request.POST)
        profile_form = ProfileForm(instance=profile, data=request.POST, files=request.FILES)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.info(request, "Data saved successfully")
            return redirect("profile", user.id)
        else:
            for field in user_form.errors:
                messages.error(request, user_form.errors[field].as_text())
            for field in profile_form.errors:
                messages.error(request, profile_form.errors[field].as_text())
            return redirect("update_profile", user.id)
    else:
        user_form = UserForm(instance=user)
        profile_form = ProfileForm(instance=profile)

    context = {
        "user_form": user_form,
        "profile_form": profile_form,
        "title": "Update Profile"
    }

    return render(request, "shop/edit_profile.html", context)


@login_required(login_url="login")
def save_comment(request, article_id):
    article = Article.objects.get(id=article_id)
    form = CommentForm(data=request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.author = request.user
        comment.article = article
        comment.save()
        messages.info(request, "Comment saved successfully !")
        return redirect("article_detail", article_id)
    else:
        messages.error(request, "Something went wrong")
        return redirect("article_detail", article_id)


def search_view(request):
    query = request.GET.get('search')
    results = Article.objects.filter(title__icontains=query)
    return render(request, 'shop/search_results.html', {'results': results})


def basket_add(request, article_id):
    article = Article.objects.get(pk=article_id)
    baskets = Basket.objects.filter(user=request.user, article=article)

    if not baskets.exists():
        Basket.objects.create(user=request.user, article=article, quantity=1)
    else:
        basket = baskets.first()
        basket.quantity += 1
        basket.save()

    return HttpResponseRedirect(request.META['HTTP_REFERER'])


def basket_remove(request, basket_id):
    basket = Basket.objects.get(pk=basket_id, user=request.user)
    basket.delete()
    return redirect('my_basket')


def basket_show(request):
    baskets = Basket.objects.filter(user=request.user)

    context = {
        'title': 'Моя корзина',
        'baskets': baskets
    }

    return render(request, 'shop/basket.html', context)

@login_required
def add_to_favorites(request, article_id):
    articles = get_object_or_404(Article, id=article_id)
    Favorites.objects.get_or_create(user=request.user, articles=articles)
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


@login_required
def remove_from_favorites(request, article_id):
    articles = get_object_or_404(Article, id=article_id)
    favorite = Favorites.objects.filter(user=request.user, articles=articles)
    favorite.delete()
    # return HttpResponseRedirect(request.META['HTTP_REFERER'])
    return redirect('favorite_list')


@login_required
def favorite_list(request):
    favorites = Favorites.objects.filter(user=request.user.id)

    context = {
        'title': "Избранное",
        'favorites': favorites
    }

    return render(request, 'shop/favorite_list.html', context)

