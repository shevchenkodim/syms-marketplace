from django.contrib.auth import logout
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse
from django.utils.decorators import method_decorator
from clients.utils.decorators import client_or_none_only, client_only
from django.views.generic import TemplateView

from common.clients.sliders.main_sliders import MainCarouselModel
from common.products.categories.categories import CategoryModel
from common.products.product.product import Product

decorators_any = [client_or_none_only]
decorators_only_client = [client_only]


@method_decorator(decorators_any, name='dispatch')
class IndexView(TemplateView):
    """Index page"""
    template_name = "main/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["main_carousel_items"] = MainCarouselModel.objects.all().only("item_alt", "item_image")
        return context


@method_decorator(decorators_any, name='dispatch')
class ProductsForCategoriesView(TemplateView):
    """Product for categories page"""
    template_name = "products_for_categories/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["category"] = get_object_or_404(CategoryModel, slug=self.kwargs['slug_c'])
        return context


@method_decorator(decorators_any, name='dispatch')
class ProductView(TemplateView):
    """Product page"""
    template_name = "product/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        product_id = self.kwargs['slug_p']
        category_slug = self.kwargs['slug_c']
        Product.check_for_category(p_id=product_id, c_slug=category_slug)

        context["product_id"] = product_id
        context["do_product_info_url"] = reverse('client_api:get_product_info',
                                                 kwargs={'slug_p': product_id})
        context["do_seller_info_url"] = reverse('client_api:get_seller_info',
                                                kwargs={'slug_p': product_id})
        context["do_comments_list_url"] = reverse('client_api:get_comments',
                                                  kwargs={'slug_p': product_id})
        return context


@method_decorator(decorators_any, name='dispatch')
class SellerView(TemplateView):
    """Seller page"""
    template_name = "seller/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class AuthView(TemplateView):
    """ Auth page """
    template_name = "auth/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


def client_logout(request):
    logout(request)
    return redirect(reverse('client:index'))
