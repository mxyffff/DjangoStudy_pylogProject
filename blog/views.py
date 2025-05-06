from django.shortcuts import render, redirect
from django.template.defaultfilters import title
from django.template.defaulttags import comment

from blog.models import Post, Comment

def post_list(request):
    posts = Post.objects.all() # 모든 Post 객체를 가진 QuerySet
    # 템플릿에 전달할 dict
    context = {
        "posts": posts,
    }
    # 3번째 인수로 템플릿에 데이터를 전달
    return render(request, "post_list.html", context)

def post_detail(request, post_id):
    post = Post.objects.get(id=post_id) # id값이 URL에서 받은 post_id값이니 Post 객체
    if request.method == "POST":
        # textarea의 "name" 속성값("comment")을 가져온다.
        comment_content = request.POST["comment"]
        # 전달된 "comment"의 값으로 Comment 객체를 생성한다.
        Comment.objects.create(
            post=post,
            content=comment_content,
        )
    # 1. GET 요청으로 글 상세 페이지를 보여주거나
    # 2. POST 요청으로 댓글이 생성되거나
    # 두 경우 모두, 이 글의 상세 페이지를 보여주면 된다.
    context = {
        # post_id 대신 Post 객체를 전달
        "post" : post,
    }
    return render(request, "post_detail.html", context)

def post_add(request):
    if request.method == "POST": # method가 POST일 때
        print(request.FILES)
        title = request.POST["title"]
        content = request.POST["content"]
        thumbnail = request.FILES["thumbnail"] # 이미지 파일
        post = Post.objects.create(
            title=title,
            content=content,
            thumbnail=thumbnail, # 이미지 파일을 객체 생성 시에 전달
        )
        print(title)
        print(content)
        return redirect(f"/posts/{post.id}")
    else: # method가 POST가 아닐 때
        print("method GET")
    # POST/GET 중 어느 요청이든 render 결과를 리턴
    return render(request, "post_add.html")