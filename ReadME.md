## Coroutines

`Coroutines` are the fundamental building blocks of asynchronous programming in Python's asyncio library. They are special functions that can be suspended (`paused`) and `resumed` later, enabling efficient handling of I/O operations without blocking the main thread.

### 1. Define an Async Function:

Use the `async def` syntax to declare a function as a coroutine. This signals that it can be suspended and resumed later.
import asyncio

```Python
async def wait_for_seconds(seconds):
    print(f"Waiting for {seconds} seconds...")
    await asyncio.sleep(seconds)  # This line suspends execution
    print("Done waiting!")

```

### 2. Suspending Execution with await:

+ The `await` keyword is used within an `async function` to pause its execution until a specific operation completes.
+ In this example, await asyncio.sleep(seconds) suspends the execution for the specified number of seconds. The event loop takes over and can schedule other tasks while waiting.

### 3. Resuming Execution:

+ Once the awaited operation (like `asyncio.sleep`) finishes, the coroutine resumes execution from the line after await.
+ In the example, after the sleep completes, the message "Done waiting!" is printed.

### 4. Running a Coroutine:

You cannot directly call an `async function`. You need to use `asyncio.run()` (Python 3.7+) to launch it and manage the `event loop`:

```Python
import asyncio

async def main():
    await wait_for_seconds(2)  # Call the coroutine

asyncio.run(main())  # Starts the event loop, runs main(), and closes the loop

```

### Explanation:

+ The main coroutine calls wait_for_seconds(2), which suspends for 2 seconds.
+ `asyncio.run()` creates and runs the event loop. It schedules the main coroutine, suspends it during the sleep, manages any other tasks if present, and resumes main when the sleep completes. Finally, it closes the event loop.

### 5. Using await with Futures (Optional):

+ Futures represent the eventual result of an asynchronous operation.
+ You can use await with a future to wait for its completion and get the result. This is less common but useful when interacting with asynchronous libraries that return futures.

# (Optional) Example with a future

```Python
async def another_task():
    # Simulate an asynchronous operation that returns a future
    future = asyncio.Future()
    await asyncio.sleep(2)  # Simulate some work
    future.set_result("Result from another_task")
    return future

async def main():
    data = await wait_for_seconds(3)
    result = await another_task()  # await with a future
    print(data)
    print(result)

asyncio.run(main())

```

### Explanation:

+ The `main` coroutine calls `wait_for_seconds` and `another_task` (which returns a future).
+ `await fetch_data` suspends main for 1 second.
+ Concurrently, `another_task` sleeps for 2 seconds and then sets the result on its future.
+ When `wait_for_seconds` completes, `main` resumes and prints the fetched data.
+ `await another_task` pauses main until the future from `another_task` resolves.
+ Once the future resolves with the result, `main` resumes and prints the result from `wait_for_seconds`.

### Futures

`Futures` are a crucial concept in asyncio when dealing with asynchronous operations.

+ `They represent the eventual result of an asynchronous operation` 
  (like a network request, file read/write, etc.).

```Python
  async def GetData():
  print("Get Data Started....")
  asyncio.sleep(2)
  return [2,3,4,5,6]

async def main():
    task = asyncio.create_task(GetData())
    # Do other things while waiting for the data to be fetched...
    #
    #
    #
    # Wait for the task to complete and get the result
    data = await task
    print(f"Fetched data: {data}")

asyncio.run(main())
```
### The Role of Futures:

+ When you create a task using `asyncio.create_task()`, it returns a future object. This future represents the eventual result of the asynchronous operation (the network request in this case).
+ The `await` keyword is used with the future to pause the execution of the coroutine (in this case, `main`) until the future resolves (the data is fetched). The event loop then manages other tasks while waiting.
+ Once the asynchronous operation completes, the future resolves with the result (the `GetData`).

### Getting the Result:

After await task, the execution of main is paused until the fetch_data task finishes. Once the data is fetched, the future resolves with the data, and main resumes execution, printing the `GetData`.
