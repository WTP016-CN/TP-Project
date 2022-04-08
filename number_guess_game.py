# 该脚本灵感来源于《广东省初中信息技术教材(B版) 八年级下册》

# 导入模块
import random

# 语言选择
language = int(input("""Language Select 言語を選択 语言选择
[1] 中文(简体) Chinese (Simplified)
[2] 英语 English
[3] 日本語 Japanese
括弧内の数字を入力し、言語を選択してください Please enter the number in brackets to select a language 请输入中括号内的数字以选择语言: """)) 

# 次数赋值
times = 5
guess_times = 1

# 随机数赋值
robot_guess_number = random.randint(1,100)

# 中文(简体) 输出结果
if language == 1:
    while times > 0:
        guess_number = int(input("氦! 让我们来玩一个猜数字游戏吧! 现在请你输入一个1-100以内的数字，你一共有 5 次机会。请输入你的数字: "))
        if guess_number == robot_guess_number:
            print("哇! 你竟然猜对了!")
            print("你只用了", guess_times, "次就猜出来了! 真聪明!")
            break
        elif guess_number > robot_guess_number:
            print("你猜的数字大于随机生成的数字哦! 请你再猜一次!")
            times = times - 1
            print("你还剩下", times, "次机会")
            guess_times = guess_times + 1
        elif guess_number < robot_guess_number:
            print("你猜的数字小于随机生成的数字哦! 请你再猜一次!")
            times = times - 1
            print('你还剩', times, '次机会')
            guess_times = guess_times + 1
    if times == 0:
        print("对不起，你用尽了所有的次数都没有猜出来，重开吧(恼")
        print("正确答案是", robot_guess_number, "我真的为你的数学能力担忧")

# 英语 输出结果
times = 5
if language == 2:
    while times > 0:
        guess_number = int(input("Hi! Let's play a guessing-number game! Now please input a number between 1 and 100. You have 5 chances. Now, it's time to input your number: "))
        if guess_number == robot_guess_number:
            print("Wow! You input the correct number!")
            print("You only use", guess_times, "chance(s) to guess the correct number! You are so clever!")
            break
        elif guess_number > robot_guess_number:
            print("Oh! The number you enter is greater than the randomly generated number! Please guess again!")
            times = times - 1
            print("Now you have", times, "chance(s).")
            guess_times = guess_times + 1
        elif guess_times < robot_guess_number:
            print("Oh! The number you enter is less than the randomly generated number! Please guess again!")
            times = times - 1
            print("Now you have", times, "chance(s)")
            guess_times = guess_times + 1
        if times == 0:
            print("Sorry, your chances ran out. Restart the game and you can play again!")
            print("The correct answer is", robot_guess_number, "I am really worried about you math skill.")

# 日语 输出结果
if language == 3:
    times = 5
    while times > 0:
        guess_number = int(input("こんにちは。数字当てゲームで遊ぼう 今度は1から100までの数字を入力すると、合計5回のチャンスがあります。 推測した数字を入力してください： "))
        if guess_number == robot_guess_number:
            print("すげえええええええええええええええええええええええ よくぞここまで！という感じです。")
            print("たった", guess_times, "回で正解になった！？ すごいなー！！！")
            break
        elif guess_number > robot_guess_number:
            print("推測した数字が、ランダムに生成された数字よりも大きい! もう一度当ててみてください！")
            times = times - 1
            print("残りのチャンスは", times, "回")
            guess_times = guess_times + 1
        elif guess_times < robot_guess_number:
            print("推測した数字が、ランダムに生成された数字よりも小さい! もう一度当ててみてください！")
            times = times - 1
            print("残りのチャンスは", times, "回")
            guess_times = guess_times + 1
        if times == 0:
            print("すみません、当てられなかった回数を使い切ったので、もう一度ゲームを始めてください！")
            print("正解は", robot_guess_number, "あなたの数学力が心配です。")

print("ゲームは、終わりました。Game has ended. 游戏结束。")