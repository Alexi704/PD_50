import json
from pprint import pprint as pp
import logging
from json import JSONDecodeError


class Posts:
    def __init__(self, path):
        self.path = path

    def get_posts_all(self):
        with open(self.path, 'r', encoding='utf-8') as my_file:
            insta_posts = json.load(my_file)
        return insta_posts

    def get_posts_by_user(self, user_name):
        posts_list = []
        insta_posts = self.get_posts_all()
        for post in insta_posts:
            if user_name.lower() in post['poster_name'].lower():
                posts_list.append(post)
        return posts_list

    def get_comments_by_post_id(self, post_id):
        insta_posts = self.get_posts_all()
        comments_list = []
        for post in insta_posts:
            if post_id == post['post_id']:
                comments_list.append(post['comment'])
        return comments_list

    def search_for_posts(self, query):
        insta_posts = self.get_posts_all()
        query_list = []
        lowered_query = query.lower()
        for post in insta_posts:
            if lowered_query in post['content'].lower().strip():
                query_list.append(post)
        return query_list

    def get_post_by_pk(self, pk):
        insta_posts = self.get_posts_all()
        for post in insta_posts:
            if pk == post['pk']:
                return post
