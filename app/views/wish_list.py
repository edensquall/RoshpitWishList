import datetime
from typing import Any

from flask import render_template, current_app, request, flash, redirect, url_for, jsonify, Blueprint
from flask_login import login_required, current_user
from flask_paginate import Pagination, get_page_args

from app import app
from app.forms import WishForm
from app.models.item import Item
from app.models.property import Property
from app.models.wish import Wish
from app.models.wish_property import WishProperty
from app.services.base_wish_list_service import BaseWishListService

wish_list = Blueprint('wish_list', __name__, url_prefix='/wish_list')


@app.route('/', methods=['GET', 'POST'])
@wish_list.route('/index', methods=['GET', 'POST'])
@login_required
def index(wish_list_service: BaseWishListService) -> Any:
    """
    Wish List主頁，列出使用者所有的Wish
    Args:
        wish_list_service: WishList相關的商業邏輯

    Returns: Any

    """
    wishes = wish_list_service.get_user_wishes(Wish(user_id=current_user.id))

    page, per_page, start = get_page_args(page_parameter='page', per_page_parameter='per_page')
    pagination = Pagination(page=page, per_page=per_page, total=len(wishes), bs_version=4, alignment='center',
                            record_name='wishes')

    img_item_dir_url = current_app.config['IMG_DIR_URL'] or ''

    return render_template('wish_list/index.html', title='Wish List', current_user=current_user,
                           wishes=wishes[start:start + per_page],
                           pagination=pagination, img_item_dir_url=img_item_dir_url)


@wish_list.route('/delete_wish/', defaults={'id': None}, methods=['POST'])
@wish_list.route('/delete_wish/<int:id>', methods=['POST'])
@login_required
def delete_wish(id, wish_list_service: BaseWishListService) -> Any:
    """
    刪除某個Wish
    Args:
        id: Wish id
        wish_list_service: WishList相關的商業邏輯

    Returns: Any

    """
    wish_list_service.delete_wish_from_list(Wish(id=id))
    return redirect(url_for('wish_list.index'))


@wish_list.route('/new_wish/', defaults={'id': None}, methods=['GET', 'POST'])
@wish_list.route('/edit_wish/<id>', methods=['GET', 'POST'])
@login_required
def edit_wish(id, wish_list_service: BaseWishListService) -> Any:
    """
    新增/修改某個Wish
    Args:
        id: Wish id
        wish_list_service: WishList相關的商業邏輯

    Returns: Any

    """
    obj = wish_list_service.get_wish_by_id(Wish(id=id))
    if obj:
        obj.item_type = obj.item.type

        if obj.item and obj.item.properties:

            num_of_types = max(property.type for property in obj.item.properties)

            current_types = [wish_property.property.type for wish_property in obj.wish_properties]
            for i in range(num_of_types):
                if i + 1 not in current_types:
                    obj.wish_properties.insert(i, WishProperty())

    form = WishForm(obj=obj)

    # bind item type
    item_typies = wish_list_service.get_all_item_types()
    form.item_type.choices = [(item_type.id, item_type.name) for item_type in item_typies]
    form.item_type.choices.insert(0, ('', 'Choose'))

    # bind item
    items = wish_list_service.get_all_these_types_of_items(Item(type=form.item_type.data))
    form.item_id.choices = [(item.id, item.name) for item in items]
    form.item_id.choices.insert(0, ('', 'Choose'))

    # bind property
    properties = wish_list_service.get_all_the_property_of_this_item(Property(item_id=form.item_id.data))

    if properties:
        num_of_types = max(property.type for property in properties)

        for i in range(num_of_types):
            if len(form.wish_properties.entries) <= i or len(form.wish_properties.entries) == 0:
                form.wish_properties.append_entry()
            form.wish_properties.entries[i].form.property_id.choices.insert(0, ('', 'Any', {'tip': ''}))

        [form.wish_properties.entries[property.type - 1].form.property_id.choices.append((property.id, property.name, {
            'tip': '★' if property.is_ability else (f'{str(property.min)} - {str(property.max)}'
                                                    if (property.min and property.max) else '>=')}))
         for property in properties]

        form.wish_properties.entries[0].form.property_id.label.text = 'Property'
        form.wish_properties.entries[0].form.roll.label.text = 'Roll'

    if request.method == 'POST' and form.validate_on_submit():

        wish = Wish(
            id=id,
            currency=form.currency.data,
            min_level=form.min_level.data,
            max_bid=form.max_bid.data,
            max_buyout=form.max_buyout.data,
            user_id=current_user.id,
            item_id=form.item_id.data,
            create_date=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            modify_date=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        )

        for property_form in form.wish_properties.data:
            if property_form['property_id'] != '':
                wish_property = WishProperty(
                    roll=property_form['roll'],
                    property_id=property_form['property_id'],
                    wish_id=id,
                    create_date=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                    modify_date=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
                wish.wish_properties.append(wish_property)

        wish_list_service.add_new_wish(wish)

        flash('Save success', 'success')
        return redirect(url_for('wish_list.index'))

    return render_template('wish_list/edit_wish.html', form=form, current_user=current_user,
                           title='New Wish' if id is None else 'Edit Wish')


@wish_list.route('/item/', defaults={'type': None}, methods=['POST'])
@wish_list.route('/item/<type>')
@login_required
def item(type, wish_list_service: BaseWishListService) -> Any:
    """
    取得所有某個類型的道具
    Args:
        type: 道具類型
        wish_list_service: WishList相關的商業邏輯

    Returns: Any

    """
    items = wish_list_service.get_all_these_types_of_items(Item(type=type))
    items_array = [{'id': item.id, 'name': item.name} for item in items]
    items_array.insert(0, {'id': '', 'name': 'Choose'})

    return jsonify({'items': items_array})


@wish_list.route('/property/', defaults={'item_id': None}, methods=['POST'])
@wish_list.route('/property/<item_id>')
@login_required
def property(item_id, wish_list_service: BaseWishListService) -> Any:
    """
    取得某個道具的屬性
    Args:
        item_id: 道具id
        wish_list_service: WishList相關的商業邏輯

    Returns: Any

    """
    properties = wish_list_service.get_all_the_property_of_this_item(Property(item_id=item_id))

    property_array = []

    if properties:
        num_of_types = max(property.type for property in properties)

        [property_array.append({'id': '', 'name': 'Any', 'type': i + 1, 'tip': '>='}) for
         i in range(num_of_types)]

        [property_array.append({'id': property.id, 'name': property.name, 'type': property.type,
                                'tip': '★' if property.is_ability else (f'{str(property.min)} - {str(property.max)}'
                                                                        if (property.min and property.max) else '>=')})
         for property in properties]

    return jsonify({'properties': property_array})
