#include <stdio.h>
#include <string.h>

/**
 * Project NIA - Core C Bridge
 * Handles high-performance message passing between language VMs.
 */

typedef struct {
    char protocol[16];
    char payload[256];
} NIAMessage;

void process_message(NIAMessage* msg) {
    printf("[C-FFI] Dispatching %s: %s\n", msg->protocol, msg->payload);
}
