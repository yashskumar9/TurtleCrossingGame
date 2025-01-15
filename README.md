# Turtle Crossing Game

Welcome to the **Turtle Crossing Game**, a fun and challenging game implemented in Python using the `turtle` module. The objective is to help the turtle cross the road while avoiding cars. As the game progresses, the difficulty increases with faster car speeds.
<br>
<br>

<p align='center'>
  <a>
    <img src='https://github.com/user-attachments/assets/3f31b287-5f94-4f0b-88b8-3179b9cfb0b7' width=300>
  </a>
</p>

<br>

## Introduction

The Turtle Crossing Game is inspired by the classic arcade game "Frogger." Players control a turtle that must navigate across a road filled with moving cars. Each successful crossing advances the player to the next level, where the cars move even faster, making the game more challenging and engaging.

## Features

- **User Control**: Move the turtle forward using the `Up Arrow` key.
- **Dynamic Gameplay**: Cars are generated dynamically at random positions, creating unpredictable obstacles.
- **Level Progression**: Each successful crossing advances the player to the next level.
- **Increasing Difficulty**: Car speeds increase with each level, adding to the challenge.
- **Game Over Display**: A "Game Over" message appears when the turtle collides with a car.

## How to Play

1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/yashskumar9/turtle-crossing-game.git
   ```
2. Navigate to the project directory:
   ```bash
   cd turtle-crossing-game
   ```
3. Ensure you have Python installed. The game requires Python 3.x.

4. Run the game:
   ```bash
   python main.py
   ```

5. Use the `Up Arrow` key to move the turtle forward and avoid oncoming cars.

## Project Structure

```
├── main.py           # Entry point of the game
├── user_turtle.py    # Contains the UserTurtle class for turtle movement
├── cars.py           # Contains the Cars class for car creation and movement
├── score_board.py    # Contains the ScoreBoard class for tracking levels and displaying game over messages
```

Enjoy playing the Turtle Crossing Game! 🐢

