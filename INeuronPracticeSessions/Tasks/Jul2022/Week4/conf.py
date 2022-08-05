class DBConf:
    MySQL = {
        'user': 'root',
        'passwd': 'root',
        'host': 'localhost',
        'clothing_db': 'clothing'
    }
    Mongo = {
        'user_name': "vasu",
        'password': "va5uMANGO",

    }

    def get_mongodb_url(self):
        """
        This function generates a mongo db URL.
        :return: str
        """
        return f"mongodb+srv://{self.Mongo['user_name']}:{self.Mongo['password']}@cluster0.34cpv.mongodb.net/?retryWrites=true&w=majority"