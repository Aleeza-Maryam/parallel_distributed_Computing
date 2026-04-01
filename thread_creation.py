import threading
import time

def thread_function(thread_name):
    """Function to be executed by each thread"""
    thread_id = threading.get_ident()  # Get thread ID
    print(f"[{thread_name}] Thread ID: {thread_id} - Thread is running")
    time.sleep(1)  # Simulate processing time
    print(f"[{thread_name}] Thread finished execution")

# Main execution for Part A
print("="*50)
print( "Thread Creation")
print("="*50)

threads = []

# Create 5 threads
for i in range(5):
    thread_name = f"Thread-{i+1}"
    thread = threading.Thread(target=thread_function, args=(thread_name,))
    threads.append(thread)
    print(f"Created and started {thread_name}")
    thread.start()

# Wait for all threads to complete
for thread in threads:
    thread.join()

print("All threads  completed")
