import time

class Algorithms:

    COLOR = "cyan"

    def __init__(self, visualizer):
        self.visualizer = visualizer

    # Choose user defined algorithm
    def start_algorithm(self, data):
        if self.visualizer.selected_alg.get() == "bubbleSort":
            self.bubble_sort(data)
        elif self.visualizer.selected_alg.get() == "insertionSort":
            self.insertion_sort(data)
        elif self.visualizer.selected_alg.get() == "mergeSort":
            self.merge_sort(data, 0, len(data) -1)
        elif self.visualizer.selected_alg.get() == "heapSort":
            self.heap_sort(data)
        elif self.visualizer.selected_alg.get() == "quickSort":
            self.quick_sort(data, 0, len(data) -1)
        elif self.visualizer.selected_alg.get() == "shellSort":
            self.shell_sort(data,  len(data))
        elif self.visualizer.selected_alg.get() == "combSort":
            self.comb_sort(data)
        elif self.visualizer.selected_alg.get() == "exchangeSort":
            self.exchange_sort(data)


    ## Type: Bubble Sort ##
    ### Time Complexity: ##
    # Best: n
    # Average: n^2
    # Worst: n^2
    ### Extra Storage Needed: ###
    # Memory: 1
    def bubble_sort(self, data):

        # Traverse through all array elements
        for _ in range(len(data) - 1):
            #Traverse the array from 0 to last element
            for j in range(len(data) - 1):

                #Swap elements if the found element if greater than the next element
                if data[j] > data[j + 1]:
                    data[j], data[j + 1] = data[j + 1], data[j]

                    #Visualize data
                    self.visualizer.draw_data(data,
                                              [self.COLOR if x == j + 1 else "white" for x in range(len(data))])
                    time.sleep(0.2)

    ## Type: Simple Sort ##
    ### Time Complexity: ##
    # Best: n
    # Average: n^2
    # Worst: n^2
    ### Extra Storage Needed: ###
    # Memory: 1
    ## Notes: good for SMALL lists, Shell sort is based on this algorithm
    def insertion_sort(self, data):

        # Iterate over the array
        for i in range(len(data)):

            #Store the current element to be inserted in the correct position
            key = data[i]
            j = i-1

            #Move elements greater than the key one position ahead
            while j >= 0 and key < data[j]:

                #Shift elements to the right
                data[j+1] = data[j]
                j = j - 1

                # Visualize data
                self.visualizer.draw_data(data,
                                          [self.COLOR if x == j + 1 else "white" for x in range(len(data))])
                time.sleep(0.2)

            # Insert the key to the correct position
            data[j+1] = key

            # Visualize data
            self.visualizer.draw_data(data,
                                      [self.COLOR if x == j + 1 else "white" for x in range(len(data))])
            time.sleep(0.2)



    ## Type: Efficient Sort ##
    ### Time Complexity: ##
    # Best: nlog(n)
    # Average: nlog(n)
    # Worst: nlog(n)
    ### Extra Storage Needed: ###
    # Memory: 1
    def merge_sort(self, data, l, r):

        if l < r:

            # Find the middle of the array
            m = l + (r-l)//2

            # Recursive call to the left half of the array
            self.merge_sort(data, l, m)
            # Recursive call to the right half of the array
            self.merge_sort(data, m+1, r)
            # Call to the helper to arrange the elements
            self.merge(data, l, m , r)


    def merge(self, data, l, m , r):
        #Visualize Data
        self.visualizer.draw_data(data,
                                  [self.COLOR if x >= l and x <= r else "white" for x in range(len(data))])
        time.sleep(0.2)
        #Visualize Data
        self.visualizer.draw_data(data,
                                  [self.COLOR if x >= l and x <= m else "white" for x in range(len(data))])
        time.sleep(0.2)

        n1 = m - l + 1
        n2 = r - m

        # create temp arrays
        L = [0] * (n1)
        R = [0] * (n2)

        # Copy data to temp arrays L[] and R[]
        for i in range(0, n1):
            L[i] = data[l + i]

        for j in range(0, n2):
            R[j] = data[m + 1 + j]

        # Merge the temp arrays back into arr[l..r]
        i = 0  # Initial index of first subarray
        j = 0  # Initial index of second subarray
        k = l  # Initial index of merged subarray

        while i < n1 and j < n2:
            self.visualizer.draw_data(data,
                                      [self.COLOR if x == 1 + i and x == m +j + 1 else "white" for x in range(len(data))])
            time.sleep(0.2)
            if L[i] <= R[j]:
                data[k] = L[i]
                i += 1
            else:
                data[k] = R[j]
                j += 1
            k += 1

        # Copy the remaining elements of L[], if there are any
        while i < n1:
            self.visualizer.draw_data(data,
                                      [self.COLOR if x == i + 1 else "white" for x in range(len(data))])
            time.sleep(0.2)
            data[k] = L[i]
            i += 1
            k += 1

        # Copy the remaining elements of R[], if there are any
        while j < n2:
            self.visualizer.draw_data(data,
                                      [self.COLOR if x == m + j + 1 else "white" for x in range(len(data))])
            time.sleep(0.2)
            data[k] = R[j]
            j += 1
            k += 1

        # Visualize Data
        self.visualizer.draw_data(data,
                                  [self.COLOR if x == (k - 1) else "white" for x in range(len(data))])
        time.sleep(0.2)



    ## Type: Efficient Sort ##
    ### Time Complexity: ##
    # Best: nlog(n)
    # Average: nlog(n)
    # Worst: nlog(n)
    ### Extra Storage Needed: ###
    # Memory: 1
    def heap_sort(self, data):

        for i in range(len(data)//2, -1, -1):
            self.heapify(data, len(data), i)

        for i in range(len(data) - 1, 0, -1):
            data[i], data[0] = data[0], data[i]
            self.heapify(data, i, 0)

    def heapify(self, data, n, i):
        # Initialize largest as root
        largest = i
        # left = 2*i + 1
        l = 2 * i + 1
        # right = 2*i + 2
        r = 2 * i + 2

        # See if left child of root exists and is greater than root

        if l < n and data[i] < data[l]:
            largest = l
            #Visualize Data
            self.visualizer.draw_data(data,
                                      [self.COLOR if x == largest else "white" for x in range(len(data))])
            time.sleep(0.2)

        if r < n and data[largest] < data[r]:
            largest = r
            # Visualize Data
            self.visualizer.draw_data(data,
                                      [self.COLOR if x == largest else "white" for x in range(len(data))])
            time.sleep(0.2)

        # Change root, if needed
        if largest != i:
            data[i], data[largest] = data[largest], data[i]

            # Visualize Data
            self.visualizer.draw_data(data,
                                      [self.COLOR if x == i else "white" for x in range(len(data))])
            time.sleep(0.2)

            # Heapify the root.
            self.heapify(data, n, largest)

        # Visualize Data
        self.visualizer.draw_data(data,
                                  [self.COLOR if x == i else "white" for x in range(len(data))])
        time.sleep(0.2)

    ## Type: Efficient Sort ##
    ### Time Complexity: ##
    # Best: nlog(n)
    # Average: nlog(n)
    # Worst: n^2
    ### Extra Storage Needed: ###
    # Memory: log(n)
    def quick_sort(self, data, l, h):
        if l < h:

            # Find pivot such that
            # Elements smaller than pivot are on the left
            # Elements greater than pivot are ont he right
            pivot = self.partition(data, l, h)

            # Recursive call on the left of the pivot
            self.quick_sort(data, l, pivot - 1)

            # Recursive call on the right of the pivot
            self.quick_sort(data, pivot + 1, h)

    def partition(self, data, l, h):

        # Right most element is the pivot
        pivot = data[h]

        # Pointer for the greater element
        i = l - 1

        # Traverse through all elements  and compare elements with pivot
        for j in range(l, h):

            # If element is smaller than pivot is found swap it with
            # the greater element pointed by i
            if data[j] <= pivot:
                i = i +1
                data[i], data[j] = data[j], data[i]

                # Visualize Data
                self.visualizer.draw_data(data,
                                          [self.COLOR if x == i or x == j else "white" for x in range(len(data))])
                time.sleep(0.2)

        data[i + 1], data[h] = data[h], data[i + 1]

        # Visualize Data
        self.visualizer.draw_data(data,
                                  [self.COLOR if x == i + 1 or x == h else "white" for x in range(len(data))])
        time.sleep(0.2)

        return i + 1





    ## Type: Efficient Sort ##
    ### Time Complexity: ##
    # Best: nlog(n)
    # Average: n^(4/3)
    # Worst: n^(3/2)
    ### Extra Storage Needed: ###
    # Memory: 1
    def shell_sort(self, data, size):

        #Start with the big gap
        gap = size//2

        while gap > 0:

            # Add data[i] to the elements that have been gap sorted
            # save data[i] in temp and make a hole at position i
            for i in range(gap, size):
                temp = data[i]
                # Shift earlier gap-sorted elements up until the correct
                # location for data[i] is found
                j = i
                while j >= gap and data[j - gap] > temp:
                    data[j] = data[j - gap]
                    j = j - gap

                # ut them in its correct location
                data[j] = temp

                # Visualize data
                self.visualizer.draw_data(data,
                                          [self.COLOR if x == i or x == j else "white" for x in range(len(data))])
                time.sleep(0.2)

            gap = gap // 2



    ## Type: Bubble Sort ##
    ### Time Complexity: ##
    # Best: nlog(n)
    # Average: n^2
    # Worst: n^2
    ### Extra Storage Needed: ###
    # Memory: 1
    def comb_sort(self, data):

        gap = len(data)
        swapped = True

        # Keep running while gap is more than 1 and last iteration caused a swap
        while gap != 1 or swapped == 1:

            # Find the gap
            gap = self.get_next_gap(gap)

            # Check if swap happened or not
            swapped = False

            # Compare all elements with current gap
            for i in range(0, len(data)-gap):
                if data[i] > data[i + gap]:
                    # Visualize data
                    self.visualizer.draw_data(data,
                                              [self.COLOR if x == i or x == i + gap else "white" for x in
                                                     range(len(data))])
                    time.sleep(0.2)
                    data[i], data[i + gap] = data[i + gap], data[i]
                    swapped = True

            # Visualize data
            self.visualizer.draw_data(data,
                                      [self.COLOR if x == i or x == i + gap else "white" for x in range(len(data))])
            time.sleep(0.2)

    def get_next_gap(self, gap):

        # Shrink the gap
        gap = (gap * 10)//13
        if gap < 1:
            return 1
        return gap




    ## Type: Bubble Sort ##
    ### Time Complexity: ##
    # Best: n^2
    # Average: n^2
    # Worst: n^2
    ### Extra Storage Needed: ###
    # Memory:
    def exchange_sort(self, data):

        for i in range(len(data) -1):
            # Sort in ascending order if previous element bigger than next
            # element we swap to make it in ascending order
            for j in range (i + 1, len(data)):
                if data[i] > data[j]:
                    data[i], data[j] = data[j], data[i]
                self.visualizer.draw_data(data,
                                          [self.COLOR if x == i or x == j else "white" for x in range(len(data))])
                time.sleep(0.2)


