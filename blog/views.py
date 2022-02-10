from django.shortcuts import render
from django.utils import timezone
from .models import Post, Region, Partition
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def post_list(request):
    page = 1

    if request.GET.getlist('page'):
        page = request.GET.getlist('page')
        page = int(page[0])

    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    parts = Partition.objects.all()
    regions = Region.objects.all()

    paginator = Paginator(posts, 3)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    
    return render(request, 'post_list.html', {'posts': posts, 'parts': parts, 'regions': regions})

def post(request, post_url):
    post = Post.objects.get(url=post_url)
    parts = Partition.objects.all()
    regions = Region.objects.all()

    return render(request, 'post.html', {'post': post, 'parts': parts, 'regions': regions})

def region(request, region_url):
    page = 1
    if request.GET.getlist('page'):
        page = request.GET.getlist('page')
        page = int(page[0])

    region = Region.objects.get(url=region_url)
    posts = Post.objects.filter(region=region.id)
    posts = posts.filter(published_date__lte=timezone.now()).order_by('published_date')

    parts = Partition.objects.all()
    regions = Region.objects.all()

    paginator = Paginator(posts, 3)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    return render(request, 'region.html', {'posts': posts, 'parts': parts, 'region': region, 'regions': regions})

def part(request, part_url):
    page = 1
    if request.GET.getlist('page'):
        page = request.GET.getlist('page')
        page = int(page[0])

    part = Partition.objects.get(url=part_url)
    parts = Partition.objects.all()
    regions = Region.objects.all()

    posts = Post.objects.filter(partition=part.id)
    posts = posts.filter(published_date__lte=timezone.now()).order_by('published_date')

    paginator = Paginator(posts, 3)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    return render(request, 'part.html', {'posts': posts, 'parts': parts, 'part': part, 'regions': regions})