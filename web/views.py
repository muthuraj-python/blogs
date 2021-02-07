from django.views.generic import TemplateView, ListView, DetailView
from django.db.models import Q, Count

from blogs.models import Blog, Entry, UserComment


class BlogListView(ListView):
	template_name = "web/index.html"
	model = Blog

	def get_context_data(self, **karg):

		context = super(BlogListView, self).get_context_data(**karg)
		context["entrys"] = Entry.objects.filter(published=True).order_by('-pub_date')
		context["blog_count_list"] = Blog.objects.filter(entry__published=True).annotate(Count('entry'))
		context["active"] = 'ALL'
		context["total_count"] = context["entrys"].count()
		if self.request.GET:
			context["entrys"] = Entry.objects.filter(blog__name=self.request.GET.get('blog'), published=True).order_by('-pub_date')
			context["active"] = self.request.GET.get('blog')

		return context


class BlogDetailView(DetailView):
	template_name = "web/blog.html"
	model = Entry

	def get_context_data(self, **karg):

		context = super(BlogDetailView, self).get_context_data(**karg)
		context["comments"] = UserComment.objects.filter(Q(entry__id=karg['object'].id) & Q(block=False))
		context["suggestions"] = Entry.objects.filter(Q(blog__name=karg['object'].blog.name) & Q(published=True)).exclude(headline=karg['object'].headline)
		return context
