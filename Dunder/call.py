class callme:
    def __init__(self, phone):
        self.phone = phone
    def __call__(self):
        print(f'Ligando para {self.phone}...')

call1 = callme('123457788')
call1()