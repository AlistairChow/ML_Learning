# -*- coding: utf8 -*-


class Movie():
    """影片实体类"""
    def __init__(self, movie_title, movie_stroyline, poster_image_url, trailer_url):
        """影片实体类初始化
        :param movie_title:标题
        :param movie_stroyline:简介
        :param poster_image_url:封面图片
        :param trailer_url:播放地址
        """
        self.title = movie_title
        self.storyline = movie_stroyline
        self.poster_image_url = poster_image_url
        self.trailer_url = trailer_url
