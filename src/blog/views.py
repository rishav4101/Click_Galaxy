from django.shortcuts import render, get_object_or_404,redirect
from django.views.generic.base import TemplateView
from django.views.generic import View
from django.http import HttpResponse 
from django.core.mail import send_mail

# Create your views here.
from django.views import generic
from .models import Post

from .forms import CommentForm, ContactForm

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'

#class PostDetail(generic.DetailView):
#    model = Post
#    template_name = 'post_detail.html'

#def about(request):
#	return render(request, "about.html")

class about(TemplateView):
	template_name = 'about.html'

class privacy(TemplateView):
	template_name = 'privacy.html'


class about_page(TemplateView):
	template_name = 'about_page.html'

def post_detail(request, slug):
    template_name = 'post_detail.html'
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.filter(active=True)
    new_comment = None
    # Comment posted
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():

            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(request, template_name, {'post': post,
                                           'comments': comments,
                                           'new_comment': new_comment,
                                           'comment_form': comment_form})


def contact_us(request, *args, **kwargs):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # send email code goes here
            sender_name = form.cleaned_data['name']
            sender_email = form.cleaned_data['email']

            message = "{0} has sent you a new message:\n\n{1}".format(sender_name, form.cleaned_data['message'])
            send_mail('New Enquiry', message, sender_email, ['rajkumarrishav4101@gmail.com'])

            return HttpResponse('Thanks for contacting us!')
    else:
        form = ContactForm()

    return render(request, 'contact_us.html', {'form': form})