class Connection:
    def __init__(self, host='Localhost'):
        self.host = host
        self.user = None
        self.password = None
    
    def set_user(self, user): #seter
        self.user = user
    
    def set_password(self, password): #seter
        self.password = password

    @classmethod
    def create_with_auth(cls, user, password, host='Localhost'):
        conn = cls(host)
        conn.set_user(user)
        conn.set_password(password)
        return conn


c1 = Connection()
print(c1.user)

c1.set_user('FabioReis')
print(c1.user)

c1.set_password('123456')
print(c1.password)

c2 = Connection.create_with_auth('AnaSilva', 'abcdef', 'localhost')
print(c2.user)
print(c2.password)