import docker
from Trace import Trace


class DockerHub(object):
    def __init__(self):
        self._tokenKey = None


    def Login(self,username,passwprd,url='https://index.docker.io/v1/'):
        try:
            d = docker.APIClient()
            res = d.login(username,passwprd,email=username,registry=url)
            print(res)
            Trace.Info(res)
        except Exception as Error:
            Trace.Error(str(Error))

