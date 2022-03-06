## **Functional Requirements**
Create CRUD API to manage news posts. The post will have the next fields: title, link, creation date, amount of upvotes, author-name
Posts should have CRUD API to manage comments on them. The comment will have the next fields: author-name, content, creation date
There should be an endpoint to upvote the post
We should have a recurring job running once a day to reset post upvotes count

## **Technical Requirements**

- Code should be written with Python 3
- REST API should be Django and Django REST Framework based
- API should be well documented with Postman collection. Make sure to use [Postman environments and variables](https://learning.postman.com/docs/postman/variables-and-environments/variables/#understanding-variables-and-environments), so you can switch between local API and deployed version. Add Postman collection link to the README
- API has to run as a Docker container. API + Postgres should be launched with docker-compose

## **Conditions**

- Task usually takes **from 4 to 6 hours**. If you need more time, you're good to take it and it's appreciated, but results should be sent **no later than 48 hours after the start**
- Skills to write clean business logic and apply best practices are important
- The challenge code should be pushed to the **GitHub** repository. Please send us a link to the repository right after that. Thanks!

If you have any questions about challenge details, ask for more information, it's appreciated.

Have a good luck and looking forward to work with you!

# HackerNews Tutorial
**Backend Dependencies/Packages
Create a virtualenv for Python 3
1.Head over to the terminal and run:**
```
virtualenv env 
```
**Replace env wih the actual name you want to give your Python virtual environment.
2.Activate the virtualenv**
```
source env/bin/activate
```

<h3>First we need to install all libraries
</h3>

```
!pip install -r requirements.txt
```
<h3> Start docker container</h3>

```
docker-compose up --build
```
 <h3> Link to HEROKU</h3> 
 https://haker-news-kiri.herokuapp.com/
 
<h3> Test Postman</h3>  

https://haker-news-kiri.herokuapp.com/api/v1/post/ # create post, list post, update post, delete post

https://haker-news-kiri.herokuapp.com/api/v1/comment/ # create comment, list comment, update comment, delete comment

