from django.core.files.storage import FileSystemStorage
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from datetime import date
import math
import pandas as pd

# Create your views here.
from django.utils.datastructures import MultiValueDictKeyError

from blog.forms import UploadFileForm

posts_list = [
    {
        'number': 1,
        'slug': 'hike-in-the-mountains1',
        'author': 'By Nikita',
        'date': date(2021, 7, 21),
        'title': 'Post Title 1',
        'excerpt': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Autem deserunt eum id ipsa neque, nostrum numquam odio praesentium. Asperiores distinctio doloremque, eveniet itaque modi nihil ratione voluptatum! Laudantium, porro possimus.',
        'content': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. At aut beatae commodi deleniti eos eveniet, iure labore nemo nostrum porro repellendus saepe ullam veniam! Autem dolore eius expedita sint tempora?'
    },
    {
        'number': 2,
        'slug': 'hike-in-the-mountains2',
        'author': 'By Nikita',
        'date': date(2021, 3, 21),
        'title': 'Post Title 2',
        'excerpt': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Autem deserunt eum id ipsa neque, nostrum numquam odio praesentium. Asperiores distinctio doloremque, eveniet itaque modi nihil ratione voluptatum! Laudantium, porro possimus.',
        'content': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. At aut beatae commodi deleniti eos eveniet, iure labore nemo nostrum porro repellendus saepe ullam veniam! Autem dolore eius expedita sint tempora?'
    },
    {
        'number': 3,
        'slug': 'hike-in-the-mountains3',
        'author': 'By Nikita',
        'date': date(2021, 6, 21),
        'title': 'Post Title 3',
        'excerpt': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Autem deserunt eum id ipsa neque, nostrum numquam odio praesentium. Asperiores distinctio doloremque, eveniet itaque modi nihil ratione voluptatum! Laudantium, porro possimus.',
        'content': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. At aut beatae commodi deleniti eos eveniet, iure labore nemo nostrum porro repellendus saepe ullam veniam! Autem dolore eius expedita sint tempora?'
    },
    {
        'number': 4,
        'slug': 'hike-in-the-mountains4',
        'author': 'By Nikita',
        'date': date(2021, 9, 21),
        'title': 'Post Title 4',
        'excerpt': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Autem deserunt eum id ipsa neque, nostrum numquam odio praesentium. Asperiores distinctio doloremque, eveniet itaque modi nihil ratione voluptatum! Laudantium, porro possimus.',
        'content': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. At aut beatae commodi deleniti eos eveniet, iure labore nemo nostrum porro repellendus saepe ullam veniam! Autem dolore eius expedita sint tempora?'
    },
    {
        'number': 5,
        'slug': 'hike-in-the-mountains4',
        'author': 'By Nikita',
        'date': date(2021, 9, 21),
        'title': 'Post Title 4',
        'excerpt': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Autem deserunt eum id ipsa neque, nostrum numquam odio praesentium. Asperiores distinctio doloremque, eveniet itaque modi nihil ratione voluptatum! Laudantium, porro possimus.',
        'content': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. At aut beatae commodi deleniti eos eveniet, iure labore nemo nostrum porro repellendus saepe ullam veniam! Autem dolore eius expedita sint tempora?'
    },

]


def custom_key(element):
    return element['date']


def starting_page(request):
    return render(request, "base.html")


def posts(request, page):
    num_of_post = 4
    sort_list = posts_list.copy()
    sort_list.sort(key=custom_key,reverse=True)
    if page == 1:
        show_posts = sort_list[:num_of_post]
    else:
        show_posts = sort_list[num_of_post:num_of_post*2]
    return render(request, "blog/index.html", context={
        'posts': show_posts,
        'counter': range(1, int( math.ceil( len(sort_list) / num_of_post  )  ) + 1)
    })


def post_detail(request, slug):
    post = next(x for x in posts_list if x['slug'] == slug)

    return render(request, "blog/post-detail.html", {
        'post': post
    })




