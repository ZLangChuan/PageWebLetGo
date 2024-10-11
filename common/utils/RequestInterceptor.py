
class RequestInterceptor:
    """
    这是一个全局拦截器
    """

    def __init__(self, request):
        self.request = request

    def process_request(self):
        # 在请求被处理之前，可以在这里进行一些预处理操作
        # 例如，检查请求头、参数等
        pass

    def process_response(self, response):

        # 在请求被处理后，可以在这里进行一些后处理操作
        # 例如，修改响应头、内容等
        return response