
from flask import jsonify,session, Blueprint, request
import logging

from models.dish import Dish
from models.order import Order
from models.order_item import OrderItem

order_bp = Blueprint('orders',__name__,url_prefix='/orders')
logger = logging.getLogger(__name__)

@order_bp.route('/dishes_order',methods=['POST'])
def order():
    data = request.get_json()
    dishId = data['dishId']
    tableId = data['tableId']
    userId = session['user_id']
    count = data['count']
    if not tableId:
        return jsonify({
            'success':False,
            "message":"先输入编号"
        })
    dish = Dish.select().where(Dish.id == dishId).first()
    order =Order.select().where((Order.table_no == tableId) & (Order.status == 0)).first()

    if not order:
        order = Order.create(table_no=tableId, user = userId, status = 0, total_amount =0)
        OrderItem.create(order = order, dish = dish, dish_name = dish.name, price = dish.price, quantity = count,sub_total = dish.price * int(count))
        order.total_amount += dish.price * int(count)
        order.save()
        logger.info('用户 %s 对桌号 %s 新建订单: %s x%s, 金额 %s',
                    userId, tableId, dish.name, count, dish.price * int(count))
        return jsonify({
            'success':True,
            'message':"success"
        })
    else:

        OrderItem.create(order=order, dish=dish, dish_name=dish.name, price=dish.price, quantity=count,
                         sub_total=dish.price * int(count))
        order.total_amount += dish.price * int(count)
        order.save()
        return jsonify({
            'success':True,
            'message':"继续下单成功"
        })

@order_bp.route('/buy',methods=['POST'])
def buy():
    data = request.get_json()
    tableId = data['tableId']
    order = Order.select().where((Order.table_no == tableId)).where(Order.status == 0).first()
    if not order:
        return jsonify({
            'success':False,
            'message':"没有需要支付的订单"
        })
    Order.update(status = 1).where(Order.table_no == tableId).execute()
    return jsonify({
        'success':True,
        'message':"success"
    })