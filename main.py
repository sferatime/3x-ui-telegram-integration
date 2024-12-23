import Integration3x
import json

I = Integration3x.Integration3x("http://localhost:2053/", "admin", "admin")
print(I.login())
# print(I.add_inbound())
inbounds = I.list_inbound()
print(json.dumps(inbounds, indent=2))