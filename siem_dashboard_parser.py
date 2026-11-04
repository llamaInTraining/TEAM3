#Adam Mohamed, Rached Aissa, Joseph Sanchez, Omer Faruk

#dictionary with user information -username, status, number of attempts
siem_logs = {
    'user_001': {
        'username': 'jdoe',
        'status': 'active',
        'failed_attempts': 1
    },
    'user_002': {
        'username': 'rsmith',
        'status': 'active',
        'failed_attempts': 15
    },
    'user_003': {
        'username': 'tjones',
        'status': 'active',
        'failed_attempts': 0
    },
    'user_004': {
        'username': 'bwayne',
        'status': 'active'
         #failed_attempts intentionally missing
    }
}
#this loop prints user and data on each dictionary
for user, data in siem_logs.items():
    print(f"{user}")
    print(f"{data}")

    #get prevents user_0004 from causing a syntax error since it has no failed attempts.
    attempts = data.get('failed_attempts', 0)
    if attempts >5:
        #changes the status from active to locked if failed attempts are higher than 5
        data['status'] = 'locked'
        print(f'Too many failed attempts...{user} has been locked')

#adds another key:value to each dictionary 
for value in siem_logs.values():
    value['2FA_enabled'] = True

print(f'---- SIEM Dashboard----')

#prints a clean dashoard with user informaition.
for user, data in siem_logs.items():
    usname = data['username']
    stat = data['status']
    twofa = data['2FA_enabled']
    
    print(f'Audit complete | ID: {user} | USERNAME: {usname} | STATUS: {stat} | 2FA: {twofa}')