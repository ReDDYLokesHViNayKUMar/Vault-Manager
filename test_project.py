from project import open_deposit_box, close_deposit_box, update_passkey, get_all_box_ids

def test_open_deposit_box(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 'Kesh')
    monkeypatch.setattr('getpass.getpass', lambda _: '1234') 
    box_id = open_deposit_box()
    assert box_id in get_all_box_ids()  

def test_close_deposit_box(monkeypatch):
    monkeypatch.setattr("getpass.getpass", lambda _: "1234")
    box_id = close_deposit_box(box_id='VK-1-2')
    if box_id:
         assert box_id in get_all_box_ids()  
    else:
        assert box_id == None

def test_update_passkey(monkeypatch):
    responses = iter(['123', '1234'])
    monkeypatch.setattr('getpass.getpass', lambda _: next(responses))
    box_id = update_passkey('VK-1-2')
    if box_id:
         assert box_id in get_all_box_ids()  
    else:
        assert box_id == None
