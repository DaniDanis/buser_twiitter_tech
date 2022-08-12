    username = "teste"
    password = "teste"
    user = User.objects.create_user(username=username, password=password)
    client.force_login(user)
    response = client.get('/home')
    print(response)
    assert response.user == 'teste'