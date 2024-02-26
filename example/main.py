import streamsync as ss

# This is a placeholder to get you started or refresh your memory.
# Delete it or adapt it as necessary.
# Documentation is available at https://streamsync.cloud

# Shows in the log when the app starts
print("Hello world!")

def button_pressed(state, context):
    print(context)
    
# Initialise the state

# "_my_private_element" won't be serialised or sent to the frontend,
# because it starts with an underscore

initial_state = ss.init_state({
    "my_app": {
        "title": "Square Brackets Bug Example"
    },
    "object1": {
        "object1_1": 1,
        "object1_2": 2
    }
})

_update_message(initial_state)