from django.utils.deprecation import MiddlewareMixin

class AnonymusUserMiddleware(MiddlewareMixin):

	def process_request(self, request):
		import pdb;pdb.set_trace()
		if not request.user.is_authenticated:
			print("\n\n\nanonymus user is trying to access our site...")

	def process_view(self, request, view_func, view_args, view_kwargs):
		import pdb;pdb.set_trace()

	def process_response(self, request, response):
		import pdb;pdb.set_trace()
		return response

