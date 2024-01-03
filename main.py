import os


#searching lists and calls
def Searching():
  print('''Searching Menu
1. Linear Search
2. Binary Search
3. Back\n''')

  choice2 = int(input("Enter your choice:"))
  os.system("clear")
  if choice2 == 1:
    print("Linear Search")
    arrayin()
    print(arr)
    target = int(input("Enter the number to be searched:"))
    position = LinearSearch(arr, target)
    if position != -1:
      print("Element is present at index", position)
    else:
      print("Element not found!")
  elif choice2 == 2:
    print("Binary search")
    arrayin()
    print(arr)
    target = int(input("Enter the number to be searched:"))
    position = BinarySearch(arr, target)
    if position != -1:
      print("Element is present at index", position)
    else:
      print("Element not found!")
  else:
    main()


#sorting lists and calls
def Sorting():
  print('''Sorting Menu
1. Bubble Sort
2. Insertion Sort
3. Selection Sort
4. Back\n''')

  choice2 = int(input("Enter your choice:"))
  os.system("clear")
  if choice2 == 1:
    print("Bubble Sort")
    arrayin()
    BubbleSort(arr)
  elif choice2 == 2:
    print("Insertion Sort")
    arrayin()
    InsertionSort(arr)

  elif choice2 == 3:
    print("Selection Sort")
    arrayin()
    SelectionSort(arr)

  else:
    main()


#array input
def arrayin():
  global arr
  n = int(input("enter number of element:"))
  os.system("clear")
  for i in range(n):
    arr.append(int(input("enter element:")))
  os.system("clear")


#linear search
def LinearSearch(arr, target):
  for i in range(len(arr)):
    if arr[i] == target:
      return i
  return -1


#binary search
def BinarySearch(arr, target):
  start = 0
  end = len(arr) - 1
  while start <= end:
    mid = start + (end - start) // 2
    if arr[mid] < target:
      start = mid + 1
    elif arr[mid] > target:
      end = mid - 1
    else:
      return mid
  return -1


#bubble sort
def BubbleSort(arr):
  n = len(arr)
  for i in range(n):
    for j in range(0, n - i - 1):
      if arr[j] > arr[j + 1]:
        arr[j], arr[j + 1] = arr[j + 1], arr[j]
  print("Sorted array:", arr)


#insertion sort
def InsertionSort(arr):
  n = len(arr)
  for i in range(1, n):
    key = arr[i]
    j = i - 1
    while j >= 0 and key < arr[j]:
      arr[j + 1] = arr[j]
      j -= 1
    arr[j + 1] = key
  print("Sorted array:", arr)


#selection sort
def SelectionSort(arr):
  n = len(arr)
  for i in range(n):
    min_idx = i
    for j in range(i + 1, n):
      if arr[j] < arr[min_idx]:
        min_idx = j
    arr[i], arr[min_idx] = arr[min_idx], arr[i]
  print("Sorted array:", arr)


#main
def main():
  os.system("clear")
  print('''Menu 1
1. Searching
2. Sorting
3. Exit\n''')
  choice1 = int(input("Enter your choice:"))
  os.system("clear")
  if choice1 == 1:
    Searching()
  elif choice1 == 2:
    Sorting()
  else:
    print("Bye,Babe!!")
    os.system("exit")


arr = []
main()
