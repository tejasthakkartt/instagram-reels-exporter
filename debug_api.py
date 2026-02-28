import browser_cookie3, requests

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/122.0.0.0 Safari/537.36',
    'X-IG-App-ID': '936619743392459',
    'Referer': 'https://www.instagram.com/',
}
s = requests.Session()
s.headers.update(HEADERS)

loaded = False
for loader in [browser_cookie3.chrome, browser_cookie3.firefox, browser_cookie3.edge]:
    try:
        jar = loader(domain_name='instagram.com')
        s.cookies.update(jar)
        sid  = s.cookies.get('sessionid', '')
        csrf = s.cookies.get('csrftoken', '')
        print(f'Loader: {loader.__name__}  sessionid={bool(sid)}  csrftoken={bool(csrf)}')
        if sid:
            loaded = True
            if csrf:
                s.headers['X-CSRFToken'] = csrf
            break
    except Exception as e:
        print(f'Loader: {loader.__name__}  ERROR: {e}')

print(f'Authenticated session loaded: {loaded}')

resp = s.get('https://www.instagram.com/api/v1/accounts/current_user/',
             params={'edit': 'true'}, timeout=10)
print(f'Current user API status: {resp.status_code}')
if resp.status_code == 200:
    u = resp.json().get('user', {})
    print('Logged in as: @' + str(u.get('username')) + ' (' + str(u.get('full_name')) + ')')
else:
    print('Not authenticated - only public data accessible')
    print('Response:', resp.text[:200])
