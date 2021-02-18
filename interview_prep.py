# stock_prices = [10, 7, 5, 8, 20, 11, 9]

# def get_max_profit(stock_prices):
#   if len (stock_prices) < 2:
#     raise ValueError('Getting a profit requires at least 2 prices!')

#   min_price = stock_prices[0]
#   max_profit = stock_prices[1] - stock_prices[0]

#   for current_time in range(1, len(stock_prices)):
#     current_price = stock_prices[current_time]

#     potential_profit = current_price - min_price

#     max_profit = max(max_profit, potential_profit)

#     min_price = min(min_price, current_price)

#   return max_profit

# print(get_max_profit(stock_prices))

# unsorted_scores = [37, 89, 41, 65, 91, 53, 41]
# HIGHEST_POSSILE_SCORE = 100

# def sort_scores(unsorted_scores, highest_possible_score):
#   score_counts = [0] * (highest_possible_score+1)

#   for score in unsorted_scores:
#     score_counts[score] += 1

#   sorted_scores = []

#   for score in range(len(score_counts) -1, -1, -1):
#     count = score_counts[score]

#     for time in range(count):
#       sorted_scores.append(score)

#   return sorted_scores

# print (sort_scores(unsorted_scores, HIGHEST_POSSILE_SCORE))
  
message = [ 'c', 'a', 'k', 'e', ' ',
            'p', 'o', 'u', 'n', 'd', ' ',
            's', 't', 'e', 'a', 'l' ]

def reverse_words(message):
  reverse_characters(message, 0, len(message)-1)
  current_word_start_index = 0

  for i in range(len(message)+1):
    if (i == len(message)) or (message[i] == ' '):
      reverse_characters(message, current_word_start_index, i - 1)
      current_word_start_index = i +1
  return message

def reverse_characters(message, left_index, right_index):
  while left_index < right_index:
    message[left_index], message[right_index] = \
      message[right_index], message[left_index]
    left_index += 1
    right_index -= 1

reverse_words(message)
print (''.join(message))
  
