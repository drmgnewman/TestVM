from webbrowser import open as openw
import time

def my_break(break_info=None):
    """
    Function to keep track of breaks
    :param break_info: a dictionary with the following info:
         t_break <int> default is 3
         url <string> default "https://www.youtube.com/watch?v=klZDJmV6MVg"
         t_sleep <int> in seconds, default = 1 hours
    :return:
    """
    if break_info is None:
        # Default info
        break_info = {}
        break_info["t_breaks"] = 3
        break_info["url"] = "https://www.youtube.com/watch?v=klZDJmV6MVg"
        break_info["t_sleep"] = 60 * 60 # one hour
        #break_info["t_sleep"] = 3 # one hour
        # TODO: test for individual keys
        # if <key> in dict

        break_count = 0
        while(break_count < break_info['t_breaks']):
            url = "https://www.youtube.com/watch?v=klZDJmV6MVg"
            openw(url)
            time.sleep(3)
            break_count += 1


if __name__ == '__main__':
    info = {}
    #my_break(info)
    my_break()
