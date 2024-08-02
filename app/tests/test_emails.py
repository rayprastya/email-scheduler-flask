import json
from datetime import datetime, timedelta
import pytz

def test_post_schedule_emails(test_client, init_database):
    timestamp = (datetime.now(pytz.timezone('Asia/Singapore')) + timedelta(days=1)).isoformat()
    data = {
        'event_id': 1, 
        'email_subject': 'Test Subject',
        'email_content': 'Test Content',
        'timestamp': timestamp
    }
    
    response = test_client.post('/api/v1/schedule-emails', data=json.dumps(data), content_type='application/json')
    
    assert response.status_code == 201
    assert json.loads(response.data)['message'] == 'Email scheduled successfully'

def test_get_emails(test_client, init_database):
    response = test_client.get('/api/v1/schedule-emails')
    
    assert response.status_code == 200
    data = json.loads(response.data)
    assert isinstance(data, list)
    assert len(data) > 0
