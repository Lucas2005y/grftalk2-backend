from accounts.models import User
from django.contrib.auth.hashers import make_password, check_password

class Authentication:
    def signin(self, email: str, password: str) -> User | bool:
        # Busca um usuário no banco de dados com o email fornecido
        user = User.objects.filter(email=email).first()
        
        # Verifica se o usuário existe e se a senha fornecida está correta
        if user and check_password(password, user.password):
            # Se a senha estiver correta, retorna o objeto do usuário
            return user
        
        return False
    
    def signup(self, name: str, email: str, password: str) -> User | bool:
        if User.objects.filter(email=email).exists():
            return False
        
        # Cria um novo usuário no banco de dados
        user = User.objects.create(
            name=name, 
            email=email, 
            password=make_password(password)
        )
        
        return user