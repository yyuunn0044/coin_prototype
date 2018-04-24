import requests


class controller:
    def __init__(self):
        return

    def send_tx(self, tx):
        res = requests.get('http://127.0.0.1:8080/tx', data=tx)
        print(res.text)
        return

    def get_budget(self):
        res = requests.get('http://127.0.0.1:8080/budget')
        print(res.text)
        return


if __name__ == '__main__':
    while(True):
        s = input("")
        if s == 'xx':
            requests.get('http://127.0.0.1/xx')
        # guitar dungdung
