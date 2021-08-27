import call
import sip_types


class State(object):
    def __init__(self):
        self.current_call_dict: dict[str, call.Call] = {}

    def callback(self, state: sip_types.CallStateChange, caller_id: str, new_call: call.Call = None) -> None:
        if state == sip_types.CallStateChange.HANGUP:
            del self.current_call_dict[caller_id]
        elif state == sip_types.CallStateChange.CALL:
            self.current_call_dict[caller_id] = new_call

    def is_active(self, caller_id: str) -> bool:
        return caller_id in self.current_call_dict

    def output(self):
        for number in self.current_call_dict.keys():
            print(number)

    def get_call(self, caller_id: str) -> call.Call:
        return self.current_call_dict[caller_id]


def create():
    new_state = State()
    return new_state