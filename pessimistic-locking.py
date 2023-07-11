import threading
import time

# Assume this is the user record in the database
user = {
    'id': 1,
    'name': 'John Doe',
    'email': 'johndoe@example.com',
    'age': 30
}

# Create a lock object to synchronize access to the user record
lock = threading.Lock()


# Function to update the user record
def update_user_record(user_id, new_name):
    print(f"Thread {threading.current_thread().name} is attempting to update the user record.")

    # Acquire the lock to ensure exclusive access to the user record
    lock.acquire()
    print(f"Thread {threading.current_thread().name} has acquired the lock.")

    try:
        # Simulate some processing time
        time.sleep(2)

        # Perform the update operation
        user['name'] = new_name
        print(f"Thread {threading.current_thread().name} has updated the user record: {user}")

        # Simulate some more processing time
        time.sleep(2)

    finally:
        # Release the lock to allow other threads to access the user record
        lock.release()
        print(f"Thread {threading.current_thread().name} has released the lock.")


# Create two threads that update the user record simultaneously
thread1 = threading.Thread(target=update_user_record, args=(1, 'Jane Smith'))
thread2 = threading.Thread(target=update_user_record, args=(1, 'Alice Johnson'))

# Start the threads
thread1.start()
thread2.start()

# Wait for the threads to finish
thread1.join()
thread2.join()

# Print the final user record
print(f"Final user record: {user}")
