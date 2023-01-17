question_data = [
                    
                    {"q0": "A slug's blood is green.", "answer": "True"},
                    {"q1": "The loudest animal is the African Elephant.", "answer": "False"},
                    {"q2": "Approximately one quarter of human bones are in the feet.", "answer": "True"},
                    {"q3": "The total surface area of a human lungs is the size of a football pitch.", "answer": "True"},
                    {"q4": "In West Virginia, USA, if you accidentally hit an animal with your car, you are free to take it home to eat.", "answer": "True"},
                    {"q5": "In London, UK, if you happen to die in the House of Parliament, you are entitled to a state funeral.", "answer": "False"},
                    {"q6": "It is illegal to pee in the Ocean in Portugal.", "answer": "True"},
                    {"q7": "You can lead a cow down stairs but not up stairs.", "answer": "False"},
                    {"q8": "Google was originally called 'Backrub'.", "answer": "True"},
                    {"q9": "Buzz Aldrin's mother's maiden name was 'Moon'.", "answer": "True"},
                    {"q10": "No piece of square dry paper can be folded in half more than 7 times.", "answer": "False"},
                    {"q11": "A few ounces of chocolate can to kill a small dog.", "answer": "True"}
                    
                    ]

#following will pring a single line, only the value part of the dictionary.
for lines in question_data:
  print(question_data[0]["q0"])
  print(question_data[0]["answer"])
  break

#following will pring a single line, all of the first dictionary item
for lines in question_data:
  print(question_data[0])
  break