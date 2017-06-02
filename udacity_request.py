# -*- coding:utf-8 -*-
'''
review counter
'''
import requests


class ReviewRequest():
    """
    Class that request review data
    """
    def __init__(self, token):
        self.token = token
        self.cetification_url = 'https://review-api.udacity.com/api/v1/me/certifications.json'
        self.comleted_url = 'https://review-api.udacity.com/api/v1/me/submissions/completed'
        self.assigned_reviews_url = 'https://review-api.udacity.com/api/v1/me/submissions/assigned'

    def get_certifications(self):
        """
        get certifications of review
        """
        return self.get_method(self.cetification_url).json()

    def get_assigned_reviews(self):
        """
        get assigned_reviews
        """
        return self.get_method(self.assigned_reviews_url).json()

    def get_method(self, url, params=None):
        """
        review get method
        """
        headers = {'Authorization': self.token, 'Content-Length': '0'}
        response = requests.get(url, headers=headers, params=params)
        return response

    def get_review_completed_in_time(self, start_time):
        """
        get review completed when it is from start_time
        """
        params = {'start_date': start_time}
        response = self.get_method(self.comleted_url, params=params)
        return response.json()


class ReviewDownloader(ReviewRequest):
    """
    Class that auto download the project from assigned review
    """
    def __init__(self, token):
        ReviewRequest.__init__(self, token)
        self.assigned_reviews = self.get_assigned_reviews()

    def re_start(self):
        """
        reload the data
        """
        self.assigned_reviews = self.get_assigned_reviews()

    def get_project_url(self):
        """
        get download url from project
        """
        return self.assigned_reviews
