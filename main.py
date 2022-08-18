import visualization.television as television
import visualization.actress as actress
from spider import start_all_tasks
from optparse import OptionParser
from config.net import port, host
from server import get_router
import uvicorn


app = get_router()


def main():
    usage = '''
    -d Deploy the server.
    -c Start all the tasks of spider system.
    '''
    parser = OptionParser(usage=usage)
    
    parser.add_option("-d", "--deploy", help="Deploy the server.", action="store_true")
    parser.add_option("-c", "--crawl", help="Start all the tasks of spider", action="store_true")
    
    (options, _) = parser.parse_args()
    
    if options.deploy:
        actress.render_all_about_actress()
        television.render_all_about_television()
        uvicorn.run(app, host=host, port=port)
    elif options.crawl:
        start_all_tasks()


if __name__ == "__main__":
    main()
