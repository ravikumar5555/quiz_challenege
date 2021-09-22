quiz = {
      "sport": {
          "q1": {
              "question": "Which one is correct team name in NBA?",
              "options": [
                  "New York Bulls",
                  "Los Angeles Kings",
                  "Golden State Warriros",
                  "Huston Rocket"
              ],
              "answer": "Huston Rocket"
          }
      },
      "maths": {
          "q1": {
              "question": "5 + 7 = ?",
              "options": [
                  "10",
                  "11",
                  "12",
                  "13"
              ],
              "answer": "12"
          },
          "q2": {
              "question": "12 - 8 = ?",
              "options": [
                  "1",
                  "2",
                  "3",
                  "4"
              ],
              "answer": "4"
          }
      }
  }


def start_quiz(topic):
    score = 0
    topic_json = quiz[topic]
    for q_no in topic_json:
        print()
        print(q_no, topic_json[q_no]["question"])
        print("options: \n{}".format("\n".join(topic_json[q_no]["options"])))
        input_answer = input("\nenter answer: ",)
        if input_answer == topic_json[q_no]["answer"]:
            score += 1
    print(f"You score is : {score}")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
        choice = int(input("enter choice: 1 for sports 2 for maths: "))
        if choice not in [1,2,3]:
            print("enter correct choice")
        else:
            quiz_topic = "sport" if choice == 1 else "maths"
            start_quiz(quiz_topic)
