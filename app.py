# from Demos.win32ts_logoff_disconnected import username, session
from flask import Flask, render_template,session
# from pandas.io.formats.format import return_docstring
# from sqlalchemy.ext.asyncio import session

import logging
# from database import create_tables
from database import db, init_db
from models import User, Dish, Order, OrderItem
from controllers.auth import auth_bp
from controllers.dishes import dish_bp
from controllers.order import order_bp

logging.basicConfig(level=logging.INFO,
                    filename='app.log',
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    encoding='utf-8'
                    )
logger = logging.getLogger(__name__)

app = Flask(__name__)
app.register_blueprint(auth_bp)
app.register_blueprint(dish_bp)
app.register_blueprint(order_bp)
app.secret_key = 'dev-secret-key'
init_db()
db.connect()
db.create_tables([User, Dish, Order, OrderItem])
db.close()


@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/dashboard')
def dashboard():
    if 'username'  not in session:
        return render_template('index.html')
    return render_template('dashboard.html')



if __name__ == '__main__':
    app.run(debug=True,port=5001)
    # logger.info('服务启动，监听 http://127.0.0.1:5001')
