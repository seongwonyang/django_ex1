from django.shortcuts import render, get_object_or_404
# Bookmark 테이블의 데이터를 가져오기 위해 models.py에서 Bookmark 클래스를 import
from .models import Bookstore
from django.db import connection

# Create your views here.
def BookstoreListView(request):
    try:
        cursor = connection.cursor()

        strSql = "SELECT code, name, author FROM bookstore_bookstore"
        result = cursor.execute(strSql)
        datas = cursor.fetchall()

        connection.commit()
        connection.close()

        books = []
        for data in datas:
            row = {'code': data[0],
                   'name': data[1],
                   'author': data[2]}

            books.append(row)

    except:
        connection.rollback()
        print("Failed selecting in BookListView")

    return render(request, 'bookstore_list.html', {'books': books})


def BookstoreDetailView(request, pk):
    """
    Bookmark 테이블의 특정 Row만 가져오는 방법 두 가지
    1. get_object_or_404(): 객체가 존재하지 않을 때 Http 404 예외를 발생
    - 하나의 오브젝트만 받을 수 있으므로 주의
    -  Django 모델을 첫번째 인자로 받고, 키워드 인수들을 모델 관리자의 get() 함수에 넘김

    2. models.py에 정의된 모델 클래스를 직접 사용
    """
    try:
        cursor = connection.cursor()

        strSql = "SELECT code, name, author, price, url FROM bookstore_bookstore WHERE code = (%s)"
        result = cursor.execute(strSql, (pk,))
        datas = cursor.fetchall()

        connection.commit()
        connection.close()

        book = {'code': datas[0][0],
                'name': datas[0][1],
                'author': datas[0][2],
                'price': datas[0][3],
                'url': datas[0][4]}

    except:
        connection.rollback()
        print("Failed selecting in BookListView")

    return render(request, 'bookstore.html', {'book': book})