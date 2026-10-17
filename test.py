
from werkzeug.security import generate_password_hash, check_password_hash
gen_password_hash = generate_password_hash('123456')
print(gen_password_hash)