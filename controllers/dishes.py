from models import Order, OrderItem, Dish
from models.dish import Dish
from flask import Blueprint, jsonify, request, session

dish_bp = Blueprint('dishes',__name__, url_prefix='/dishes')

@dish_bp.route('/query/dishes_list')
def query_all():
    dishes =Dish.select().where(Dish.is_active == 1)
    data_list = []
    for dish in dishes:
        data_list.append(dish.dump())
    return jsonify({
        'success':True,
        'message':"查询成功",
        'dishlist':data_list
    })


@dish_bp.route('/query/dishes_list/<int:id>')
def query_by_id(id):

    query = OrderItem.select(OrderItem,Order).join(Order,on = (OrderItem.order == Order.id), attr = 'order' ).where(Order.table_no == id).where(Order.status == 0)
    if not query:
        return jsonify({
            'success':False,
            'message':"没有2订单"
        })
    order = Order.select().where(Order.table_no == id).where(Order.status == 0).first()
    data_list = []
    for item in query:
        data_list.append(item.dump())
    return jsonify({
        'success':True,
        "message":"订单查询成功",
        'dishlist':data_list,
        'amount':order.total_amount
    })
@dish_bp.route('/delete',methods=['Delete'])

def delete():
    orderItemId = request.args.get('orderItemId')
    orderItem = OrderItem.select().where(OrderItem.id == orderItemId).first()
    order = Order.select().where(Order.id == orderItem.order).first()
    order.total_amount -= orderItem.sub_total
    order.save()

    OrderItem.delete().where(OrderItem.id == orderItemId).execute()
    return jsonify({
        'success':True,
    })

@dish_bp.route('/addDish',methods=['POST'])
def add_dish():
    data = request.get_json()
    dishName = data['dishName']
    price = data['price']
    cost = data['cost']
    if not dishName:
        return jsonify({
            'success':False,
            "message":"名称不能为空"
        })
    dish = Dish.create(name = dishName,price = price,cost = cost,is_active = 1)
    return jsonify({
        'success':True,
        "message":dish.name
    })

@dish_bp.route('/query/dish_one/<dish_name>')
def query_by_dishid(dish_name):
    dish = Dish.select().where(Dish.name == dish_name).first()
    if not dish:
        return jsonify({
            'success':False,
            "message": "没有查询到"
        })
    return jsonify({
        'success':True,
        "message":"查询成功",
        'data':dish.dump()
    })