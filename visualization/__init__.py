height = "500px"
width = "700px"
pos_top = "80%"


class Router:
    def __inti__(self):
        self.charts = []

    def append_router(self, path):
        self.charts.append(path)

    def clear(self):
        self.charts = []
