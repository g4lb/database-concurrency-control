# Database Concurrency Control Examples

This repository contains examples of implementing concurrency control mechanisms in Python for managing concurrent access to a shared database. Two commonly used locking mechanisms, pessimistic locking and optimistic locking, are demonstrated in separate code examples.

## Pessimistic Locking Example

The `pessimistic-locking.py` file demonstrates how to implement pessimistic locking in Python using the `threading.Lock` object. Pessimistic locking ensures exclusive access to a shared resource by acquiring a lock before performing write operations. In the example, the `update_user_record` function represents the code that updates a user record in a database. The `Lock` object is used to synchronize access to the user record, allowing only one thread to modify it at a time. This ensures data consistency and prevents conflicts.

To run the pessimistic locking example, execute the following command:
```
python pessimistic-locking.py
```

## Optimistic Locking Example

The `optimistic-locking.py` file demonstrates how to implement optimistic locking in Python using versioning. Optimistic locking assumes that conflicts are rare and allows concurrent access to a shared resource. In the example, the `update_user_record` function represents the code that updates a user record in a database. It reads the current version of the user record and compares it with the stored version. If the versions match, the update operation proceeds; otherwise, a conflict is detected. This approach minimizes the need for locking and allows for better concurrency while still ensuring data integrity.

To run the optimistic locking example, execute the following command:
```
python optimistic-locking.py
```

## Requirements

The code examples require Python 3.x.