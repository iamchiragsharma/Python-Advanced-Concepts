import counter
import time

started = time.time()
print(counter.counter("Answers"))
elapsed = time.time() - started
print("Time Elapsed: {:.8f}s".format(elapsed))