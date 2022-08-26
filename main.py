from config.net import port as default_port, host as default_host
from visualization import render_all
from spider import start_all_tasks
from optparse import OptionParser
from server import get_router
import uvicorn


def main():
    usage = '''
    -d Deploy the server.
    -c Start all the tasks of spider system.
    -r Render all the routers.
    '''
    parser = OptionParser(usage=usage)
    
    parser.add_option("-d", "--deploy", help="Deploy the server.", action="store_true")
    parser.add_option("-r", "--render", help="Render all the routers.", action="store_true")
    parser.add_option("-c", "--crawl", help="Start all the tasks of spider.", action="store_true")
    
    (options, _) = parser.parse_args()
    app = get_router()
    
    if options.deploy:
        uvicorn.run(app, host=default_host, port=default_port)
    elif options.crawl:
        start_all_tasks()
    elif options.render:
        render_all()


if __name__ == "__main__":
    main()
