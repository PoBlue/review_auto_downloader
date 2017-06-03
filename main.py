import pickle
import time
from clint.arguments import Args
from udacity_request import ReviewDownloader

args = Args()


class StoreData():
    """
    store data in a file
    """

    def __init__(self, data_file_name):
        self.data_file = data_file_name

    def save_data(self, data):
        """
        save data to data file
        """
        with open(self.data_file, 'wb') as f:
            pickle.dump(data, f)

    def load_data(self, default_data):
        """
        load data from data file
        """
        try:
            with open(self.data_file, 'rb') as f:
                data = pickle.load(f)
                return data
        except FileNotFoundError:
            self.save_data(default_data)
            return None


class DownloaderInterface():
    """
    interface for down load file
    """

    def __init__(self):
        self.downloader = None
        self.downloaded_ids = []
        self.token = ''
        self.src_path = ''
        self.project_path = ''
        self.check_time = 200
        self.data_file = 'data.pkl'
        self.store_data = StoreData(self.data_file)
        self.load_data()

    def start(self):
        """
        start to download object
        """
        if self.token != '' and self.src_path != '' and self.project_path != '':
            self.downloader = ReviewDownloader(
                self.token, self.src_path, self.project_path)
            self.download()
        else:
            print('please set token/src_path/project_path')

    def download(self):
        """
        download review
        """
        while True:
            for review in self.downloader.get_reviews():
                review_id = review.get_review_id()
                if review_id not in self.downloaded_ids:
                    self.downloader.download_review(review)
                    self.downloaded_ids.append(review_id)
                    self.save_data()
                else:
                    continue
            time.sleep(self.check_time)
            print("checking......")

    def save_data(self):
        """
        save data to data file
        """
        d = {"token": self.token,
             "src_path": self.src_path,
             "project_path": self.project_path,
             "downloaded_ids": self.downloaded_ids}
        self.store_data.save_data(d)

    def load_data(self):
        """
        load data from data file
        """
        default_data = {"token": self.token,
                        "src_path": self.src_path,
                        "project_path": self.project_path,
                        "downloaded_ids": self.downloaded_ids}
        data = self.store_data.load_data(default_data)
        if data is not None:
            self.token = data["token"]
            self.src_path = data["src_path"]
            self.project_path = data["project_path"]
            self.downloaded_ids = data["downloaded_ids"]

    def cli_handler(self):
        """
        command line handler
        """
        flag_args = args.grouped
        cmd = flag_args['_']
        if '-token' in flag_args:
            self.token = flag_args['-token'][0]
        if '-src_path' in flag_args:
            self.src_path = flag_args['-src_path'][0]
        if '-project_path' in flag_args:
            self.project_path = flag_args['-project_path'][0]
        if len(cmd) > 0:
            if cmd[0] == 'help':
                print("""
                    [-token] to set token
                    [-src_path] to set src path
                    [-project_path] to set project paht
                """)
            if cmd[0] == 'show':
                print("token: {0}\nsrc_path: {1}\nproject_path: {2}\nids: {3}"
                      .format(self.token,
                              self.src_path,
                              self.project_path,
                              self.downloaded_ids))
            if cmd[0] == 'start':
                self.start()
        self.save_data()


download_interface = DownloaderInterface()
download_interface.cli_handler()
# download_interface.start()
