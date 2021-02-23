# times = [(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]

# def merge_ranges(meetings):
  
#   sorted_meetings = sorted(meetings)
  
#   merged_meetings = [sorted_meetings[0]]

#   for current_meeting_start, current_meeting_end in sorted_meetings[1:]:
#     last_merged_meeting_start, last_merged_meeting_end = merged_meetings[-1]

#     if (current_meeting_start <= last_merged_meeting_end):
#       merged_meetings[-1] = (last_merged_meeting_start, max(last_merged_meeting_end, current_meeting_end))

#     else:
#       merged_meetings.append((current_meeting_start, current_meeting_end))
      
#   return merged_meetings

# print(merge_ranges(times))

# def reverse_list(list):
#   left_index = 0
#   right_index = len(list)-1

#   while left_index < right_index:
#     list[left_index], list[right_index] = list[right_index], list[left_index]

#     left_index += 1
#     right_index -= 1

# list = [1,2,6,54,7,3,2]
# reverse_list(list)
# print(list)

# my_list     = [3, 4, 6, 10, 11, 15]
# alices_list = [1, 5, 8, 12, 14, 19]

# def merge_lists(list1, list2):
#   merged_list = [None] * (len(list1) + len(list2))
#   idx1 = 0
#   idx2 = 0
#   merged_idx = 0
#   while merged_idx < len(merged_list):
#     list1_exhausted = idx1 >= len(list1)
#     list2_exhausted = idx2 >= len(list2)
#     if (not list1_exhausted and (list2_exhausted or list1[idx1] < list2[idx2])):
#       merged_list[merged_idx] = list1[idx1]
#       idx1 += 1
#     else:
#       merged_list[merged_idx] = list2[idx2]
#       idx2 += 1
#     merged_idx += 1
  
#   return merged_list

# # Prints [1, 3, 4, 5, 6, 8, 10, 11, 12, 14, 15, 19]
# print (merge_lists(my_list, alices_list))


# Take_Out_Orders = [17, 8, 24]
# Dine_In_Orders = [12, 19, 2]
# Served_Orders = [17, 8, 12, 19, 24, 2]

# def order_check(take_out_orders, dine_in_orders, served_orders):
#   if len(served_orders) == 0:
#     return True

#   if len(take_out_orders) and take_out_orders[0] == served_orders[0]:
#     return order_check(take_out_orders[1:], dine_in_orders, served_orders[1:])

#   elif len(dine_in_orders) and dine_in_orders[0] == served_orders[0]:
#     return order_check(take_out_orders, dine_in_orders[1:], served_orders[1:])

#   else:
#     return False
  
# print(order_check(Take_Out_Orders, Dine_In_Orders, Served_Orders))

