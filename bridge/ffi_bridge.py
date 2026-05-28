from cffi import FFI
import os

ffi = FFI()

# Define the C structures and functions
ffi.cdef("""
    typedef struct {
        char protocol[16];
        char payload[256];
    } NIAMessage;

    void process_message(NIAMessage* msg);
""")

# Build and load the C library
C_CODE = open(os.path.join(os.path.dirname(__file__), "bridge.c")).read()
lib = ffi.verify(C_CODE)

def send_bridge_message(protocol, payload):
    """Sends a message through the C FFI bridge."""
    msg = ffi.new("NIAMessage*")

    # Safely copy strings
    p_proto = protocol.encode('utf-8')[:15]
    p_pay = payload.encode('utf-8')[:255]

    ffi.memmove(msg.protocol, p_proto, len(p_proto))
    ffi.memmove(msg.payload, p_pay, len(p_pay))

    lib.process_message(msg)

if __name__ == "__main__":
    send_bridge_message("LUA", "update_ltc_state")
    send_bridge_message("WREN", "transition_idle")
