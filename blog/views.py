from django.shortcuts import render
from datetime import date

# Create your views here.

posts_list = [
    {
        'slug': 'hike-in-the-mountains',
        'author': 'By Nikita',
        'date': date(2021, 7, 21),
        'title': 'Post Title One',
        'excerpt': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Autem deserunt eum id ipsa neque, nostrum numquam odio praesentium. Asperiores distinctio doloremque, eveniet itaque modi nihil ratione voluptatum! Laudantium, porro possimus.',
        'content': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. At aut beatae commodi deleniti eos eveniet, iure labore nemo nostrum porro repellendus saepe ullam veniam! Autem dolore eius expedita sint tempora?'
    }

]

def custom_key (element):
    return element['date']

def starting_page(request):
    return render(request, "base.html", )

def posts(request):
    sort_list = posts_list.copy()
    sort_list.sort(key=custom_key)
    last_posts = sort_list[-3:]
    return render(request, "blog/index.html", context={'posts': last_posts})

def post_detail(request, slug):
    return render(request,"blog/post-detail.html")