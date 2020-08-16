# -*- coding: utf-8 -*-
import os
import json
import random
from datetime import datetime, timedelta

from gevent.pywsgi import WSGIServer
from flask import Flask, request, render_template, session, redirect, url_for, make_response, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SECRET_KEY'] = 'wojiushishijianguanlidashi'  # 设置session加密的密钥
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(hours=2)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///webhw.db'

db = SQLAlchemy(app)

class User(db.Model):
    '''用户'''
    __tablename__ = 'user'
    _id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(45), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    phone = db.Column(db.String(45), nullable=True)
    password = db.Column(db.String(45), nullable=False)
    create_time = db.Column(db.DateTime, default=datetime.now)

    def header(self):
        header = {}
        header['name'] = self.name
        cartcount = Cart.query.filter(Cart.userid == self._id).count()
        header['cartcount'] = cartcount
        return header


class Item(db.Model):
    '''商品'''
    __tablename__ = 'item'
    _id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    price = db.Column(db.Float, nullable=False)
    image = db.Column(db.Text)
    desc = db.Column(db.Text)
    time = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)


class Cart(db.Model):
    '''购物车'''
    __tablename__ = "cart"
    _id = db.Column(db.Integer, primary_key=True)
    userid = db.Column(db.Integer, db.ForeignKey("user._id", ondelete='cascade'))
    user = db.relationship("User", backref=db.backref("the_Cart"))
    itemid = db.Column(db.Integer, db.ForeignKey("item._id"))
    item = db.relationship('Item', backref=db.backref("the_Cart"))
    count = db.Column(db.Integer)


class Order(db.Model):
    '''订单'''
    __tablename__ = "order"
    _id = db.Column(db.Integer, primary_key=True)
    userid = db.Column(db.Integer, db.ForeignKey("user._id", ondelete='cascade'))
    user = db.relationship("User", backref=db.backref("the_Order"))


class OrderItem(db.Model):
    '''订单项'''
    __tablename__ = "order_item"
    _id = db.Column(db.Integer, primary_key=True)
    userid = db.Column(db.Integer, db.ForeignKey("user._id", ondelete='cascade'))
    user = db.relationship("User", backref=db.backref("the_Orderitem"))
    itemid = db.Column(db.Integer, db.ForeignKey("item._id"))
    item = db.relationship("Item", backref=db.backref("the_Orderitem"))
    count = db.Column(db.Float, nullable=False)


db.create_all()
import init

@app.route('/')
def index():
    user = {}
    if 'id' in session and User.query.get(session['id']):
        dbuser = User.query.get(session['id'])
        user['name'] = dbuser.name
        cartcount = Cart.query.filter(Cart.userid == dbuser._id).count()
        user['cartcount'] = cartcount

    slides = [{'href': "product.html", 'url': url_for('static', filename="image/banner/01.png")},
              {'href': "product.html", 'url': url_for('static', filename="image/banner/02.png")},
              {'href': "product.html", 'url': url_for('static', filename="image/banner/03.png")},
              {'href': "product.html", 'url': url_for('static', filename="image/banner/04.png")},
              {'href': "product.html", 'url': url_for('static', filename="image/banner/05.png")}]

    list1 = Item.query.limit(8).all()
    list2 = Item.query.offset(8).limit(10).all()

    headerlist = [[Item.query.offset(random.randint(0, 13)).limit(random.randint(3, 6)).all()
                   for col in range(random.randint(2, 4))] for i in range(7)]

    return render_template('index.html',
                           slides=slides,
                           user=user,
                           list1=list1,
                           list2=list2,
                           headerlist=headerlist)


@app.route('/product')
@app.route('/product/<int:_id>')
def product(_id=0):
    user = {}
    if 'id' in session and User.query.get(session['id']):
        user = User.query.get(session['id']).header()
    item = Item.query.filter(Item._id == _id).first()
    product = {}
    product['name'] = item.name
    product['desc'] = item.desc
    product['price'] = item.price
    product['slides'] = [{'url': item.image}]
    product['images'] = [{'url': item.image}, {'url': item.image}, {'url': item.image}]

    headerlist = [[Item.query.offset(random.randint(0, 13)).limit(random.randint(3, 6)).all()
                   for col in range(random.randint(2, 4))] for i in range(7)]

    return render_template('product.html',
                           user=user,
                           product=product,
                           headerlist=headerlist)


@app.route('/cart')
def cart():
    if 'id' not in session or not User.query.get(session['id']):
        return redirect(url_for('login', src=request.url))
    dbuser = User.query.get(session['id'])
    carts = Cart.query.filter(User._id == session['id']).all()
    return render_template('cart.html',
                           user=dbuser.header(),
                           carts=carts)


@app.route('/order')
def order():
    if 'id' not in session or not User.query.get(session['id']):
        return redirect(url_for('login', src=request.url))
    dbuser = User.query.get(session['id'])
    _id = request.args.get('id')
    # order = Order.query.filter(User._id == session['id']).first()
    # if not _id:
    # _id = order._id
    orderItem = OrderItem.query.filter(OrderItem.userid == session['id']).all()
    orderItemShow = []
    for oditem in orderItem:
        item = Item.query.filter(Item._id == oditem.itemid).first()
        if not item:
            continue
        itemShow = {
            'id': item._id,
            'name': item.name,
            'image': item.image,
            'price': item.price,
            'count': oditem.count
        }
        orderItemShow.append(itemShow)
    headerlist = [[Item.query.offset(random.randint(0, 13)).limit(random.randint(3, 6)).all()
                   for col in range(random.randint(2, 4))] for i in range(7)]
    return render_template('order.html',
                           user=dbuser.header(),
                           headerlist=headerlist,
                           order=order,
                           orderItem=orderItemShow)


@app.route('/login')
def login():
    return render_template('login.html',
                           src=request.args.get('src', ''))


@app.route('/register')
def register():
    return render_template('register.html')


@app.route('/api/login', methods=["POST"])
def api_login():
    email = request.form.get('email')
    password = request.form.get('password')
    user = User.query.filter(User.email == email).first()
    if user and user.password == password:
        session['id'] = user._id
        return jsonify({'status': 'ok', 'location': url_for('index')})
    else:
        return jsonify({'status': 'error'}), 400


@app.route('/api/logout', methods=["POST"])
def api_logout():
    if 'id' in session and User.query.get(session['id']):
        session.pop('id')
        return jsonify({'status': 'ok'})
    return jsonify({'status': 'error'}), 400


@app.route('/api/register', methods=["POST"])
def api_register():
    email = request.form.get('email')
    name = request.form.get('name')
    password = request.form.get('password')
    if User.query.filter(User.email == email).first():
        return jsonify({'status': '邮箱重复'}), 400
    elif User.query.filter(User.name == name).first():
        return jsonify({'status': '用户名重复'}), 400
    else:
        user = User(name=name, email=email, password=password)
        db.session.add(user)
        db.session.commit()
        session['id'] = user._id
        return jsonify({'status': 'ok', 'location': url_for('index')})


@app.route('/api/addcart', methods=["POST"])
def api_addcart():
    if 'id' not in session or not User.query.get(session['id']):
        return jsonify({'status': 'error', 'location': url_for('login')}), 400
    itemid = request.form.get('itemid')
    count = float(request.form.get('count'))
    exist = Cart.query.filter(Cart.userid == session['id']).filter(Cart.itemid == itemid).first()
    if exist:
        exist.count += count
    else:
        cart = Cart(userid=session['id'], itemid=itemid, count=count)
        db.session.add(cart)
    db.session.commit()
    return jsonify({'status': 'ok'})


@app.route('/api/delcart', methods=["POST"])
def api_delcart():
    if 'id' not in session or not User.query.get(session['id']):
        return jsonify({'status': 'error', 'location': url_for('login')}), 400
    itemid = request.form.get('itemid')
    Cart.query.filter(Cart.userid == session['id']).filter(Cart.itemid == itemid).delete()
    db.session.commit()
    return jsonify({'status': 'ok'})


@app.route('/api/addorder', methods=["POST"])
def api_addorder():
    if 'id' not in session or not User.query.get(session['id']):
        return jsonify({'status': 'error', 'location': url_for('login')}), 400
    items = request.json.get('items')
    # order = Order(userid=session['id'])
    # db.session.add(order)
    # db.session.flush()
    for item in items:
        orderItem = OrderItem(userid=session['id'], itemid=item.get('id'), count=item.get('count'))
        db.session.add(orderItem)
        cart = Cart.query.filter(Cart.userid == session['id']).filter(Cart.itemid == item.get('id')).delete()
    db.session.commit()
    return jsonify({'status': 'ok', 'location': url_for('order')})


# @app.route('/api/order')
# def api_order():
#     if 'id' not in session or not User.query.get(session['id']):
#         return jsonify({'status': 'error', 'location': url_for('login')}), 400
#     order = Order.query.filter(User._id == session['id']).all()
#     return jsonify({'status': 'ok', 'data': order})


@app.route('/api/orderItem')
def api_orderItem():
    if 'id' not in session or not User.query.get(session['id']):
        return jsonify({'status': 'error'}), 400
    # orderId = request.form.get('orderId')
    # if not Order.query.filter(User._id == session['id']).filter(Order._id == orderId).first():
    #     return jsonify({'status': 'error', 'res': 'sj is NG!'}), 400
    orderItem = OrderItem.query.filter(OrderItem.userid == session['id']).all()
    return jsonify({'status': 'ok', 'data': orderItem})


@app.route('/api/cart')
def api_cart():
    if 'id' not in session or not User.query.get(session['id']):
        return jsonify({'status': 'error'}), 400
    cart = Cart.query.filter(User._id == session['id']).all()
    return jsonify({'status': 'ok', 'data': cart})


@app.errorhandler(404)
def not_foundPage(error):
    return redirect(url_for('index'))


if __name__ == '__main__':
    httpserver = WSGIServer(('', 8000), app)
    httpserver.serve_forever()
