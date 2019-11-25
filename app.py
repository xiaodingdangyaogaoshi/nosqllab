from flask import Flask
from pymongo import MongoClient
import datetime
import os
import random
from functools import wraps
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import *

from flask_bootstrap import Bootstrap
from flask import Flask, render_template, request, redirect, url_for, session, flash

app = Flask(__name__)


@app.route('/',methods=['GET','POST'])
def index():
    db=MongoDBlink()
    student=db.student
    course=db.course
    teacher=db.teacher
    if request.method=="POST":
        sid=request.form.get("SID")
        sname=request.form.get("SNAME")
        ssex=request.form.get("SSEX")
        age=request.form.get("AGE")
        birthday=request.form.get("BIRTHDAY")
        sdname=request.form.get("SDNAME")
        sclass=request.form.get("SCLASS")

        tid=request.form.get("TID")
        tname=request.form.get("TNAME")
        tsex=request.form.get("TSEX")
        tage=request.form.get("TAGE")
        tdname=request.form.get("TDNAME")

        cid=request.form.get("CID")
        cname=request.form.get("CNAME")
        fcid=request.form.get("FCID")
        credit=request.form.get("CREDIT")

        bs=request.form.get("charustudent")
        bt=request.form.get("charuteacher")
        bc=request.form.get("charucourse")
        if bs !=None:
            student_data={
                'SID':sid,
                'NAME':sname,
                'SEX':ssex,
                'AGE':age,
                'BIRTHDAY':birthday,
                'DNAME':sdname,
                'CLASS':sclass
            }
            task_sresult=student.insert_one(student_data)
            print(task_sresult)
        if bt !=None:
            teacher_data={
                'TID':tid,
                'NAME':tname,
                'SEX':tsex,
                'AGE':tage,
                'DNAME':tdname
            }
            task_tresult=teacher.insert_one(teacher_data)
            print(task_tresult)
        if bc!=None:
            course_data={
                'CID':cid,
                'NAME':cname,
                'FCID':fcid,
                'CREDIT':credit
            }
            task_cresult=course.insert_one(course_data)
            print(task_cresult)

    return render_template("index.html")
@app.route('/lab5',methods=['GET','POST'])
def lab5():
    u=""
    return render_template("lab5update.html",u=u)
@app.route('/lab6',methods=['GET','POST'])
def lab6():
    return render_template("lab6.html")
@app.route('/addcourse',methods=['GET','POST'])
def addcourse():
    u=""
    return render_template("addcourse.html",u=u)
@app.route('/lab4_charu/<state>',methods=['GET','POST'])
def lab4_charu(state):
    print(type(state))
    print("llll")
def MongoDBlink():
    username = 'ting'
    password = 'zys9970304'
    host = '152.136.81.178:27017'
    mongo_url = 'mongodb://{}/'.format(host)
    mg = MongoClient(mongo_url)
    mg.nosql.authenticate(username, password, mechanism='SCRAM-SHA-1')
    db = mg['nosql']
    return db

if __name__ == '__main__':
    app.run()
