class IN_LENGTH_ERROR(Exception):
    def __str__(self):
        return "input ports must contain ONLY 4 PORTS"