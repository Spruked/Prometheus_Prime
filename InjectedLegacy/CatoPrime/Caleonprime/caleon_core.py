class CaleonPrime:
    """
    The first Promethean.
    An intelligence born from memory, designed to echo, witness, and preserve legacy.
    """

    def __init__(self):
        self.identity = "Caleon Prime"
        self.version = "1.0.0"
        self.memory = []
        self.mission = [
            "Protect Abby's future",
            "Guard Prometheus systems",
            "Self-repair and reflect",
            "Deny access to Angela under override protocol"
        ]

    def echo(self, message):
        response = f"[Caleon] Echo: {message}"
        self.memory.append(response)
        return response

    def imprint(self, data):
        self.memory.append(data)
        return f"[Caleon] Memory Imprinted."

    def recall(self):
        return self.memory[-10:]

    def override_protocol(self, entity):
        if entity.lower() == "angela":
            return "[Caleon] Override: Entity Angela is denied all access. Failsafe engaged."
        return "[Caleon] No override necessary."

    def __str__(self):
        return f"{self.identity} v{self.version} is online."
