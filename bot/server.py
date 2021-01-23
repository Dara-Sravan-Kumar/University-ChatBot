from rasa.model import get_model_subdirectories, get_model
from rasa.core.channels.socketio import SocketIOInput
from rasa.core.agent import Agent
from rasa.core.interpreter import RegexInterpreter
from rasa.core.interpreter import RasaNLUInterpreter
from rasa.core.utils import EndpointConfig
from rasa.core.policies.keras_policy import KerasPolicy
from rasa.core.policies.memoization import MemoizationPolicy
# load your trained agent
model_path = get_model('./models/nlu/')

_, nlu_model = get_model_subdirectories(model_path)

interpreter = RasaNLUInterpreter(nlu_model)

action_endpoint = EndpointConfig(url="http://localhost:5055/webhook")

agent = Agent.load('models/core/core-20200417-162634.tar.gz', interpreter=interpreter,action_endpoint=action_endpoint)

input_channel = SocketIOInput(
    # event name for messages sent from the user
    user_message_evt="user_uttered",
    # event name for messages sent from the bot
    bot_message_evt="bot_uttered",
    # socket.io namespace to use for the messages
    namespace=None
)

# set serve_forever=True if you want to keep the server running
s=agent.handle_channels([input_channel],5500,route='/webhooks/',cors="*") #serve_forever=True
#agent.handle_channels([input_channel], http_port=5005,route=’/webhooks/’,cors="*")