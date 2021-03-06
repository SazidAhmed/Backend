from rest_framework import serializers

from .models import Category, Menu, MenuCategory, ItemCategory

from v1.shop.models import ShopBranch


class CategoryCreateSerializer(serializers.ModelSerializer):
    branch = serializers.PrimaryKeyRelatedField(queryset=ShopBranch.objects.all())

    class Meta:
        model = Category
        fields = ('uuid', 'branch', 'name', 'created_at', 'updated_at')
        read_only_fields = 'created_at', 'updated_at'


class CategoryUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('uuid', 'name', 'created_at', 'updated_at')
        read_only_fields = 'created_at', 'updated_at'


class MenuCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Menu
        fields = ('uuid', 'name', 'start_time', 'end_time', 'branch', 'created_at', 'updated_at')
        read_only_fields = 'created_at', 'updated_at'


class MenuUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Menu
        fields = ('uuid', 'name', 'start_time', 'end_time', 'created_at', 'updated_at')
        read_only_fields = 'created_at', 'updated_at'


class MenuCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = MenuCategory
        fields = ('__all__')
        read_only_fields = 'created_at', 'updated_at'


class ItemCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = ItemCategory
        fields = ('__all__')
        read_only_fields = 'created_at', 'updated_at'
