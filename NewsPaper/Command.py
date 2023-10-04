# 'Список всех команд запускаемых в Django Shell.'
# from news.models import *
#
# '1.Создать двух пользователей.'
# u1 = User.objects.create_user('Ivan')
# u2 = User.objects.create_user('Sam')
#
# '2.Создать два объекта модели Author, связанные с пользователями.'
# at1=Author.objects.create(authorUser=u1)
# at2=Author.objects.create(authorUser=u2)
#
# '3.Добавить 4 категории в модель Category.'
# Category.objects.create(name='Sport')
# Category.objects.create(name='Economy')
# Category.objects.create(name='IT')
# Category.objects.create(name='Policy')
#
# '4.Добавить 2 статьи и 1 новость.'
# Post.objects.create(author=at1, choice="NW", title="sometitleNews", text="sometext")
# Post.objects.create(author=at1, choice="AR", title="sometitleART1", text="sometext")
# Post.objects.create(author=at2, choice="AR", title="sometitleART2", text="sometext")
#
# '5.Присвоить им категории (как минимум в одной статье/новости должно быть не меньше 2 категорий).'
# Post.objects.get(id=1).category.add(Category.objects.get(id=1))
# Post.objects.get(id=1).category.add(Category.objects.get(id=2))
# Post.objects.get(id=2).category.add(Category.objects.get(id=2))
# Post.objects.get(id=2).category.add(Category.objects.get(id=3))
# Post.objects.get(id=3).category.add(Category.objects.get(id=3))
# Post.objects.get(id=3).category.add(Category.objects.get(id=4))
#
# '6.Создать как минимум 4 комментария к разным объектам модели Post \
#  (в каждом объекте должен быть как минимум один комментарий).'
# Comment.objects.create(post=Post.objects.get(id=1), user=at1.authorUser, text_com='anytext')
# Comment.objects.create(post=Post.objects.get(id=2), user=at1.authorUser, text_com='anytext')
# Comment.objects.create(post=Post.objects.get(id=3), user=at2.authorUser, text_com='anytext')
# Comment.objects.create(post=Post.objects.get(id=1), user=at2.authorUser, text_com='anytext')
#
# '7.Применяя функции like() и dislike() к статьям/новостям и комментариям, скорректировать рейтинги этих объектов.'
# Comment.objects.get(id=1).like()
# Comment.objects.get(id=2).like()
# Comment.objects.get(id=3).like()
# Comment.objects.get(id=3).like()
# Comment.objects.get(id=4).like()
# Comment.objects.get(id=2).dislike()
# Comment.objects.get(id=4).dislike()
# Post.objects.get(id=1).like()
# Post.objects.get(id=1).like()
# Post.objects.get(id=2).like()
# Post.objects.get(id=3).like()
# Post.objects.get(id=3).like()
# Post.objects.get(id=1).dislike()
# Post.objects.get(id=2).dislike()
#
# '8.Обновить рейтинги пользователей.'
# at1.update_rating()
# at2.update_rating()
#
# '9.Вывести username и рейтинг лучшего пользователя (применяя сортировку и возвращая поля первого объекта).'
# Author.objects.order_by('-ratingAuthor').values('authorUser__username','ratingAuthor')[0]
#
# '10.Вывести дату добавления, username автора, рейтинг, заголовок и превью лучшей статьи,\
#  основываясь на лайках/дислайках к этой статье.'
# Post.objects.order_by('-rating').values('time_creat','author__authorUser__username','rating','title')[0]
# Post.objects.order_by('-rating').first().preview()
#
# '11.Вывести все комментарии (дата, пользователь, рейтинг, текст) к этой статье.'
# best_post=Post.objects.order_by('-rating').first()
# best_post.comment_set.all()
# best_post.comment_set.values('time_com', 'user__username','rating','text_com')


