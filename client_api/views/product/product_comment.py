import math

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from clients.utils.decorators import client_or_none_only
from common.products.product.product import Product
from common.products.comments.comments import ProductComment


@api_view(['GET'])
@client_or_none_only
def get_comments_by_product(request, slug_p):
    data = dict()
    state = dict()
    page = int(request.GET.get('page', 0))
    page_size = 10
    first = int(page * page_size)
    try:
        product = Product.objects.get(product_id=slug_p)
        comments = ProductComment.objects.filter(product_id__product_id=product.product_id, reply_to=None).order_by('-date_time_add')
        rows_count = comments.count()
        rows_db = comments[first:first + page_size]
        pages_count = math.floor(rows_count / page_size) + (1 if rows_count % page_size > 0 else 0)
        comments_list = list()
        for comment in rows_db:
            com_data = dict()
            com_data["owner"] = comment.owner_id.get_full_name()
            com_data["owner_image"] = comment.owner_id.image.url if comment.owner_id.image.url else '/assets/images' \
                                                                                                    '/users/user.jpg '
            com_data["text"] = comment.text
            com_data["likes_count"] = comment.likes_count
            com_data["dislikes_count"] = comment.dislikes_count
            com_data["rating_stars"] = comment.rating_stars
            com_data["date_time_add"] = comment.date_time_add.strftime("%d.%m.%Y %H:%M")
            com_data["comment_answer"] = [{"owner": answer.owner_id.get_full_name(),
                                           "owner_image": answer.owner_id.image.url if
                                           answer.owner_id.image.url else '/assets/images/users/user.jpg',
                                           "date_time_add": answer.date_time_add.strftime("%d.%m.%Y %H:%M"),
                                           "text": answer.text}
                                          for answer in ProductComment.objects.filter(reply_to_id=comment.id)]
            comments_list.append(com_data)
        data["comments_list"] = comments_list
        state["pages"] = {'count': pages_count}
    except Product.DoesNotExist:
        data = {"errors": {"message": "Такого продукта немає"}}
        return Response(data, status=status.HTTP_404_NOT_FOUND)
    return Response({"data": data, "state": state}, status=status.HTTP_200_OK)
