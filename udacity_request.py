# -*- coding:utf-8 -*-
'''
review counter
'''
import os
from shutil import copyfile
import requests
from base_func import move_file, unzip_file, download_file, notify


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


class ReviewData():
    """
    Class that handle review data
    """
    def __init__(self, data):
        self.data = data

    def get_project_url(self):
        """
        get download url from project
        """
        return self.data['archive_url']

    def get_language(self):
        """
        get language 
        """
        return self.data['language']

    def get_review_id(self):
        """
        get review id
        """
        return self.data['id']

    def get_project_name(self):
        """
        get project name
        """
        return self.data['project']['name']

    def get_project_price(self):
        """
        get project price
        """
        return self.data['price']


class ReviewDownloader(ReviewRequest):
    """
    Class that auto download the project from assigned review
    """
    def __init__(self, token, src_path, project_path):
        ReviewRequest.__init__(self, token)
        self.src_path = src_path
        self.project_path = project_path

    def get_reviews(self):
        """
        get assigned reviews
        """
        assigned_reviews = []
        for review in self.get_assigned_reviews():
            assigned_reviews.append(ReviewData(review))
        return assigned_reviews

    def download_review(self, review):
        """
        download project file with review data
        """
        review_id = review.get_review_id()
        local_file_name = download_file(review.get_project_url())
        unzip_file_name = self.move_download_file(local_file_name)
        self.notify_review(review_id,
                           review.get_project_name(),
                           unzip_file_name)
        print("finished download, url: " + review.get_project_url())

    def notify_review(self, review_id, review_name, file_name):
        """
        notify with review message
        """
        message = "ReviewId: {0}".format(review_id)
        title = review_name
        subtitle = "File: {0}".format(file_name)
        notify(title, subtitle, message)

    def move_download_file(self, file_name):
        """
        move download file to src path and project path

        return:
            unzip files name
        """
        current_dir_path = os.getcwd()
        current_file_path = current_dir_path + '/' + file_name
        src_file_path = self.src_path + '/' + file_name
        project_file_path = self.project_path + '/' + file_name

        move_file(current_file_path, src_file_path)
        copyfile(src_file_path, project_file_path)

        unzip_file_name = unzip_file(src_file_path, self.src_path)
        unzip_file_name = unzip_file(project_file_path, self.project_path)

        os.remove(src_file_path)
        os.remove(project_file_path)
        return unzip_file_name


