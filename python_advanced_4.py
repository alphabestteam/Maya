import requests
import time
import threading

def timer(func):
    def wrapper(*args, **kwargs) -> None:
        start_time = time.time()
        func(*args, **kwargs)
        end_time = time.time()
        print(end_time - start_time)
        # return end_time - start_timeS
    return wrapper


def download_to_machine(url: str, index: int):
    get_url = requests.get(url, allow_redirects=True)
    open(f'new_file{index}.png', "wb").write(get_url.content)

@timer
def main():
    # download_to_machine("https://upload.wikimedia.org/wikipedia/commons/thumb/e/e2/Matzov-unit-insignia-2020.png/330px-Matzov-unit-insignia-2020.png", 1)
    url_list = ["https://upload.wikimedia.org/wikipedia/commons/thumb/e/e2/Matzov-unit-insignia-2020.png/330px-Matzov-unit-insignia-2020.png",
                "https://ssl.gstatic.com/ui/v1/icons/mail/rfr/logo_gmail_lockup_default_1x_rtl.png",
                "https://github.githubassets.com/images/modules/open_graph/github-mark.png",
                "https://www.google.co.il/images/branding/googlelogo/2x/googlelogo_color_160x56dp.png",
                ]
    running_time = 0
    threads_list = []
    for index in range(len(url_list)):
        download_to_machine(url_list[index], index + 1)


    for index in range(len(url_list)):
        threads_list.append(threading.Thread(target = download_to_machine, args=[url_list[index], index + 1]))
    for index in range(len(url_list)):
        threads_list[index].start()
    for index in range(len(url_list)):
        threads_list[index].join()


if __name__ == "__main__":
    main()