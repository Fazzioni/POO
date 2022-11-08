class Camera():
    def __init__(self, code, config_code):
        self.code = code
        self.config_code = config_code
        self.backup_img = False
        self.backup_img_days = 30
        self.cam_modules = []
        
    def check_token(self,token):
        pass
            