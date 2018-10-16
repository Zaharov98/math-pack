""" Event loop """

from event_loop import EventLoop


def main():
    while True:
        event_loop = EventLoop()
        event_loop.start()


if __name__ == '__main__':
    main()
