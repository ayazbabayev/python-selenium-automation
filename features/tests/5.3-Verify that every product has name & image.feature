# Created by ababa at 8/6/2021
Feature: Search results are displayed.

  Scenario: User can see every that product has name & image
    Given User opens Amazon(No Sign In)
    When User searches for coffee
    Then Verify that every product has name & image
