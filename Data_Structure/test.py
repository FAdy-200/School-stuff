# QYESTION 1
function delete_node(list,k):
	# set a temporary value (current) that points to the lists head
	current <- list.head
	# if the current is equal to NAN then the list is empty and should return the list
	if current IS EQUAL NAN, do
		return list
	# iterating through the list
	for i <- 1:k-1, do
		current <- current.next
		# checking if the current elemnet is the last element in the list if so return the list
		if current.next is equal NAN,do
			return list
	# changing the value of the next of teh current element to point to the element after the one
	# that is deleted
	current.next <- current.next.next
	return list

# QUESTON 2
function min_max_finder(list):
	# set a temporary value (current) that points to the lists head
	current <- list.head
	# set two values called minimum,maximum to be the list.head
	minimum <- list head
	maximum <- list.head
	# iterating through the list
	while current is not equal NAN:
		# checking if the current value is bigger than maximum then assigning maximum accordingly
		if current is greater than maximum, do
			maximum <- current
		# checking if the current value is smaller than mimum then assigning maximum accordingly
		if current is smaller than minimum, do
			minimum <- current
	return minimum, maximum

# QUESTION 3
function number_of_even(list):
	# set a temporary value (current) that points to the lists head
	current < - list.head
	# set a value to count the even numbers
	numberOfEven <- 0
	# iterating through the list
	while current is not equal NAN,do
		if current.data modulus 2 is equal 0,do
			numberOfEven <- numberOfEven + 1
		current <- current.next
	return numberOfEven



# QUESTION 4
function duplicate_remover(list):
	"""
	this function takes the list and deletes any duplicates it finds in it 
	it is of complexity O(n^2) as it is iterating through the list once for each element in the list
	"""
	# set a temporary value that points to the lists head to be the first element to be checked for duplicates
	value <- list.head
	# set the current variable to be value as it will be used to iterate through the list and delete
	# any duplicates
	current <- value
	# iterating through the list for each element to be checked for duplicates
	while value.next is not equal NAN, do
		# iterating through the list to check for duplicates for the element value
		while current.next is not equal NAN, do
			# checking if there is a match
			if current.next.data is equal value.data, do
				# deleting the duplicate from the original list
				current.next <- current.next.next
			current <- current.next
		value <- value.next
	return list

# QUESTION 8
function rotate(list,k):
	# doing the k rotations
	for i <-0 : k,do
		# finding the last and second to last element
		current <- list.head
		while current.next is not equal NAN, do
			current<-current.next
		lastelement <- current
		seclastelement <- current.last
		# doing the necessary changes to the attributes to
		lastelement.next <- list.head
		lsatelement.last <- NAN
		seclastelement.next <- NAN
		list.head <- lastelement

# QUESTION 9
function counter(circularlyList):
	# checking if the list is empty
	if circularlyList.head is not equal NAN, do
		# iterating through the list untill the current gets back to the lists head
		current <- circularlyList.head.next
		n <- 1
		while current is not equal circularlyList.head, do
			n<-n+1
			current <- current.next
		return n
	else,do
		return circularlyList