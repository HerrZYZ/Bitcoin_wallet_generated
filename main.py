```python
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_socketio import SocketIO
from user import User
from wallet import Wallet
from transaction import Transaction
from notification import Notification
import sqlite3

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

users = {}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        email = request.form.get('email')
        user = User(username, password, email)
        users[username] = user
        flash('Registration successful. Please login.')
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = users.get(username)
        if user and user.check_password(password):
            flash('Login successful.')
            return redirect(url_for('wallet', username=username))
        flash('Invalid username or password.')
    return render_template('login.html')

@app.route('/wallet/<username>', methods=['GET', 'POST'])
def wallet(username):
    user = users.get(username)
    if not user:
        flash('User not found.')
        return redirect(url_for('index'))
    if request.method == 'POST':
        amount = float(request.form.get('amount'))
        recipient = request.form.get('recipient')
        try:
            transaction = user.wallet.send_bitcoin(amount, recipient)
            flash('Transaction successful.')
            socketio.emit('balance change', {'balance': user.wallet.balance}, room=username)
        except Exception as e:
            flash(str(e))
    return render_template('wallet.html', user=user)

@app.route('/transaction/<username>')
def transaction(username):
    user = users.get(username)
    if not user:
        flash('User not found.')
        return redirect(url_for('index'))
    return render_template('transaction.html', transactions=user.wallet.transactions)

@app.route('/notification/<username>')
def notification(username):
    user = users.get(username)
    if not user:
        flash('User not found.')
        return redirect(url_for('index'))
    return render_template('notification.html', notifications=user.notifications)

if __name__ == '__main__':
    socketio.run(app)
```
