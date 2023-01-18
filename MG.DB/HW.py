post = {
    'id': 'it_09',
    'topic': 'Тема поста',
    'author_id': '019',
    'tags': ['java', 'mongodb'],
    'content': ['text', 'pictures'],
    'datetime': '......',
    'is_approved': True,
    'status': 'publish',
    'type': 'post',
    'comment_status': 'open',
    'post_password': 'asdhjfn09'
}

employee = {
    'employee_id': '018',
    'division_id': 'm45',
    'full_name': 'Robert Schwarz',
    'b_data': '10_03_1987',
    'position': 'manager',
    'contact': {
        'mobile': '0178-9874653',
        'address': {
            'Country': 'Germany',
            'City': 'Berlin',
            'Street': 'Bahnhofstrasse',
            'House_number': '34'
        },
        'email': ['marun@example.org', 'berlin@test.com']},
    'salary': 3876,
}

order = {
    'order_id': 'gh076',
    'is_paid': True,
    'datetime': {
        'created': '.....',
        'paid': '......'},
    'client_id': 'gt045',
    'quantity': 1,
    'products': [
        {'id': 'g5', 'price': 450, 'q': 1, 'name': 'monitor'},
        {'id': 'g6', 'price': 300, 'q': 1, 'name': 'printer'},
        {'id': 'g9', 'price': 500, 'q': 1, 'name': 'graphics_card'}

    ]
}
