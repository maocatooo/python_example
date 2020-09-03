from celery_.demo1.service import add

add.apply_async((1, 2), countdown=1)

add.apply_async((2, 3), expires=1)


add.apply_async((3, 3), countdown=2, expires=1)