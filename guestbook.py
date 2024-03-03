from datetime import datetime
from dateutil import tz
from flask import Flask, request, redirect, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from jinja2 import evalcontextfilter, Markup, escape
from flask_login import (UserMixin, LoginManager, login_user, 
                        logout_user, login_required, current_user)
import re

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bbs.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = b'my_very_secret_key'

@app.template_filter()
def datetimefilter(utc):
    utc_zone = tz.gettz('UTC')
    tw_zone = tz.gettz('Asia/Taipei')
    utc = utc.replace(tzinfo=utc_zone)
    tw_time = utc.astimezone(tw_zone)
    return tw_time.strftime('%Y/%m/%d %H:%M')

# 把新行字元（\n）轉換成<br>斷行標籤
# 範例取自：http://flask.pocoo.org/snippets/28/
_paragraph_re = re.compile(r'(?:\r\n|\r|\n){2,}')

@app.template_filter()
@evalcontextfilter
def nl2br(eval_ctx, value):
    result = u'\n\n'.join(u'<p>%s</p>' % p.replace('\n', Markup('<br>\n'))
                          for p in _paragraph_re.split(escape(value)))
    if eval_ctx.autoescape:
        result = Markup(result)
    return result

db = SQLAlchemy(app)

class Guestbook(db.Model):  # 留言板資料表
    id = db.Column(db.Integer, primary_key=True)
    guestname = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    message = db.Column(db.Text, nullable=False)
    icon = db.Column(db.String(10), nullable=False, 
        default='ico1.png')
    postdate = db.Column(db.DateTime, nullable=False,
        default=datetime.utcnow)

    def __repr__(self):
        return 'guestname:{},email:{},postdate:{}'.format(
            self.guestname, 
            self.email,
            self.postdate
        )

class User(UserMixin, db.Model):  # 使用者資料表
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    pwd_hash = db.Column(db.String(80), nullable=False)
    is_admin = db.Column(db.Boolean, nullable=False, default=False)

    def verify_password(self, password):
        """
        驗證密碼
        """
        return check_password_hash(self.pwd_hash, password)

    @property
    def password(self):
        """
        避免密碼被外部程式存取
        """
        raise AttributeError('無法讀取password屬性')

    @password.setter
    def password(self, password):
        """
        將密碼加密
        """
        self.pwd_hash = generate_password_hash(password)
    
    def __repr__(self):
        return f'name:{self.name},email:{self.email}'

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'admin'

@login_manager.user_loader
def load_user(user_id):
    print('使用者id：', user_id)
    return User.query.get(int(user_id))

@app.route('/')
def index():
    gb = Guestbook.query.all()
    return render_template("index.html", books=gb)

@app.route("/add_msg", methods=["POST"])
def add_msg():
    try:
        guestname = request.form["guestname"]
        email = request.form["email"]
        message = request.form["message"]
        icon = request.form["icon"]
        gb = Guestbook(guestname=guestname, email=email,
                        message=message, icon=icon)
        db.session.add(gb)
        db.session.commit()
    except Exception as e:
        print("出錯啦～無法新增留言！")
        print(e)
    return redirect("/")

@app.route('/admin')
def admin():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    email = request.form['email']
    pwd = request.form['password']
    user = User.query.filter_by(email=email).first()

    if not user:
        return '找不到此使用者！'
    elif not user.verify_password(pwd):
        return '密碼錯誤！'
    elif not user.is_admin:
        return '你不是管理員！'

    login_user(user)

    if current_user.is_active:
        usr = current_user.name

    gb = Guestbook.query.all()
    return render_template('list.html', books=gb, user=usr)

@app.route('/list')
@login_required
def list_db():
    if current_user.is_active:
        usr = current_user.name

    gb = Guestbook.query.all()
    return render_template('list.html', books=gb, user=usr)

@app.route("/delete", methods=["POST"])
@login_required
def delete():
    id = request.form["id"]
    msg = Guestbook.query.filter_by(id=id).first()
    db.session.delete(msg)
    db.session.commit()
    
    return 'ok!'

@app.route('/update')
@login_required
def update():
    id = request.args.get('id')
    gb = Guestbook.query.filter_by(id=id).first()

    return render_template('update.html', book=gb)

@app.route("/update_msg", methods=["POST"])
@login_required
def update_msg():
    try:
        id = request.form["id"]
        guestname = request.form["guestname"]
        email = request.form["email"]
        message = request.form["message"]
        icon = request.form["icon"]

        b = Guestbook.query.filter_by(id=id).first()
        b.email = email
        b.guestname = guestname
        b.message = message
        b.icon = icon
        db.session.commit()
    except Exception as e:
        print("出錯啦～無法更新留言！")
        print(e)
    return redirect(url_for('list_db'))

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run('0.0.0.0', 80, debug=True)