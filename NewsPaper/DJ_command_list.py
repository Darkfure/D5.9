# >>> from news.models import *
# >>> from django.db.models import Sum
#
# User.objects.create_user('Semenov')
# User.objects.create_user('Andreev')
#
# Author.object.create(user_id=1)
# Author.object.create(user_id=2)
#
# Category.objects.create(name='Спорт')
# Category.objects.create(name='Политика')
# Category.objects.create(name='Бизнес')
# Category.objects.create(name='Игровая индустрия')
#
# Post.objects.create(heading='Россия - чемпион!', text='Россия стала чемпионом мира по футболу', author_id=1, type='NW')
# Post.objects.create(heading='Большая покупка Microsoft!', text='Компания Microsoft покупает Activision Blizzard! Видимо, Bethesda им было мало!', author_id=2, type='AR')
# Post.objects.create(heading='Бедная Sony!', text='Sony прибедняется, чтобы сорвать сделку между Microsoft и Activision Blizzard', author_id=2, type='AR')
#
# PostCategory.objects.create(post_id=1, category_id=1)
# PostCategory.objects.create(post_id=2, category_id=3)
# PostCategory.objects.create(post_id=2, category_id=4)
# PostCategory.objects.create(post_id=3, category_id=4)
#
# c=Comment.objects.get(id=1)
# >>> Comment.like(c)
# #вот таким образом накрутил рейтинг у всех статей и комментариев, расписывать все не буду, они одинаковые)
#
#
# >>> a11=Post.objects.filter(author_id=1).aggregate(Sum("rating"))['rating__sum']
# >>> a12=Comment.objects.filter(author_id=1).aggregate(Sum("rating"))['rating__sum']
# >>> a13=Comment.objects.filter(post__author_id=1).aggregate(Sum("rating"))['rating__sum']
# >>> a1=Author.objects.get(id=1)
# >>> Author.update_rating(a1, a11, a12, a13)
#
# >>> a2=Author.objects.get(id=2)
# >>> a21=Post.objects.filter(author_id=2).aggregate(Sum("rating"))['rating__sum']
# >>> a22=Comment.objects.filter(author_id=2).aggregate(Sum("rating"))['rating__sum']
# >>> a23=Comment.objects.filter(post__author_id=2).aggregate(Sum("rating"))['rating__sum']
# >>> Author.update_rating(a2, a21, a22, a23)
#
#
# Author.objects.all().order_by('-rating').values('user__username', 'rating')[0]
#
# Post.objects.all().order_by('-rating').values('create_time', 'author__user__username', 'rating', 'heading')[0]
# prw=Post.objects.get(id=2)
# Post.preview(prw)
#
# Comment.objects.filter(post_id=2).values('create_time', 'author__username', 'rating', 'text')



