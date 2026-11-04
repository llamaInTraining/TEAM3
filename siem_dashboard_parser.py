#Adam Mohamed, Rached Aissa, Joseph Sanchez, Omer Faruk

siem_logs = {
    'user_001': {
        'username': 'jdoe',
        'status': 'active',
        'failed_attempts': 1
    },
    'user_002': {
        'username': 'rsmith',
        'status': 'locked',
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
        # failed_attempts intentionally missing
    }
}
for user, data in siem_logs.items():
    print(f"{user}")
    print(f"{data}")

