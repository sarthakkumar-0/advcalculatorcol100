# Python Calculator Project

This repository contains a Python-based calculator program that includes both simple and advanced functionality. The project demonstrates the use of object-oriented programming concepts, data structures, and basic user interface design.

---

## Features

1. **Simple Calculator**:
   - Supports basic arithmetic operations: addition, subtraction, multiplication, and division.
   - Returns results as floating-point numbers.
   - Maintains a history of evaluated expressions.

2. **Advanced Calculator**:
   - Supports operations with parentheses, curly braces `{}`, and square brackets `[]`.
   - Can handle complex expressions with operator precedence.
   - Includes input validation for bracket balancing and syntax correctness.
   - Maintains a history of evaluated expressions.

3. **User Interface**:
   - A command-line interface allows switching between simple and advanced calculators.
   - Displays options to evaluate expressions, view history, or exit.

4. **Stack Data Structure**:
   - Custom implementation of a stack is used for managing operations and operands.

---

## File Overview

- **`simple_calculator.py`**:
  - Implements the `SimpleCalculator` class for basic arithmetic operations.
  - Maintains a history of calculations using the stack.

- **`advanced_calculator.py`**:
  - Extends `SimpleCalculator` to handle complex expressions.
  - Includes methods for tokenizing input, validating brackets, and evaluating expressions.

- **`simple_ui.py`**:
  - Provides a command-line interface for interacting with the calculators.
  - Allows users to switch between simple and advanced modes, calculate expressions, and view history.

- **`stack.py`**:
  - A custom stack implementation with methods to push, pop, peek, and check if the stack is empty.
  - Supports the internal workings of both calculators.
