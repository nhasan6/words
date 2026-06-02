from pwdlib import PasswordHash

# creates a hasher using the reccomended algorithm
password_hash = PasswordHash.recommended()

# security trick --> doesn't differentiate w wrong password & user not found
DUMMY_HASH = password_hash.hash("dummypassword")


# returns a boolean
def verify_password(plain_password, hashed_password):
    return password_hash.verify(plain_password, hashed_password)

def get_password_hash(password):
    return password_hash.hash(password)