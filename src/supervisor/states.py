class ProcessStates:
    STOPPED = 0
    STARTING = 10
    RUNNING = 20
    BACKOFF = 30
    STOPPING = 40
    EXITED = 100
    FATAL = 200
    UNKNOWN = 1000

def getProcessStateDescription(code):
    for statename in ProcessStates.__dict__:
        if getattr(ProcessStates, statename) == code:
            return statename

class SupervisorStates:
    ACTIVE = 0
    SHUTDOWN = 1

def getSupervisorStateDescription(code):
    for statename in SupervisorStates.__dict__:
        if getattr(SupervisorStates, statename) == code:
            return statename


class EventListenerStates:
    READY = 10 # the process ready to be sent an event from supervisor
    BUSY = 20 # event listener is processing an event sent to it by supervisor
    ACKNOWLEDGED = 30 # the event listener processed an event
    UNKNOWN = 40 # the event listener is in an unknown state

def getEventListenerStateDescription(code):
    for statename in EventListenerStates.__dict__:
        if getattr(EventListenerStates, statename) == code:
            return statename

