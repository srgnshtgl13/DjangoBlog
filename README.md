# DjangoBlog
## Description
A blog application with django framework. It includes tree category system and advanced registration system of django.
## Install
* Clone repository<br>
`$ git clone https://github.com/srgnshtgl13/DjangoBlog`<br>
`$ cd DjangoBlog`<br>
* Add python virtual environment in to the repository<br>
`$ python3 -m virtualenv venv`<br>
* Activate python virtual environment<br>
for Linux => `$ source venv/bin/activate`<br>
for Windows => `\Scripts\activate`<br>
* create **requirements.txt** file and add dependencies like below;<br>
```
      astroid==2.2.5
      autopep8==1.4.4
      Django==2.2.8
      django-active-link==0.1.5
      django-ckeditor==5.7.1
      django-cleanup==3.2.0
      django-crispy-forms==1.7.2
      django-js-asset==1.2.2
      django-mptt==0.10.0
      isort==4.3.20
      lazy-object-proxy==1.4.1
      mccabe==0.6.1
      pep8==1.7.1
      Pillow==6.2.0
      pycodestyle==2.5.0
      pylint==2.3.1
      pytz==2019.1
      six==1.12.0
      sqlparse==0.3.0
      typed-ast==1.3.5
      wrapt==1.11.1
```
* Install dependencies<br>
`$ pip install -r requirements.txt`<br>
* Apply Database Migrations<br>
`$ python manage.py migrate`<br>
* start the server<br> 
`$ python manage.py runserver`
## Screens
### Login
![Login](https://user-images.githubusercontent.com/48659439/61064333-3e198980-a40a-11e9-90d6-324ae591c580.jpg)
![Login-2](https://user-images.githubusercontent.com/48659439/61064454-791bbd00-a40a-11e9-8339-fc19b861d53d.jpg)
### Register
![register](https://user-images.githubusercontent.com/48659439/61064493-905aaa80-a40a-11e9-9b59-2a3cc30b5dd8.jpg)
### Profile
![profile-1](https://user-images.githubusercontent.com/48659439/61064554-ab2d1f00-a40a-11e9-95e2-fbb5213f238b.jpg)
![profile-2](https://user-images.githubusercontent.com/48659439/61064555-ab2d1f00-a40a-11e9-9915-1ec131d87a0e.jpg)
### Change Password
![change-password](https://user-images.githubusercontent.com/48659439/61064680-ec253380-a40a-11e9-890f-dc605141f4d8.jpg)
### Blog
![blog-1](https://user-images.githubusercontent.com/48659439/61064601-c5ff9380-a40a-11e9-9d5b-9baf01918f16.jpg)
![blog-2](https://user-images.githubusercontent.com/48659439/61064602-c6982a00-a40a-11e9-9b78-f9170d9584f7.jpg)
### Create Post
![create-post](https://user-images.githubusercontent.com/48659439/61064682-ecbdca00-a40a-11e9-8e87-2dfb34933fc7.jpg)
