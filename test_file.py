Accounts = {
    "admin": 0
}

username = "Admin"
username = username.lower()

try:
    account_id = Accounts[username]

except:
    new_data = {username: len(Accounts)}
    Accounts.update(new_data)
    account_id = Accounts[username]

print(str(account_id))
print(Accounts)