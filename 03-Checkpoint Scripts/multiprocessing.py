import time
import multiprocessing

def delayed_print_one():
  print("one: i will sleep for 5 seconds")
  time.sleep(5)
  print("one: I am done sleeping")


def delayed_print_two():
  print("two: i will sleep for 5 seconds")
  time.sleep(5)
  print("two: I am done sleeping")


def delayed_print_three():
  print("three: i will sleep for 5 seconds")
  time.sleep(5)
  print("three: I am done sleeping")


# delayed_print_one()
# delayed_print_two()
# delayed_print_three()


if __name__ == "__main__":  #this is a must for the processes to work.

  start_time = time.perf_counter()
  # print(start_time)

  

  p1 = multiprocessing.Process(target = delayed_print_one)
  p2 = multiprocessing.Process(target = delayed_print_two)
  
  p1.start()
  p2.start()

  p1.join()
  p2.join()

  finish_time = time.perf_counter()
  # print(finish_time)

  print(f"program took {finish_time - start_time} seconds to run")

