# Created by ababa at 8/8/2022
Feature: Switching Windows in Amazon: T&C - Privacy Notice - T&C

  Scenario: User can open and close Amazon Privacy Notice
 Given Open Amazon Terms & Conditions page
 When Store original window
 And Click on Privacy Notice link
 And Switch to newly opened window
 Then Verify Amazon Privacy Notice page opened
 And User can close new window & switch back to original