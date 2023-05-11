from flask import Flask, render_template, request, redirect, send_file
from crawler import book_list

app = Flask("Bookmate")
db = { "student_number" : [20220001, 20221234], 
      }


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/UserData", methods=["GET", "POST"])
def inputData():
    if request.method == "POST":
        id = request.form.get("ID")
        pw = request.form.get("PASSWORD")

    if (id == "" or pw == "") or (id == None or pw == None):
        # return "아이디와 비밀번호가 비어있습니다."
        return redirect("/")
    
    if len(id) != 8:
        return redirect("/")
    id, pw = int(id), str(pw)
    
    return f"아이디: {id}, 비밀번호: {pw}, 학번 길이: {len(str(id))}"
    return render_template("SearchResult.html")

# 이스터 에그, html 연습용
@app.route("/EarthAndMoon")
def EarthAndMoon():
    return render_template("EarthAndMoon.html")

app.run(debug=True)