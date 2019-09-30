# __author__ == "Priya"
import dialogflow_v2 as dflow
import uuid
import os

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = os.path.join(os.getenv('HOME'), 'PIP-ASSISTANT.json')

def get_response(text):
    session_client = dflow.SessionsClient()
    session_id = uuid.uuid4()
    project_id='pip-assistant'
    session = session_client.session_path(project_id, session_id)
    print('Session path: {}\n'.format(session))
    text_input = dflow.types.TextInput(text=text, language_code='en')
    query_input = dflow.types.QueryInput(text=text_input)
    response = session_client.detect_intent(session=session, query_input=query_input)
    print('Query text: {}'.format(response.query_result.query_text))
    print('Detected intent: {} (confidence: {})\n'.format(
        response.query_result.intent.display_name,
        response.query_result.intent_detection_confidence))
    print('Fulfillment text: {}\n'.format(
        response.query_result.fulfillment_text))
    res = response.query_result.fulfillment_text
    return res




