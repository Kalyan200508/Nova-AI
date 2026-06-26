from intent_ai.engine import intent_engine

result = intent_engine.detect(
    "Could you please open Chrome and Gmail?"
)

print(result)

for cmd in result.commands:
    print(cmd.action, cmd.target, cmd.query)