import visualization.actress as actress
from config.net import port, host
from server import get_router
import uvicorn


app = get_router()


def main():
    actress.render_all()
    uvicorn.run(app, host=host, port=port)


if __name__ == "__main__":
    main()
