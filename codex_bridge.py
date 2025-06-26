class CodexBridge:
    def __init__(self, codex):
        self.codex = codex
        self.bridge_log = []

    def bridge_process(self, data):
        result = self.codex.process(data)
        self.log_bridge("bridge_process", result)
        return result

    def log_bridge(self, context, output):
        self.bridge_log.append({"context": context, "output": output})
        print(f"[Bridge] {context} → {output}")
