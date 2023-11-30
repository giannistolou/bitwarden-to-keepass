import pandas as pd

print('Add bitwarden csv file path')
print('If you are in the same folder write just the file name')
print('example: bitwarden_export_20231111160739.csv')
file_path = input('csv file: ')

try:
    df = pd.read_csv(file_path)
    df['login_uri'] = df['login_uri'].str.split(',').str[0]
    print('Login Url decoration ✅')
    df.rename(columns={'group': 'folder'}, inplace=True)
    df = df.drop(columns=['type'])
    new_order = ['folder', 'name', 'login_username', 'login_password', 'login_uri', 'notes', 'login_totp']
    print('Re struct csv ✅')
    df = df[new_order]
    df.to_csv('keep-pass-decoration-from-bitwarden.csv', index=False)
    print('Export done ✅')
except: 
    print('Something went wrong 🚫')