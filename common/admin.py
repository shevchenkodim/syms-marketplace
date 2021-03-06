from django.contrib import admin

from common.cart.cart_items import CartItems
from common.products.categories.categories import CategoryModel
from common.clients.sliders.main_sliders import MainCarouselModel
from common.products.characteristic.characteristic import CharacteristicAttributes, CharacteristicProduct, \
    CharacteristicHandbookDict
from common.products.comments.comments import ProductComment
from common.products.product.product import Product
from common.products.product.product_description import ProductDescription
from common.products.product.product_image import ProductImage
from common.seller.seller import SellerModel
from common.models import User
from common.access.access import AccessRole, UserRole
from common.dictionaries.dictionaries import BrandDict, UnitDict, CurrencyDict, \
    TextSizeDict, TextColorDict, BackgroundColorDict, IconDict
from common.geo.geo import CityModel, CountryModel, DistrictModel, IpAddressModel
from common.geo.user_location_history import UserLocationHistoryModel


@admin.register(CartItems)
class CartItemsAdmin(admin.ModelAdmin):
    pass


@admin.register(ProductDescription)
class ProductDescriptionAdmin(admin.ModelAdmin):
    list_display = ('id', 'product_id', 'title', 'description', 'order_id')


@admin.register(UserLocationHistoryModel)
class UserLocationHistoryModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_id', 'ip_address', 'city_id', 'district_id', 'country_id', 'date_add')


@admin.register(IpAddressModel)
class IpAddressModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'ip_address')


@admin.register(CityModel)
class CityModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'code')


@admin.register(DistrictModel)
class CityModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'code')


@admin.register(CountryModel)
class CityModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'code')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'code')


@admin.register(ProductComment)
class ProductCommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'owner_id', 'text', 'likes_count', 'dislikes_count', 'rating_stars', 'date_time_add')


@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'image', 'item_alt', 'product_id')


@admin.register(UnitDict)
class UnitDictAdmin(admin.ModelAdmin):
    list_display = ('id', 'value', 'code')


@admin.register(CharacteristicHandbookDict)
class CharacteristicHandbookDictAdmin(admin.ModelAdmin):
    list_display = ('id', 'value', 'code', 'category_id')


@admin.register(CharacteristicAttributes)
class CharacteristicAttributesAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'field_type')


@admin.register(CharacteristicProduct)
class CharacteristicProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'value', 'product_id', 'attribute_id')


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'phone', 'first_name', 'last_name', 'is_active', 'date_joined')


@admin.register(AccessRole)
class AccessRoleAdmin(admin.ModelAdmin):
    list_display = ('id', 'role', 'code_role')


@admin.register(UserRole)
class UserRoleAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'role')


@admin.register(CategoryModel)
class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'code_name', 'slug', 'is_active')


@admin.register(MainCarouselModel)
class MainCarouselModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'order_id', 'item_alt', 'item_image')


@admin.register(SellerModel)
class SellerModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'code_name')


@admin.register(BrandDict)
class BrandDictAdmin(admin.ModelAdmin):
    list_display = ('id', 'value', 'code')


@admin.register(CurrencyDict)
class CurrencyDictAdmin(admin.ModelAdmin):
    list_display = ('id', 'value', 'code')


admin.site.register(TextSizeDict)
admin.site.register(TextColorDict)
admin.site.register(BackgroundColorDict)
admin.site.register(IconDict)
