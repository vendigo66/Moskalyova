# TODO Найдите количество книг, которое можно разместить на дискете

kb_ = 1024 #b
mb_= kb_ * 1024 #b
volume_ = 1.44 * mb_ #b
page_ = 100
str_ = 50
symb_ = 25
rec_ = 4 #b
information_ = (rec_ * symb_ * str_ * page_) #b
book_ = int(volume_//information_)

print("Количество книг, помещающихся на дискету:", book_)
