from datetime import date
from django.shortcuts import render

posts = [
    {
        "slug": "hike-in-karnataka",
        "image": "sunset-back-full.jpg",
        "author": "Jayachandra M",
        "date": date(2021, 11, 4),
        "title": "Mountain Hiking in Karnataka",
        "excerpt":   """
                        There's nothing like the views you get when hiking in the mountains! and
                        I wasn't even prepared for what happened whilst I was enjoying the view!
                    """,
        "content":  """
                        Lorem ipsum, dolor sit amet consectetur adipisicing elit. Neque nesciunt hic atque possimus. Alias veritatis expedita voluptatibus?
                        Cumque impedit nemo pariatur necessitatibus ipsum eum incidunt sint autem architecto dolore! Nisi!

                        Lorem ipsum, dolor sit amet consectetur adipisicing elit. Neque nesciunt hic atque possimus. Alias veritatis expedita voluptatibus?
                        Cumque impedit nemo pariatur necessitatibus ipsum eum incidunt sint autem architecto dolore! Nisi!

                        Lorem ipsum, dolor sit amet consectetur adipisicing elit. Neque nesciunt hic atque possimus. Alias veritatis expedita voluptatibus?
                        Cumque impedit nemo pariatur necessitatibus ipsum eum incidunt sint autem architecto dolore! Nisi!
                    """,
    },
    {
        "slug": "hike-in-kerala",
        "image": "mountain-top-kerala.jpg",
        "author": "Jayachandra M",
        "date": date(2020, 11, 4),
        "title": "Mountain Hiking in Kerala",
        "excerpt":   """
                        There's nothing like the views you get when hiking in the mountains! and
                        I wasn't even prepared for what happened whilst I was enjoying the view!
                    """,
        "content":  """
                        Lorem ipsum, dolor sit amet consectetur adipisicing elit. Neque nesciunt hic atque possimus. Alias veritatis expedita voluptatibus?
                        Cumque impedit nemo pariatur necessitatibus ipsum eum incidunt sint autem architecto dolore! Nisi!

                        Lorem ipsum, dolor sit amet consectetur adipisicing elit. Neque nesciunt hic atque possimus. Alias veritatis expedita voluptatibus?
                        Cumque impedit nemo pariatur necessitatibus ipsum eum incidunt sint autem architecto dolore! Nisi!

                        Lorem ipsum, dolor sit amet consectetur adipisicing elit. Neque nesciunt hic atque possimus. Alias veritatis expedita voluptatibus?
                        Cumque impedit nemo pariatur necessitatibus ipsum eum incidunt sint autem architecto dolore! Nisi!
                    """,
    },
    {
        "slug": "hike-in-the-mountains",
        "image": "silhouette-people-fire.jpg",
        "author": "Jayachandra M",
        "date": date(2021, 11, 4),
        "title": "Mountain Hiking",
        "excerpt":   """
                        There's nothing like the views you get when hiking in the mountains! and
                        I wasn't even prepared for what happened whilst I was enjoying the view!
                    """,
        "content":  """
                        Lorem ipsum, dolor sit amet consectetur adipisicing elit. Neque nesciunt hic atque possimus. Alias veritatis expedita voluptatibus?
                        Cumque impedit nemo pariatur necessitatibus ipsum eum incidunt sint autem architecto dolore! Nisi!

                        Lorem ipsum, dolor sit amet consectetur adipisicing elit. Neque nesciunt hic atque possimus. Alias veritatis expedita voluptatibus?
                        Cumque impedit nemo pariatur necessitatibus ipsum eum incidunt sint autem architecto dolore! Nisi!

                        Lorem ipsum, dolor sit amet consectetur adipisicing elit. Neque nesciunt hic atque possimus. Alias veritatis expedita voluptatibus?
                        Cumque impedit nemo pariatur necessitatibus ipsum eum incidunt sint autem architecto dolore! Nisi!
                    """,
    }
]


def get_date(post):
    return post.get("date")


def starting_page(request):
    sorted_posts = sorted(posts, key=get_date)
    latest_posts = sorted_posts[-3:]
    return render(request, "blog/index.html", {
        "posts": latest_posts
    })


def all_posts(request):
    return render(request, "blog/all-posts.html", {
        "all_posts": posts
    })


def individual_post(request, slug):
    post = next(post for post in posts if slug == post["slug"])
    return render(request, "blog/post-detail.html", {
        "post": post
    })
