from django.shortcuts import render, redirect, get_object_or_404
from comments.forms import CommentForm
from takeout.models import Food

def comment(request, food_pk):
	food = get_object_or_404(Food, pk=food_pk)

	if request.method == 'POST':
		form = CommentForm(request.POST)

		if form.is_valid():
			comment = form.save(commit=False)
			comment.food = food
			comment.user = request.user
			comment.save()
			return redirect(food)
		else:
			comment_list = food.comment_set.all()
			context = {
				'food': food,
			    'form': form,
	            'comment_list': comment_list
			}
			return render(request, 'takeout/food.html', context=context)
	return redirect(food)