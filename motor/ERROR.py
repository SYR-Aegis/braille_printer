class IN_LENGTH_ERROR(Exception):
    def __str__(self):
        return "input ports must contain ONLY 4 PORTS"

class PARAMETER_LENGTH_ERROR(Exception):
    def __str__(self):
        return "parameter length error!"

class SOLENOID_STATE_ERROR(Exception):
    def __str__(self):
        return "solenoid state must be 1 or 0"