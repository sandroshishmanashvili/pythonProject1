from flask import render_template, redirect
from form import Add, login
from ext import app, db
from models import headphones,washingmachin,PC,mobilephones
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker





test = ['washingmachin','PC','headphones','mobilephones']
admin = [True]



@app.route("/pythonProject1/", methods = ["post", "get"])
def home():
    add = Add()
    return render_template("index.html", add = add)

@app.route("/base")
def base():
    admin_index = admin[0]
    return render_template("base.html", admin_index = admin_index)

@app.route("/add_transfer")
def add_transfer():
    return render_template("add_transfer.html")

@app.route("/add/<string:type>", methods = ["post", "get"])
def add(type):
    add = Add()
    c = add.name.data
    info1_name = None
    info2_name = None
    info3_name = None

    if type == 'washingmachin':
        info1_name = 'volume'
        info2_name = 'price'
    elif type == 'PC':
        info1_name = 'resolution - hight'
        info2_name = 'price'
        info3_name = 'resouliton - width'
    elif type == 'headphones':
        info1_name = 'sound qwality'
        info2_name = 'price'
    elif type == 'mobilephones':
        info1_name = 'battary life'
        info2_name = 'price'
    if add.validate_on_submit and c == None:
        print('hello')
    else:
        if type == 'washingmachin':
            password = add.add_password.data
            if password == "DATAsandro!1":
                new_product = washingmachin(name=add.name.data, volume=add.info1.data, price=add.info2.data, image_url=add.image_url.data)
                db.session.add(new_product)
                db.session.commit()
                print(new_product.name)
            return redirect('/add/washingmachin')
        elif type == 'PC':
            password = add.add_password.data
            if password == "DATAsandro!1":
                new_product = PC(name=add.name.data, resolution_h=add.info1.data, resolution_w=add.info3.data, price=add.info2.data, image_url=add.image_url.data)
                db.session.add(new_product)
                db.session.commit()
            return redirect('/add/PC')
        elif type == 'headphones':
            password = add.add_password.data
            if password == "DATAsandro!1":
                new_product = headphones(name=add.name.data, s_q=add.info1.data, price=add.info2.data, image_url=add.image_url.data)
                db.session.add(new_product)
                db.session.commit()
            return redirect('/add/headphones')
        elif type == 'mobilephones':
            password = add.add_password.data
            if password == "DATAsandro!1":
                new_product = mobilephones(name=add.name.data, battery_life=add.info1.data, price=add.info2.data, image_url=add.image_url.data)
                db.session.add(new_product)
                db.session.commit()
            return redirect('/add/mobilephones')




    return render_template("add.html", add=add , type = type, info1_name = info1_name, info2_name = info2_name, info3_name = info3_name)





@app.route("/about_me")
def about_me():
    return render_template("about_me.html")



@app.route("/login")
def login():
    form = login()
    a = form.name.data()
    if form.validate_on_submit() and a != None:
        if form.name.data().lower() == 'sandro' and form.email.data().lower() == 's.shishmanashvili@gmail.com' and form.password.data().lower() == 'paroli123':
            admin.append(True)
            redirect('/')


    return render_template("login.html", login = form)


@app.route("/compare/<string:type>/<string:type1>/<string:type2>", methods = ['post', 'get'])
def compare(type, type1, type2):
    info3_name =None
    info1_3 =None
    info2_3 =None
    im1_1 = None
    im1_2 = None
    im2_1 = None
    im2_2 = None
    if type == 'washingmachin':
        info1_name = 'volume'
        info2_name = 'price'
        type_0 = f'/compare/{type}'
        type_1 = type1
        type_2 = type2
        database = washingmachin.query.all()
        info1_1 = None
        info1_2 = None
        info_img1 = None
        info2_1 = None
        info2_2 = None
        info_img2 = None
        if type_1 and type_2 != '1':
            for item in database:
                if item.name == type1:
                    info1_1 = item.volume
                    info1_2 = item.price
                    info_img1 = item.image_url
                if item.name == type2:
                    info2_1 = item.volume
                    info2_2 = item.price
                    info_img2 = item.image_url
        if info1_1 and info1_2 and info2_1 and info2_2 != None:
            if info1_1 > info2_1:
                im1_1 = '★'
            elif info1_1 < info2_1:
                im2_1 = '★'
            if info1_2 > info2_2:
                im2_2 = '★'
            elif info1_2 < info2_2:
                im1_2 = '★'

    elif type == 'PC':
        info1_name = 'resolution - hight'
        info2_name =  'price'
        info3_name = 'resolution - width'
        type_0 = f'/compare/{type}'
        type_1 = type1
        type_2 = type2
        database = PC.query.all()
        info1_1 = None
        info1_2 = None
        info1_3 = None
        info_img1 = None
        info2_1 = None
        info2_2 = None
        info2_3 = None
        info_img2 = None
        if type_1 and type_2 != '1':
            for item in database:
                if item.name == type1:
                    info1_1 = item.resolution_h
                    info1_2 = item.price
                    info1_3 = item.resolution_w
                    info_img1 = item.image_url
                if item.name == type2:
                    info2_1 = item.resolution_h
                    info2_2 = item.price
                    info2_3 = item.resolution_w
                    info_img2 = item.image_url
        if info1_1 and info1_2 and info2_1 and info2_2 and info1_3 and info2_3 != None:
            if info1_1 > info2_1 and info1_3 > info2_3:
                im1_1 = '★'
            elif info1_1 < info2_1 and info1_3 < info2_3:
                im2_1 = '★'
            if info1_2 > info2_2:
                im2_2 = '★'
            elif info1_2 < info2_2:
                im1_2 = '★'
    if type == 'headphones':
        info1_name = 'sound qwuality'
        info2_name = 'price'
        type_0 = f'/compare/{type}'
        type_1 = type1
        type_2 = type2
        database = headphones.query.all()
        info1_1 = None
        info1_2 = None
        info_img1 = None
        info2_1 = None
        info2_2 = None
        info_img2 = None
        if type_1 and type_2 != '1':
            for item in database:
                if item.name == type1:
                    info1_1 = item.s_q
                    info1_2 = item.price
                    info_img1 = item.image_url
                if item.name == type2:
                    info2_1 = item.s_q
                    info2_2 = item.price
                    info_img2 = item.image_url
        if info1_1 and info1_2 and info2_1 and info2_2 != None:
            if info1_1 > info2_1:
                im1_1 = '★'
            elif info1_1 < info2_1:
                im2_1 = '★'
            if info1_2 > info2_2:
                im2_2 = '★'
            elif info1_2 < info2_2:
                im1_2 = '★'
    if type == 'mobilephones':
        info1_name = 'battary_life'
        info2_name = 'price'
        type_0 = f'/compare/{type}'
        type_1 = type1
        type_2 = type2
        database = mobilephones.query.all()
        info1_1 = None
        info1_2 = None
        info_img1 = None
        info2_1 = None
        info2_2 = None
        info_img2 = None
        if type_1 and type_2 != '1':
            for item in database:
                if item.name == type1:
                    info1_1 = item.battery_life
                    info1_2 = item.price
                    info_img1 = item.image_url
                if item.name == type2:
                    info2_1 = item.battery_life
                    info2_2 = item.price
                    info_img2 = item.image_url
        if info1_1 and info1_2 and info2_1 and info2_2 != None:
            if info1_1 > info2_1:
                im1_1 = '★'
            elif info1_1 < info2_1:
                im2_1 = '★'
            if info1_2 > info2_2:
                im2_2 = '★'
            elif info1_2 < info2_2:
                im1_2 = '★'



    return render_template("compare.html",im1_1=im1_1, im1_2 = im1_2, im2_1 = im2_1, im2_2 = im2_2, type = type, info1_name = info1_name, info2_name = info2_name, info3_name = info3_name, db=database, type_2=type_2, type_1=type_1, type_0=type_0, info1_1 = info1_1, info1_2 = info1_2, info1_3 = info1_3, info2_1 = info2_1, info2_2 = info2_2, info2_3 = info2_3, info_img1 = info_img1, info_img2 = info_img2,)







@app.route("/404")
def error():
    return render_template("404.html")


app.run(debug=True)