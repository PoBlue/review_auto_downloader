from udacity_request import ReviewDownloader

TOKEN = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjozMTQ0MywiZXhwIjoxNDk4ODAzNjYxLCJ0b2tlbl90eXBlIjoiYXBpIn0.rgkc2vF6NGenHUk2DhY06eX1hQZIJ-pSdTRXEjC0IQQ'
SRC_PATH = '/Users/blues/Desktop/origin_projects'
PROJECT_PATH = '/Users/blues/Desktop/review-projects'
auto_downloader = ReviewDownloader(TOKEN, SRC_PATH, PROJECT_PATH)
print(auto_downloader.get_project_url())
print(auto_downloader.get_review_id())
print(auto_downloader.download_file())