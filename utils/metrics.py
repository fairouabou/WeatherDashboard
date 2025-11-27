import time
from flask import request

# Global counters
REQUEST_COUNT = 0
ERROR_COUNT = 0
TOTAL_LATENCY = 0.0

def record_request_latency(start_time):
    global TOTAL_LATENCY
    TOTAL_LATENCY += time.time() - start_time

def record_request():
    global REQUEST_COUNT
    REQUEST_COUNT += 1

def record_error():
    global ERROR_COUNT
    ERROR_COUNT += 1


def generate_metrics():
    # Avoid division by zero
    avg_latency = TOTAL_LATENCY / REQUEST_COUNT if REQUEST_COUNT > 0 else 0

    output = [
        "# HELP weather_request_count Total number of requests",
        "# TYPE weather_request_count counter",
        f"weather_request_count {REQUEST_COUNT}",

        "# HELP weather_error_count Total number of errors",
        "# TYPE weather_error_count counter",
        f"weather_error_count {ERROR_COUNT}",

        "# HELP weather_request_latency_seconds Average request latency",
        "# TYPE weather_request_latency_seconds gauge",
        f"weather_request_latency_seconds {avg_latency}",
    ]

    return "\n".join(output)
