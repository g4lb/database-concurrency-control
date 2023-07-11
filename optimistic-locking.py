import threading
import time

# Assume this is the user record in the database
user = {
    'id': 1,
    'name': 'John Doe',
    'email': 'johndoe@example.com',
    'age': 30,
    'version': 1  # Version number for optimistic locking
}


# Function to update the user record
def update_user_record(user_id, new_name):
    print(f"Thread {threading.current_thread().name} is attempting to update the user record.")

    # Simulate some processing time
    time.sleep(2)

    # Read the current version of the user record
    current_version = user['version']

    # Simulate some more processing time
    time.sleep(2)

    # Perform the update operation only if the version hasn't changed
    if current_version == user['version']:
        # Update the user record
        user['name'] = new_name
        user['version'] += 1

        print(f"Thread {threading.current_thread().name} has updated the user record: {user}")
    else:
        print(
            f"Thread {threading.current_thread().name} detected a conflict. The user record has been updated by another thread.")


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
