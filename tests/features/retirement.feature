Feature: Retirement age calculator.
The user wants to know the retirement age of the person born on 1941 to verify that the retirement age is
shown correctly.

  Scenario: Retirement age calculation for the person born on 1941.
Given: a running the program.
When: the user enters the birthyear as 1941.
Then: the user is asked to enter the birth month.
When: the user enters the birth month as 2.
Then: result for the “Retirement age” with the time are shown.
And: the following related result are shown.
| Full retirement age is 65 and 8 months. |
| this will be in October of 2006 |

Scenario:: Retirement age Calculation.
The user wants to know the retirement age of the person born on 1954.
Given: a running the program.
When: the user enters the birthyear as 1954.
Then: the user is asked to enter the birth month.
When: the user enters the birth month as 9.
Then: result for the “Retirement age” with the exact date are shown.
And: the following related result are shown.
| Full retirement age is 66 and 0 months. |
| this will be in October of 2020 |

Scenario: Retirement age Calculation.
The user wants to know the retirement age of the person born on 1958.
Given: a running the program.
When: the user enters the birthyear as 1958.
Then: the user is asked to enter the birth month.
When: the user enters the birth month as 11.
Then: result for the “Retirement age” with the exact date are shown.
And: the following related result are shown.
| Full retirement age is 66 and 8 months. |
| this will be in October of 2025 |

Scenario:: Retirement age Calculation.
The user wants to know the retirement age of the person born on 1960.
Given: a running the program.
When: the user enters the birthyear as 1960.
Then: the user is asked to enter the birth month.
When: the user enters the birth month as 12.
Then: result for the “Retirement age” with the exact date are shown.
And: the following related result are shown.
| Full retirement age is 67 and 0 months. |
| this will be in October of 2027 |

